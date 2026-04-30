# Gerado pelo Gemini via prompt nos slides!

import yfinance as yf
import pandas as pd
from datetime import date
import os

# Definir parâmetros do exercício
tickers = ['PETR4.SA', 'VALE3.SA', 'ITUB4.SA', 'ABEV3.SA', 'WEGE3.SA']
benchmark = '^BVSP'
benchmark_label = 'IBOV'

# Calcular o intervalo de 20 anos com base na data atual
start_date = date.today().replace(year=date.today().year - 20).isoformat()
end_date = date.today().isoformat()

valid_stocks = []
all_data = []

print("Baixando dados das ações...")
for tk in tickers:
    try:
        # Download dos dados
        df = yf.download(tk, start=start_date, end=end_date, auto_adjust=True, progress=False)
        
        if not df.empty and 'Close' in df.columns:
            # Filtra os dados e remove valores vazios
            df = df[['Close']].dropna().reset_index()
            df.columns = ['date', 'adjusted_close']
            df['ticker'] = tk
            
            if not df.empty:
                all_data.append(df)
                valid_stocks.append(tk)
        else:
            print(f"Aviso: O ticker {tk} não retornou dados válidos.")
    except Exception as e:
        print(f"Erro ao baixar os dados do ticker {tk}: {e}")

print("\nBaixando dados do benchmark (IBOV)...")
ibov_df = None
try:
    df_ibov = yf.download(benchmark, start=start_date, end=end_date, auto_adjust=True, progress=False)
    
    if not df_ibov.empty and 'Close' in df_ibov.columns:
        ibov_df = df_ibov[['Close']].dropna().reset_index()
        ibov_df.columns = ['date', 'adjusted_close']
        ibov_df['ticker'] = benchmark_label
except Exception as e:
    print(f"Erro ao baixar o benchmark {benchmark}: {e}")

# Verificação dos requisitos 10 e 11
if ibov_df is None or ibov_df.empty:
    raise SystemExit("Erro crítico: O índice IBOV falhou ou está vazio. O script será encerrado.")

if len(valid_stocks) < 3:
    raise SystemExit(f"Erro crítico: Apenas {len(valid_stocks)} ações foram carregadas com sucesso. Mínimo necessário: 3. O script será encerrado.")

# Concatena todos os dataframes válidos
final_df = pd.concat(all_data + [ibov_df], ignore_index=True)

# Define o caminho do arquivo na mesma pasta onde o script está salvo
script_dir = os.path.dirname(os.path.abspath(__file__))
output_path = os.path.join(script_dir, "precos_acoes_brasil.csv")

# Salva o arquivo CSV
final_df.to_csv(output_path, index=False)

# Exibe o resultado e a contagem de observações
print(f"\nSucesso! Arquivo salvo em: {output_path}")
print("Observações válidas por ativo:")
for tk in valid_stocks + [benchmark_label]:
    count = len(final_df[final_df['ticker'] == tk])
    print(f"- {tk}: {count} observações")