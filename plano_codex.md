# Plano de Implementação (Codex)

## Estrutura do Projeto

2026_FURG/
  dia1/
    slides.qmd
  dia2/
    slides.qmd
  dia3/
    slides.qmd
    demo/
      data_analysis.py
      sentiment_analysis.py
      corporate_valuation.py

---

## DIA 1 — Aplicações em Finanças

### Objetivo

Mostrar aplicações práticas de IA em:
- dados financeiros
- texto
- decisões

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

- rodar script python
- navegar pastas

---

#### 5. Custos

- assinatura mensal
- API usage

---

## DIA 3 — DEMO

### Objetivo

Executar 3 exemplos completos usando agents

---

## DEMO 1 — Análise de Dados (Setor)

Arquivo:
data_analysis.py

### Função

- baixar dados de múltiplas empresas de um setor
- calcular retornos
- plotar gráfico comparativo

### Inputs

- lista de tickers

### Outputs

- gráfico de preços
- gráfico de retornos

---

## DEMO 2 — Sentimento (Política Monetária Brasil)

Arquivo:
sentiment_analysis.py

### Função

- analisar texto (ata do COPOM ou similar)

### Outputs

- classificação de sentimento
- resumo curto
- pontos principais

---

## DEMO 3 — Valuation (Projeto Agro)

Arquivo:
corporate_valuation.py

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

## Regras para os Scripts

- devem rodar com:
  python script.py

- devem:
  - imprimir resultados
  - gerar gráficos (quando aplicável)

---

## Prioridades

1. código funcionando
2. outputs claros
3. simplicidade

---

## Evitar

- bibliotecas complexas
- código longo
- dependências externas frágeis
