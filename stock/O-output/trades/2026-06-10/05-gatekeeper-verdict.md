# Gatekeeper Verdict — MRVL — 2026-06-10

## Checklist Results

| # | Check | Rule | Value | Result |
|---|-------|------|-------|--------|
| 1 | Risk per trade | <= 1% | 0.99% | **PASS** |
| 2 | Total positions | <= 6 | 1 (after entry) | **PASS** |
| 3 | Total exposure | <= 70% | 6.8% | **PASS** |
| 4 | Position size | <= 15% | 6.8% | **PASS** |
| 5 | R:R ratio (soft) | Meets strategy min | 1.57:1 (req 1.5:1) | **PASS** |
| 6 | ATR stop set | Required | Yes (bracket order) | **PASS** |
| 7 | Earnings clear | > 3 days | No earnings flagged | **PASS** |
| 8 | Daily loss | < 3% | $0.00 (0.00%) | **PASS** |
| 9 | Monthly drawdown | < 10% | 0.00% | **PASS** |
| 10 | Conviction (soft) | >= 6/12 | 8/12 | **PASS** |
| 11 | Strategy confirmed | Required | MA Crossover confirmed by Agent 02 | **PASS** |
| 12 | News-tech aligned (soft) | No contradictions | Bullish alignment confirmed | **PASS** |
| 13 | Not adding to loser | Required | New position (no existing) | **PASS** |
| 14 | No correlation (soft) | Required | Portfolio empty (no correlation) | **PASS** |

---

## Verdict: **GO**

### APPROVED FOR EXECUTION

**Symbol:** MRVL  
**Direction:** LONG  
**Entry:** $263.67  
**Stop Loss:** $225.14  
**Target:** $324.20  
**Shares:** 36  
**Position Value:** $9,492.12 (6.8% of equity)  
**Risk Amount:** $1,387.08 (0.99% of equity)  
**R:R Ratio:** 1.57:1  

**Order Type:** Bracket (Limit Entry + Stop Loss + Take Profit)  
**Time in Force:** GTC (Good-til-canceled)  

---

## Detailed Check Analysis

### Hard Checks (All Pass ✓)

**1. Risk Per Trade: 0.99% ✓**
- Account equity: $139,389.34
- Risk amount: $1,387.08
- Calculation: Stop distance = $263.67 - $225.14 = $38.53 per share
- Shares: $1,387.08 / $38.53 = 35.98 ≈ 36 shares
- **Well within 1.0% hard limit**

**2. Total Open Positions: 1 ✓**
- Current positions: 0
- After entry: 1
- **Well within 6-position limit**

**3. Total Portfolio Exposure: 6.8% ✓**
- Position value: 36 × $263.67 = $9,492.12
- Current equity: $139,389.34
- Exposure: $9,492.12 / $139,389.34 = 6.8%
- **Well within 70% hard limit**

**4. Single Position Size: 6.8% ✓**
- Same calculation as #3
- **Well within 15% hard limit**

**6. Stop Loss Set: Yes ✓**
- ATR-based stop: $225.14 (1.5 × ATR(14) below 10 EMA entry per MA Crossover strategy)
- Stop is set in bracket order at submission
- **Non-negotiable requirement satisfied**

**7. Earnings Proximity: Clear ✓**
- Agent 04 confirms: "No earnings within 3 trading days"
- No earnings date flagged in risk analysis
- **No binary event risk**

**8. Daily Loss Limit: 0.00% ✓**
- Today's P&L: $0.00 (0.00%)
- Daily loss threshold: 3% = $4,181.68
- Current loss: $0.00
- **No circuit breaker triggered**

**9. Monthly Drawdown: 0.00% ✓**
- Month-to-date drawdown: 0.00%
- Monthly limit: 10% = $13,938.93
- Current drawdown: $0.00
- **No circuit breaker triggered**

**11. Strategy Confirmation: Yes ✓**
- Agent 02 confirms: "MA Crossover (10 EMA > 50 EMA) confirmed"
- Technical trigger: Price at 10 EMA ($263.67) with bullish 10/50/200 alignment
- **Fully validated by Agent 02**

**13. Not Adding to Loser: Yes ✓**
- This is a new position (portfolio currently has 0 positions)
- Not increasing an existing losing position
- **Rule satisfied**

---

### Soft Checks (All Pass — 0 Warnings)

**5. R:R Ratio: 1.57:1 ✓**
- Strategy minimum: 1.5:1 for MA Crossover
- Actual ratio: 1.57:1
- **Exceeds requirement — PASS**
- *No warning*

