# Criado pelo Claude com prompt dos slides.
import pandas as pd
import numpy as np
from scipy.optimize import minimize

# ── 1. Carrega e prepara os dados ─────────────────────────────────────────────
df = pd.read_csv("dia1/precos_acoes_brasil.csv", parse_dates=["date"])
prices = df.pivot(index="date", columns="ticker", values="adjusted_close")

# Exclui IBOV; mantém apenas ações
stocks = prices.drop(columns=["IBOV"])

# Retornos logarítmicos diários
rets = np.log(stocks / stocks.shift(1)).dropna()

# ── 2. Parâmetros anualizados ─────────────────────────────────────────────────
T   = 252
mu  = rets.mean() * T          # retorno esperado anual
cov = rets.cov()  * T          # covariância anual
n   = len(stocks.columns)
rf  = 0.1075                   # taxa livre de risco

# ── 3. Funções auxiliares ─────────────────────────────────────────────────────
def portfolio_stats(w, mu, cov):
    ret = w @ mu
    vol = np.sqrt(w @ cov @ w)
    sr  = (ret - rf) / vol
    return ret, vol, sr

constraints = [{"type": "eq", "fun": lambda w: w.sum() - 1}]
bounds = [(0, 1)] * n
w0 = np.ones(n) / n

# ── 4. Portfólio de tangência (máximo Sharpe) ─────────────────────────────────
neg_sharpe = lambda w: -portfolio_stats(w, mu, cov)[2]
res_tan = minimize(neg_sharpe, w0, method="SLSQP",
                   bounds=bounds, constraints=constraints)
w_tan = res_tan.x

# ── 5. Mínima variância ───────────────────────────────────────────────────────
res_mv = minimize(lambda w: w @ cov @ w, w0, method="SLSQP",
                  bounds=bounds, constraints=constraints)
w_mv = res_mv.x

# ── 6. Risk parity ────────────────────────────────────────────────────────────
def risk_parity_obj(w, cov):
    vol  = np.sqrt(w @ cov @ w)
    rc   = w * (cov @ w) / vol    # contribuições de risco
    target = vol / n
    return np.sum((rc - target) ** 2)

res_rp = minimize(risk_parity_obj, w0, args=(cov,), method="SLSQP",
                  bounds=bounds, constraints=constraints,
                  options={"ftol": 1e-14, "maxiter": 5000})
w_rp = res_rp.x

# ── 7. Output ─────────────────────────────────────────────────────────────────
tickers = stocks.columns.tolist()
print(f"{'Ticker':<12} {'Tangência':>12} {'Mín. Var.':>12} {'Risk Parity':>12}")
for i, t in enumerate(tickers):
    print(f"{t:<12} {w_tan[i]*100:>11.1f}%  {w_mv[i]*100:>11.1f}%  {w_rp[i]*100:>11.1f}%")

for label, w in [("Tangência", w_tan), ("Mín. Variância", w_mv), ("Risk Parity", w_rp)]:
    r, v, sr = portfolio_stats(w, mu, cov)
    print(f"\n{label}: retorno={r*100:.2f}%  vol={v*100:.2f}%  Sharpe={sr:.3f}")