"""
backtest_portfolios.py
──────────────────────────────────────────────────────────────────────────────
Backtest de três estratégias de alocação de carteira com rebalanceamento mensal
e janela de estimação rolante de 2 anos.

Estratégias:
  1. Tangência (máximo Sharpe ratio)
  2. Mínima variância
  3. Risk parity (contribuição de risco igual por ativo)

Benchmark: IBOV

Saída: três figuras independentes com fundo claro
  - backtest_retorno.{png,pdf}   — retorno acumulado (escala log)
  - backtest_drawdown.{png,pdf}  — drawdown relativo ao pico
  - backtest_tabela.{png,pdf}    — tabela de estatísticas

Uso:
  python backtest_portfolios.py [--csv PATH] [--rf FLOAT] [--lookback INT] [--out PREFIX]

Dependências: pandas numpy scipy matplotlib
"""

import argparse
import os
import warnings
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

warnings.filterwarnings("ignore")

# ═══════════════════════════════════════════════════════════════════════════════
# PARÂMETROS DEFAULT
# ═══════════════════════════════════════════════════════════════════════════════
_HERE            = os.path.dirname(os.path.abspath(__file__))
DEFAULT_CSV      = os.path.join(_HERE, "..", "precos_acoes_brasil.csv")
DEFAULT_OUT      = os.path.join(_HERE, "..", "images", "backtest")
DEFAULT_RF       = 0.1075   # taxa livre de risco anual
DEFAULT_LOOKBACK = 2        # anos de janela de estimação
TRADING_DAYS     = 252
COLORS = {
    "Tangência":      "#1A5FA8",
    "Mín. Variância": "#C0392B",
    "Risk Parity":    "#1A7A3C",
    "IBOV":           "#777777",
}


# ═══════════════════════════════════════════════════════════════════════════════
# OTIMIZADORES
# ═══════════════════════════════════════════════════════════════════════════════
def _base_minimize(obj, n, args=()):
    w0   = np.ones(n) / n
    cons = [{"type": "eq", "fun": lambda w: w.sum() - 1}]
    bnds = [(0, 1)] * n
    res  = minimize(obj, w0, args=args, method="SLSQP",
                    bounds=bnds, constraints=cons,
                    options={"ftol": 1e-13, "maxiter": 3000})
    return res.x if res.success else w0


def port_stats(w, mu, cov, rf):
    ret = float(w @ mu)
    vol = float(np.sqrt(w @ cov @ w))
    return ret, vol, (ret - rf) / vol


def opt_tangency(mu, cov, rf):
    n = len(mu)
    return _base_minimize(lambda w, m, c: -port_stats(w, m, c, rf)[2],
                          n, args=(mu, cov))


def opt_minvar(cov):
    n = cov.shape[0]
    return _base_minimize(lambda w, c: float(w @ c @ w), n, args=(cov,))


def opt_riskparity(cov):
    n = cov.shape[0]

    def obj(w, c):
        vol = np.sqrt(float(w @ c @ w))
        rc  = w * (c @ w) / vol
        return float(np.sum((rc - vol / n) ** 2))

    return _base_minimize(obj, n, args=(cov,))


# ═══════════════════════════════════════════════════════════════════════════════
# BACKTEST
# ═══════════════════════════════════════════════════════════════════════════════
def run_backtest(csv_path, rf, lookback_years):
    df = pd.read_csv(csv_path, parse_dates=["date"])
    prices = (df.pivot(index="date", columns="ticker",
                       values="adjusted_close").sort_index())
    ibov   = prices["IBOV"].copy()
    stocks = prices.drop(columns=["IBOV"])
    n      = stocks.shape[1]

    log_rets = np.log(stocks / stocks.shift(1)).dropna()

    lookback_days = int(lookback_years * TRADING_DAYS)
    all_dates     = stocks.index
    month_ends    = stocks.resample("ME").last().index
    valid_rebal   = [d for d in month_ends
                     if d >= all_dates[lookback_days] and d <= all_dates[-1]]

    print(f"Rebalanceamentos: {len(valid_rebal)} "
          f"({valid_rebal[0].date()} → {valid_rebal[-1].date()})")

    port_vals  = {"Tangência": [1.0], "Mín. Variância": [1.0], "Risk Parity": [1.0]}
    port_dates = [valid_rebal[0]]

    for i, d0 in enumerate(valid_rebal[:-1]):
        d1     = valid_rebal[i + 1]
        window = log_rets.loc[:d0].iloc[-lookback_days:]
        mu_e   = window.mean() * TRADING_DAYS
        cov_e  = window.cov()  * TRADING_DAYS

        w_tan = opt_tangency(mu_e, cov_e, rf)
        w_mv  = opt_minvar(cov_e)
        w_rp  = opt_riskparity(cov_e)

        month_r = log_rets.loc[(log_rets.index > d0) & (log_rets.index <= d1)]
        for label, w in [("Tangência", w_tan),
                         ("Mín. Variância", w_mv),
                         ("Risk Parity", w_rp)]:
            port_vals[label].append(
                port_vals[label][-1] * np.exp(float((month_r @ w).sum())))
        port_dates.append(d1)

    perf = pd.DataFrame(port_vals, index=port_dates)

    # IBOV acumulado nos mesmos intervalos mensais
    ibov_log = np.log(ibov / ibov.shift(1)).dropna()
    ibov_cum, v = {valid_rebal[0]: 1.0}, 1.0
    for i in range(len(valid_rebal) - 1):
        d0, d1 = valid_rebal[i], valid_rebal[i + 1]
        m = ibov_log.loc[(ibov_log.index > d0) & (ibov_log.index <= d1)]
        v *= np.exp(m.sum())
        ibov_cum[d1] = v
    perf["IBOV"] = pd.Series(ibov_cum)

    return perf, rf