**10. Conviction Score: 8/12 ✓**
- Agent 04 scored: 8/12
- Minimum threshold: 6/12
- Position sizing matched: 1.0% risk (full size for 8/12 conviction)
- **Above threshold — PASS**
- *No warning*

**12. News-Tech Alignment: Yes ✓**
- Agent 03/04 analysis: "Bullish alignment: +32.9% MTD momentum + EMA pullback setup agree"
- News: Semiconductor structural AI demand persisting
- Technicals: MA Crossover confirmed, pullback to 10 EMA
- **No contradictions — PASS**
- *No warning*

**14. Correlation Check: None ✓**
- Current portfolio: 0 positions
- After entry: 1 position (MRVL)
- Correlation with existing positions: N/A
- **No overlapping sector bets — PASS**
- *No warning*

---

## Position Sizing Validation

**Conviction-Based Sizing Check:**
- Conviction score from Agent 04: **8/12** (HIGH)
- Required sizing tier: **1.0% risk** (full allocation for 8+/10)
- Actual risk amount: **$1,387.08 = 0.99% of equity**
- ✓ **Sizing matches conviction tier**

**Hard Limits Check:**
- Position value: $9,492.12
- Max allowed (15% of equity): $20,908.40
- ✓ **Position size 6.8% is well within 15% limit**

- Total exposure after entry: 6.8%
- Max allowed (70% of equity): $97,572.54
- ✓ **Total exposure 6.8% is well within 70% limit**

---

## Gatekeeper Notes

**Assessment:** This is a clean, professional trade setup. **APPROVED without hesitation.**

**Why this trade passes:**
1. **Technical confirmation is solid:** 10 EMA > 50 EMA with price pulling back to entry zone is the exact MA Crossover trigger Agent 02 specified. No ambiguity.
2. **Risk/reward geometry is favorable:** 1.57:1 ratio exceeds the 1.5:1 MA Crossover minimum. Upside (22.9% to target) justifies downside (14.6% to stop).
3. **Structural tailwind is real:** Semiconductor AI demand is not a short-term narrative — it's a persistent macro driver. MRVL benefits from this without being overextended like AMAT.
4. **Position sizing is disciplined:** 0.99% risk, 6.8% exposure with empty portfolio leaves ample dry powder for follow-up trades. No concentration risk.
5. **Conviction score (8/12) justifies full 1% risk allocation:** Agent 04 evaluated this properly — the setup is medium-to-high conviction, and the position size reflects that with full risk weight.

**Residual concerns (minor, non-blocking):**
- **Weak volume (0.27x relative):** This is a soft point, but not disqualifying for MA Crossover. Volume can improve after entry if the technical setup holds. Agent 04's kill condition "volume dries up after entry" is appropriate safeguard.
- **Analyst target only 22.9% above entry:** This is tight but workable. The $324.20 target sits at R1 resistance, which is realistic for mean reversion off pullback. Not a weakness — just a reminder this is a measured swing trade, not a moonshot.

**Execution notes:**
- Use **limit order at $263.67 or slightly below** to ensure fill given weak volume. Market order risks overfill at $266–$268 range.
- Set **daily alerts** at $255 (10 EMA support) and $324.20 (target) for active monitoring.
- **Review kill conditions** each morning for first 3 trading days:
  - Volume drops below 0.15x on any 5-bar window → exit at market
  - Price closes below $255 → exit at market
  - XSD (semis index) drops > 2% in single day → evaluate early exit
  - RSI(2) falls below 40 → consider taking 50% profits and trailing stop

**Bottom line:** All hard checks pass, soft checks show zero warnings, position sizing is disciplined, risk geometry is favorable, and conviction is high. This trade has a clear thesis (MA Crossover + structural AI tailwind), proper technical confirmation from Agent 02, and professional risk management. **Execute as specified. No modifications after GO.**

---

## Order Submission Details

**Bracket Order — MRVL**
- **Primary Leg (Entry):** Limit $263.67 × 36 shares
- **Stop Loss Leg:** Stop $225.14 (market on stop trigger)
- **Take Profit Leg:** Limit $324.20 (profit target)
- **Time in Force:** GTC
- **Status:** Ready for submission to Alpaca

---

**Gatekeeper Sign-Off:** ✓ **GO**  
**Decision Timestamp:** 2026-06-10 14:25 UTC  
**Next Review:** Monitor daily. Reassess if any kill condition triggers.