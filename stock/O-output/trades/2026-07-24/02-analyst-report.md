# Technical Analysis Report — 2026-07-24

## Ticker: UNH

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $423.56 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 0.79x |
| ATR(14) | $12.26 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $461.62 | +9.0% |
| Support 1 | $406.65 | -4.0% |
| 200 SMA | $339.51 | -19.8% |
| 50 EMA | $406.08 | -4.1% |
| 10 EMA | $426.14 | +0.6% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=26.9, Price=ABOVE 200 SMA | NO SETUP |
| MACD + RSI | FAIL | MACD=-1.25, RSI(14)=53.5, Volume=0.79x | NO SETUP |
| Bollinger Squeeze | FAIL | BW=4.99 (at min), No breakout, Volume=0.79x | NO SETUP |
| MA Crossover | FAIL | 10 EMA > 50 EMA (bullish), Price BELOW 10 EMA | NO SETUP |
| VIX Fear | N/A | Not applicable for equity ticker | N/A |

### Decision
**NO SETUP** — UNH fails all entry criteria. RSI(2) is elevated (26.9), volume is weak (0.79x), and price has not broken above upper Bollinger Band despite squeeze condition. No actionable setup.

---

## Ticker: JNJ

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $259.27 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 0.93x |
| ATR(14) | $6.08 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $269.43 | +3.9% |
| Support 1 | $240.89 | -7.1% |
| 200 SMA | $222.52 | -14.2% |
| 50 EMA | $240.91 | -7.1% |
| 10 EMA | $254.12 | -2.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=91.1, Price=ABOVE 200 SMA | NO SETUP |
| MACD + RSI | FAIL | MACD=-0.92, RSI(14)=59.5, Volume=0.93x | NO SETUP |
| Bollinger Squeeze | FAIL | BW=8.67, No squeeze, No breakout | NO SETUP |
| MA Crossover | SETUP CONFIRMED | 10 EMA > 50 EMA (bullish), Price > 10 EMA, RSI=59.5 | **SETUP CONFIRMED** |
| VIX Fear | N/A | Not applicable for equity ticker | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $259.27 |
| Stop Loss | $250.15 |
| Target | $269.43 |
| R:R Ratio | 1.11:1 |

### Decision
**SETUP CONFIRMED — MA Crossover** — JNJ triggers MA Crossover setup with bullish 10 EMA > 50 EMA, price above both moving averages, and RSI(14) in healthy zone (59.5). However, **R:R ratio of 1.11:1 falls below minimum threshold of 1.5:1 for this strategy. Trade fails risk/reward validation.** Recommend passing on this setup.

---

## Ticker: WMT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $108.40 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 0.94x |
| ATR(14) | $2.70 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $118.58 | +9.3% |
| Support 1 | $106.79 | -1.5% |
| 200 SMA | $117.37 | +8.2% |
| 50 EMA | $118.08 | +8.9% |
| 10 EMA | $111.57 | +2.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=3.6 (oversold), Price=BELOW 200 SMA | NO SETUP |
| MACD + RSI | FAIL | MACD=-0.14, RSI(14)=34.7 (out of range), Price=BELOW 50 SMA | NO SETUP |
| Bollinger Squeeze | FAIL | BW=7.68, No squeeze, Price at lower band | NO SETUP |
| MA Crossover | FAIL | 10 EMA > 50 EMA (bearish), Price BELOW 10 EMA, RSI=34.7 | NO SETUP |
| VIX Fear | N/A | Not applicable for equity ticker | N/A |

### Decision
**NO SETUP** — WMT is in a downtrend with price below both 50 EMA and 200 SMA. RSI(2) is oversold at 3.6, but trend filter (Connors strategy) fails because price is below 200 SMA. MACD and MA Crossover fail due to bearish positioning. No tradeable setup.

---

## Ticker: JPM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $349.90 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 1.04x |
| ATR(14) | $7.52 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $351.24 | +0.4% |
| Support 1 | $323.55 | -7.5% |
| 200 SMA | $307.78 | -12.0% |
| 50 EMA | $320.38 | -8.4% |
| 10 EMA | $343.02 | -1.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=90.1, Price=ABOVE 200 SMA | NO SETUP |
| MACD + RSI | SETUP CONFIRMED | MACD cross=YES, RSI(14)=66.4, Volume=1.04x | **SETUP CONFIRMED** |
| Bollinger Squeeze | FAIL | BW=8.14, No squeeze, Price at upper band | NO SETUP |
| MA Crossover | SETUP CONFIRMED | 10 EMA > 50 EMA (bullish), Price > 10 EMA, RSI=66.4 | **SETUP CONFIRMED** |
| VIX Fear | N/A | Not applicable for equity ticker | N/A |

### Suggested Parameters (if setup confirmed)
**MACD + RSI Setup:**
| Parameter | Value |
|-----------|-------|
| Entry | $349.90 |
| Stop Loss | $338.62 |
| Target | $351.24 |
| R:R Ratio | 0.12:1 |

**MA Crossover Setup:**
| Parameter | Value |
|-----------|-------|
| Entry | $349.90 |
| Stop Loss | $338.62 |
| Target | $351.24 |
| R:R Ratio | 0.12:1 |

### Decision
**NO SETUP — Both strategies fail risk/reward validation.** JPM triggers both MACD + RSI and MA Crossover setups with strong technical alignment (bullish MACD crossover, RSI in range, price above key moving averages, above-average volume). However, both pre-computed trade parameters show R:R ratios of 0.12:1, which fall far below the minimum 1.0:1 (MACD) and 1.5:1 (MA Crossover) thresholds. The target is only $1.34 away while risk is $11.28 — unfavorable risk/reward geometry. **Pass on this setup.**

---

## Ticker: GS

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $1,074.72 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 0.90x |
| ATR(14) | $36.49 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $1,153.99 | +7.4% |
| Support 1 | $1,003.00 | -6.7% |
| 200 SMA | $902.98 | -16.0% |
| 50 EMA | $1,038.81 | -3.3% |
| 10 EMA | $1,079.40 | +0.4% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=34.4, Price=ABOVE 200 SMA | NO SETUP |
| MACD + RSI | SETUP CONFIRMED | MACD cross=YES, RSI(14)=52.1, Volume=0.90x | **SETUP CONFIRMED** |
| Bollinger Squeeze | FAIL | BW=14.30, No squeeze, Price mid-band | NO SETUP |
| MA Crossover | FAIL | 10 EMA > 50 EMA (bullish), Price BELOW 10 EMA | NO SETUP |
| VIX Fear | N/A | Not applicable for equity ticker | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $1,074.72 |
| Stop Loss | $1,019.99 |
| Target | $1,153.99 |
| R:R Ratio | 1.45:1 |

### Decision
**SETUP CONFIRMED — MACD + RSI** — GS triggers MACD + RSI setup with bullish MACD crossover (histogram +0.29), RSI(14) in healthy zone (52.1), and price above 50 EMA. Volume is slightly weak at 0.90x, but not disqualifying. **R:R ratio of 1.45:1 passes the 1.0:1 minimum threshold.** Risk per share is $54.73, reward is $79.27. Setup is valid. Entry at current price $1,074.72, targeting resistance at $1,153.99.

---

## Ticker: PANW

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $325.63 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 0.80x |
| ATR(14) | $16.50 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 