# ═══════════════════════════════════════════════════════════════════════════════
# ESTATÍSTICAS
# ═══════════════════════════════════════════════════════════════════════════════
PCT_ROWS = {"Retorno anual", "Volatilidade", "Max drawdown",
            "Melhor mês", "Pior mês", "Retorno total"}


def compute_stats(perf, rf):
    cols = ["Tangência", "Mín. Variância", "Risk Parity", "IBOV"]

    def _s(series):
        mr      = np.log(series / series.shift(1)).dropna()
        ann_ret = float(mr.mean() * 12)
        ann_vol = float(mr.std()  * np.sqrt(12))
        return {
            "Retorno anual":    ann_ret,
            "Volatilidade":     ann_vol,
            "Sharpe":           (ann_ret - rf) / ann_vol,
            "Assimetria":       float(stats.skew(mr)),
            "Curtose (excess)": float(stats.kurtosis(mr)),
            "Max drawdown":     float((series / series.cummax() - 1).min()),
            "Melhor mês":       float(mr.max()),
            "Pior mês":         float(mr.min()),
            "Retorno total":    float(series.iloc[-1] - 1),
        }

    return pd.DataFrame({c: _s(perf[c]) for c in cols})


# ═══════════════════════════════════════════════════════════════════════════════
# ESTILO BASE — fundo claro
# ═══════════════════════════════════════════════════════════════════════════════
def apply_light_style():
    plt.rcParams.update({
        "figure.facecolor": "white",
        "axes.facecolor":   "#F7F7F7",
        "axes.edgecolor":   "#CCCCCC",
        "axes.labelcolor":  "#222222",
        "xtick.color":      "#444444",
        "ytick.color":      "#444444",
        "grid.color":       "#DDDDDD",
        "text.color":       "#222222",
        "font.family":      "sans-serif",
    })


def style_ax(ax):
    ax.spines[["top", "right"]].set_visible(False)
    ax.spines[["left", "bottom"]].set_color("#CCCCCC")
    ax.grid(True, alpha=0.6, color="#DDDDDD", lw=0.7)
    ax.set_facecolor("#F7F7F7")


def _save(fig, prefix, exts=("png", "pdf")):
    for ext in exts:
        path = f"{prefix}.{ext}"
        fig.savefig(path, dpi=150, bbox_inches="tight",
                    facecolor=fig.get_facecolor())
        print(f"  Salvo: {path}")
    plt.close(fig)


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURA 1 — Retorno acumulado
# ═══════════════════════════════════════════════════════════════════════════════
def fig_retorno(perf, lookback_years, rf, out_prefix):
    cols       = ["Tangência", "Mín. Variância", "Risk Parity", "IBOV"]
    title_sub  = (f"Rebalanceamento mensal · Janela {lookback_years} anos · "
                  f"rf = {rf:.2%} a.a.")

    fig, ax = plt.subplots(figsize=(11, 5.5))
    fig.patch.set_facecolor("white")
    for col in cols:
        kw = dict(lw=2.0 if col != "IBOV" else 1.3,
                  alpha=1.0 if col != "IBOV" else 0.65,
                  linestyle="-" if col != "IBOV" else "--")
        ax.plot(perf.index, perf[col], color=COLORS[col], label=col, **kw)
    ax.set_yscale("log")
    ax.yaxis.set_major_formatter(
        mticker.FuncFormatter(lambda y, _: f"{y:.0f}×"))
    ax.set_ylabel("Valor acumulado (escala log)")
    ax.set_title(f"Retorno Acumulado\n{title_sub}", fontsize=11, pad=8)
    ax.legend(framealpha=0.9, fontsize=9)
    ax.axhline(1, color="#AAAAAA", lw=0.8, ls=":")
    style_ax(ax)
    fig.tight_layout()
    _save(fig, out_prefix + "_retorno")


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURA 2 — Drawdown
# ═══════════════════════════════════════════════════════════════════════════════
def fig_drawdown(perf, lookback_years, rf, out_prefix):
    cols      = ["Tangência", "Mín. Variância", "Risk Parity", "IBOV"]
    title_sub = (f"Rebalanceamento mensal · Janela {lookback_years} anos · "
                 f"rf = {rf:.2%} a.a.")

    fig, ax = plt.subplots(figsize=(11, 4.5))
    fig.patch.set_facecolor("white")
    for col in cols:
        dd = (perf[col] / perf[col].cummax() - 1) * 100
        ax.fill_between(perf.index, dd, 0, color=COLORS[col], alpha=0.20)
        ax.plot(perf.index, dd, color=COLORS[col],
                lw=1.8 if col != "IBOV" else 1.1,
                alpha=1.0 if col != "IBOV" else 0.65,
                linestyle="-" if col != "IBOV" else "--",
                label=col)
    ax.set_ylabel("Drawdown (%)")
    ax.yaxis.set_major_formatter(
        mticker.FuncFormatter(lambda y, _: f"{y:.0f}%"))
    ax.set_title(f"Drawdown relativo ao pico\n{title_sub}", fontsize=11, pad=8)
    ax.legend(framealpha=0.9, fontsize=9)
    style_ax(ax)
    fig.tight_layout()
    _save(fig, out_prefix + "_drawdown")


