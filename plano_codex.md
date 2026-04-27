# Plano de Implementação (Codex)

## Estrutura do Projeto

2026_FURG/
  dia1/
    slides.qmd
    demo/
  dia2/
    slides.qmd
    demo/
  dia3/
    slides.qmd
    demo/
      materiais_dados_financeiros
      materiais_sentimento
      materiais_valuation

---

## Diretrizes

- Seguir as regras permanentes em `AGENTS.md`
- Este arquivo define apenas o roteiro de conteúdo e implementação

---

## DIA 1 — Aplicações em Finanças

### Objetivo

Mostrar aplicações práticas de IA em:
- dados financeiros
- texto
- decisões

Observação:
- os histogramas dos participantes serão preparados depois
- não incluir scripts de histogramas neste momento

---

### slides.qmd deve conter

#### Bloco 1 — O que IA faz bem

- leitura de texto
- geração de código
- análise simples

---

#### Bloco 2 — Aplicações

##### 1. Dados financeiros

- baixar preços
- calcular retornos
- plotar gráfico

---

##### 2. Análise de sentimento

- classificar texto
- resumir notícia

---

##### 3. Finanças corporativas (OBRIGATÓRIO)

**Avaliação de projeto**

Exemplo:
- investimento inicial
- receita esperada
- custos

Output:
- análise de cenários:
  - otimista
  - base
  - pessimista

---

## DIA 2 — Ferramentas

### Objetivo

Ensinar uso de ferramentas de IA

---

### slides.qmd deve conter

#### 1. Chatbots

- estrutura de prompt
- iteração

---

#### 2. Ferramentas

Cobrir:

- GitHub Copilot
- OpenAI Codex
- Claude Code
- Cursor

---

#### 3. Agentic Workflow

Fluxo padrão:

1. definir problema
2. gerar código
3. executar
4. corrigir
5. iterar

---

#### 4. Terminal (breve)

- noções básicas de terminal
- navegar pastas

---

#### 5. Custos

- assinatura mensal
- API usage

---

## DIA 3 — DEMO

### Objetivo

Conduzir 3 exemplos completos usando agents, com material de apoio nas pastas `demo/`.

Observação:
- não haverá scripts prontos para os demos
- os materiais devem orientar a execução ao vivo pelos agents

---

## DEMO 1 — Análise de Dados (Setor)

Material:
demo/materiais_dados_financeiros

### Função

- baixar dados de múltiplas empresas de um setor
- calcular retornos
- plotar gráfico comparativo
- demonstrar o fluxo com apoio de agents, sem script pronto

### Inputs

- lista de tickers

### Outputs

- gráfico de preços
- gráfico de retornos

---

## DEMO 2 — Sentimento (Política Monetária Brasil)

Material:
demo/materiais_sentimento

### Função

- analisar texto (ata do COPOM ou similar)
- demonstrar o fluxo com apoio de agents, sem script pronto

### Outputs

- classificação de sentimento
- resumo curto
- pontos principais

---

## DEMO 3 — Valuation (Projeto Agro)

Material:
demo/materiais_valuation

### Problema

Decidir entre plantar soja ou milho

---

### Inputs

- investimento inicial
- preço esperado
- custo
- produtividade

---

### Lógica

- construir 3 cenários:
  - otimista
  - base
  - pessimista

- calcular lucro esperado

---

### Outputs

- tabela com cenários
- recomendação simples

---

## Regras para os Materiais de Apoio

As pastas `demo/` devem conter apenas materiais de apoio, como:
- dados pequenos
- textos-base
- instruções curtas
- resultados esperados
- prompts ou roteiros de execução

---

## Prioridades

1. material claro
2. outputs esperados bem definidos
3. simplicidade
