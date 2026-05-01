# AGENTS.md

## Visão Geral do Projeto

Este repositório contém materiais para um minicurso de Inteligência Artificial aplicada a Finanças.

Estrutura esperada:

```text
2026_FURG/
  _quarto.yml
  styles.css
  requirements.txt
  dia1/
    slides_dia1.qmd
    slides_dia1.html
    precos_acoes_brasil.csv
    dashboard_acoes_brasil.html
    images/
    scripts/
  dia2/
    slides_dia2.qmd
    slides_dia2.html
    demo/              # a criar se necessário
  dia3/
    slides_dia3.qmd    # a criar
    slides_dia3.html   # a criar
    demo/
      materiais_dados_financeiros/
      materiais_sentimento/
      materiais_valuation/
```

Cada dia deve conter:
- slides em Quarto + RevealJS
- materiais de demonstração em `demo/`, quando aplicável

---

## Estado Atual do Repositório

Referência para futuras sessões do Codex, inclusive em ambiente local e em nuvem.

Em 2026-04-30:
- o dia 1 está implementado em `dia1/slides_dia1.qmd`
- o HTML renderizado do dia 1 está em `dia1/slides_dia1.html`
- os QR codes usados no dia 1 estão em `dia1/images/QR_code.png` e `dia1/images/github_repo_QR.png`
- há materiais auxiliares já gerados para o exemplo de dados financeiros:
  - `dia1/precos_acoes_brasil.csv`
  - `dia1/dashboard_acoes_brasil.html`
  - figuras de backtest em `dia1/images/` (`backtest_retorno`, `backtest_drawdown`, `backtest_tabela` em `.png` e `.pdf`)
- há scripts de apoio em `dia1/scripts/`:
  - `baixar_precos.py`
  - `computar_portfolios.py`
  - `backtest_portfolios.py`
- `styles.css` contém o estilo global do deck RevealJS
- `_quarto.yml` contém a configuração global do Quarto/RevealJS
- `requirements.txt` contém dependências Python mínimas
- o dia 2 está implementado em `dia2/slides_dia2.qmd`
- o HTML renderizado do dia 2 está em `dia2/slides_dia2.html`
- `dia3/` existe, mas ainda está vazio

Conteúdo já construído no dia 1:
- introdução do instrutor e contato
- perfil dos participantes com histogramas
- mapa conceitual IA / Machine Learning / Deep Learning / LLMs
- produtos comerciais de IA
- perspectiva histórica de IA
- usos gerais de IA
- tradução desses usos para Finanças
- três exemplos-base: dados financeiros, texto financeiro e decisão corporativa
- seção prática de prompt engineering (prompt curto vs prompt detalhado)
- exemplo de dados financeiros com fluxo aplicado:
  - download de preços
  - comparação visual/dashboard
  - cálculo de portfólios
  - backtest e leitura de limitações
- ponte explícita para os dias 2 e 3

Importante para execução em nuvem:
- a planilha local de respostas na raiz do projeto contém os dados dos histogramas, mas `*.xlsx` está ignorado no `.gitignore`
- o deck do dia 1 procura automaticamente o primeiro `.xlsx` no diretório atual ou no diretório pai; não depender do nome literal da planilha, pois acentos podem variar por normalização Unicode no macOS/Dropbox
- portanto, a planilha pode não estar disponível quando o projeto for aberto fora da máquina local
- não assumir que `dia1/slides_dia1.qmd` renderiza do zero em nuvem sem antes verificar se a planilha ou uma versão derivada dos dados existe
- se for necessário tornar o render do dia 1 reprodutível em nuvem, criar uma entrada pequena e versionada com os dados agregados dos histogramas, em vez de depender da planilha bruta ignorada

Arquivos gerados/cache:
- não editar manualmente `.quarto/`, `*_files/` ou `*.quarto_ipynb*`
- regenerar esses arquivos com Quarto quando necessário
- tratar `.qmd` e `styles.css` como fontes principais
- atualizar `dia1/slides_dia1.html` após mudanças substantivas no deck, se o HTML renderizado precisar acompanhar o fonte
- `dia1/precos_acoes_brasil.csv`, `dia1/dashboard_acoes_brasil.html` e figuras em `dia1/images/` são artefatos de execução de scripts e podem ser regenerados

---

## Ambiente de Execução

Quando houver código auxiliar, ele deve ser executado no environment conda chamado:

```text
FURG
```

Assuma que, localmente:
- o environment já está criado
- as bibliotecas necessárias podem ser instaladas nele
- não se deve criar ambiente novo

Comandos preferidos:

