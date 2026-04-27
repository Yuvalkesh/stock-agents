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