# Technical Analysis Report — 2026-08-13

## Ticker: NVDA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $224.09 |
| 20-Day Avg Volume | — |
| Relative Volume | 0.87x |
| ATR(14) | $7.51 |
| Support | $190.01 |
| Resistance | $225.10 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $225.10 | +0.45% |
| Support 1 | $190.01 | -15.22% |
| 200 SMA | $194.38 | -13.30% |
| 50 SMA | $206.25 | -7.99% |
| 10 EMA | $215.31 | -3.94% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=82.15, Price above 200 SMA ✓ | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO, RSI(14)=62.43, Volume=0.87x | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=18.32 (min=7.76), Breakout=NO | NO SETUP |
| MA Crossover | FAILED | Crossover=YES, but no pullback zone detected | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP** — RSI(2) at 82.15 indicates overbought condition, eliminating mean reversion opportunity. MACD shows no crossover. Volume confirmation weak at 0.87x. Price already extended above all key moving averages with no pullback zone for MA crossover entry.

---

## Ticker: AVGO

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $416.05 |
| 20-Day Avg Volume | — |
| Relative Volume | 0.87x |
| ATR(14) | $15.81 |
| Support | $357.80 |
| Resistance | $432.73 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $432.73 | +4.00% |
| Support 1 | $357.80 | -13.95% |
| 200 SMA | $367.75 | -11.63% |
| 50 SMA | $393.30 | -5.47% |
| 10 EMA | $411.14 | -1.18% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=25.0, Price above 200 SMA ✓ | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO, RSI(14)=58.34, Volume=0.87x | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=18.88 (min=6.43), Breakout=NO | NO SETUP |
| MA Crossover | CONFIRMED | Crossover=YES, Pullback zone=YES, RSI(14)=58.34 | SETUP ✓ |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Suggested Parameters (Pre-Computed)
| Parameter | Value |
|-----------|-------|
| Entry | $416.05 |
| Stop Loss | $392.34 |
| Take Profit | $432.73 |
| Risk/Share | $23.71 |
| Reward/Share | $16.68 |
| R:R Ratio | 0.7:1 |

### ⚠️ CRITICAL NOTE
**R:R Ratio FAILS minimum requirement (0.7:1 vs required 1.5:1).** Although MA crossover strategy confirms, reward-to-risk ratio is insufficient for portfolio risk management. **RECOMMEND: REJECT THIS SETUP** — do not trade. Wait for a better entry point or tighter stop loss.

### Decision
**NO TRADE** — While MA Crossover setup technically confirms, the R:R ratio of 0.7:1 is well below the 1.5:1 minimum threshold for this strategy. Position risk ($23.71/share) far exceeds potential reward ($16.68/share). This setup violates portfolio risk discipline.

---

## Ticker: CRWD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $221.78 |
| 20-Day Avg Volume | — |
| Relative Volume | 0.89x |
| ATR(14) | $9.32 |
| Support | $174.14 |
| Resistance | $226.90 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $226.90 | +2.31% |
| Support 1 | $174.14 | -21.44% |
| 200 SMA | $136.25 | -38.54% |
| 50 SMA | $188.37 | -15.08% |
| 10 EMA | $211.10 | -4.84% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=66.23, Price above 200 SMA ✓ | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO, RSI(14)=68.04, Volume=0.89x | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=29.49 (min=15.44), Breakout=NO | NO SETUP |
| MA Crossover | FAILED | No crossover detected within lookback period | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP** — RSI(2) at 66.23 eliminates mean reversion. No MACD crossover. MA crossover not detected. Price extended above 10 EMA with limited upside to resistance ($226.90, only +2.31% away). Volume weak at 0.89x. Insufficient technical confirmation for any strategy.

---

## Ticker: AMGN

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $416.18 |
| 20-Day Avg Volume | — |
| Relative Volume | 0.76x |
| ATR(14) | $11.46 |
| Support | $357.74 |
| Resistance | $421.79 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $421.79 | +1.35% |
| Support 1 | $357.74 | -14.04% |
| 200 SMA | $345.27 | -17.08% |
| 50 SMA | $366.89 | -11.83% |
| 10 EMA | $403.55 | -3.03% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=74.41, Price above 200 SMA ✓ | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO, RSI(14)=72.22, Volume=0.76x | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=18.57 (min=3.98), Breakout=NO | NO SETUP |
| MA Crossover | FAILED | No crossover detected within lookback period | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP** — RSI(2) at 74.41 indicates extreme overbought condition. RSI(14) at 72.22 also elevated. No MACD crossover. Volume weak at 0.76x (lowest in group). Minimal upside to resistance ($421.79, only +1.35% away). Downside risk exceeds upside potential. No actionable setup.

---

## Ticker: GOOGL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $343.54 |
| 20-Day Avg Volume | — |
| Relative Volume | 0.76x |
| ATR(14) | $11.93 |
| Support | $314.90 |
| Resistance | $384.48 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $384.48 | +11.90% |
| Support 1 | $314.90 | -8.37% |
| 200 SMA | $330.28 | -3.85% |
| 50 SMA | $354.45 | +3.17% |
| 10 EMA | $351.32 | +2.27% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=11.68 (borderline), Price below 50 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO, Price below 50 SMA ✗ | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=17.96 (min=5.06), Breakout=NO | NO SETUP |
| MA Crossover | FAILED | Bearish crossover detected (10 EMA < 50 EMA), RSI=45.74 | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stock | N/A |

### Decision
**NO SETUP** — Price below 50 EMA eliminates most bullish strategies. Bearish MA crossover underway (10 EMA approaching bearish cross below 50 EMA). RSI(2) at 11.68 near oversold but trend filter (50 SMA) fails. Volume weak at 0.76x. Directional bias is bearish; no bullish entry warranted.

---

## Ticker: JPM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $365.18 |
| 20-Day Avg Volume | — |
| Relative Volume | 0.61x |
| ATR(14) | $6.60 |
| Support | $335.05 |
| Resistance | $366.09 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $366.09 | +0.25% |
| Support 1 | $335.05 | -8.24% |
| 200 SMA | $311.86 | -14.60% |
| 50 SMA | $336.25 | -7.93% |
| 10 EMA | $357.98 | -1.97% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=96.32, Price above 200 SMA ✓ | NO SETUP |
| MACD + RSI | CONFIRMED | MACD cross=YES, RSI(14)=68.92, Price above 50 SMA ✓ |