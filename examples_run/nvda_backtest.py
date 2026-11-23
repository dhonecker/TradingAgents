"""Backtest NVDA über ein Datumsraster.
Aufruf: python examples_run/nvda_backtest.py START END EVERY_DAYS [--run-id ID]"""
import argparse
from _setup import config
from tradingagents.backtest import iter_grid, run_backtest, summarize

p = argparse.ArgumentParser()
p.add_argument("start", nargs="?", default="2026-08-03")
p.add_argument("end", nargs="?", default="2026-11-09")
p.add_argument("every", nargs="?", type=int, default=7)
p.add_argument("--run-id")
p.add_argument("--analysts", default="market,news,fundamentals")
a = p.parse_args()

dates = iter_grid(a.start, a.end, a.every)
print(f"{len(dates)} Zellen: {dates[0]} .. {dates[-1]}")
res = run_backtest(["NVDA"], dates, config(), run_id=a.run_id,
                   selected_analysts=a.analysts.split(","),
                   progress=lambda d, t, tk, dt: print(f"[{d}/{t}] {tk} {dt}", flush=True))
print(summarize(res).render())
print(f"Zellen: {res.cells_run}, übersprungen: {res.skipped}, Log: {res.log_path}, run-id: {res.run_id}")
for f in res.failures: print("FEHLER:", f)
