"""TradingAgents-Signale als Orders im Alpaca-Paper-Konto umsetzen.

Aufruf:
  python examples_run/paper_trade.py NVDA,AAPL,MSFT [--date YYYY-MM-DD] [--dry-run]

Ablauf je Ticker:
  1. Signal holen: aus examples_run/results/signals.json, sonst neue Analyse.
  2. Zielgröße bestimmen. Jeder Ticker hat einen gleich großen "Slot"
     (Konto-Equity / Anzahl Ticker). Das Rating legt fest:
       Buy         -> 100 % des Slots
       Overweight  ->  75 % des Slots
       Hold        -> Position unverändert lassen
       Underweight -> höchstens 25 % des Slots (nur verkaufen, nie zukaufen)
       Sell        ->   0 % (Position schließen)
     Es wird nie geshortet.
  3. Differenz als Market-Order (ganze Aktien) senden, außer bei --dry-run.

Alpaca: Key ID aus ALPACA_KEY_ID oder ~/.alpaca/key_id. Den Secret Key setzt
der Netzwerk-Proxy der Cloud-Session ein; lokal kann er über
ALPACA_SECRET_KEY kommen.
"""
import argparse
import datetime as dt
import json
import math
import os
import shutil
from pathlib import Path

import requests

BASE = "https://paper-api.alpaca.markets"
RESULTS = Path(__file__).parent / "results"
SIGNALS = RESULTS / "signals.json"
SLOT_FRACTION = {"buy": 1.0, "overweight": 0.75, "underweight": 0.25, "sell": 0.0}


def headers():
    key_id = os.environ.get("ALPACA_KEY_ID") or Path("~/.alpaca/key_id").expanduser().read_text().strip()
    return {"APCA-API-KEY-ID": key_id,
            "APCA-API-SECRET-KEY": os.environ.get("ALPACA_SECRET_KEY", "proxy-injected")}


def api(method, path, **kw):
    r = requests.request(method, BASE + path, headers=headers(), timeout=30, **kw)
    if r.status_code >= 400:
        raise RuntimeError(f"{method} {path}: HTTP {r.status_code} {r.text[:300]}")
    return r.json() if r.text else None


def last_trading_day():
    d = dt.date.today() - dt.timedelta(days=1)
    while d.weekday() >= 5:
        d -= dt.timedelta(days=1)
    return d.isoformat()


def load_signals():
    return json.loads(SIGNALS.read_text()) if SIGNALS.exists() else {}


def get_signal(ticker, date, signals):
    key = f"{ticker}@{date}"
    if key in signals:
        return signals[key]["rating"]
    from _setup import config
    from tradingagents.graph.trading_graph import TradingAgentsGraph
    print(f"Analysiere {ticker} zum {date} ...", flush=True)
    ta = TradingAgentsGraph(debug=False, config=config())
    state, rating = ta.propagate(ticker, date)
    report = Path(ta.save_reports(state, ticker))
    dest = RESULTS / date / ticker
    shutil.copytree(report.parent, dest, dirs_exist_ok=True)
    signals[key] = {"rating": rating, "report": str((dest / report.name).relative_to(RESULTS.parent.parent))}
    SIGNALS.parent.mkdir(parents=True, exist_ok=True)
    SIGNALS.write_text(json.dumps(signals, indent=2, ensure_ascii=False))
    return rating


def last_price(ticker):
    import yfinance as yf
    return float(yf.Ticker(ticker).history(period="5d")["Close"].iloc[-1])


def main():
    p = argparse.ArgumentParser()
    p.add_argument("tickers")
    p.add_argument("--date", default=last_trading_day())
    p.add_argument("--dry-run", action="store_true")
    a = p.parse_args()
    tickers = [t.strip().upper() for t in a.tickers.split(",") if t.strip()]

    signals = load_signals()
    ratings = {t: get_signal(t, a.date, signals) for t in tickers}

    acct = api("GET", "/v2/account")
    equity = float(acct["equity"])
    slot = equity / len(tickers)
    positions = {p["symbol"]: float(p["qty"]) for p in api("GET", "/v2/positions")}
    clock = api("GET", "/v2/clock")
    print(f"\nEquity {equity:,.2f} $, Slot je Ticker {slot:,.2f} $, Markt offen: {clock['is_open']}\n")

    lines = [f"Stichtag {a.date}, Lauf {dt.datetime.now(dt.timezone.utc):%Y-%m-%d %H:%M} UTC",
             f"Equity {equity:,.2f} $, Cash {float(acct['cash']):,.2f} $, Slot je Ticker {slot:,.2f} $"]
    orders = []
    for t in tickers:
        rating = ratings[t].strip().lower()
        have = positions.get(t, 0.0)
        price = last_price(t)
        if rating == "hold" or rating not in SLOT_FRACTION:
            target = have
        else:
            target = math.floor(slot * SLOT_FRACTION[rating] / price)
            if rating == "underweight":
                target = min(have, target)
        delta = int(target - have)
        line = f"{t:6} {ratings[t]:12} Kurs {price:9.2f}  Bestand {have:6.0f}  Ziel {target:6.0f}  Order {delta:+d}"
        print(line)
        lines.append(line)
        if delta:
            orders.append((t, delta))

    if a.dry_run or not orders:
        lines.append("Keine Orders gesendet." if not orders else "Dry-Run: keine Orders gesendet.")
    else:
        for t, delta in orders:
            o = api("POST", "/v2/orders", json={"symbol": t, "qty": str(abs(delta)),
                                                 "side": "buy" if delta > 0 else "sell",
                                                 "type": "market", "time_in_force": "day"})
            lines.append(f"Order {o['side']} {o['qty']} {t}: {o['status']} (id {o['id']})")
    pos = api("GET", "/v2/positions")
    lines.append("Positionen: " + (", ".join(f"{p['symbol']} {p['qty']} (P/L {float(p['unrealized_pl']):+.2f} $)" for p in pos) or "keine"))
    print("\n" + "\n".join(lines[-(len(orders) + 2):]))
    out = RESULTS / a.date / "orders.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
