# Trade Decision — Multiple Candidates — 2026-06-10

## Summary of Decisions
Three candidates evaluated: **LRCX (REJECT)**, **MRVL (BUY)**, **AMAT (REJECT)**

---

## LRCX — Trade Decision

### Score: 3/12

#### Scoring Breakdown
| # | Criterion | Score | Evidence |
|---|-----------|-------|----------|
| 1 | Strategy confirmed | 2 | MACD + RSI mechanics confirmed by Agent 02 |
| 2 | News + tech agree | 2 | Bullish alignment: chip demand + MACD crossover |
| 3 | Macro aligned | 1 | Semiconductor structural tailwind valid |
| 4 | R:R meets strategy min | 0 | **0.22:1 ratio vs 1.0:1 minimum required — FAILS** |
| 5 | Volume confirms | 0 | 0.31x relative volume (weak) |
| 6 | Risk rules pass | 0 | Entry already above analyst target $318 |
| 7 | No earnings | 1 | No earnings within 3 days |
| 8 | High confidence | 0 | Agent 02 explicitly rejected: "Do not trade this setup" |
| **Total** | | **3/12** | **BELOW 6-point threshold** |

#### Decision: **PASS**

### Why This Trade Fails
**Fatal geometry error:** Entry at $342.68 is already 7.8% *above* the analyst's $318 target. This creates inverted risk/reward:
- Risk per share: $28.63 (downside to stop)
- Reward per share: $6.41 (upside to target)
- **Ratio: 0.22:1 — requires 4.5x the risk to win 1x reward**

While the MACD + RSI setup mechanics are technically confirmed and the narrative is bullish (chip equipment acceleration), the entry point is fundamentally broken. Agent 02's own analysis explicitly states: *"Do not trade this setup."*

### Kill Condition (N/A)
Trade rejected pre-entry. No position will be opened.

### Lesson for Learning Log
**Reminder:** News-driven bullish sentiment does not justify entry at resistance levels with poor R:R geometry. Wait for pullback to create favorable risk/reward, or skip entirely if target has already been reached.

---

## MRVL — Trade Decision

### Score: 8/12

#### Scoring Breakdown
| # | Criterion | Score | Evidence |
|---|-----------|-------|----------|
| 1 | Strategy confirmed | 2 | MA Crossover (10 EMA > 50 EMA) confirmed by Agent 02 |
| 2 | News + tech agree | 2 | Bullish alignment: +32.9% MTD momentum + EMA pullback setup agree |
| 3 | Macro aligned | 1 | Semiconductor structural AI demand persisting (no macro headwind) |
| 4 | R:R meets strategy min | 1 | 1.57:1 ratio exceeds 1.5:1 minimum for MA Crossover |
| 5 | Volume confirms | 0 | 0.27x relative volume (weak, below 0.8x threshold) |
| 6 | Risk rules pass | 1 | Position sized to 1.0% account risk ($1,387 max loss, 6.8% exposure) |
| 7 | No earnings | 1 | No earnings within 3 trading days |
| 8 | High confidence | 1 | Confidence rating: MEDIUM (setup valid, but volume weak) |
| 9 | Fundamentals healthy | 2 | Positive earnings growth + analyst target above current ($324 > $263.67) |
| **Total** | | **8/12** | **MEETS 6-point threshold** |

#### Decision: **BUY**

### Trade Parameters
| Parameter | Value |
|-----------|-------|
| Symbol | MRVL |
| Direction | LONG |
| Strategy | MA Crossover (10 EMA / 50 EMA) |
| Entry | $263.67 |
| Stop Loss | $225.14 |
| Take Profit | $324.20 |
| Shares | 36 |
| Risk Amount | $1,387.08 (1.0% of account) |
| R:R Ratio | 1.57:1 |

### Trade Thesis
Marvell is riding structural AI-driven semiconductor demand (+32.9% monthly momentum) and has pulled back to the 10 EMA ($263.67), providing a clean MA Crossover entry point with bullish 10/50/200 EMA alignment. Risk/reward of 1.57:1 justifies entry; analyst target of $324 sits above resistance R1, providing a realistic 22.9% upside target with only 14.6% downside risk. Portfolio is empty, so no correlation concerns; position sized conservatively to 1% account risk.

