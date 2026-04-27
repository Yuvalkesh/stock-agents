# Rejected by Gatekeeper

## Agent 4 Decision
# Trade Decision — Multi-Asset — 2026-04-27

## Score: 3/12

### Scoring Breakdown
| # | Criterion | Score | Evidence |
|---|-----------|-------|----------|
| 1 | Strategy confirmed | 0/2 | SPY & AAPL have MA Crossover setup confirmed, BUT both fail R:R minimum. No other tickers have triggered technical strategies. |
| 2 | News + tech agree | 1/2 | SPY: news (RISK-ON) aligns with setup (bullish MA crossover), but reward insufficient. AMD/AMAT: news bullish but tech shows exhaustion (RSI 71-99). Partial alignment only. |
| 3 | Macro aligned | 0/1 | Macro is RISK-ON per Agent 01, but Mag-7 earnings within 3 days create binary event risk that contradicts swing-trade suitability. Geopolitical caution on energy. |
| 4 | R:R meets strategy min | 0/1 | SPY R:R = 0.04:1 (MIN: 1.5:1) ❌. AAPL R:R = 0.53:1 (MIN: 1.5:1) ❌. Both fail catastrophically. |
| 5 | Volume confirms | 0/1 | SPY/AAPL volume not explicitly confirmed in Agent 02 output. AMD/AMAT have 2.11x vol but RSI exhaustion negates signal. |
| 6 | Risk rules pass | 0/1 | AAPL violates hard rule: earnings on 2026-04-30 (3 days away = within exclusion zone). MSFT/GOOGL/AMZN/META on 2026-04-29 create correlated volatility spike risk. |
| 7 | No earnings within 3 trading days | 0/1 | **AAPL fails**: earnings 2026-04-30 (3 days). **MSFT fails**: 2026-04-29 (2 days). 5 Mag-7 names report within 3 days = elevated binary risk environment. |
| 8 | High confidence | 0/1 | Agent 03 explicitly states confidence is "N/A — NO TRADES EXECUTED" due to setup failures. Confidence rating does not exist for any candidate today. |
| 9 | Fundamentals healthy | 2/2 | AMD: +72.2% YTD, AI demand intact, analyst bullish. AMAT: +23.7% YTD, chip equipment demand. LRCX: +26.7% YTD. **BUT**: Price action exhaustion overrides fundamental strength. |
| **Total** | | **3/12** | **BELOW THRESHOLD** |

---

## Decision: **PASS**

### Rationale

**This is a NO-GO day.** The scoring summary above masks a critical point: even the "best" candidates today are **not actually good trades**.

#### Why SPY and AAPL Are Rejected Despite Setup Confirmation

1. **SPY MA Crossover (0.04:1 R:R)**
   - Risk $12.96/share to win $0.53/share
   - This violates the fundamental principle of swing trading: **risk more to win less**
   - Professional minimum is 1.5:1; this is 3,000% worse
   - Agent 03 is correct: "Not viable under any professional standard"

2. **AAPL MA Crossover (0.53:1 R:R) + Earnings Risk**
   - Risk $8.82/share to win $4.71/share
   - 64% below minimum R:R requirement
   - **AND** earnings in 3 days = binary event risk
   - Learning Log shows: "HINDSIGHT REVIEW (GOOD_PASS): ...We correctly passed" on similar earnings-zone trades (JNJ, COP, WMT, MTD)
   - **Lesson applied**: Do not trade into earnings windows. This has been proven correct multiple times.

#### Why Semiconductor Names (AMD, AMAT, LRCX) Are Rejected Despite Bullish Fundamentals

**Agent 01 narrative is sound**: AI chip demand is real, earnings surprises likely, relative strength is strong.

**Agent 02 price action screams overbought**:
- AMD: RSI(14) = 88.94 (extreme exhaustion)
- AMAT: RSI(2) = 97.48 (most extreme possible overbought)
- LRCX: RSI(2) = 71.49 (overbought), MACD histogram narrowing (momentum divergence)

**The conflict resolution**: Fundamentals and news can be correct *and* price can still be overextended. The chart is saying "you're 3-4 standard deviations above fair value right now." Entering a breakout at max overbought = **chasing momentum into a mean reversion trap.**

Learning Log evidence: "HINDSIGHT REVIEW (MISSED_WIN): ...EOG reached target...We passed...LESSON: This type of pass was WRONG — consider loosening criteria." However, many passes were also CORRECT (JNJ, CAT, DE, LIN, MCD, PEP, WMT, COP, MTD). **The pattern is: strict passes work when R:R is poor OR momentum is exhausted. This trade has BOTH problems.**

#### Why Today Is a Waiting Game, Not a Trading Day

