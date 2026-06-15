# Gatekeeper Verdict — NVDA — 2026-06-15

## Checklist Results

| # | Check | Rule | Value | Result |
|---|-------|------|-------|--------|
| 1 | Risk per trade | <= 1% of equity | 0.84% | **PASS** |
| 2 | Total positions | <= 6 | 1 (after entry) | **PASS** |
| 3 | Total exposure | <= 70% | 14.96% | **PASS** |
| 4 | Position size | <= 15% of equity | 14.96% | **PASS** |
| 5 | R:R ratio (soft) | >= 1.5:1 (MA Crossover min) | 1.63:1 | **PASS** |
| 6 | ATR stop set | Required | Yes — $200.51 (2.0× ATR below entry) | **PASS** |
| 7 | Earnings clear | > 3 trading days | 29+ days | **PASS** |
| 8 | Daily loss limit | < 3% of equity | 0.00% (no loss yet) | **PASS** |
| 9 | Monthly drawdown | < 10% of equity | 0.00% | **PASS** |
| 10 | Conviction (soft) | >= 6/12 | 9/12 | **PASS** |
| 11 | Strategy confirmed | Required | MA Crossover fully confirmed by Agent 02 | **PASS** |
| 12 | News-tech aligned (soft) | No contradictions | Both bullish; aligned | **PASS** |
| 13 | Not adding to loser | Required | First position; N/A | **PASS** |
| 14 | No correlation (soft) | N/A for first trade | No existing positions | **PASS** |

---

## Verdict: **GO**

### APPROVED FOR EXECUTION

| Parameter | Value |
|-----------|-------|
| **Symbol** | NVDA |
| **Direction** | LONG |
| **Entry Price** | $212.50 |
| **Stop Loss** | $200.51 |
| **Take Profit** | $232.01 |
| **Shares** | 98 |
| **Order Type** | Bracket (Market entry + Stop + Take Profit) |
| **Risk Amount** | $1,175.02 (0.84% of equity) |
| **Position Value** | $20,830.00 (14.96% of equity) |
| **R:R Ratio** | 1.63:1 ✓ |

---

## Summary

**All hard checks pass. All soft checks pass. Conviction score 9/12 justifies full 1% risk allocation (0.84% actual). Position sizing matches conviction tier.**

### Gatekeeper Notes

This is a **clean, high-conviction setup**. Here's what I see:

✅ **Technical Structure**: MA Crossover is textbook — price above 10 EMA ($209.54), 10 EMA above 50 EMA ($207.41), price in pullback zone at entry. This is exactly the setup the strategy requires.

✅ **Risk Geometry**: 1.63:1 R:R exceeds the 1.5:1 MA Crossover minimum. Stop at $200.51 is rational (2.0× ATR distance) and not arbitrary. Risk per trade is 0.84% — well within the 1% hard limit.

✅ **Narrative Support**: Bullish news (analyst $299 target) aligns with technical structure. RSI(14)=51.44 means momentum room — not overbought, not oversold. This reduces the risk of a fake-out reversal.

✅ **Earnings Clear**: 29+ days to next earnings. No binary event risk.

✅ **Portfolio Health**: First position of the day. Account is clean. 14.96% position size leaves 85%+ dry powder for subsequent opportunities.

⚠️ **One Minor Flag**: Volume at 0.39x is weak for a momentum strategy. This doesn't fail the hard check, but it's worth noting. If volume stays weak (< 0.8x) over the next 2 days and price hasn't moved higher, consider tightening the stop to breakeven. **Do not widening the stop — ever.**

### Kill Conditions (Agent 04 recommended)
- **Price closes below 10 EMA ($209.54) on volume > 0.8x** → Exit at market
- **RSI(14) < 40 AND price below 50 EMA** → Exit at market
- **Macro shock (VIX >30, Fed surprise)** → Consider partial exit; full exit if sector rotation evident
- **2+ days of volume collapse** → Tighten stop to breakeven

### Execution Instructions
1. **Submit bracket order immediately** (market entry)
2. **Entry**: Market order for 98 shares
3. **Stop**: $200.51 (good-til-cancelled)
4. **Take Profit**: $232.01 (good-til-cancelled)
5. **Hold until stop OR target hits** — no discretionary exits
6. **Min hold 1 trading day** — do not exit same-day unless stopped out

---

**EXECUTE NOW. No further review needed.**