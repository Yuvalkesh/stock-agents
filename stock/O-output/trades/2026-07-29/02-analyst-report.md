# Technical Analysis Report — 2026-07-29

## Ticker: NVDA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $197.01 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.02x |
| ATR(14) | $7.56 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $214.39 | +8.8% |
| Support 1 | $191.14 | -2.9% |
| 200 SMA | $192.82 | -2.1% |
| 50 EMA | $207.76 | +5.5% |
| 10 EMA | $203.59 | +3.3% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=13.35 (threshold: <10), Price above 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD=-0.65, Signal=-0.07 (no cross), RSI(14)=42.97 (in range), Price below 50 SMA | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=11.35 (6m low=5.37, no squeeze), Price below upper band, Volume=1.02x (weak) | NO SETUP |
| MA Crossover | FAILED | 10 EMA=203.59 vs 50 EMA=204.41 (bearish cross), Price=197.01 (below 10 EMA) | NO SETUP |
| VIX Fear | N/A | VIX data not provided | N/A |

### Decision
**NO SETUP**

Price is caught between a broken 10/50 EMA crossover (bearish orientation) and support at $191.14. RSI(2) elevated at 13.35 blocks Connors entry. MACD histogram negative. No strategy triggers on this data.

---

## Ticker: GOOGL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $333.71 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.01x |
| ATR(14) | $11.73 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $375.27 | +12.4% |
| Support 1 | $314.9 | -5.6% |
| 200 SMA | $324.45 | -2.8% |
| 50 EMA | $361.77 | +8.4% |
| 10 EMA | $337.68 | +1.2% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=75.42 (threshold: <10), Price above 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD=-8.73, Signal=-5.89 (no cross, both negative), RSI(14)=41.72 (in range), Price below 50 SMA | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=17.14 (6m low=5.06, no squeeze), Price below upper band, Volume=1.01x (weak) | NO SETUP |
| MA Crossover | FAILED | 10 EMA=337.68 vs 50 EMA=352.62 (bearish cross), Price=333.71 (below both MAs) | NO SETUP |
| VIX Fear | N/A | VIX data not provided | N/A |

### Decision
**NO SETUP**

Stock pulled back sharply below both 10 EMA and 50 EMA, confirming bearish crossover. RSI(2) is extremely overbought at 75.42, negating mean reversion setup. MACD deeply negative with histogram=-2.84. No entry conditions met.

---

## Ticker: V

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $366.59 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.4x |
| ATR(14) | $7.55 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $371.16 | +1.2% |
| Support 1 | $339.08 | -7.5% |
| 200 SMA | $329.1 | -10.2% |
| 50 EMA | $338.19 | -7.8% |
| 10 EMA | $358.1 | -2.3% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=93.64 (threshold: <10), Price above 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD=6.72, Signal=6.92 (no cross), RSI(14)=65.16 (in range), MACD histogram=-0.20 (bearish divergence) | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=6.74 (6m low=3.23, no squeeze at this level), Price at upper band, Volume=1.4x (adequate), RSI(14)=65.16 | NO SETUP |
| MA Crossover | **SETUP TRIGGERED** | 10 EMA=358.10 vs 50 EMA=341.72 (bullish), Price=366.59 (above both), Within pullback zone, RSI(14)=65.16 (valid) | TRIGGERS ENTRY |
| VIX Fear | N/A | VIX data not provided | N/A |

### Suggested Parameters
| Parameter | Value |
|-----------|-------|
| Entry | $366.59 |
| Stop Loss | $355.26 |
| Take Profit | $371.16 |
| Risk/Share | $11.33 |
| Reward/Share | $4.57 |
| R:R Ratio | 0.4:1 |

### Decision
**SETUP TRIGGERED — MA Crossover (10 EMA / 50 EMA)**

**⚠️ RISK WARNING**: R:R ratio of 0.4:1 falls significantly short of the MA Crossover minimum requirement of 1.5:1. While the technical setup is valid (10 EMA bullish cross, price above both moving averages, RSI in momentum zone, elevated relative volume at 1.4x), the risk-reward structure is **UNFAVORABLE**. Stop loss ($355.26) is $11.33 away while target ($371.16) is only $4.57 away. This violates position-sizing discipline.

**RECOMMENDATION**: Do not execute. Wait for better price geometry or a closer stop loss level.

---

## Ticker: SNOW

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $270.36 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.16x |
| ATR(14) | $13.51 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $279.49 | +3.4% |
| Support 1 | $246.01 | -9.0% |
| 200 SMA | $209.84 | -22.4% |
| 50 EMA | $240.16 | -11.1% |
| 10 EMA | $268.93 | -0.5% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=50.1 (threshold: <10), Price above 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD=9.31, Signal=11.23 (no cross, signal above), RSI(14)=60.87 (in range), MACD histogram=-1.92 (bearish divergence) | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=8.14 (6m low=8.14, at squeeze threshold but no breakout), Price within bands, Volume=1.16x (weak for breakout) | NO SETUP |
| MA Crossover | **SETUP TRIGGERED** | 10 EMA=268.93 vs 50 EMA=240.16 (bullish), Price=270.36 (above both), Within pullback zone, RSI(14)=60.87 (valid) | TRIGGERS ENTRY |
| VIX Fear | N/A | VIX data not provided | N/A |

### Suggested Parameters
| Parameter | Value |
|-----------|-------|
| Entry | $270.36 |
| Stop Loss | $250.1 |
| Take Profit | $279.49 |
| Risk/Share | $20.26 |
| Reward/Share | $9.13 |
| R:R Ratio | 0.45:1 |

### Decision
**SETUP TRIGGERED — MA Crossover (10 EMA / 50 EMA)**

**⚠️ RISK WARNING**: R:R ratio of 0.45:1 falls significantly short of the MA Crossover minimum requirement of 1.5:1. While the technical setup is valid (10 EMA bullish cross, price above both moving averages, RSI in momentum zone, relative volume at 1.16x), the risk-reward structure is **UNFAVORABLE**. Stop loss ($250.1) is $20.26 away while target ($279.49) is only $9.13 away. This violates position-sizing discipline.

**RECOMMENDATION**: Do not execute. Wait for better price geometry or a closer stop loss level.

---

## Summary

| Ticker | Setup Status | Strategy | R:R Verdict |
|--------|--------------|----------|------------|
| NVDA | NO SETUP | — | — |
| GOOGL | NO SETUP | — | — |
| V | TRIGGERED | MA Crossover | **REJECT** (0.4:1 < 1.5:1 min) |
| SNOW | TRIGGERED | MA Crossover | **REJECT** (0.45:1 < 1.5:1 min) |

**Market Condition**: Mixed/Bearish bias. Two tickers (NVDA, GOOGL) show bearish EMA crosses with weak MACD and elevated pullback risk. Two tickers (V, SNOW) show technically valid MA crossover setups but with unfavorable risk-reward ratios that fail strategy minimum thresholds.

**Action**: **NO TRADES RECOMMENDED** for 2026-07-29. Both triggered setups (V, SNOW) fail the 1.5:1 minimum R:R requirement for MA Crossover strategy. Execution would violate position-sizing discipline.