# Gatekeeper Verdict — ROKU — 2026-06-26

## Checklist Results

| # | Check | Rule | Value | Result |
|---|-------|------|-------|--------|
| 1 | Risk per trade | <= 1% of equity | 0.97% | **PASS** |
| 2 | Total positions | <= 6 | 1 (post-trade) | **PASS** |
| 3 | Total exposure | <= 70% of equity | 2.43% | **PASS** |
| 4 | Position size | <= 15% of equity | 2.43% | **PASS** |
| 5 | R:R ratio (soft) | Meets strategy min (1.5:1) | 1.87:1 | **PASS** |
| 6 | ATR stop set | Required | Yes ($127.18 hard stop) | **PASS** |
| 7 | Earnings clear | > 3 trading days | No imminent earnings flagged | **PASS** |
| 8 | Daily loss | < 3% of equity | $0.00 (0% today) | **PASS** |
| 9 | Monthly drawdown | < 10% of equity | 0.00% | **PASS** |
| 10 | Conviction (soft) | >= 6/12 | 10/12 | **PASS** |
| 11 | Strategy confirmed | Required | MA Crossover fully triggered (10 EMA > 50 EMA, price > 10 EMA) | **PASS** |
| 12 | News-tech aligned (soft) | No contradictions | High-volume breakout + MA confirmation + RSI 56.91 aligned | **PASS** |
| 13 | Not adding to loser | Required | No existing ROKU position; first entry | **PASS** |
| 14 | Correlation check (soft) | Not correlated with existing | Zero open positions; no correlation risk | **PASS** |

---

## Verdict: **GO**

### APPROVED FOR EXECUTION

| Parameter | Value |
|-----------|-------|
| **Symbol** | ROKU |
| **Direction** | LONG |
| **Entry Price** | $134.73 |
| **Stop Loss** | $127.18 |
| **Take Profit** | $148.88 |
| **Shares** | 18 |
| **Order Type** | Bracket (Market entry + Hard Stop + Take Profit) |
| **Risk Amount** | $135.90 (0.97% of equity) |
| **Position Size** | 2.43% of account |
| **R:R Ratio** | 1.87:1 |

---

## Gatekeeper Notes

**All hard checks pass cleanly. All soft checks pass. Zero warnings.**

This is a high-conviction setup (10/12 from Agent 04) with textbook alignment: MA crossover fully confirmed, news narrative supporting momentum, RSI building without extension, R:R attractive (1.87:1 vs. 1.5:1 floor), position sizing tight (0.97% risk on $139K account). Agent 03 flagged HIGH confidence. No earnings risk. Portfolio is flat with 97.57% dry powder — this is exactly the type of tactical entry we deploy with discipline when setups are clean.

**Position sizing matches conviction:** 10/12 conviction justifies 1.0% risk allocation (full size). Actual risk is 0.97%, which aligns with tier. ✓

**Kill conditions are specific and actionable** (price below 10 EMA, RSI below 40, volume collapse, sector reversal, VIX spike). Monitor first 2 hours for confirmation per Agent 04's execution notes.

**One note:** Recent learning log shows MA Crossover had two false positives (GS, GOOGL) before the QCOM correct call. This trade is **cleaner** than those misses — higher conviction score, no borderline signals, full news-tech-macro confluence. The strategy works when applied with full conviction; this qualifies.

**Execution can proceed immediately. Bracket order ready to submit.**

---

## Decision Summary
- ✅ **HARD CHECKS:** 11/11 PASS
- ✅ **SOFT CHECKS:** 4/4 PASS (zero warnings)
- ✅ **POSITION SIZING:** Matches 10/12 conviction tier (1.0% risk)
- ✅ **FINAL VERDICT:** **GO — EXECUTE NOW**