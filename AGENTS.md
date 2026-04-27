# AGENTS.md

## Visão Geral do Projeto

Este repositório contém materiais para um minicurso de Inteligência Artificial aplicada a Finanças.

Estrutura:

2026_FURG/
  dia1/
  dia2/
  dia3/

Cada dia contém:
- Slides (Quarto + RevealJS)
- Scripts de demonstração (Python, quando aplicável)

---

## Ambiente de Execução

Todo o código deve ser executado no environment conda chamado:

FURG

Assuma que:
- O environment já está criado
- As bibliotecas necessárias podem ser instaladas nele

Não criar ambientes novos.

---

## Diretrizes Gerais de Implementação

### 1. Simplicidade

- Evitar abstrações desnecessárias
- Preferir código curto e legível
- Priorizar clareza sobre sofisticação

---

### 2. Linguagem e Bibliotecas

- Usar Python
- Priorizar:
  - pandas
  - matplotlib
  - yfinance (ou equivalente)

- Evitar:
  - frameworks
  - bibliotecas pouco estáveis
  - dependências complexas

---

### 3. Confiabilidade

- Todo código deve rodar sem erros
- Evitar dependências externas frágeis
- Evitar APIs que exigem autenticação

---

### 4. Reprodutibilidade

- Outputs devem ser consistentes
- Evitar aleatoriedade quando possível
- Fixar seeds se necessário

---

### 5. Organização de Arquivos

Estrutura esperada:

diaX/
  slides.qmd
  demo/
    script.py
    outputs/ (opcional)

---

### 6. Slides (Quarto + RevealJS)

- Slides devem ser curtos
- Usar bullet points
- Evitar blocos longos de texto
- Código deve ser simples e legível

---

### 7. Scripts de Demonstração

- Devem rodar via terminal:
  python script.py

- Devem:
  - produzir output visível (gráficos, tabelas, prints)
  - não depender de input interativo

---

### 8. Tratamento de Erros

- Priorizar código robusto
- Evitar falhas durante execução ao vivo
- Usar verificações simples quando necessário

---

### 9. Performance

- Tempo de execução deve ser curto (<5 segundos)
- Evitar datasets grandes

---

### 10. Evitar Overengineering

Não introduzir:
- pipelines complexos
- arquitetura sofisticada
- configurações desnecessárias

---

## Objetivo

Gerar código que seja:

- Simples
- Confiável
- Executável em tempo real
- Adequado para demonstrações ao vivo
