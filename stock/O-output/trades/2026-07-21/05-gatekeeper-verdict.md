# Gatekeeper Verdict — MULTI-CANDIDATE REVIEW — 2026-07-21

## Checklist Results

| # | Check | Rule | Value | Result |
|---|-------|------|-------|--------|
| 1 | Risk per trade | <= 1% of equity | N/A (no position) | PASS |
| 2 | Total positions | <= 6 | 0 | PASS |
| 3 | Total exposure | <= 70% of equity | 0.0% | PASS |
| 4 | Position size | <= 15% of equity | N/A (no position) | PASS |
| 5 | R:R ratio (soft) | Meets strategy min (1.5:1) | PANW 0.81:1, CRWD 1.22:1, NET 0.89:1, DDOG 0.66:1 | WARN |
| 6 | ATR stop set | Required | N/A (no position) | PASS |
| 7 | Earnings clear | > 3 days | N/A (all clear per Agent 04) | PASS |
| 8 | Daily loss | < 3% | 0.00% | PASS |
| 9 | Monthly drawdown | < 10% | 0.00% | PASS |
| 10 | Conviction (soft) | >= 6/12 | 2/12 aggregate | WARN |
| 11 | Strategy confirmed | Required | Confirmed by Agent 02 (MA structure) | PASS |
| 12 | News-tech aligned (soft) | No contradictions | Bullish alignment across all candidates | PASS |
| 13 | Not adding to loser | Required | N/A (no existing positions) | PASS |
| 14 | No correlation (soft) | Required | N/A (no existing positions) | PASS |

---

## Verdict: **NO-GO**

### Status: FIXABLE (conditionally) / NOT FIXABLE (today)

---

## Hard Checks: ✓ ALL PASS

All hard checks pass cleanly. Portfolio metrics are healthy. No position size violations, no exposure limits breached, no earnings conflicts, no daily/monthly circuit breakers triggered.

---

## Soft Checks: 2 WARNINGS

**Soft Check #5 — R:R Ratio (WARN)**
- Rule: Meets strategy minimum (1.5:1)
- Reality: All four candidates fail R:R requirement
  - PANW: 0.81:1 (46% shortfall)
  - CRWD: 1.22:1 (19% shortfall)
  - NET: 0.89:1 (41% shortfall)
  - DDOG: 0.66:1 (56% shortfall)
- Severity: **High** — This is a structural payout failure, not a margin call

**Soft Check #10 — Conviction Score (WARN)**
- Rule: >= 6/12 for trade approval
- Reality: 2/12 aggregate
- Rationale: Agent 04 explicitly failed the 6-point minimum threshold due to broken R:R across the cohort

---

## Analysis

**2 soft warnings = within tolerance (max 2 allowed).** However, this is not a borderline case where warnings are abstract. This is a **deliberate hold decision**.

### Why NO-GO (Even Though Checklist Allows It)

Agent 04's decision to PASS (hold all trades) is **correct and enforceable** because:

1. **Soft warnings do not override fundamental risk-reward geometry.** The rule allows up to 2 soft warnings, but wisdom requires respecting them.
2. **R:R failure is systematic across the entire candidate set.** This is not one bad setup; it's an environmental mismatch.
3. **Agent 04 explicitly noted:** "A technically perfect setup with 0.66:1 R:R is still a losing trade."
4. **The learning log shows recent missed wins** (ABNB, V, ROKU), but those were conviction-based passes with viable R:R. Today's candidates have **broken payouts**, making them structurally different.

### Is This Fixable?

**YES, but not today.**

Agent 04 provided the solution: "Monitor, don't trade. When R:R approaches 1.5:1, reassess."

This means:
- PANW, CRWD, NET, DDOG remain on watchlist
- **Deeper pullbacks** (3-5% further) while maintaining 10 EMA > 50 EMA > 200 SMA structure will improve geometry
- When R:R recalibrates to ~1.5:1, these become resubmittable candidates

---

## Decision: **NO-GO (FIXABLE)**

**REJECTED FOR TODAY — RESUBMIT WHEN R:R IMPROVES**

### Fixable Instructions for Agent 04

1. **Do not size any position from today's candidate set.**
2. **Monitor PANW, CRWD, NET, DDOG daily** for deeper pullbacks while maintaining bullish MA structure.
3. **Recalculate R:R daily.** When any candidate approaches 1.5:1 or better:
   - Resubmit that candidate to full workflow (Agent 01 → 02 → 03 → 04 → 05)
   - Do NOT skip the full chain
4. **Expected timeframe:** 1-3 trading days (based on typical pullback cycles)
5. **If no pullback occurs** after 5 trading days, mark candidates as "macro headwinds changed" and drop from watchlist.

### Loop Count
**Loop: 1 of 2**

This is the first rejection. Agent 04 retains one final loop to resubmit these candidates (or others) with improved geometry.

---

## Gatekeeper Notes

**This is a difficult decision to articulate because the checklist technically allows the trade.** But professional risk management sometimes means saying "no" to technically sound setups with broken payouts.

Here's the reality:
- MA structure is confirmed bullish ✓
- Sector momentum is positive ✓
- News-tech alignment is clean ✓
- Fundamentals are healthy ✓
- Macro is risk-on ✓
- **But the risk-reward ratio is 0.66:1 to 1.22:1, and we require 1.5:1.** ✗

**This is not a setup problem. It is an entry-timing problem.** These stocks are in the right trend at the wrong price-to-reward ratio. That's OK. We wait.

The learning log shows we missed ABNB (+2.49%), V (+2.78%), ROKU (+0.17%) in recent days. I understand the FOMO. But those trades had acceptable R:R; we passed them on conviction. **Today's candidates have broken R:R.** That's the difference.

**Patience is an edge. We sit in cash, we preserve capital, and we wait for geometry to improve.**

When these candidates pull back 3-5% while maintaining their bullish structure, they'll become high-probability entries. That's the trade to take.

---

## Final Verdict

**NO-GO — FIXABLE**
- **Reason:** R:R failure across all four candidates
- **Sent back to:** Agent 04
- **Resubmit when:** Any candidate achieves R:R ≥ 1.5:1
- **Loop count:** 1 of 2
- **Action:** Hold portfolio in cash. Monitor watchlist daily.

**Capital preserved. Discipline maintained. We'll trade when the odds are in our favor.**