### Kill Conditions
- **Volume dries up after entry:** If relative volume drops below 0.15x on any 5-bar period within first 3 days, momentum play is invalidated — exit at market.
- **Price closes below $255 (below 10 EMA support):** Technical breakdown suggests false signal — exit at market.
- **Sector momentum breaks (semis index XSD drops > 2% in single day):** Structural tailwind is shattered — evaluate for early exit.
- **RSI(2) drops below 40:** Momentum cooling suggests pullback is deeper than expected — consider taking half profits and trailing stop on remainder.

### Portfolio Context
- Current positions: 0
- Total exposure after this trade: 6.8% ($9,492 of $139,389)
- Correlation: N/A (portfolio empty)
- **Verdict:** Position is safe within all risk limits and adds no correlation complexity.

### Reference Comparison
- **Similar to past trade:** MA Crossover strategy has shown mixed results in learning log (GOOD_PASS on QCOM rejection, MISSED_WIN on GS and XLK setups where we were too strict).
- **Lesson applied:** This MRVL setup scores 8/12 (above 6-threshold) with genuine 1.57:1 R:R and structural tailwind. Unlike past rejections, this trade has **technical confirmation + news alignment + proper risk geometry**. The weak volume (0.27x) is a secondary concern, not disqualifying for MA Crossover. **Approve this trade.**

---

## AMAT — Trade Decision

### Score: 2/12

#### Scoring Breakdown
| # | Criterion | Score | Evidence |
|---|-----------|-------|----------|
| 1 | Strategy confirmed | 0 | **No technical entry trigger — price overextended, no pullback** |
| 2 | News + tech agree | 1 | News is bullish but technicals say "already moved" (contradiction) |
| 3 | Macro aligned | 1 | Semiconductor structural tailwind valid |
| 4 | R:R meets strategy min | 0 | No viable stop/target geometry (overextended entry) |
| 5 | Volume confirms | 0 | 0.31x relative volume (weak); no momentum confirmation |
| 6 | Risk rules pass | 0 | Entry at $525.36 is already above analyst target $511 |
| 7 | No earnings | 1 | No earnings within 3 days |
| 8 | High confidence | 0 | Agent 02 states: "NO SETUP — price extended, no pullback trigger" |
| **Total** | | **2/12** | **BELOW 6-point threshold** |

#### Decision: **PASS**

### Why This Trade Fails
**Setup already exhausted:** AMAT has already rallied 7.8% above analyst target ($525.36 vs $511) with price extended 7.8% above 10 EMA and 20.3% above 50 EMA. RSI(2) of 86.9 indicates overbought conditions, not oversold pullback opportunity.

Agent 01's bullish narrative (AI chip demand, breakout momentum) is **true but already priced in**. Agent 02 correctly identifies that **there is no technical entry point** — the move has happened, and price is now chasing momentum with no support level to anchor a stop loss.

This is a classic "buy high" trap: news confirms the bull case, but technicals show the trade has already executed. Waiting for a pullback to $484–$495 (to 10 EMA) would create a viable entry with proper R:R geometry.

### Kill Condition (N/A)
Trade rejected pre-entry. No position will be opened.

### Lesson for Learning Log
**Pattern Recognition:** When analyst target is already breached by entry price, do not force a trade. Wait for **pullback confirmation or new technical catalyst** (e.g., breakout to new high on volume). Riding momentum at resistance is high-risk.

---

## Final Summary

| Symbol | Decision | Score | Reason |
|--------|----------|-------|--------|
| **LRCX** | **PASS** | 3/12 | R:R geometry inverted (0.22:1). Entry above analyst target. Agent 02 explicit reject. |
| **MRVL** | **BUY** | 8/12 | MA Crossover confirmed, 1.57:1 R:R valid, structural tailwind, proper risk sizing. |
| **AMAT** | **PASS** | 2/12 | No technical entry trigger. Price already extended above target. No pullback zone. |

---

## Actions to Execute

### BUY Order — MRVL
**Bracket Order Parameters:**
- **Entry:** $263.67 (36 shares)
- **Stop Loss:** $225.14 (hard stop, max loss $1,387.08)
- **Take Profit:** $324.20 (target at R1 resistance)
- **Time in Force:** GTC (good-til-canceled)
- **Order Type:** Limit (to control slippage given weak volume)

**Execution Notes:**
- Place limit order at or slightly below $263.67 to ensure fill at pullback zone
- Set alerts at $255 (10 EMA support) and $324.20 (target) for monitoring
- Review kill conditions daily for first 3 trading days

---

**Output Written:** `O-output/trades/2026-06-10/04-trade-decision.md`