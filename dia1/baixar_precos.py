from datetime import datetime
from pathlib import Path
import pandas as pd
import yfinance as yf

tickers = ["PETR4.SA", "VALE3.SA", "ITUB4.SA", "ABEV3.SA", "WEGE3.SA"]
output_file = Path(__file__).resolve().parent / "precos_acoes_brasil.csv"

end_date = datetime.today()
start_date = end_date.replace(year=end_date.year - 20)

valid_parts = []

for ticker in tickers:
    print(f"Baixando {ticker}...")

    try:
        data = yf.download(
            ticker,
            start=start_date,
            end=end_date,
            interval="1d",
            auto_adjust=True,
            progress=False,
        )

        if data.empty or "Close" not in data.columns:
            print(f"Aviso: {ticker} não retornou dados válidos.")
            continue

        temp = data[["Close"]].reset_index()
        temp.columns = ["date", "adjusted_close"]
        temp["ticker"] = ticker
        temp = temp[["date", "ticker", "adjusted_close"]]
        temp = temp.dropna(subset=["adjusted_close"])

        n_obs = len(temp)

        if n_obs == 0:
            print(f"Aviso: {ticker} não tem preços válidos.")
            continue

        print(f"{ticker}: {n_obs} observações válidas.")
        valid_parts.append(temp)

    except Exception as e:
        print(f"Aviso: falha ao baixar {ticker}. Erro: {e}")

if len(valid_parts) < 3:
    raise SystemExit(
        f"Erro: apenas {len(valid_parts)} tickers têm dados válidos. "
        "É necessário ter pelo menos 3."
    )

prices = pd.concat(valid_parts, ignore_index=True)

counts = prices.groupby("ticker")["adjusted_close"].count()
print("\nObservações válidas por ticker:")
print(counts)

prices.to_csv(output_file, index=False)

print(f"\nArquivo salvo com sucesso: {output_file}")