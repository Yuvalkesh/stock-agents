"""Track start-of-month equity for monthly drawdown calculation."""

import json
import logging
from datetime import datetime
from pathlib import Path

from config import PORTFOLIO_PATH

logger = logging.getLogger(__name__)

MONTHLY_EQUITY_FILE = PORTFOLIO_PATH / "monthly_start_equity.json"


def _read_monthly_equity() -> dict:
    """Read the monthly start equity file."""
    if not MONTHLY_EQUITY_FILE.exists():
        return {}
    try:
        return json.loads(MONTHLY_EQUITY_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as e:
        logger.warning(f"Error reading monthly equity file: {e}")
        return {}


def _write_monthly_equity(data: dict) -> None:
    """Write the monthly start equity file."""
    MONTHLY_EQUITY_FILE.parent.mkdir(parents=True, exist_ok=True)
    MONTHLY_EQUITY_FILE.write_text(
        json.dumps(data, indent=2), encoding="utf-8"
    )


def get_monthly_drawdown_pct(current_equity: float) -> float:
    """Calculate month-to-date drawdown percentage.

    On the first call of each month (or if no data exists), records
    the current equity as the start-of-month baseline.

    Returns a positive number representing drawdown (0 = no drawdown).
    """
    now = datetime.now()
    month_key = now.strftime("%Y-%m")

    data = _read_monthly_equity()
    start_equity = data.get(month_key)

    if start_equity is None:
        # First run this month — record baseline
        data[month_key] = current_equity
        _write_monthly_equity(data)
        logger.info(
            f"Monthly equity baseline set: ${current_equity:,.2f} for {month_key}"
        )
        return 0.0

    if start_equity <= 0:
        return 0.0

    drawdown = ((start_equity - current_equity) / start_equity) * 100
    return max(0.0, round(drawdown, 2))
