# Gatekeeper Verdict — ROKU — 2026-06-17

## Checklist Results

| # | Check | Rule | Value | Result |
|---|-------|------|-------|--------|
| 1 | Risk per trade | <= 1% of equity | 0.5% | **PASS** |
| 2 | Total positions | <= 6 | 1 (after trade) | **PASS** |
| 3 | Total exposure | <= 70% of equity | 7.5% | **PASS** |
| 4 | Position size | <= 15% of equity | 7.5% | **PASS** |
| 5 | R:R ratio (soft) | Meets strategy min (1.0:1) | 1.06:1 | **PASS** |
| 6 | ATR stop set | Required | Yes ($129.70 hard stop) | **PASS** |
| 7 | Earnings clear | > 3 days | Not in 5-day window | **PASS** |
| 8 | Daily loss | < 3% of equity | $0.00 (0.00%) | **PASS** |
| 9 | Monthly drawdown | < 10% of equity | 0.00% | **PASS** |
| 10 | Conviction (soft) | >= 6/12 | 7/12 | **PASS** |
| 11 | Strategy confirmed | Required | Yes (MACD + RSI confirmed) | **PASS** |
| 12 | News-tech aligned (soft) | No contradictions flagged | Yes (both bullish) | **PASS** |
| 13 | Not adding to loser | Required | N/A (no existing position) | **PASS** |
| 14 | No correlation (soft) | Not correlated with existing | N/A (clean portfolio) | **PASS** |

---

## Verdict: **GO**

### APPROVED FOR EXECUTION

**Symbol:** ROKU  
**Direction:** LONG  
**Entry:** $139.03  
**Stop Loss:** $129.70  
**Take Profit:** $148.88  
**Shares:** 75 (half position)  
**Risk Amount:** $696.95 (0.5% of $139,389.34 equity)  
**Position Value:** $10,427.25 (7.5% of equity)  
**Order Type:** Bracket (Market + Stop + Take Profit)

---

## Execution Parameters
```
Entry Order:    BUY 75 ROKU @ MARKET ($139.03)
Stop Order:     SELL 75 ROKU @ $129.70 (hard stop)
Target Order:   SELL 75 ROKU @ $148.88 (profit target)
```

**Bracket setup:** Both stop and target active simultaneously. First-to-trigger closes the position.

---

## Gatekeeper Notes

**This trade passes all hard checks cleanly.** Let me be blunt about what I'm seeing:

### What Works
- **MACD + RSI setup is textbook.** MACD crossover is *confirmed*, not pending. RSI at 62.8 is in the optimal zone (40-70). This is legitimate technical signal, not a guess.
- **Position sizing is intelligent.** Agent 04 correctly identified a 7/12 conviction score and right-sized it at 0.5% risk / 50% position. That's professional risk management — you don't take full-size bets on marginal setups. I respect that discipline.
- **News-tech alignment holds.** Rising Star breakout (+14.9% MoM) aligns with the MACD cross and RSI momentum. No contradictions. Sector (XLY) is supporting momentum trades in a risk-on regime.
- **Portfolio is clean.** Zero existing positions means zero correlation noise, zero compounding risk. This is a fresh entry into dry powder.
- **All hard limits are respected.** Risk is 0.5%, exposure is 7.5%, stop is hard-set, no earnings, no circuit breaker violations. Nothing to block here.

### What Concerns Me (But Doesn't Kill the Trade)
- **Volume is legitimately weak (0.36x vs. 2.2x historical).** This is Agent 04's stated weakness, and it's real. If the stock breaks up but volume doesn't follow, you could get stopped out on a false breakout. However:
  - The half-position sizing *acknowledges this risk*. You're not over-committing.
  - Agent 04's kill conditions (#1: exit 50% if volume stays below 0.5x for 2 bars) are appropriate guardrails. **Enforce these on tape.**
  - Weak volume at entry doesn't invalidate the MACD signal — it just means you need to watch tape on the first 2 bars.

- **R:R ratio is tight (1.06:1).** Not ideal, but it meets the strategy minimum (1.0:1). You'd prefer 1.5:1, but this setup delivers what it delivers. A 1.06:1 ratio on a high-probability MACD cross is still +EV if the win rate is high enough.

- **Medium confidence (Agent 03).** The 7/12 score reflects this. But 7/12 means "more likely than not to work," and confidence isn't measured by conviction alone — it's measured by the quality of the checklist. This trade checks all the boxes that matter.

---

## Final Confirmation
✅ **All hard checks PASS**  
✅ **All soft checks PASS**  
✅ **Position sizing matches conviction (0.5% risk for 7/12 score)**  
✅ **Stop loss is hard-set, not mental**  
✅ **Kill conditions are defined and rational**  
✅ **Portfolio structure supports the trade**

---

## Critical Reminders for Execution
1. **Watch the first 2 bars for volume.** If relative volume is still <0.5x after entry, execute Agent 04's kill condition #1: exit 50% immediately. Don't wait. Thin tape kills trades.
2. **Don't widen the stop.** $129.70 is the line. Period. If the trade touches it, it's done.
3. **Monitor MACD histogram.** If it starts to flatten or invert, tighten the stop to breakeven. Don't let a winner turn into a loser because you were hoping.
4. **Check XLY (Consumer Discretionary ETF) on big red days.** If the sector breaks, reduce exposure. Momentum trades ride the wave; they don't fight the tide.
5. **Half position means optionality.** If volume expands and MACD stays strong, you can add. If tape shows weakness, you've already cut risk in half.

---

## Trade Status
**🟢 APPROVED FOR EXECUTION**

Execute the bracket order exactly as specified. No modifications after GO.

---

**Gatekeeper Sign-Off:** Agent 05  
**Verdict Timestamp:** 2026-06-17 14:24  
**Loop Count:** 0 of 2 (approved on first pass)