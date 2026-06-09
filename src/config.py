"""Configuration for the Stock Trading Multi-Agent System."""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


# --- API Keys ---
ANTHROPIC_API_KEY = os.getenv("ANTHROPIC_API_KEY", "")
ALPACA_API_KEY = os.getenv("ALPACA_API_KEY", "")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY", "")
NEWS_API_KEY = os.getenv("NEWS_API_KEY", "")  # Finnhub
RESEND_API_KEY = os.getenv("RESEND_API_KEY", "")
NOTIFICATION_EMAIL = os.getenv("NOTIFICATION_EMAIL", "yuval.kesh@gmail.com")

# --- Paths ---
PROJECT_ROOT = Path(__file__).parent.parent
VAULT_PATH = PROJECT_ROOT / "stock"
AGENTS_PATH = VAULT_PATH / "A-agents"
CORE_PATH = VAULT_PATH / "C-core"
MEMORY_PATH = VAULT_PATH / "M-memory"
OUTPUT_PATH = VAULT_PATH / "O-output"
PORTFOLIO_PATH = VAULT_PATH / "P-portfolio"
REFERENCES_PATH = VAULT_PATH / "R-references"
STRATEGY_PATH = VAULT_PATH / "S-strategy"

# --- LLM Model ---
LLM_MODEL = "claude-haiku-4-5-20251001"  # cheapest capable model — keep
LLM_MAX_TOKENS = 3000  # output cap; agent briefs/verdicts fit well under this

# --- Alpaca ---
ALPACA_PAPER = True  # Always paper trading

# --- Risk Management (Hard Limits) ---
MAX_RISK_PER_TRADE = 0.01       # 1% of equity
MAX_SINGLE_POSITION = 0.15      # 15% of equity
MAX_TOTAL_EXPOSURE = 0.70       # 70% of equity
MAX_OPEN_POSITIONS = 6
MIN_RR_RATIO = 1.0              # Default minimum risk:reward (fallback)
# Strategy-specific R:R minimums — high win-rate strategies compensate
# with frequency, so they don't need 2:1 R:R to be profitable.
STRATEGY_MIN_RR = {
    "connors_rsi":       0.5,   # ~75% win rate, mean reversion
    "macd_rsi":          1.0,   # ~73% win rate, momentum
    "bollinger_squeeze": 1.5,   # ~65% win rate, breakout
    "ma_crossover":      1.5,   # ~60% win rate, trend-following
    "vix_fear":          0.5,   # ~80% win rate, fear reversal
}
MAX_DAILY_LOSS = 0.03           # 3% of equity
MAX_MONTHLY_DRAWDOWN = 0.10     # 10% of equity
EARNINGS_BUFFER_DAYS = 3
MIN_CONVICTION_SCORE = 6        # Out of 12 (added 2pts for fundamentals)
MAX_LOOPBACKS = 1               # Gatekeeper max retries (was 2 — saves up to 2 LLM calls/run)

# --- Trading Parameters ---
MIN_STOCK_PRICE = 10.0
MIN_AVG_VOLUME = 500_000        # Was 1M — too restrictive
TARGET_TRADES_PER_MONTH = (6, 10)  # min, max

# --- Exit / hold management ---
TIME_STOP_STAGNANT_DAYS = 10    # exit if position goes nowhere (<0.5%) after N days
TIME_STOP_MAX_HOLD_DAYS = 40    # hard max hold (fixed-target mode)

# "Let winners run" mode: drop the fixed take-profit cap and ride a trailing
# stop instead, so a trend like MRVL isn't scratched at +3%. Off by default;
# the backtest flips it on to compare. Trailing arms once the trade is up
# TRAILING_STOP_TRIGGER_R (in R multiples), then trails by a per-strategy %.
LET_WINNERS_RUN = True           # backtested +60% vs fixed targets (2024-2026)
LIVE_TRAILING_STOP_PCT = 12.0    # live trailing-stop distance for new entries
TRAILING_STOP_TRIGGER_R = 1.0    # arm trailing once trade is up 1R (backtest mode)
TRAILING_STOP_DEFAULTS = {       # trail distance (% below high) once armed
    "connors_rsi":       6.0,
    "macd_rsi":          10.0,
    "bollinger_squeeze": 12.0,
    "ma_crossover":      14.0,
    "vix_fear":          6.0,
}

# --- Schedule (EST times as UTC cron) ---
SCHEDULE = {
    "morning_scan": "06:00",    # EST
    "execute": "09:30",         # EST
    "monitor_start": "10:00",   # EST
    "monitor_end": "15:00",     # EST
    "monitor_interval_min": 60,
    "post_market": "16:30",     # EST
}

# --- Watchlist ---
DEFAULT_WATCHLIST = [
    "SPY", "QQQ",
    "AAPL", "MSFT", "GOOGL", "AMZN", "NVDA", "META", "TSLA",
    "JPM", "GS",
    "UNH", "JNJ",
    "XOM", "CVX",
    "WMT", "HD",
    "XLK", "XLF", "XLE", "XLV",
]

MACRO_SYMBOLS = {
    "vix": "^VIX",
    "sp500": "^GSPC",
    "yield_10y": "^TNX",
    "btc": "BTC-USD",
    "sp_futures": "ES=F",
}
