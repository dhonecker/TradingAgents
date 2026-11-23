"""Gemeinsame Konfiguration: Anthropic als Provider, Key aus ANTHROPIC_API_KEY oder TA_ANTHROPIC_API_KEY."""
import os, sys
from tradingagents.default_config import DEFAULT_CONFIG

key = os.environ.get("ANTHROPIC_API_KEY") or os.environ.get("TA_ANTHROPIC_API_KEY")
if not key:
    sys.exit("Kein Anthropic-Key: weder ANTHROPIC_API_KEY noch TA_ANTHROPIC_API_KEY ist gesetzt.")
os.environ["ANTHROPIC_API_KEY"] = key

def config():
    c = DEFAULT_CONFIG.copy()
    c["llm_provider"] = "anthropic"
    c["deep_think_llm"] = os.environ.get("TA_DEEP", "claude-opus-5-5")
    c["quick_think_llm"] = os.environ.get("TA_QUICK", "claude-sonnet-5-5")
    c["output_language"] = "German"
    c["llm_max_retries"] = 6
    return c