- **Volatility backdrop**: 5 mega-cap earnings in 60 hours create uncertainty
- **Pullback opportunity cost**: If AMD/AMAT pullback to 10 EMA (inevitable given RSI 71-99), we'll have better entry prices *and* better R:R setups
- **Current portfolio**: MRVL is +$14K unrealized. Risking that edge on a 0.04:1 R:R trade is irresponsible

---

## Portfolio Context

| Metric | Status |
|--------|--------|
| Current positions | 1 (MRVL long) |
| Total exposure | $34,454.16 |
| Unrealized P&L | +$14,183.02 |
| Room for new trades | Yes, within 1% risk limit |
| Correlation risk | SPY/QQQ/AAPL are system beta; adding now while MRVL is up contradicts concentration rule |

**Portfolio decision**: We have a winning trade in MRVL. Today's candidates (SPY, AAPL, semiconductors) are all positively correlated with MRVL's gains. Adding exposure now = stacking the same bet. Better to wait for a *negative* correlation opportunity (energy hedge, short setup, or mean-reversion in sold-off sector).

---

## Kill Conditions
(Not applicable — no trade is being initiated)

---

## Reference Comparison

### Past Similar Trades

**From Learning Log**:
- **MISSED_WIN**: "LRCX reached target $273.50 (+3.93%) within 4 days. We passed because: Gatekeeper NO-GO. Strategy: ma_crossover. LESSON: This type of pass was WRONG."
  - *Interpretation*: We passed on LRCX 4 days ago; it did hit target. So why pass today?
  - *Answer*: That LRCX setup likely had better R:R or occurred outside earnings window. Today's LRCX has NO ACTIVE SETUP (Agent 02 confirms: "MACD histogram flattening, no crossover"). We're not passing on a setup; the setup doesn't exist yet.

**GOOD_PASS Examples**:
- "JNJ hit stop $236.94 (-2.51%) within 3 days. We correctly passed. Reason: Agent 4 PASS — scored below threshold. Strategy: ma_crossover. LESSON: This type of pass was CORRECT."
- "CAT dropped to $722.18 (-4.08%) after 3 days. We correctly passed. Strategy: none."
- Multiple earnings-zone passes (JNJ, COP, WMT) that avoided losses when stops were hit

**Lesson applied**: When score is 3/12 and R:R is catastrophic, passing is historically correct. Earnings exclusion zone is defensible (multiple GOOD_PASS confirmations on this exact rule).

---

## Trade Thesis
(N/A — No trade is being executed)

---

## Detailed Rejection Summary

### SPY: 0.04:1 R:R is Disqualifying
- Setup: MA Crossover confirmed (50 EMA > 200 SMA)
- Entry: ~$677.19
- Stop: $690.15
- Target: $677.72
- **Risk/Reward**: Risk $12.96 to win $0.53
- **Why this fails**: This setup is *technically valid* but *economically invalid*. You are risking $1,300 to make $50 on a $67,000 position. The win rate would need to be 96%+ to justify the asymmetry. Our historical win rate is ~50-60%. **REJECT on R:R alone.**

### AAPL: 0.53:1 R:R + Earnings Disqualification
- Setup: MA Crossover confirmed
- Entry: ~$266.67
- Stop: $275.49
- Target: $271.38
- **Risk/Reward**: Risk $8.82 to win $4.71 = 0.53:1 (64% below 1.5:1 minimum)
- **Earnings**: 2026-04-30 (3 days away = within exclusion zone)
- **Why this fails**: Even without earnings, R:R doesn't justify entry. Combined with earnings, it's a double no-go. Learning Log shows repeated GOOD_PASS confirmations on earnings exclusion rule.

### AMD, AMAT, LRCX: Momentum Exhaustion Despite Bullish News
- **AMD**: Bollinger breakout but RSI(14)=88.94 → imminent mean reversion
- **AMAT**: No active setup, RSI(2)=97.48 (most extreme overbought), MACD flat
- **LRCX**: MACD histogram narrowing (momentum divergence), no active crossover
- **Why this fails**: Fundamentals are bullish, but *price has already moved 70%+*. Entering at max overbought without a confirmed pullback is **variance betting, not edge betting**. Wait for RSI to cool to 50-60 range; then re-run analysis.

---

## Recommendation to Agent 04 (Self)

### Today's Action
**STAND DOWN. Monitor, don't trade.**

### Watchlist for Pullback Entry (Action Items)

| Ticker | Setup to Monitor | Entry Trigger | Expected R:R |
|--------|------------------|---------------|--------------|
| AMD | Bollinger mean reversion | RSI falls to 50-60, price pulls to 10 EMA | 2:1+ (estimated) |
| AMAT | MA crossover re-trigger | RSI falls to <70, price consolidates | 2:1+ (estimated) |
| LRCX | MACD histogram divergence | RSI <70, MACD hist begins to widen | 1.5:1+ (estimated) |
| SPY | Better R:R setup | VIX spikes >22 or price pulls to 50 EMA | 2:1+ (estimated) |
| AAPL | Post-earnings setup | After 2026-04-30 earnings release | TBD (monitor) |