```bash
conda run -n FURG quarto render dia1/slides_dia1.qmd
conda run -n FURG python caminho/do/script.py
```

Em ambiente de nuvem:
- não assumir caminhos absolutos de Dropbox
- usar sempre caminhos relativos ao repositório
- se o environment `FURG` não existir, usar o Python disponível apenas para inspeção ou renderização necessária, mantendo o projeto compatível com o fluxo local acima
- não versionar ambientes, caches ou diretórios `.venv/`, `env/`, `FURG/`

Dependências:
- manter dependências simples em `requirements.txt`
- priorizar `pandas`, `matplotlib` e `yfinance` quando houver demos financeiros
- para leitura de `.xlsx` com `pandas`, garantir que o environment local tenha um engine como `openpyxl` se necessário

---

## Diretrizes Gerais

### 1. Simplicidade

- Evitar abstrações desnecessárias
- Preferir código curto e legível
- Priorizar clareza sobre sofisticação

---

### 2. Código Auxiliar

- Usar Python quando houver código auxiliar
- Priorizar:
  - pandas
  - matplotlib
  - yfinance ou equivalente simples

- Evitar:
  - frameworks
  - bibliotecas pouco estáveis
  - dependências complexas
  - APIs que exigem autenticação

---

### 3. Confiabilidade

- Todo código auxiliar deve rodar sem erros
- Evitar dependências externas frágeis
- Preferir dados pequenos e exemplos que funcionem durante demonstração ao vivo
- Em demos com dados de mercado, incluir verificações simples para falhas de download ou retornos vazios

---

### 4. Reprodutibilidade

- Outputs devem ser consistentes
- Evitar aleatoriedade quando possível
- Fixar seeds quando necessário
- Não depender de arquivos locais ignorados pelo git sem registrar isso claramente no plano

---

### 5. Organização de Arquivos

Estrutura esperada:

```text
diaX/
  slides_diaX.qmd
  slides_diaX.html
  demo/
    materiais_de_apoio
    outputs/          # opcional
```

Materiais de apoio devem ser curtos, legíveis e versionáveis. Evitar datasets grandes.

---

### 6. Slides (Quarto + RevealJS)

- Slides devem ser curtos
- Usar bullet points
- Evitar blocos longos de texto
- Código deve ser simples e legível
- Usar RevealJS explicitamente via Quarto
- Reutilizar a configuração global em `_quarto.yml`
- Reutilizar o estilo global em `styles.css`
- Explorar funcionalidades do RevealJS de forma intencional e sóbria:
  - fragments
  - incremental lists
  - columns
  - callouts
  - speaker notes, quando úteis
- Evitar efeitos espalhafatosos, transições chamativas ou excesso de animações
- Priorizar uma apresentação sóbria, clara e profissional

### 6.1 Plots e Gráficos

- Todas as fontes de todos os plots devem ser Arial
- Em matplotlib, definir explicitamente:
  `plt.rcParams["font.family"] = "Arial"`
- Quando possível, os plots devem tentar usar as cores base da FURG:
  - vermelho: RGB `(163, 18, 41)` / `#A31229`
  - laranja: RGB `(199, 120, 36)` / `#C77824`
  - amarelo: RGB `(229, 173, 42)` / `#E5AD2A`
- As cores podem ser adaptadas conforme a ocasião, especialmente para legibilidade, contraste, acessibilidade ou clareza analítica
- Gráficos devem ser legíveis em tela projetada
- Evitar paletas confusas, excesso de séries e rótulos pequenos

---

### 7. Materiais de Demonstração

- As pastas `demo/` devem conter material de apoio para demonstrações
- Não assumir a existência de scripts executáveis para os demos
- Quando houver código auxiliar, ele deve ser simples, curto e não interativo
- Para o dia 3, a ideia central é demonstrar o uso de agents ao vivo; os materiais devem orientar a execução, não substituir a demonstração por scripts prontos

---

### 8. Tratamento de Erros

- Priorizar código robusto
- Evitar falhas durante execução ao vivo
- Usar verificações simples quando necessário
- Em downloads de dados, tratar retorno vazio, ticker inválido e falta de conexão com mensagens claras

---

### 9. Performance

- Quando houver código auxiliar, o tempo de execução deve ser curto, idealmente abaixo de 5 segundos
- Evitar datasets grandes
- Evitar loops, modelos ou chamadas externas que possam atrasar a demonstração

---

### 10. Evitar Overengineering

Não introduzir:
- pipelines complexos
- arquitetura sofisticada
- configurações desnecessárias
- frameworks para tarefas que cabem em um script Python curto

---

## Objetivo Geral

Gerar materiais simples, confiáveis e adequados para demonstrações ao vivo.
