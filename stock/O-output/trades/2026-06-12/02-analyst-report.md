# Technical Analysis Report — 2026-06-12

## Ticker: NVDA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $205.46 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.13x |
| ATR(14) | $7.97 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $232.01 | +12.9% |
| Support 1 | $199.34 | -2.98% |
| 200 SMA | $189.04 | -7.98% |
| 50 EMA | $206.71 | +0.61% |
| 10 EMA | $208.93 | +1.69% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=55.58, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=45.6, Price vs 50 SMA=BELOW | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=13.38, 6m Low=5.37, Breakout=NO, Volume=WEAK | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BULLISH, Pullback=YES, Above EMA10=NO | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP** — No strategy triggers. RSI(2) elevated; price below 50 EMA; volume severely depressed at 0.13x. Chart does not support entry.

---

## Ticker: MRVL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $280.36 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.19x |
| ATR(14) | $25.66 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $324.20 | +15.6% |
| Support 1 | $162.85 | -41.9% |
| 200 SMA | $108.46 | -61.3% |
| 50 EMA | $194.43 | -30.6% |
| 10 EMA | $265.08 | -5.46% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=66.15, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=63.19, Price vs 50 SMA=ABOVE, Volume=WEAK | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=80.64, 6m Low=10.06, Breakout=NO, Volume=WEAK | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BULLISH, Pullback zone=NO, Above EMA10=YES | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP** — No strategy triggers. Stock extended above 10 EMA; no pullback zone present; volume weak at 0.19x. RSI elevated but no MACD confirmation. Chart lacks setup conditions.

---

## Ticker: AMAT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $555.92 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.15x |
| ATR(14) | $28.72 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $557.62 | +0.31% |
| Support 1 | $396.88 | -28.6% |
| 200 SMA | $308.54 | -44.5% |
| 50 EMA | $426.65 | -23.4% |
| 10 EMA | $504.08 | -9.32% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=94.36, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=72.67, Price vs 50 SMA=ABOVE, Volume=WEAK | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=35.31, 6m Low=8.80, Breakout=YES, Volume=WEAK | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BULLISH, Pullback zone=NO, Above EMA10=YES | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP** — RSI(2) at extreme overbought (94.36); RSI(14) at 72.67 (overextension); volume critically weak at 0.15x. Bollinger breakout present but volume insufficient. Stock near resistance with no pullback. High risk of mean reversion downside.

---

## Ticker: LRCX

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $364.24 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.15x |
| ATR(14) | $20.28 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $364.81 | +0.16% |
| Support 1 | $263.71 | -27.6% |
| 200 SMA | $204.24 | -43.9% |
| 50 EMA | $285.88 | -21.5% |
| 10 EMA | $335.12 | -7.99% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=90.55, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | CONFIRMED | MACD cross=YES, RSI(14)=68.02 (in range), Price vs 50 SMA=ABOVE | SETUP CONFIRMED |
| Bollinger Squeeze | FAIL | Bandwidth=30.28, 6m Low=11.03, Breakout=NO, Volume=WEAK | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BULLISH, Pullback zone=NO, Above EMA10=YES | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Suggested Parameters (MACD + RSI)
| Parameter | Value |
|-----------|-------|
| Entry | $364.24 |
| Stop Loss | $333.82 |
| Take Profit | $364.81 |
| Risk/Share | $30.42 |
| Reward/Share | $0.57 |
| R:R Ratio | 0.02:1 |

### Decision
**SETUP CONFIRMED [MACD + RSI]** — MACD bullish crossover confirmed. RSI(14) at 68.02 within optimal range (35-75). Price above 50 EMA ($285.88). **CRITICAL CAVEAT: Risk/Reward ratio at 0.02:1 dramatically fails minimum 1.0:1 requirement.** Reward ($0.57/share) is negligible versus risk ($30.42/share). Take Profit at resistance too close relative to stop loss distance. **TRADE NOT RECOMMENDED** despite technical setup due to unacceptable risk/reward structure. Relative volume also weak at 0.15x — volume confirmation lacking.

---

## Ticker: META

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $564.08 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.14x |
| ATR(14) | $18.57 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $643.00 | +13.9% |
| Support 1 | $557.01 | -1.25% |
| 200 SMA | $657.41 | +16.5% |
| 50 EMA | $621.77 | +10.2% |
| 10 EMA | $587.40 | +4.13% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=2.5 (OVERSOLD), Price vs 200 SMA=BELOW | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=33.91 (OUT OF RANGE), Price vs 50 SMA=BELOW | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=13.90, 6m Low=4.12, Breakout=NO, Volume=WEAK | NO SETUP |
| MA Crossover | FAIL | 10 EMA vs 50 EMA=BEARISH, Pullback zone=NO, Below EMA10=YES | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP** — Stock in clear downtrend. Price below 200 SMA ($657.41), 50 EMA ($621.77), and 10 EMA ($587.40). RSI(14) at 33.91 below Connors entry threshold of 35. MACD histogram negative. While RSI(2) is oversold at 2.5, Connors RSI strategy requires price ABOVE 200 SMA — condition fails. Bearish MA alignment. Volume severely weak at 0.14x. No entry signal.

---

## Ticker: GOOGL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $359.74 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.19x |
| ATR(14) | $10.50 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $408.37 | +13.5% |
| Support 1 | $346.36 | -3.72% |
| 200 SMA | $307.56 | -14.5% |
| 50 EMA | $362.06 | +0.65% |
| 10 EMA | $365.23 | +1.53% |

### Strategy