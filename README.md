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
  dia2/
    slides_dia2.qmd     # fonte principal do deck — Dia 2
    slides_dia2.html    # HTML renderizado (não editar manualmente)
  dia3/                 # a construir
    slides_dia3.qmd     # fonte principal do deck — Dia 3
    slides_dia3.html    # HTML renderizado (não editar manualmente)
    demo/
      materiais_dados_financeiros/
      materiais_sentimento/
      materiais_valuation/
```

Arquivos gerados automaticamente — **não editar manualmente**:

- `.quarto/`
- `*.quarto_ipynb*`

Exceção de publicação:

- `dia1/slides_dia1_files/` e `dia2/slides_dia2_files/` são gerados pelo Quarto, mas precisam ficar versionados porque os HTMLs renderizados dependem desses assets no GitHub Pages.

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

### Dias 2 e 3

```bash
conda run -n FURG quarto render dia2/slides_dia2.qmd
conda run -n FURG quarto render dia3/slides_dia3.qmd
```

## Publicação no GitHub Pages

O repositório está preparado para ser publicado como Project Page:

- Página inicial: <https://rgriva.github.io/minicurso_FURG_SBFin/>
- Slides do Dia 1: <https://rgriva.github.io/minicurso_FURG_SBFin/dia1/slides_dia1.html>
- Slides do Dia 2: <https://rgriva.github.io/minicurso_FURG_SBFin/dia2/slides_dia2.html>
- Dashboard do Exemplo 1: <https://rgriva.github.io/minicurso_FURG_SBFin/dia1/dashboard_acoes_brasil.html>

Configuração recomendada no GitHub:

1. Acesse `Settings > Pages` no repositório.
2. Em `Build and deployment`, selecione `Deploy from a branch`.
3. Use branch `main` e pasta `/(root)`.
4. Salve a configuração.

Notas:

- O arquivo `.nojekyll` instrui o GitHub Pages a servir os HTMLs estáticos diretamente, sem processamento adicional por Jekyll.
- O arquivo `index.html` na raiz lista os links para os dias disponíveis.
- As pastas `dia1/slides_dia1_files/` e `dia2/slides_dia2_files/` devem ser commitadas junto com seus respectivos HTMLs, pois contêm JavaScript, CSS, fontes e figuras usados pelos decks renderizados.
- O dashboard `dia1/dashboard_acoes_brasil.html` é autocontido e pesa cerca de 8,4 MB. Ele está dentro dos limites do GitHub Pages, mas pode demorar um pouco para carregar em redes lentas.
- Para testar localmente antes de publicar:

```bash
python3 -m http.server 8000
```

Depois abra <http://localhost:8000/>.

---

## Conteúdo por dia

### Dia 1 — Fundamentos ✅

- Introdução do instrutor e perfil dos participantes
- Mapa conceitual: IA → Machine Learning → Deep Learning → LLMs
- Produtos comerciais de IA
- Perspectiva histórica
- Usos gerais de IA e sua tradução para Finanças
- Três exemplos-base: dados financeiros, texto financeiro e decisão corporativa

### Dia 2 — Ferramentas ✅

- Chat na web, prompting e gerenciamento de contexto
- Preços e decisão de assinatura
- ChatGPT, Claude, Gemini, Microsoft Copilot e Perplexity
- GitHub Copilot vs Cursor para código
- NotebookLM, Perplexity e Deep Research para documentos e fontes
- Terminal básico antes de workflows com agentes
- Claude Code, Codex, GitHub Copilot agent mode e Cursor Agent
- APIs, tokens, chaves, privacidade e automação

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
