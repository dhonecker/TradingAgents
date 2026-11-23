"""Einzelanalyse NVDA. Aufruf: python examples_run/nvda_analyse.py [YYYY-MM-DD]"""
import sys
from _setup import config
from tradingagents.graph.trading_graph import TradingAgentsGraph

date = sys.argv[1] if len(sys.argv) > 1 else "2026-11-20"
ta = TradingAgentsGraph(debug=False, config=config())
state, signal = ta.propagate("NVDA", date)
path = ta.save_reports(state, "NVDA")
print(f"\nNVDA {date}: {signal}\nReport: {path}")
