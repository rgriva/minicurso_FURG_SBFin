# Plano de Implementação (Codex)

Este arquivo é o mapa de continuidade do projeto. `AGENTS.md` contém as regras permanentes; este plano registra o estado atual, decisões tomadas e próximos passos.

Última atualização: 2026-05-01.

---

## Leitura Rápida para Futuras Sessões

- Projeto: minicurso de Inteligência Artificial aplicada a Finanças, FURG / Escola SBFin
- Fonte principal do dia 1: `dia1/slides_dia1.qmd`
- Fonte principal do dia 2: `dia2/slides_dia2.qmd`
- HTML renderizado do dia 1: `dia1/slides_dia1.html`
- HTML renderizado do dia 2: `dia2/slides_dia2.html`
- Estilo global: `styles.css`
- Configuração Quarto: `_quarto.yml`
- Ambiente local esperado: conda `FURG`
- Comando local preferido:

```bash
conda run -n FURG quarto render dia1/slides_dia1.qmd
conda run -n FURG quarto render dia2/slides_dia2.qmd
```

Ponto crítico para nuvem:
- os histogramas do dia 1 dependem da planilha local de respostas na raiz do projeto
- essa planilha está ignorada por `*.xlsx` no `.gitignore`
- o deck procura automaticamente o primeiro `.xlsx` no diretório atual ou no diretório pai; não depender do nome literal da planilha, pois acentos podem variar por normalização Unicode no macOS/Dropbox
- uma sessão em nuvem pode não conseguir renderizar o dia 1 do zero sem esse arquivo
- solução futura recomendada: salvar dados agregados dos histogramas em arquivo pequeno versionado, ou adaptar o deck para fallback claro quando a planilha estiver ausente

---

## Estrutura Atual

```text
2026_FURG/
  AGENTS.md
  README.md
  index.html
  plano_codex.md
  _quarto.yml
  styles.css
  requirements.txt
  *.xlsx local com respostas dos participantes          # ignorado pelo git
  dia1/
    slides_dia1.qmd
    slides_dia1.html
    slides_dia1.quarto_ipynb
    precos_acoes_brasil.csv
    dashboard_acoes_brasil.html
    images/
      QR_code.png
      github_repo_QR.png
      backtest_retorno.png/.pdf
      backtest_drawdown.png/.pdf
      backtest_tabela.png/.pdf
      outros PNGs de apoio visual dos exemplos
    scripts/
      baixar_precos.py
      computar_portfolios.py
      backtest_portfolios.py
    slides_dia1_files/                                   # render/cache RevealJS
  dia2/
    slides_dia2.qmd
    slides_dia2.html
    slides_dia2_files/                                 # render/cache RevealJS
  dia3/
```

Arquivos gerados ou cache que não devem ser editados manualmente:
- `.quarto/`
- `dia1/slides_dia1_files/`
- `dia2/slides_dia2_files/`
- `*.quarto_ipynb*`

---

## Estado Atual do Dia 1

Status: conteúdo principal construído e bloco prático de dados financeiros já materializado com scripts e outputs.

O deck `dia1/slides_dia1.qmd` já contém:
- título, autor, data e metadados Quarto
- setup Python com `pandas` e `matplotlib`
- fontes Arial nos plots
- paleta FURG nos gráficos e elementos visuais
- função para localizar a planilha no diretório atual ou no pai
- limpeza simples das respostas dos participantes
- normalização de cursos para os histogramas
- introdução do instrutor e QR code de contato
- perfil dos participantes:
  - grau de ensino
  - curso
  - conforto com programação
  - percepção sobre IA
- plano de voo dos três dias
- mapa conceitual de IA, ML, Deep Learning e LLMs
- produtos comerciais de IA
- perspectiva histórica
- explicação simples de ML
- diferença entre modelo, produto e integração
- prática de prompts (pedido pouco detalhado vs pedido bem especificado)
- usos gerais de IA
- usos de IA em Finanças
- exemplo de dados financeiros com artefatos concretos:
  - `dia1/scripts/baixar_precos.py`: baixa preços com validações e gera `dia1/precos_acoes_brasil.csv`
  - `dia1/scripts/computar_portfolios.py`: calcula alocações (tangência, mínima variância e risk parity)
  - `dia1/scripts/backtest_portfolios.py`: executa backtest com rebalanceamento mensal e gera figuras em `dia1/images/`
  - `dia1/dashboard_acoes_brasil.html`: dashboard exportado do exemplo
- exemplos-base no fechamento do dia:
  - dados financeiros
  - texto financeiro
  - decisão corporativa
- ponte para os dias 2 e 3

`styles.css` já contém estilos para:
- links e códigos inline em vermelho FURG
- callouts customizados
- setas e fluxos visuais
- cards conceituais
- tabela de produtos
- linha do tempo
- grades de workflow

