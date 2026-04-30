# IA Aplicada a Finanças

Materiais do minicurso **IA Aplicada a Finanças**, ministrado por **Raul Riva** na
[Escola SBFin — edição FURG](https://www.linkedin.com/events/escolasbfin-edi-ofurg7445593378785796097/),
maio de 2026.

---

## Estrutura do repositório

```text
2026_FURG/
  _quarto.yml           # configuração global Quarto / RevealJS
  styles.css            # estilo visual global (cores FURG, layout)
  requirements.txt      # dependências Python mínimas
  AGENTS.md             # regras permanentes para agents / Codex
  plano_codex.md        # estado atual e próximos passos
  dia1/
    slides_dia1.qmd     # fonte principal do deck — Dia 1
    slides_dia1.html    # HTML renderizado (não editar manualmente)
    QR_code.png         # QR de contato do instrutor
    github_repo_QR.png  # QR do repositório GitHub
  dia2/                 # a construir
  dia3/                 # a construir
    demo/
      materiais_dados_financeiros/
      materiais_sentimento/
      materiais_valuation/
```

Arquivos gerados automaticamente — **não editar manualmente**:

- `.quarto/`
- `dia1/slides_dia1_files/`
- `*.quarto_ipynb*`

---

## Pré-requisitos

| Ferramenta | Versão mínima | Observação |
|---|---|---|
| [Quarto](https://quarto.org/docs/get-started/) | 1.4+ | necessário para renderizar os slides |
| conda env `FURG` | — | ambiente local já criado; ver abaixo |
| Python | 3.10+ | gerenciado pelo conda |

Instalar dependências Python no ambiente local:

```bash
conda run -n FURG pip install -r requirements.txt
conda run -n FURG pip install openpyxl   # necessário para leitura de .xlsx no dia 1
```

---

## Como renderizar

### Dia 1

```bash
conda run -n FURG quarto render dia1/slides_dia1.qmd
```

> **Atenção — planilha de respostas:** o deck do Dia 1 gera histogramas a partir
> de uma planilha `.xlsx` com as respostas dos participantes. Esse arquivo está
> **ignorado pelo git** (regra `*.xlsx` no `.gitignore`) e não está disponível
> em ambientes de nuvem ou em outras máquinas. O deck procura automaticamente o
> primeiro `.xlsx` no diretório atual ou no diretório pai — não dependa do nome
> literal do arquivo. Sem a planilha, a renderização falhará nos slides de perfil
> dos participantes.

### Dias 2 e 3 (a construir)

```bash
conda run -n FURG quarto render dia2/slides.qmd
conda run -n FURG quarto render dia3/slides.qmd
```

---

## Conteúdo por dia

### Dia 1 — Fundamentos ✅

- Introdução do instrutor e perfil dos participantes
- Mapa conceitual: IA → Machine Learning → Deep Learning → LLMs
- Produtos comerciais de IA
- Perspectiva histórica
- Usos gerais de IA e sua tradução para Finanças
- Três exemplos-base: dados financeiros, texto financeiro e decisão corporativa

### Dia 2 — Ferramentas 🔲

- Chatbots e estrutura básica de prompt
- Fluxo de iteração: pedir, avaliar, corrigir, refinar
- Ferramentas: ChatGPT, GitHub Copilot, OpenAI Codex, Claude Code, Cursor
- Agentic workflow aplicado a Finanças
- Terminal básico: navegar pastas, rodar scripts, interpretar erros
- Custos: assinatura, API, limites e dados sensíveis

### Dia 3 — Demos com Agents 🔲

Três demonstrações ao vivo com suporte de agents:

1. **Dados financeiros** — baixar preços de múltiplas empresas, calcular retornos e plotar comparativo
2. **Sentimento em texto financeiro** — resumir e classificar ata do COPOM ou notícia de mercado
3. **Valuation / Projeto Agro** — decidir entre soja e milho com tabela de cenários e análise de risco

---

## Convenções visuais

- Slides RevealJS, resolução **1280 × 720**
- Fonte dos plots: **Arial** (`plt.rcParams["font.family"] = "Arial"`)
- Paleta de cores FURG:

| Cor | Hex | RGB |
|---|---|---|
| Vermelho | `#A31229` | 163, 18, 41 |
| Laranja | `#C77824` | 199, 120, 36 |
| Amarelo | `#E5AD2A` | 229, 173, 42 |

---

## Para agents e Codex

- **[`AGENTS.md`](AGENTS.md)** — regras permanentes: convenções de código, estilo, organização de arquivos e diretrizes de execução
- **[`plano_codex.md`](plano_codex.md)** — estado atual do projeto, decisões tomadas e próximos passos

Sempre leia esses dois arquivos antes de propor ou implementar mudanças.

---

## Contato

Raul Riva · [rgriva.github.io](https://rgriva.github.io) · [@rgriva](https://github.com/rgriva)
