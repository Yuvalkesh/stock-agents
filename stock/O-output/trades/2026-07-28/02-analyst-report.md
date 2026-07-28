# Technical Analysis Report — 2026-07-28

## Ticker: SNOW

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $272.92 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.13x |
| ATR(14) | $12.74 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $279.49 | +2.36% |
| Support 1 | $246.01 | -9.86% |
| 200 SMA | $209.74 | -23.13% |
| 50 EMA | $237.51 | -13.00% |
| 10 EMA | $268.61 | -1.57% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=82.6, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAILED | MACD histogram=-1.88, RSI(14)=63.5, Price vs 50 SMA=ABOVE | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=9.45 (at 6m low), Breakout=NO, Volume=1.13x | NO SETUP |
| MA Crossover | TRIGGERED | 10 EMA=268.61, 50 EMA=238.93, Price=272.92, RSI(14)=63.5 | SETUP TRIGGERED |
| VIX Fear | N/A | Not applicable (ticker-specific analysis) | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $272.92 |
| Stop Loss | $253.81 |
| Take Profit | $279.49 |
| Risk/Share | $19.11 |
| Reward/Share | $6.57 |
| R:R Ratio | 0.34:1 |

### Decision
**NO SETUP** — MA Crossover setup triggered but **R:R Ratio of 0.34:1 FAILS minimum requirement of 1.5:1**. Risk-to-reward is severely unfavorable. This setup does not meet entry standards for execution.

---

## Ticker: NET

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $265.61 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.87x |
| ATR(14) | $12.89 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $291.00 | +9.57% |
| Support 1 | $235.00 | -11.51% |
| 200 SMA | $212.19 | -20.11% |
| 50 EMA | $243.34 | -8.36% |
| 10 EMA | $266.91 | +0.49% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=60.0, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAILED | MACD histogram=-1.96, RSI(14)=55.6, Relative Volume=0.87x (WEAK) | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=18.32 (not at 6m low), Breakout=NO, Volume=0.87x | NO SETUP |
| MA Crossover | FAILED | 10 EMA=266.91, Price=265.61 (BELOW 10 EMA), Pullback zone detected but price not above 10 EMA | NO SETUP |
| VIX Fear | N/A | Not applicable (ticker-specific analysis) | N/A |

### Decision
**NO SETUP** — No strategy meets entry criteria. Price below 10 EMA disqualifies MA Crossover. MACD shows no crossover and relative volume is weak at 0.87x. Connors RSI(2) and Bollinger Squeeze do not trigger.

---

## Ticker: COP

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $115.58 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.14x |
| ATR(14) | $2.97 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $122.38 | +5.91% |
| Support 1 | $102.69 | -11.12% |
| 200 SMA | $106.18 | -8.10% |
| 50 EMA | $114.00 | -1.37% |
| 10 EMA | $115.95 | +0.32% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=13.5, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAILED | MACD histogram=+1.15, RSI(14)=54.3, Price vs 50 SMA=ABOVE (but no crossover) | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=19.75 (not at 6m low), Breakout=NO, Volume=1.14x (weak) | NO SETUP |
| MA Crossover | FAILED | 10 EMA=115.95, 50 EMA=113.92 (crossover recent but price below 10 EMA at 115.58), RSI(14)=54.3 | NO SETUP |
| VIX Fear | N/A | Not applicable (ticker-specific analysis) | N/A |

### Decision
**NO SETUP** — MA Crossover triggered recently (10 EMA > 50 EMA), but price is currently **below the 10 EMA** at $115.58 vs $115.95. The pullback has not yet bounced back above 10 EMA. No other strategies qualify.

---

## Ticker: GOOGL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $326.56 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.97x |
| ATR(14) | $11.76 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $375.27 | +14.93% |
| Support 1 | $314.90 | -3.56% |
| 200 SMA | $324.00 | -0.78% |
| 50 EMA | $363.11 | +11.20% |
| 10 EMA | $338.56 | +3.68% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=52.5, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAILED | MACD histogram=-3.64 (bearish), RSI(14)=37.2, Price vs 50 SMA=BELOW | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=16.52 (not at 6m low), Breakout=NO, Volume=0.97x (weak) | NO SETUP |
| MA Crossover | FAILED | 10 EMA=338.56, 50 EMA=353.40 (10 EMA < 50 EMA, BEARISH crossover), Price=326.56 (below both MAs) | NO SETUP |
| VIX Fear | N/A | Not applicable (ticker-specific analysis) | N/A |

### Decision
**NO SETUP** — 10 EMA has crossed **below** 50 EMA, signaling a bearish crossover. Price is below both the 10 EMA and 50 EMA, and the MACD histogram is deeply negative. This is a downtrend environment. No bullish setup exists.

---

## Ticker: JPM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $356.20 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.80x |
| ATR(14) | $7.33 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $359.05 | +0.80% |
| Support 1 | $323.55 | -9.17% |
| 200 SMA | $308.28 | -13.44% |
| 50 EMA | $322.52 | -9.45% |
| 10 EMA | $346.93 | -2.59% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=97.77 (extremely overbought), Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAILED | MACD histogram=+0.75 (weak positive), RSI(14)=70.45 (elevated), Price vs 50 SMA=ABOVE, Relative Volume=0.80x (WEAK) | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=9.51 (not at 6m low), Breakout=YES but Volume=0.80x (WEAK), RSI(14)=70.45 (overbought) | NO SETUP |
| MA Crossover | FAILED | 10 EMA=346.93, 50 EMA=328.07 (bullish but no recent crossover), Price above 10 EMA, but pullback zone NOT triggered (no recent pullback) | NO SETUP |
| VIX Fear | N/A | Not applicable (ticker-specific analysis) | N/A |

### Decision
**NO SETUP** — All strategies fail. Connors RSI(2) shows extreme overbought condition at 97.77 (opposite of reversal signal). MACD momentum is weak. Bollinger Squeeze shows breakout but volume confirmation is absent at 0.80x. MA Crossover has no recent crossover to reference. Relative volume across all setups is subthreshold (0.80x).

---

## Summary: 2026-07-28

| Ticker | Status | Reasoning |
|--------|--------|-----------|
| SNOW | NO SETUP | MA Crossover triggered but R:R 0.34:1 fails 1.5:1 minimum |
| NET | NO SETUP | No strategy triggers; price below 10 EMA; weak volume |
| COP | NO SETUP | MA Crossover pullback incomplete; price still below 10 EMA |
| GOOGL | NO SETUP | Bearish MA crossover (10 < 50); price below both MAs; negative MACD |
| JPM | NO SETUP | Extreme overbought RSI(2)=97.77; weak volume across all setups |

**ZERO CONFIRMED SETUPS FOR EXECUTION** — No trades meet the system's entry standards today