# ═══════════════════════════════════════════════════════════════════════════════
# FIGURA 3 — Tabela
# ═══════════════════════════════════════════════════════════════════════════════
def fig_tabela(stats_df, out_prefix):
    cols       = ["Tangência", "Mín. Variância", "Risk Parity", "IBOV"]
    row_labels = list(stats_df.index)

    cell_text = []
    for row in row_labels:
        cell_text.append([
            f"{stats_df.loc[row, c]:.2%}" if row in PCT_ROWS
            else f"{stats_df.loc[row, c]:.3f}"
            for c in cols
        ])

    # cores alternadas nas linhas
    row_colors = [
        ["#FFFFFF" if r % 2 == 0 else "#F0F4F8"] * len(cols)
        for r in range(len(row_labels))
    ]

    fig, ax = plt.subplots(figsize=(10, 4.2))
    fig.patch.set_facecolor("white")
    ax.axis("off")

    tbl = ax.table(
        cellText=cell_text,
        rowLabels=row_labels,
        colLabels=cols,
        cellLoc="center",
        loc="center",
        cellColours=row_colors,
    )
    tbl.auto_set_font_size(False)
    tbl.set_fontsize(9)
    tbl.scale(1.1, 1.7)

    header_colors = [COLORS[c] for c in cols]
    for (r, c), cell in tbl.get_celld().items():
        cell.set_edgecolor("#CCCCCC")
        if r == 0:
            if c >= 0:
                cell.set_facecolor(header_colors[c])
                cell.set_text_props(color="white", fontweight="bold")
            else:
                cell.set_facecolor("#E8E8E8")
                cell.set_text_props(color="#333333", fontweight="bold")
        elif c == -1:
            cell.set_facecolor("#E8EDF2")
            cell.set_text_props(color="#333333", fontweight="bold")

    ax.set_title("Estatísticas do Backtest  (retornos mensais log)",
                 fontsize=11, pad=14, color="#222222")
    fig.tight_layout()
    _save(fig, out_prefix + "_tabela")


# ═══════════════════════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════════════════════
def main():
    parser = argparse.ArgumentParser(
        description="Backtest de portfólios de ações brasileiras")
    parser.add_argument("--csv",      default=DEFAULT_CSV,
                        help="Caminho do CSV de preços")
    parser.add_argument("--rf",       default=DEFAULT_RF, type=float,
                        help="Taxa livre de risco anual (ex: 0.1075)")
    parser.add_argument("--lookback", default=DEFAULT_LOOKBACK, type=int,
                        help="Janela de estimação em anos (ex: 2)")
    parser.add_argument("--out",      default=DEFAULT_OUT,
                        help="Prefixo dos arquivos de saída")
    args = parser.parse_args()

    apply_light_style()

    print(f"\nCarregando dados: {args.csv}")
    perf, rf  = run_backtest(args.csv, args.rf, args.lookback)
    stats_df  = compute_stats(perf, rf)

    # Resumo no terminal
    print("\n── Estatísticas do Backtest ──")
    for row in stats_df.index:
        print(f"\n{row}")
        for col in stats_df.columns:
            v = stats_df.loc[row, col]
            s = f"{v:.2%}" if row in PCT_ROWS else f"{v:.3f}"
            print(f"  {col:<20} {s}")

    # Figuras separadas
    print("\nGerando figuras...")
    fig_retorno(perf,     args.lookback, rf, args.out)
    fig_drawdown(perf,    args.lookback, rf, args.out)
    fig_tabela(stats_df,  args.out)
    print("\nConcluído.")


if __name__ == "__main__":
    main()
