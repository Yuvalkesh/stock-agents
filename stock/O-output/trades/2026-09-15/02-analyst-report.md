# Technical Analysis Report — 2026-09-15

## Ticker: CRM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $258.95 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.16x |
| ATR(14) | $9.93 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $268.27 | +3.60% |
| Support 1 | $193.23 | -25.37% |
| 200 SMA | $200.75 | -22.45% |
| 50 SMA | $202.34 | -21.81% |
| 10 EMA | $250.02 | -3.43% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=84.17, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=69.33, Volume=0.16x | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=40.57 (6m low=7.48), Breakout=NO, Volume=0.16x | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BULLISH, No pullback zone triggered | NO SETUP |
| VIX Fear | N/A | Not applicable for equity-specific analysis | N/A |

### Decision
**NO SETUP**

**Rationale:** CRM fails all strategy entry conditions. RSI(2) at 84.17 disqualifies Connors RSI (requires < 10). MACD shows no crossover signal. Bollinger Bandwidth (40.57) is far above 6-month low (7.48), eliminating squeeze setup. MA crossover is present but price has not pulled back into the 10 EMA zone. Critical issue: **Relative volume at 0.16x is severely weak** — far below minimum thresholds for any setup (1.0x+ required). No entry warranted.

---

## Ticker: CRWD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $238.38 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.5x |
| ATR(14) | $12.39 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $239.37 | +0.42% |
| Support 1 | $181.24 | -23.95% |
| 200 SMA | $145.22 | -39.10% |
| 50 SMA | $204.19 | -14.34% |
| 10 EMA | $218.60 | -8.30% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=95.25 (>= 10), Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | CONDITIONAL | MACD cross=YES, RSI(14)=63.28, Volume=0.5x | SETUP TRIGGERED (R:R RATIO FAILS) |
| Bollinger Squeeze | FAIL | Bandwidth=28.95 (6m low=15.44), Breakout=NO, Volume=0.5x | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BULLISH, No pullback zone triggered | NO SETUP |
| VIX Fear | N/A | Not applicable for equity-specific analysis | N/A |

### Suggested Parameters (MACD+RSI Technical Trigger)
| Parameter | Value |
|-----------|-------|
| Entry | $238.38 |
| Stop Loss | $219.79 |
| Target | $239.37 |
| Risk/Share | $18.59 |
| Reward/Share | $0.99 |
| R:R Ratio | 0.05:1 |

### Decision
**NO SETUP — MACD Signal Rejected on Risk/Reward**

**Rationale:** MACD + RSI strategy shows a technical trigger: MACD histogram positive (1.99), MACD line above signal line, RSI(14) in optimal range (63.28), and price above 50 SMA. However, **the R:R ratio (0.05:1) catastrophically fails the strategy minimum of 1.0:1**. Risk per share ($18.59) is 18.8x the reward per share ($0.99). Resistance is only $0.99 away; stop loss is $18.59 away. This setup is mathematically unviable — the risk-to-reward asymmetry makes it a failed trade before entry. Additionally, relative volume at 0.5x is weak (minimum 1.0x preferred). Entry REJECTED.

---

## Ticker: FTNT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $169.89 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.24x |
| ATR(14) | $6.88 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $173.89 | +2.35% |
| Support 1 | $148.25 | -12.72% |
| 200 SMA | $112.52 | -33.77% |
| 50 SMA | $159.41 | -6.15% |
| 10 EMA | $162.10 | -4.61% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=87.44 (>= 10), Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | CONDITIONAL | MACD cross=YES, RSI(14)=59.57, Volume=0.24x | SETUP TRIGGERED (R:R RATIO FAILS) |
| Bollinger Squeeze | FAIL | Bandwidth=16.79 (6m low=9.03), Breakout=NO, Volume=0.24x | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BULLISH, No pullback zone triggered | NO SETUP |
| VIX Fear | N/A | Not applicable for equity-specific analysis | N/A |

### Suggested Parameters (MACD+RSI Technical Trigger)
| Parameter | Value |
|-----------|-------|
| Entry | $169.89 |
| Stop Loss | $159.57 |
| Target | $173.89 |
| Risk/Share | $10.32 |
| Reward/Share | $4.00 |
| R:R Ratio | 0.39:1 |

### Decision
**NO SETUP — MACD Signal Rejected on Risk/Reward**

**Rationale:** MACD + RSI strategy shows a technical trigger: MACD histogram positive (0.83), MACD line above signal line, RSI(14) in optimal range (59.57), and price above 50 SMA. However, **the R:R ratio (0.39:1) fails the strategy minimum of 1.0:1**. Risk per share ($10.32) is 2.58x the reward per share ($4.00). Target (resistance at $173.89) is only $4.00 away; stop loss is $10.32 away. The asymmetrical risk structure violates core strategy risk management rules. Additionally, relative volume at 0.24x is weak (minimum 1.0x preferred). Entry REJECTED.

---

## Summary

**Total Tickers Analyzed:** 3  
**Confirmed Setups:** 0  
**No Setup:** 3  

**Reason for Zero Setups:**
1. **CRM:** Fails all five strategies due to extreme overbought conditions (RSI(2)=84.17) and critically weak volume (0.16x).
2. **CRWD:** MACD crossover signal present, but R:R ratio (0.05:1) is unacceptable — reward is trivial relative to risk. Weak volume (0.5x).
3. **FTNT:** MACD crossover signal present, but R:R ratio (0.39:1) fails minimum threshold (1.0:1). Weak volume (0.24x).

**Key Observation:** All three tickers suffer from **critically weak relative volume** (0.16x – 0.5x), which undermines signal reliability across all strategies. CRWD and FTNT show MACD technical triggers but are rejected purely on risk/reward mathematics — these are setup *failures*, not false signals. The risk-reward asymmetry on both is severe enough that continuation into entry is not justified.

**Recommendation:** Monitor for improved volume profile and better R:R setups on next analysis cycle.