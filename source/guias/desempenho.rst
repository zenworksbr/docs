******************************
Guia de melhoria de desempenho
******************************

Se você está enfrentando quedas de FPS, travamentos ou lentidão no Garry's Mod, este guia vai ajudar a otimizar seu jogo.

=========================
Configurações do Jogo
=========================

Configurações de Vídeo
----------------------

Acesse **Opções > Vídeo** e ajuste:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Configuração
     - Recomendação
   * - **Resolução**
     - Use a resolução nativa do seu monitor
   * - **Modo de Exibição**
     - Tela cheia (melhor performance que janela)
   * - **Anti-Aliasing**
     - Desativar ou 2x (consome muita GPU)
   * - **Filtering Mode**
     - Bilinear ou Trilinear
   * - **Wait for VSync**
     - Desativar (aumenta input lag)
   * - **Motion Blur**
     - Desativar
   * - **Field of View**
     - 90 (padrão, aumentar consome mais)

Configurações Avançadas
-----------------------

Acesse **Opções > Vídeo > Avançado**:

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Configuração
     - Recomendação
   * - **Model Detail**
     - Medium ou Low
   * - **Texture Detail**
     - Medium (Low se necessário)
   * - **Shader Detail**
     - Low ou Medium
   * - **Water Detail**
     - Simple Reflections ou None
   * - **Shadow Detail**
     - Low
   * - **Color Correction**
     - Desativar
   * - **High Dynamic Range**
     - None ou Bloom
   * - **Multicore Rendering**
     - **Ativar** (importante!)

.. important::
   **Multicore Rendering** deve estar **ativado**! Isso permite que o jogo use múltiplos núcleos do processador.

=========================
Comandos de Console
=========================

Abra o console (tecla ``~``) e digite estes comandos para melhorar a performance:

Comandos Essenciais
-------------------

.. code-block:: text

   // Limpar cache e lixo
   r_cleardecals

   // Desativar ragdolls (corpos mortos)
   g_ragdoll_maxcount 0

   // Reduzir partículas
   mat_reduceparticles 1

   // Desativar sprays de outros jogadores
   cl_playerspraydisable 1

   // Limitar FPS (reduz uso de recursos)
   fps_max 120

   // Desativar motion blur
   mat_motion_blur_enabled 0

Comandos de Rede
----------------

Para melhorar a conexão:

.. code-block:: text

   // Aumentar taxa de atualização
   cl_updaterate 66
   cl_cmdrate 66

   // Interpolação suave
   cl_interp 0
   cl_interp_ratio 1

Autoexec Recomendado
--------------------

Crie um arquivo ``autoexec.cfg`` em ``garrysmod/cfg/`` com:

.. code-block:: text

   // === Performance Otimizada ===
   
   // Gráficos
   mat_reduceparticles 1
   mat_motion_blur_enabled 0
   r_decals 100
   r_shadows 0
   
   // Ragdolls e física
   g_ragdoll_maxcount 0
   props_break_max_pieces 0
   
   // Sprays
   cl_playerspraydisable 1
   
   // Rede
   cl_updaterate 66
   cl_cmdrate 66
   cl_interp 0
   cl_interp_ratio 1
   
   // FPS
   fps_max 0
   
   echo "Autoexec carregado!"

=========================
Versão 64-bit
=========================

A versão 64-bit do Garry's Mod oferece **muito mais performance** e estabilidade.

Como Ativar
-----------

1. Feche o jogo
2. Na Steam, clique com botão direito em **Garry's Mod**
3. Selecione **Propriedades**
4. Vá em **Betas**
5. Selecione **x86-64 - Chromium + 64-bit binaries**
6. Ao abrir, escolha **Launch Garry's Mod (64-bit)**

.. tip::
   A versão 64-bit pode usar mais que 4GB de RAM e geralmente tem FPS muito mais estável!

=========================
Gerenciamento de Addons
=========================

Muitos addons podem causar problemas de performance.

Identificando Addons Problemáticos
----------------------------------

1. Desabilite todos os addons na Steam Workshop
2. Entre no servidor e veja se a performance melhora
3. Ative os addons um por um para identificar o problemático

Addons que Costumam Causar Problemas
------------------------------------

- **Packs de armas muito grandes** (M9K completo, TFA completo)
- **Modelos de playermodel com alta poly count**
- **Addons de efeitos visuais exagerados**
- **Múltiplos HUDs customizados**

.. warning::
   Addons do Workshop são baixados toda vez que você entra no servidor. Muitos addons = download lento!

=========================
Limpeza do Jogo
=========================

Limpar Cache
------------

1. Feche o Garry's Mod
2. Vá até a pasta: ``Steam/steamapps/common/GarrysMod/garrysmod/``
3. Delete as pastas:
   - ``cache/``
   - ``downloads/``
4. Reinicie o jogo

Verificar Integridade
---------------------

1. Na Steam, clique com botão direito em **Garry's Mod**
2. Selecione **Propriedades**
3. Vá em **Arquivos Instalados**
4. Clique em **Verificar integridade dos arquivos do jogo**

Reinstalação Limpa
------------------

Se nada funcionar:

1. Desinstale o Garry's Mod
2. Delete a pasta ``Steam/steamapps/common/GarrysMod/``
3. Delete a pasta ``Steam/steamapps/workshop/content/4000/``
4. Reinstale o jogo

=========================
Otimização do Windows
=========================

Modo de Jogo
------------

1. Pressione **Win + G** durante o jogo
2. Ative o **Modo de Jogo**

Prioridade do Processo
----------------------

1. Abra o **Gerenciador de Tarefas** (Ctrl+Shift+Esc)
2. Encontre ``hl2.exe`` ou ``gmod.exe``
3. Clique com botão direito > **Ir para detalhes**
4. Clique com botão direito > **Definir prioridade** > **Alta**

Drivers de Vídeo
----------------

Mantenha seus drivers de vídeo atualizados:

- **NVIDIA:** `GeForce Experience <https://www.nvidia.com/pt-br/geforce/geforce-experience/>`_
- **AMD:** `AMD Software <https://www.amd.com/pt/technologies/software>`_
- **Intel:** `Intel Driver Support <https://www.intel.com.br/content/www/br/pt/support/detect.html>`_

=========================
Problemas Específicos
=========================

Travamento ao Entrar no Servidor
--------------------------------

**Possíveis causas:**

- Muitos addons sendo baixados
- Falta de memória RAM
- Cache corrompido

**Soluções:**

1. Use a versão 64-bit
2. Limpe o cache (veja acima)
3. Aumente a memória virtual do Windows

FPS Baixo Constante
-------------------

**Possíveis causas:**

- Configurações gráficas muito altas
- Drivers desatualizados
- Addons pesados

**Soluções:**

1. Reduza as configurações gráficas
2. Atualize os drivers
3. Remova addons desnecessários

Quedas de FPS (Stuttering)
--------------------------

**Possíveis causas:**

- VSync ativado
- Falta de VRAM
- Garbage collection do Lua

**Soluções:**

1. Desative o VSync
2. Reduza a qualidade de texturas
3. Use ``lua_run collectgarbage()`` no console periodicamente

=========================
Resumo Rápido
=========================

.. list-table::
   :header-rows: 1
   :widths: 40 60

   * - Problema
     - Solução Rápida
   * - FPS baixo
     - Reduza configurações gráficas
   * - Travamentos
     - Use versão 64-bit + limpe cache
   * - Downloads lentos
     - Remova addons do Workshop
   * - Stuttering
     - Desative VSync
   * - Crashes frequentes
     - Verifique integridade dos arquivos