---

## Pendências do Dia 1

Antes de considerar o dia 1 fechado:
- renderizar novamente após qualquer mudança substancial
- revisar visualmente `dia1/slides_dia1.html`
- decidir se o projeto precisa renderizar integralmente em nuvem sem a planilha local
- se sim, criar dados agregados versionados para os histogramas ou remover a dependência direta da planilha ignorada
- adicionar speaker notes apenas onde ajudarem a execução ao vivo
- decidir quais artefatos gerados em `dia1/images/` e `dia1/dashboard_acoes_brasil.html` devem ser mantidos como referência permanente no repositório

---

## Dia 2 -- Ferramentas

Status: deck construído e renderizado em `dia2/slides_dia2.html`.

Objetivo:
- ensinar uso prático de ferramentas de IA, com menos ênfase em Finanças e mais foco em escolha de ferramenta, preço, prompting, contexto, agentes e APIs.

O deck `dia2/slides_dia2.qmd` cobre:
- chat na web: ChatGPT, Claude, Gemini, Microsoft Copilot e Perplexity
- preços e faixas de custo, com fontes oficiais verificadas em 2026-05-01
- boas práticas de prompt, contexto, validação e escolha entre modelos grandes/pequenos
- GitHub Copilot vs Cursor para ajuda a escrever código
- ferramentas especializadas: NotebookLM, Perplexity e Deep Research
- terminal mínimo antes de agentes: `pwd`, `ls`, `cd`, execução, erro, `git status` e `git diff`
- agentes: Claude Code, Codex, Copilot agent mode e Cursor Agent
- APIs: tokens, chaves, limites, privacidade e automação
- sete microdemos guiadas para execução ao vivo, sem scripts ou datasets novos

Direção de estilo:
- manter o foco em fluxo de trabalho, não em comparação promocional de ferramentas
- usar exemplos pequenos e mistos, preparando o dia 3 sem substituir as demos ao vivo

---

## Dia 3 -- Demos com Agents

Status: ainda não construído.

Objetivo:
- conduzir três exemplos completos usando agents, com material de apoio nas pastas `demo/`
- não criar scripts prontos que substituam a demonstração
- criar materiais curtos que orientem o que o agent deve fazer ao vivo

Estrutura planejada:

```text
dia3/
  slides_dia3.qmd
  slides_dia3.html
  demo/
    materiais_dados_financeiros/
    materiais_sentimento/
    materiais_valuation/
```

### Demo 1 -- Análise de Dados Financeiros

Material:
- `dia3/demo/materiais_dados_financeiros/`

Função:
- baixar dados de múltiplas empresas de um setor
- calcular retornos
- plotar gráfico comparativo
- demonstrar o fluxo com apoio de agents, sem script pronto

Inputs:
- lista pequena de tickers

Outputs esperados:
- gráfico de preços
- gráfico de retornos
- interpretação curta

Observações:
- usar `yfinance` ou equivalente simples
- tratar falha de download ou retorno vazio
- manter tempo de execução curto

### Demo 2 -- Sentimento em Texto Financeiro

Material:
- `dia3/demo/materiais_sentimento/`

Função:
- analisar texto, preferencialmente ata do COPOM, notícia de mercado ou trecho de relatório
- demonstrar resumo, classificação e pontos principais com apoio de agents

Outputs esperados:
- resumo curto
- classificação de tom/sentimento
- principais evidências textuais
- ressalvas de validação humana

Observações:
- evitar depender de API paga ou autenticada
- se usar texto externo, salvar trecho curto e versionável como material de apoio

### Demo 3 -- Valuation / Projeto Agro

Material:
- `dia3/demo/materiais_valuation/`

Problema:
- decidir entre plantar soja ou milho

Inputs:
- investimento inicial
- preço esperado
- custo
- produtividade
- cenários otimista, base e pessimista

Outputs esperados:
- tabela de cenários
- lucro esperado por cultura
- recomendação simples
- lista curta de riscos e hipóteses

Observações:
- manter a matemática transparente
- preferir tabela pequena a modelo sofisticado

---

## Regras para Materiais de Apoio

As pastas `demo/` devem conter apenas materiais de apoio, como:
- dados pequenos
- textos-base
- instruções curtas
- resultados esperados
- prompts ou roteiros de execução

Não introduzir:
- datasets grandes
- pipelines
- notebooks complexos
- dependências instáveis
- APIs com autenticação

---

## Prioridades

1. material claro
2. demonstrações que rodam ao vivo
3. outputs esperados bem definidos
4. compatibilidade com execução local no conda `FURG`
5. consciência explícita das diferenças entre ambiente local e nuvem
