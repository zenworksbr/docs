# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Zenworks - Docs'
copyright = '2024, Zenworks'
author = 'Razor'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    # External stuff
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_inline_tabs",
]

templates_path = ['_templates']
exclude_patterns = []

language = 'pt_BR'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

import furo

html_theme = 'furo'
html_title = 'Zenworks'

html_theme_options = {
    'logo_only': True,
    'display_version': False,
    'prev_next_buttons_location': 'bottom',
    'light_css_variables': {
            
    },
    'dark_css_variables': {
        # f05
        "color-problematic": "#ee5151",
        "color-foreground-primary": "#cecece",
        "color-foreground-secondary": "#cecece",
        "color-foreground-muted": "#f05727",
        "color-foreground-border": "#cecece",
        "color-background-primary": "#36314d",
        "color-background-secondary": "#1a162c",
        "color-background-hover": "#36314d",
        "color-background-hover--transparent": "#f05727",
        "color-background-border": "rgba(0,0,0,0)",
        "color-background-item": "black",
        "color-announcement-background": "#000000dd",
        "color-announcement-text": "#eeebee",
        "color-brand-primary": "#cecece",
        "color-brand-content": "#f05727",
        "color-highlighted-background": "#083563",
        "color-guilabel-background": "#08356380",
        "color-guilabel-border": "#13395f80",
        "color-highlight-on-target": "#330",
        "color-admonition-background": "#18181a",
        "color-card-background": "#18181a"
    }
}

html_static_path = ['_static']
html_logo = '_static/favicon.png'
html_favicon = '_static/favicon.png'

#html_style = '' - overwrites everything

# additional CSS files
html_css_files = ['_static/css/custom.css']

pygments_style = "sphinx"
pygments_dark_style = "dracula"

html_last_updated_fmt = ''
