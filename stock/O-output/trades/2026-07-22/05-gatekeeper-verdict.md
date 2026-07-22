# Gatekeeper Verdict — NET — 2026-07-22

## Checklist Results

| # | Check | Rule | Value | Result |
|---|-------|------|-------|--------|
| 1 | Risk per trade | <= 1% of equity | 1.1% | **FAIL** |
| 2 | Total positions | <= 6 | 1 | PASS |
| 3 | Total exposure | <= 70% of equity | 14.8% | PASS |
| 4 | Position size | <= 15% of equity | 14.8% | PASS |
| 5 | R:R ratio (soft) | Meets strategy min | 0.92:1 | PASS |
| 6 | ATR stop set | Required | Yes ($252.03) | PASS |
| 7 | Earnings clear | > 3 days | 15 days | PASS |
| 8 | Daily loss | < 3% of equity | 0.0% | PASS |
| 9 | Monthly drawdown | < 10% of equity | 0.0% | PASS |
| 10 | Conviction (soft) | >= 6/12 | 7/12 | PASS |
| 11 | Strategy confirmed | Required | Yes (MA Crossover) | PASS |
| 12 | News-tech aligned (soft) | Required | Yes (aligned) | PASS |
| 13 | Not adding to loser | Required | Yes (first position) | PASS |
| 14 | No correlation (soft) | Required | N/A (empty portfolio) | PASS |

---

## Verdict: **NO-GO (FIXABLE)**

### Failed Checks
- **Hard Check #1: Risk per trade** — Position carries 1.1% risk, which exceeds the hard limit of 1.0% of equity

---

### Why This Fails
Agent 04 calculated max loss as $1,541.28 against account equity of $139,389.34:
```
$1,541.28 / $139,389.34 = 1.1%
```

This is a **hard check failure**. The rule is absolute: **Max risk per trade = 1% of equity.** There are no exceptions, no "close enough," no rounding grace. The market doesn't negotiate.

---

### Is This Fixable?
**YES.** The position is slightly oversized. The fix is straightforward: reduce shares to bring risk down to exactly 1.0%.

---

### Specific Fix Instructions (Send Back to Agent 04)

**Recalculate position size to 1.0% risk (not 1.1%):**

1. Target risk amount: $139,389.34 × 0.01 = **$1,393.89**
2. Stop distance: $272.31 - $252.03 = **$20.28**
3. Corrected shares: $1,393.89 / $20.28 = **68.7 shares** → **68 shares** (round down)
4. Verify:
   - Max loss: 68 × $20.28 = **$1,379.04** (0.99% of equity) ✓
   - Position value: 68 × $272.31 = **$18,516.98** (13.3% of account) ✓

**All other parameters remain identical:**
- Entry: $272.31
- Stop: $252.03
- Target: $291.00
- Direction: LONG
- Strategy: MA Crossover

**Return updated trade decision with 68 shares and resubmit.**

---

### Loop Count
**Loop 1 of 2** — First rejection. One more loop allowed before permanent kill.

---

### Sent Back To
**Agent 04** — Position sizing recalculation only. No strategic changes needed. All other checks pass cleanly.

---

## Gatekeeper Notes

This is a **solid trade that's simply one share too heavy.** Everything else is correct:
- Strategy is confirmed and clean (MA Crossover in textbook bullish alignment)
- News and technicals agree on the direction
- Earnings are safely 15 days away
- Conviction score of 7/12 is earned (developing trend, acceptable R:R, medium confidence)
- No portfolio conflicts (empty account, no correlation issues)

The only problem is a **math error on position sizing.** Agent 04 noted the correction was applied ("corrected to 76 shares"), but the resulting 1.1% risk exceeds our hard limit by 0.1%. This is not a character flaw of the trade — it's a rounding artifact.

**Fix it and resubmit.** At 68 shares, this trade is ready to execute. I'm not killing a clean setup over 8 shares.

**Correction confidence: HIGH.** The trade thesis is sound. The gating issue is purely mechanical. Turnaround should be immediate.