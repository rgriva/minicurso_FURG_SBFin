# IA Aplicada a Finanças

Materiais do minicurso **IA Aplicada a Finanças**, ministrado por **[Raul Riva](https://rgriva.github.io)** na
[Escola SBFin — edição FURG](https://www.linkedin.com/events/escolasbfin-edi-ofurg7445593378785796097/),
em maio de 2026.

## Links principais

- **Landing page:** <https://rgriva.github.io/minicurso_FURG_SBFin/>
- **Slides — Dia 1:** <https://rgriva.github.io/minicurso_FURG_SBFin/dia1/slides_dia1.html>
- **Slides — Dia 2:** <https://rgriva.github.io/minicurso_FURG_SBFin/dia2/slides_dia2.html>
- **Slides — Dia 3:** <https://rgriva.github.io/minicurso_FURG_SBFin/dia3/slides_dia3.html>
- **Material de apoio — Dia 3 / projeto de investimento:** <https://rgriva.github.io/minicurso_FURG_SBFin/dia3/demo/projeto_investimento/premissas_projeto_investimento.csv>
- **Material de apoio — Dia 3 / skill de gráficos:** <https://rgriva.github.io/minicurso_FURG_SBFin/dia3/demo/skill_plot_financeiro/AGENTS.md>

## Ementa

### Dia 1 — Fundamentos

- O que são IA, Machine Learning, Deep Learning e LLMs
- Como produtos de IA se conectam a modelos e interfaces
- Boas práticas iniciais de prompting
- Aplicações de IA em Finanças
- Exemplo aplicado com dados financeiros, carteiras e backtest

### Dia 2 — Ferramentas

- Como escolher a ferramenta certa para cada tarefa
- Custos, assinaturas e decisão de uso
- Boas práticas de prompt, contexto e validação
- Chatbots, copilots, pesquisa com fontes e NotebookLM
- Terminal mínimo para trabalhar com código
- Agentes: fluxos de trabalho, limites e riscos

### Dia 3 — Demos com agents

- Dados financeiros: preços, retornos e comparações
- Sentimento em texto financeiro: atas, notícias e classificação
- Valuation / projeto agro: cenários, risco e decisão

## Mapa do repositório

```text
2026_FURG/
  index.html          # landing page publicada no GitHub Pages
  requirements.txt    # dependências Python dos exemplos
  dia1/               # slides e materiais do Dia 1
  dia2/               # slides e materiais do Dia 2
  dia3/               # slides e materiais do Dia 3
  AGENTS.md           # notas de manutenção para uso com agents
```

## Instalação

Para instalar as dependências Python usadas nos exemplos:

```bash
conda run -n FURG pip install -r requirements.txt
```

Se for necessário renderizar materiais que leem planilhas `.xlsx`, instale também:

```bash
conda run -n FURG pip install openpyxl
```

## Contato

[Raul Riva](https://rgriva.github.io) · [rgriva.github.io](https://rgriva.github.io) · [@rgriva](https://github.com/rgriva)
