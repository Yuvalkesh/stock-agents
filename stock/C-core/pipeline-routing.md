# Pipeline Routing — How Data Flows Through Agents

## Overview

```
Data Fetcher (news + prices + macro)
       ↓
Agent 1: Head of Investment → STAND DOWN or PROCEED with ticker list
       ↓
Agent 2: Stock Analyst → NO SETUP or SETUP CONFIRMED per ticker
       ↓
Agent 3: Data Merger → Standardized merged report
       ↓
Agent 4: Swing Trader MegaBot → PASS or BUY/SHORT (score X/10)
       ↓
Agent 5: Gatekeeper Boss → NO-GO (loop back, max 2x) or GO
       ↓
Trade Executor → Alpaca bracket order (entry + stop + take profit)
       ↓
Position Monitor → Track until close
       ↓
Post-Mortem → Log result, update learning log, update strategy performance
```

## Detailed Flow

### Step 0: Data Fetching
- **Trigger**: Scheduled (6:00 AM EST) or manual
- **Actions**:
  1. Fetch news headlines from Finnhub for watchlist tickers
  2. Fetch OHLCV data (200 days daily) from yfinance
  3. Fetch macro indicators: VIX, S&P 500, 10Y yield, BTC
  4. Fetch earnings calendar for next 5 trading days
- **Output**: Raw data objects passed to Agent 1

### Step 1: Agent 1 — Head of Investment
- **Input**: Raw news, macro data, earnings calendar, current portfolio
- **Processing**: Assess macro regime, filter news, select tickers
- **Output**: `01-investment-brief.md`
- **Routing**:
  - If STAND DOWN → Skip to Post-Mortem (log the stand-down)
  - If PROCEED → Pass ticker list + active strategies to Agent 2

### Step 2: Agent 2 — Stock Analyst
- **Input**: Ticker list from Agent 1, OHLCV data, strategy parameters
- **Processing**: Run all 5 strategies per ticker, calculate indicators
- **Output**: `02-analyst-report.md`
- **Routing**:
  - Tickers with NO SETUP → Dropped from pipeline
  - Tickers with SETUP CONFIRMED → Pass to Agent 3

### Step 3: Agent 3 — Data Merger
- **Input**: Agent 1 brief + Agent 2 report (only confirmed setups)
- **Processing**: Align news with technicals, flag contradictions, calculate trade params
- **Output**: `03-merged-data.md`
- **Routing**: All merged candidates pass to Agent 4

### Step 4: Agent 4 — Swing Trader MegaBot
- **Input**: Merged data + portfolio + learning log + references
- **Processing**: Score each candidate (10-point system), decide BUY/SHORT/PASS
- **Output**: `04-trade-decision.md`
- **Routing**:
  - PASS → Log to rejected, skip to Post-Mortem
  - BUY/SHORT → Pass to Agent 5

### Step 5: Agent 5 — Gatekeeper Boss
- **Input**: Trade decision + risk rules + portfolio + account status
- **Processing**: Run 14-point zero-tolerance checklist
- **Output**: `05-gatekeeper-verdict.md`
- **Routing**:
  - GO → Execute trade
  - NO-GO (FIXABLE) → Loop back to Agent 4 (or 1/2) with instructions
  - NO-GO (KILLED) → Log to rejected, stop

### Loop-Back Mechanism
```
Agent 5 NO-GO (fixable)
    ↓
    ├── Issue with scoring → Send back to Agent 4 (re-score with adjusted params)
    ├── Issue with sizing → Send back to Agent 4 (recalculate position)
    ├── Issue with data → Send back to Agent 2 (re-analyze)
    └── Issue with macro → Send back to Agent 1 (re-assess)
    ↓
Re-run from that agent forward
    ↓
Agent 5 checks again
    ↓
    ├── GO → Execute
    └── NO-GO again → If loop count < 2: loop back
                       If loop count >= 2: TRADE KILLED
```

### Step 6: Trade Execution
- **Input**: Approved trade from Agent 5
- **Processing**: Submit bracket order to Alpaca (market + stop + take profit)
- **Output**: Order confirmation, update `P-portfolio/pending-orders.md`
- **Post-execution**: Update `P-portfolio/current-positions.md` and `P-portfolio/account-status.md`

### Step 7: Position Monitoring
- **Trigger**: Every hour during market hours (10 AM - 3 PM EST)
- **Processing**:
  1. Check all open positions vs current prices
  2. Log unrealized P&L
  3. Check if any bracket legs have filled (stop or target)
  4. Update portfolio files
- **Output**: Updated portfolio files

### Step 8: Post-Mortem (On Trade Close)
- **Trigger**: When a position is fully closed (stop hit, target hit, or manual exit)
- **Processing**:
  1. Calculate final P&L and R-multiple
  2. Write trade journal entry
  3. Update learning log
  4. Update strategy performance log
  5. If R >= 2: Copy to `R-references/best-trades/`
  6. If R <= -1: Copy to `R-references/worst-trades/`
- **Output**: Trade journal entry, updated logs

## Schedule (GitHub Actions)

| Time (EST) | Action | Mode |
|------------|--------|------|
| 6:00 AM | Morning scan + full pipeline | `scan` |
| 9:30 AM | Execute approved trades | `execute` |
| 10:00 AM - 3:00 PM | Position checks (hourly) | `monitor` |
| 4:30 PM | Post-market review | `review` |

## Error Handling
- If data fetch fails → Retry once, then STAND DOWN
- If Claude API fails → Retry once, then STAND DOWN
- If Alpaca API fails → Retry once, then alert and STAND DOWN
- If any agent produces unparseable output → Retry once, then skip that ticker
- All errors logged to `M-memory/learning-log.md`
