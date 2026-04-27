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
- Materiais de demonstração em `demo/`, quando aplicável

---

## Ambiente de Execução

Quando houver código auxiliar, ele deve ser executado no environment conda chamado:

FURG

Assuma que:
- O environment já está criado
- As bibliotecas necessárias podem ser instaladas nele

Não criar ambientes novos.

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
  - yfinance (ou equivalente)

- Evitar:
  - frameworks
  - bibliotecas pouco estáveis
  - dependências complexas

---

### 3. Confiabilidade

- Todo código auxiliar deve rodar sem erros
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
    materiais_de_apoio
    outputs/ (opcional)

---

### 6. Slides (Quarto + RevealJS)

- Slides devem ser curtos
- Usar bullet points
- Evitar blocos longos de texto
- Código deve ser simples e legível
- Usar RevealJS explicitamente via Quarto
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
- As cores podem ser adaptadas conforme a ocasião, especialmente para legibilidade,
  contraste, acessibilidade ou clareza analítica
- Gráficos devem ser legíveis em tela projetada
- Evitar paletas confusas, excesso de séries e rótulos pequenos

---

### 7. Materiais de Demonstração

- As pastas `demo/` devem conter material de apoio para as demonstrações
- Não assumir a existência de scripts executáveis para os demos
- Quando houver código auxiliar, ele deve ser simples, curto e não interativo

---

### 8. Tratamento de Erros

- Priorizar código robusto
- Evitar falhas durante execução ao vivo
- Usar verificações simples quando necessário

---

### 9. Performance

- Quando houver código auxiliar, o tempo de execução deve ser curto (<5 segundos)
- Evitar datasets grandes

---

### 10. Evitar Overengineering

Não introduzir:
- pipelines complexos
- arquitetura sofisticada
- configurações desnecessárias

---

## Objetivo Geral

Gerar materiais simples, confiáveis e adequados para demonstrações ao vivo.
