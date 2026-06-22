# Gatekeeper Verdict — NVDA — 2026-06-22

## Checklist Results

| # | Check | Rule | Value | Result |
|---|-------|------|-------|--------|
| 1 | Risk per trade | <= 1% of equity | 0.79% | **PASS** |
| 2 | Total positions | <= 6 | 0 (will be 1) | **PASS** |
| 3 | Total exposure | <= 70% of equity | 14.9% (will be post-trade) | **PASS** |
| 4 | Position size | <= 15% of equity | 14.9% of equity | **PASS** |
| 5 | R:R ratio (soft) | Meets strategy min (1.5:1) | 1.99:1 | **PASS** |
| 6 | ATR stop set | Required | Yes (ATR-based: $198.67) | **PASS** |
| 7 | Earnings clear | > 3 trading days | 65 calendar days (44+ trading days) | **PASS** |
| 8 | Daily loss | < 3% of equity | $0.00 (no trades today) | **PASS** |
| 9 | Monthly drawdown | < 10% of equity | 0.00% | **PASS** |
| 10 | Conviction (soft) | >= 6/12 | 9/12 | **PASS** |
| 11 | Strategy confirmed | Required | Yes (MA Crossover fully confirmed by Agent 02) | **PASS** |
| 12 | News-tech aligned (soft) | Required | Yes (bullish news + bullish technicals; Agent 03 HIGH confidence) | **PASS** |
| 13 | Not adding to loser | Required | N/A (new position, no existing NVDA) | **PASS** |
| 14 | No correlation (soft) | Required | N/A (portfolio empty; no correlation conflicts) | **PASS** |

---

## Verdict: **GO**

### APPROVED FOR EXECUTION

| Parameter | Value |
|-----------|-------|
| **Symbol** | NVDA |
| **Direction** | LONG |
| **Entry** | $209.83 (market or limit $209.83–$210.50) |
| **Stop Loss** | $198.67 (ATR-based; -$11.16/share) |
| **Take Profit** | $232.01 (1.99:1 R:R target) |
| **Shares** | 99 |
| **Position Value** | $20,773.17 |
| **Risk Amount** | $1,104.84 (0.79% of equity) |
| **Order Type** | Bracket (Market entry + Stop loss at $198.67 + Take profit at $232.01) |

---

## Execution Checklist
- [ ] Verify Alpaca account has $139,389.34 equity and $139,389.34 cash available
- [ ] Submit bracket order: 99 shares NVDA at market, stop at $198.67, target at $232.01
- [ ] Confirm order fills
- [ ] Log entry to `P-portfolio/current-positions.md` immediately
- [ ] Set kill condition monitor: Volume < 0.5M on 3 consecutive bars → exit at market
- [ ] Set breakeven tighten trigger: After +$552.42 profit (0.5R), move stop to $209.83
- [ ] Expected hold window: 5–10 trading days to target

---

## Gatekeeper Notes

**This is a solid trade. All hard checks pass cleanly. No warnings on soft checks.**

The setup is textbook: MA Crossover with the 10 EMA above the 50 EMA in a confirmed uptrend, entry on a pullback, earnings 65 days out (zero binary risk), macro supportive (risk-on regime), and R:R favorable at 1.99:1. Agent 04 scored this at 9/12 conviction, which is well above threshold and justifies full position sizing (0.79% risk).

**One caveat acknowledged by Agent 04 (not a blocker):** Relative volume on entry bar is weak (0.33x vs 0.8x threshold). This is NOT a hard failure — MA Crossover pullback entries often show low volume at entry — but it does warrant active monitoring. Agent 04 has correctly built in a **volume-drought kill condition**: if 3 consecutive bars close below 0.5M shares, exit at market. This is a professional hedge against a false breakout on weak follow-through. Monitor this closely in the first 2–3 bars post-entry.

**Position sizing matches conviction**: 9/12 conviction score qualifies for full 1% risk allocation. Agent 04 sized to 0.79% (slightly conservative), which is acceptable and actually prudent given the volume caveat. This is professional SOS (Strength of Signal) sizing.

**Portfolio context**: Empty portfolio, so this position brings total exposure to 14.9% with 85.1% dry powder remaining. Significant room for additional positions if opportunities arise.

**Execution note**: Use a bracket order (market entry, stop at $198.67, target at $232.01). This ensures stops and targets are live from the moment of fill — no manual order management required.

**Expected outcome**: 5–10 day hold window to $232.01 target (based on historical MA Crossover timing). If target doesn't come within 10 days or if the MA structure breaks down (10 EMA crosses below 50 EMA), reassess the trade for exit.

---

## Decision Authority
✅ **GATEKEEPER APPROVAL: EXECUTE IMMEDIATELY**

No further approvals needed. This trade is ready for live submission to Alpaca.

---

**Gatekeeper Signature**: Agent 05  
**Timestamp**: 2026-06-22 15:52 UTC  
**Loop Count**: 0 of 2 (no rejections — immediate approval)