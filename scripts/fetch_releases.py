#!/usr/bin/env python3
"""
Fetch releases from GitHub and generate novidades.rst for Sphinx.
Groups releases by date for cleaner output.
"""

import os
import sys
import json
import re
from datetime import datetime
from collections import defaultdict
from urllib.request import Request, urlopen
from urllib.error import HTTPError

# Configuration
REPO_OWNER = "zenworksbr"
REPO_NAME = "addons"
MAX_RELEASES = 10
OUTPUT_FILE = "source/novidades.rst"

def fetch_releases(token: str) -> list:
    """Fetch releases from GitHub API."""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/releases"
    
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    
    req = Request(url, headers=headers)
    
    try:
        with urlopen(req) as response:
            releases = json.loads(response.read().decode())
            return releases[:MAX_RELEASES]
    except HTTPError as e:
        print(f"Error fetching releases: {e.code} {e.reason}")
        sys.exit(1)

def format_date(date_str: str) -> str:
    """Format ISO date to readable format."""
    dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    return dt.strftime("%d/%m/%Y")

def get_date_key(date_str: str) -> str:
    """Get date key for grouping (YYYY-MM-DD)."""
    dt = datetime.fromisoformat(date_str.replace("Z", "+00:00"))
    return dt.strftime("%Y-%m-%d")

def convert_markdown_to_rst(text: str) -> list:
    """Convert markdown formatting to RST and return list of items."""
    if not text:
        return []
    
    items = []
    current_section = None
    
    for line in text.split('\n'):
        line = line.strip()
        
        # Skip comparison links at the start
        if re.match(r'^#?\s*\[[\d.]+\]\(https://github\.com/.+/compare/.+\)', line):
            continue
        
        # Skip empty lines
        if not line:
            continue
        
        # Detect section headers (Features, Bug Fixes, etc.)
        header_match = re.match(r'^#{1,3}\s+(.+)$', line)
        if header_match:
            current_section = header_match.group(1)
            continue
        
        # Convert markdown links to RST: [text](url) -> `text <url>`_
        line = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'`\1 <\2>`_', line)
        
        # Convert bullet points with scope: * **scope:** message
        bullet_match = re.match(r'^\*\s+\*\*([^:]+):\*\*\s+(.+)$', line)
        if bullet_match:
            scope = bullet_match.group(1)
            message = bullet_match.group(2)
            items.append({
                'section': current_section,
                'scope': scope,
                'message': message
            })
            continue
        
        # Simple bullet point
        simple_match = re.match(r'^\*\s+(.+)$', line)
        if simple_match:
            items.append({
                'section': current_section,
                'scope': None,
                'message': simple_match.group(1)
            })
    
    return items

def group_releases_by_date(releases: list) -> dict:
    """Group releases by date."""
    grouped = defaultdict(list)
    
    for release in releases:
        published = release.get("published_at", "")
        if published:
            date_key = get_date_key(published)
            grouped[date_key].append(release)
    
    # Sort by date descending
    return dict(sorted(grouped.items(), reverse=True))

def generate_rst(releases: list) -> str:
    """Generate RST content from releases, grouped by date."""
    lines = []
    
    # Header
    lines.append("*********")
    lines.append("Novidades")
    lines.append("*********")
    lines.append("")
    lines.append("Acompanhe as últimas atualizações do servidor Zenworks TTT.")
    lines.append("")
    
    if not releases:
        lines.append("Nenhuma novidade disponível no momento.")
        return "\n".join(lines)
    
    # Group by date
    grouped = group_releases_by_date(releases)
    
    for date_key, date_releases in grouped.items():
        # Format date for display
        dt = datetime.strptime(date_key, "%Y-%m-%d")
        date_display = dt.strftime("%d/%m/%Y")
        
        # Collect all versions for this date
        versions = [r.get("tag_name", "") for r in date_releases]
        
        # Title
        if len(versions) == 1:
            title = f"{versions[0]} ({date_display})"
        else:
            # Show range: v1.70.0 ~ v1.70.4
            title = f"{versions[-1]} ~ {versions[0]} ({date_display})"
        
        title_line = "=" * len(title)
        
        lines.append(title_line)
        lines.append(title)
        lines.append(title_line)
        lines.append("")
        
        # Collect all items by section
        features = []
        fixes = []
        other = []
        
        for release in date_releases:
            body = release.get("body", "")
            items = convert_markdown_to_rst(body)
            
            for item in items:
                section = (item.get('section') or '').lower()
                if 'feature' in section:
                    features.append(item)
                elif 'fix' in section or 'bug' in section:
                    fixes.append(item)
                else:
                    other.append(item)
        
        # Output Features
        if features:
            lines.append("**Novidades:**")
            lines.append("")
            for item in features:
                scope = item.get('scope')
                msg = item.get('message', '')
                if scope:
                    lines.append(f"- **{scope}:** {msg}")
                else:
                    lines.append(f"- {msg}")
            lines.append("")
        
        # Output Bug Fixes
        if fixes:
            lines.append("**Correções:**")
            lines.append("")
            for item in fixes:
                scope = item.get('scope')
                msg = item.get('message', '')
                if scope:
                    lines.append(f"- **{scope}:** {msg}")
                else:
                    lines.append(f"- {msg}")
            lines.append("")
        
        # Output Other
        if other:
            lines.append("**Outras alterações:**")
            lines.append("")
            for item in other:
                scope = item.get('scope')
                msg = item.get('message', '')
                if scope:
                    lines.append(f"- **{scope}:** {msg}")
                else:
                    lines.append(f"- {msg}")
            lines.append("")
        
        # If no items were parsed, show a simple message
        if not features and not fixes and not other:
            lines.append("*Atualizações de manutenção.*")
            lines.append("")
        
        lines.append("----")
        lines.append("")
    
    # Remove last separator
    if len(lines) >= 2 and lines[-2] == "----":
        lines = lines[:-2]
    
    lines.append("")
    
    return "\n".join(lines)

def main():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("ADDONS_PAT")
    
    if not token:
        print("Error: GITHUB_TOKEN or ADDONS_PAT environment variable is required")
        sys.exit(1)
    
    print(f"Fetching releases from {REPO_OWNER}/{REPO_NAME}...")
    releases = fetch_releases(token)
    print(f"Found {len(releases)} releases")
    
    print(f"Generating {OUTPUT_FILE}...")
    content = generate_rst(releases)
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(content)
    
    print("Done!")

if __name__ == "__main__":
    main()