### Macro Catalysts to Watch
- **2026-04-29**: MSFT, GOOGL, AMZN, META earnings (volatility spike likely)
- **2026-04-30**: AAPL earnings (tech sector sentiment setter)
- **Post-earnings (2026-05-01+)**: Pullback opportunities likely as profit-taking hits overbought names

### Why This Discipline Matters
Your learning log shows you have been making **correct passes on bad setups**. The pattern is clear: when you pass due to low scores or R:R failures, the position often hits its stop within days. When you pass on earnings-zone trades, you avoid binary losses. **Keep this filter active.** Today's pass continues the winning pattern.

---

**Decision Final: PASS on all candidates. Preserve capital. Monitor watchlist. Reassess 2026-05-01 after earnings volatility settles.**

## Gatekeeper Verdict
# Gatekeeper Verdict — MULTI-ASSET — 2026-04-27

## Checklist Results

| # | Check | Rule | Value | Result |
|---|-------|------|-------|--------|
| 1 | Risk per trade | <= 1% | N/A (no trade) | PASS |
| 2 | Total positions | <= 6 | 1 open | PASS |
| 3 | Total exposure | <= 70% | 29.6% | PASS |
| 4 | Position size | <= 15% | 29.6% (MRVL only) | PASS |
| 5 | R:R ratio (soft) | Meets strategy min | SPY: 0.04:1 / AAPL: 0.53:1 / Semis: N/A | WARN |
| 6 | ATR stop set | Required | No trades submitted | PASS |
| 7 | Earnings clear | > 3 days | AAPL: 3 days (fail) / MSFT/GOOGL/AMZN/META: 2 days (fail) | FAIL |
| 8 | Daily loss | < 3% | -0.85% YTD, within limits | PASS |
| 9 | Monthly drawdown | < 10% | 0.00% | PASS |
| 10 | Conviction (soft) | >= 6/12 | 3/12 | WARN |
| 11 | Strategy confirmed | Required | SPY/AAPL confirmed but R:R fails; semis have no active setup | FAIL |
| 12 | News-tech aligned (soft) | Required | AMD/AMAT/LRCX: news bullish but RSI exhaustion contradicts | WARN |
| 13 | Not adding to loser | Required | N/A (MRVL is winning) | PASS |
| 14 | No correlation (soft) | Required | SPY/AAPL/semis all correlated with MRVL; stacking same bet | WARN |

---

## Verdict: **NO-GO (KILLED)**

---

## Hard Check Failures

### ❌ Hard Check #7: Earnings Proximity
- **AAPL**: Earnings 2026-04-30 = **3 trading days away** (exactly at boundary, functionally within exclusion zone)
- **MSFT, GOOGL, AMZN, META**: All report 2026-04-29 = **2 trading days away** (clear violation)
- **Rule violated**: No trade within 3 trading days of earnings
- **Status**: **IMMEDIATE DISQUALIFICATION** for any Mag-7 exposure
- **Impact**: This eliminates AAPL (hard stop) and makes SPY/QQQ exposure problematic (indirect Mag-7 correlation)

### ❌ Hard Check #11: Strategy Confirmation + R:R Alignment
- **SPY**: MA crossover confirmed BUT R:R = 0.04:1 (minimum required: 1.5:1) → **catastrophic failure**
  - Risk $12.96/share to win $0.53/share on a $67K position
  - This violates the core swing-trade principle: asymmetric reward-to-risk
  - Professional standard: not viable under any circumstance
  
- **AAPL**: MA crossover confirmed BUT R:R = 0.53:1 (minimum required: 1.5:1) → **severe failure** 
  - 64% below minimum threshold
  - Combined with earnings disqualification = double knockout
  
- **AMD/AMAT/LRCX**: No active technical setup confirmed
  - Agent 02 explicitly states: "AMAT has no active setup," "LRCX histogram flattening (no crossover)"
  - AMD has Bollinger breakout but **Agent 04 correctly notes this is exhaustion, not confirmation**
  - **Status**: No confirmed strategy = automatic rejection per hard rule #11

---

## Soft Check Warnings (4 total — Exceeds 2-warning threshold)

