# Gatekeeper Verdict — AMAT — 2026-07-08

## Checklist Results

| # | Check | Rule | Value | Result |
|---|-------|------|-------|--------|
| 1 | Risk per trade | <= 1% of equity | 0.95% | **PASS** |
| 2 | Total positions | <= 6 | 1 (after entry) | **PASS** |
| 3 | Total exposure | <= 70% of equity | 5.6% | **PASS** |
| 4 | Position size | <= 15% of equity | 5.6% | **PASS** |
| 5 | R:R ratio (soft) | Meets strategy min (0.5:1) | 0.74:1 | **PASS** |
| 6 | ATR stop set | Required | Yes — $459.86 set | **PASS** |
| 7 | Earnings clear | > 3 days | 49 days (2026-08-26) | **PASS** |
| 8 | Daily loss | < 3% of equity | $0.00 (0.0%) | **PASS** |
| 9 | Monthly drawdown | < 10% of equity | 0.0% | **PASS** |
| 10 | Conviction (soft) | >= 6/12 | 10/12 | **PASS** |
| 11 | Strategy confirmed | Fully confirmed by Agent 02 | Yes — Connors RSI(2) validated | **PASS** |
| 12 | News-tech aligned (soft) | No contradictions | Yes — bullish alignment | **PASS** |
| 13 | Not adding to loser | Required | N/A (fresh entry, no existing position) | **PASS** |
| 14 | No correlation (soft) | Required | N/A (0 existing positions) | **PASS** |

---

## Soft Check Summary
- **Soft Check 5 (R:R)**: PASS — 0.74:1 exceeds 0.5:1 minimum
- **Soft Check 10 (Conviction)**: PASS — 10/12 is well above 6/12 threshold
- **Soft Check 12 (News-tech)**: PASS — Bullish alignment confirmed by Agent 03
- **Soft Check 14 (Correlation)**: PASS — Zero existing positions, no conflicts

**Total Soft Check Warnings: 0 of 2 allowed** ✓

---

## Conviction-Based Sizing Validation
| Parameter | Rule | Value | Check |
|-----------|------|-------|-------|
| Conviction Score | 10/12 | Full confidence tier | ✓ |
| Required Risk Tier | 1.0% of equity for 8+/10 | 0.95% deployed | ✓ |
| Position Sizing | Matches conviction | 14 shares × $554.50 = $7,763 | ✓ |

**Position sizing is properly aligned with conviction score. At 10/12, this trade justifies full 1% risk allocation. Actual risk (0.95%) is within acceptable tolerance.**

---

## Verdict: **GO**

### APPROVED FOR EXECUTION

| Parameter | Value |
|-----------|-------|
| **Symbol** | AMAT |
| **Direction** | LONG |
| **Entry Price** | $554.50 (market open, 2026-07-08) |
| **Stop Loss** | $459.86 |
| **Take Profit Target** | $624.85 |
| **Shares** | 14 |
| **Position Value** | $7,763.00 (5.6% of equity) |
| **Risk Amount** | $1,324.96 (0.95% of equity) |
| **Risk:Reward Ratio** | 0.74:1 |
| **Order Type** | Bracket (Buy Market + Stop + Take Profit) |
| **Expected Hold Window** | 3–8 trading days |

---

## Gatekeeper Notes

**All hard checks pass. All soft checks pass. This is a clean, high-conviction setup.**

The AMAT trade ticks every box:

- **Risk management**: Position is appropriately sized at 0.95% risk on a 10/12 conviction score. Well below all hard limits.
- **Technical setup**: Connors RSI(2)=6.55 is a textbook oversold condition within an established uptrend (price >> 200 SMA). Mechanically sound.
- **Fundamental tailwind**: Semiconductor sector leadership (+33.7% relative strength), analyst target $587 above current price, Rising Star discovery signals institutional interest. Macro and micro aligned.
- **Execution clarity**: Kill conditions are explicitly defined (sector reversal, volume collapse, RSI failure to bounce). Trade has clear decision points.
- **Portfolio fit**: Zero existing positions means zero correlation risk. This is a clean first entry with maximum room to trade.

**One small observation** (not a blocker): The R:R ratio of 0.74:1 is slimmer than ideal for a mean reversion trade — you're risking $1,324.96 to make ~$980. This is acceptable for Connors RSI(2) where win rate is higher, but understand that this trade needs to work 4 out of 5 times to be profitable. The 10/12 conviction score gives us confidence it will. If this were a 6/12 setup with 0.74:1 R:R, I'd reduce the position. But at 10/12, the math works.

**Execute with full conviction. No modifications after GO.**

---

## Execution Checklist
- [ ] Confirm entry at market open (2026-07-08)
- [ ] Bracket order: Buy 14 shares AMAT at market, Stop at $459.86, Profit target at $624.85
- [ ] Monitor for sector reversal signals (NVDA/AMD below 10 EMA same day)
- [ ] Track RSI(2) bounce on day 1-2; if it fails to reach 30, reassess
- [ ] Max hold 8 trading days; reassess on 2026-07-18 if still open
- [ ] Log trade to portfolio tracker upon fill

**Status: READY TO EXECUTE**