| Warning | Criterion | Issue |
|---------|-----------|-------|
| ⚠️ #1 | R:R ratio (soft check #5) | SPY 0.04:1 and AAPL 0.53:1 both catastrophically below 1.5:1 minimum |
| ⚠️ #2 | Conviction score (soft check #10) | 3/12 = well below 6/12 threshold (50% below minimum) |
| ⚠️ #3 | News-tech alignment (soft check #12) | AMD/AMAT/LRCX: bullish news contradicted by RSI exhaustion (88.94 / 97.48 / 71.49) |
| ⚠️ #4 | Correlation check (soft check #14) | SPY/AAPL/semis all positively correlated with existing MRVL position; stacking same trade |

**Soft warning count: 4 of 4 checks warn → Exceeds 2-warning limit by 2x**

---

## Combined Verdict Assessment

**Multiple disqualification layers:**

1. **Hard failures alone** (earnings + R:R + no confirmed setup) = **immediate NO-GO**
2. **Soft warnings** (4 warnings = 2x limit) = **secondary NO-GO confirmation**
3. **Portfolio logic** = MRVL is up $14K; adding correlated exposure risks concentration on a single beta narrative

**This is not a fixable issue. Every dimension fails.**

---

## Final Decision: **NO-GO (KILLED)**

### Reason for Kill
- **Primary**: Hard check #7 (earnings within 3 days) + Hard check #11 (R:R catastrophically below minimum + no confirmed setup on semis)
- **Secondary**: Soft check failures (4 warnings) exceed tolerance threshold by 2x
- **Tertiary**: Portfolio concentration risk (stacking MRVL's correlated beta)

### Fixable: **NO**

The failures are structural, not tactical:
- ~~Cannot fix earnings calendar~~ (fixed in time, not trade design)
- ~~Cannot improve R:R on SPY/AAPL~~ (targets are price-driven; widening targets introduces new risk)
- ~~Cannot create a confirmed setup on semis~~ (breakout is exhaustion, not entry)
- ~~Cannot reduce correlation to MRVL~~ (all mega-cap tech are systemic beta)

**No repositioning, size adjustment, or stop placement can salvage these trades.**

### Loop Count
**0 of 2 loop-backs required** — Trade is fundamentally unsound and is killed outright.

### Sent Back To
**N/A** — No loop-back needed. Agent 04 already concluded PASS (correctly). Gatekeeper confirms KILL.

---

## Output Log

**Trade Status**: PERMANENTLY KILLED  
**Date**: 2026-04-27  
**Reason Code**: EARNINGS_PROXIMITY + NEGATIVE_R:R + ZERO_SETUP + CORRELATION_STACKING  
**Logged to**: `O-output/rejected/2026-04-27-multi-asset-killed.md`

---

## Gatekeeper Notes

**This is a textbook pass-day. Agent 04 got it right.**

Agent 04's decision to PASS was sound and matches our hard rules perfectly. The market is throwing three different temptations at us today:

1. **"Safe" index plays (SPY)** — Technically valid setup, but the reward is so small it's disrespectful to the risk. This isn't a trade; it's noise. **Rejected.**

2. **"Popular" mega-cap (AAPL)** — Better R:R than SPY, but directly in the earnings exclusion zone with 4 other Mag-7 names reporting in the next 60 hours. Our learning log shows repeated GOOD_PASS confirmations on earnings trades. This one hits 3-day boundary. **Rejected.**

3. **"Momentum" semiconductors (AMD, AMAT, LRCX)** — Fundamentals are genuinely bullish (AI demand is real), but price has *already sprinted 70%+ YTD*. RSI readings of 88, 97, and 71 scream mean reversion, not breakout. This is **chasing momentum into a whipsaw**, which has historically burned us. Better entry prices are coming. **Rejected.**

**Portfolio context**: We have MRVL up $14K. It's a *good* trade, but it's also a mega-cap tech exposure. Adding SPY, AAPL, or semiconductors today means we're *stacking* the same beta bet. If tech pulls back 2-3% after Mag-7 earnings, we lose on *all three legs simultaneously*. **Concentration risk.**

**The disciplined move**: Hold MRVL, preserve capital, and monitor the watchlist. Post-earnings (2026-05-01+), when overbought names have cooled and pullbacks created better R:R setups, we'll have better opportunities. This patience has paid off repeatedly in the learning log.

**Conviction level**: 95% certain this kill is correct. The hard failures alone justify it; everything else is confirmation.

**Risk of this call**: We're passing on AMD while it's up 72% YTD and fundamentals are strong. If it gaps up another 5% post-earnings, we'll have missed it. *This is acceptable.* Better to miss one runner than to chase momentum into a reversal. Our win rate will be higher with better-setup entries.

---

## Recommendation to Agent 04

**Maintain the PASS. This gatekeeper verdict strongly endorses your decision.**

The market will provide better opportunities. Rest capital. Watch the watchlist. Act decisively on post-earnings pullbacks when RSI cools and R:R improves.

**Next review**: 2026-05-01 (after Mag-7 earnings volatility settles).