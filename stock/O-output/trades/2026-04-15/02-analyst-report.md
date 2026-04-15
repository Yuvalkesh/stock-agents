# Technical Analysis Report — 2026-04-15

## Ticker: AI

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $8.40 |
| 20-Day Avg Volume | {data not provided} |
| Today's Volume | {data not provided} |
| Relative Volume | 1.03x |
| ATR(14) | $0.48 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $9.31 | +10.8% |
| Support 1 | $7.68 | -8.6% |
| 200 SMA | $15.69 | +86.8% |
| 50 SMA | $9.35 | +11.3% |
| 10 EMA | $8.49 | +1.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=37.51 | Price below 200 SMA | NO SETUP |
| MACD + RSI | MACD=-0.26, RSI(14)=43.16 | No crossover, price below 50 SMA | NO SETUP |
| Bollinger Squeeze | BW=13.52, min=7.95 | Squeeze=NO, RSI(14)=43.16 | NO SETUP |
| MA Crossover | EMA10=8.49, EMA50=9.59 | Bearish crossover (EMA10 < EMA50), price below EMA10 | NO SETUP |
| VIX Fear | N/A | Not applicable for individual stock | N/A |

### Decision
**NO SETUP**

All five strategies fail to trigger. AI is below both its 50 EMA and 200 SMA, indicating a downtrend. The 10 EMA is above price but the 50 EMA is above the 10 EMA—bearish configuration. RSI(2) at 37.51 does not meet the < 10 threshold. No volume confirmation. This ticker is not tradeable on 2026-04-15.

---

## Ticker: PPI

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $21.94 |
| 20-Day Avg Volume | {data not provided} |
| Today's Volume | {data not provided} |
| Relative Volume | 1.17x |
| ATR(14) | $0.31 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $21.97 | +0.1% |
| Support 1 | $20.09 | -8.4% |
| 200 SMA | $18.77 | -14.4% |
| 50 SMA | $20.98 | -4.5% |
| 10 EMA | $21.45 | -2.2% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=99.58 | RSI(2) >= 10, price above 200 SMA | NO SETUP |
| MACD + RSI | MACD=0.25, RSI(14)=67.60 | No crossover, price above 50 SMA, volume confirms | NO SETUP |
| Bollinger Squeeze | BW=9.54, min=3.84 | Squeeze=NO (BW not at 6m low), RSI(14)=67.60 | NO SETUP |
| MA Crossover | EMA10=21.45, EMA50=20.83 | **Bullish (EMA10 > EMA50), price above EMA10, RSI(14)=67.60** | **SETUP CONFIRMED** |
| VIX Fear | N/A | Not applicable for individual stock | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $21.94 |
| Stop Loss | $21.48 |
| Take Profit | $21.97 |
| R:R Ratio | 0.07:1 |

### Decision
**SETUP CONFIRMED — MA Crossover (with R:R caveat)**

**CRITICAL ALERT:** While MA Crossover criteria are technically met (EMA10 > EMA50, price above EMA10, RSI in neutral range, relative volume 1.17x), the risk/reward ratio fails the strategy minimum. R:R Ratio is 0.07:1; the strategy requires minimum 1.5:1. Stop loss ($21.48) is only $0.46 below entry, while take profit ($21.97) is only $0.03 above entry. This is an asymmetric, low-conviction setup. **This trade violates strategy risk management rules and should NOT be executed.** The resistance at $21.97 is too tight to the entry price.

---

## Ticker: JNJ

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $240.10 |
| 20-Day Avg Volume | {data not provided} |
| Today's Volume | {data not provided} |
| Relative Volume | 1.35x |
| ATR(14) | $4.54 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $247.21 | +2.9% |
| Support 1 | $232.24 | -3.3% |
| 200 SMA | $199.82 | -16.8% |
| 50 SMA | $240.75 | +0.3% |
| 10 EMA | $240.08 | -0.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=68.22 | RSI(2) >= 10, price above 200 SMA | NO SETUP |
| MACD + RSI | MACD=0.19, RSI(14)=50.48 | No crossover (MACD histogram negative), price below 50 SMA | NO SETUP |
| Bollinger Squeeze | BW=4.48, min=3.91 | Squeeze=NO (BW close but not at 6m low), volume 1.35x confirms | NO SETUP |
| MA Crossover | EMA10=240.08, EMA50=236.38 | **Bullish (EMA10 > EMA50), price above EMA10, RSI(14)=50.48** | **SETUP CONFIRMED** |
| VIX Fear | N/A | Not applicable for individual stock | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $240.10 |
| Stop Loss | $233.29 |
| Take Profit | $247.21 |
| R:R Ratio | 1.04:1 |

### Decision
**SETUP CONFIRMED — MA Crossover (with R:R caveat)**

**CRITICAL ALERT:** MA Crossover criteria are met (EMA10 > EMA50, price above EMA10, RSI neutral at 50.48, relative volume 1.35x strong). However, the risk/reward ratio is 1.04:1, which falls **below** the strategy minimum of 1.5:1. Risk per share is $6.81 (difference between entry and stop loss); reward per share is $7.11 (to resistance). While this is closer to acceptable than PPI, it still violates risk management. **This trade should NOT be executed.** The reward-to-risk asymmetry is insufficient for the MA Crossover strategy's historical win rate (~60%).

---

## Ticker: TSLA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $364.20 |
| 20-Day Avg Volume | {data not provided} |
| Today's Volume | {data not provided} |
| Relative Volume | 0.92x |
| ATR(14) | $14.33 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $403.07 | +10.7% |
| Support 1 | $337.24 | -7.4% |
| 200 SMA | $397.67 | +9.2% |
| 50 SMA | $391.70 | +7.6% |
| 10 EMA | $357.48 | -1.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=95.44 | RSI(2) >= 10, price below 200 SMA | NO SETUP |
| MACD + RSI | MACD=-12.45, RSI(14)=45.88 | Crossover=YES, but price below 50 SMA, volume weak (0.92x) | NO SETUP |
| Bollinger Squeeze | BW=17.77, min=7.04 | Squeeze=NO, breakout=NO, volume weak | NO SETUP |
| MA Crossover | EMA10=357.48, EMA50=387.54 | Bearish (EMA10 < EMA50), price above EMA10 but below EMA50 | NO SETUP |
| VIX Fear | N/A | Not applicable for individual stock | N/A |

### Decision
**NO SETUP**

TSLA is in a downtrend. Price is below both the 50 EMA ($391.70) and 200 SMA ($397.67). The 10 EMA ($357.48) is below the 50 EMA—bearish crossover configuration. While MACD histogram shows a crossover signal forming, it's undermined by weak volume (0.92x) and price being below the 50 EMA trend filter. RSI(2) at 95.44 (not < 10) rules out mean reversion. No tradeable setup on this date.

---

## Ticker: TXN

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $218.87 |
| 20-Day Avg Volume | {data not provided} |
| Today's Volume | {data not provided} |
| Relative Volume | 0.92x |
| ATR(14) | $5.79 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $219.49 | +0.3% |
| Support 1 | $184.90 | -15.5% |
| 200 SMA | $188.71 | -13.8% |
| 50 SMA | $206.71 | -5.5% |
| 10 EMA | $208.22 | -4.8% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=98.29 | RSI(2) >= 10, price above 200 SMA | NO SETUP |
| MACD + RSI | MACD=3.98, RSI(14)=69.46 | No crossover (histogram positive but signal below MACD), price above 50 SMA, volume weak | NO SETUP |
| Bollinger Squeeze | BW=20.61, min=5.41 | Squeeze=NO (BW expanded), breakout=NO, volume weak | NO SETUP |
| MA Crossover | EMA10=208.22, EMA50=200.84 | Crossover=YES, EMA10 > EMA50, price above EMA10, RSI(14)=69.46 | NO SETUP |
| VIX Fear | N/A | Not applicable for individual stock | N/A |

### Decision
**NO SETUP**

While TXN shows a bullish 10/50 EMA crossover (EMA10 at $208.22 > EMA50 at $200.84) and price above the 10 EMA, the MA Crossover strategy requires a **pullback to the 10 EMA within 1.0% before entry**. Current price ($218.87) is $10.65 above the 10 EMA—well outside the pullback zone. This is not a pullback entry setup; it's an extended move. Relative volume is weak (0.92x). The resistance is at $219.49, only $0.62 above current price. No proper setup for entry on 2026-04-15.

---

## Ticker: LRCX

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $272.41 |
| 20-Day Avg Volume | {data not provided} |
| Today's Volume | {data not provided} |
| Relative Volume | 0.83x |
| ATR(14) | $11.85 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $273.50 | +0.4% |
| Support 1 | $198.60 | -27.1% |
| 200 SMA | $163.46 | -40.0% |
| 50 SMA | $229.24 | -15.8% |
| 10 EMA | $247.89 | -9.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=99.60 | RSI(2) >= 10, price above 200 SMA | NO SETUP |
| MACD + RSI | MACD=10.20, RSI(14)=69.61 | No crossover, price above 50 SMA, volume weak (0.83x) | NO SETUP |
| Bollinger Squeeze | BW=33.61, min=15.05 | Squeeze=NO (BW expanded), **Breakout=YES**, volume weak (0.83x), RSI(14)=69.61 | NO SETUP |
| MA Crossover | EMA10=247.89, EMA50=226.24 | Bullish (EMA10 > EMA50), price above EMA10, RSI(14)=69.61 | NO SETUP |
| VIX Fear | N/A | Not applicable for individual stock | N/A |

### Decision
**NO SETUP**

Although Bollinger Squeeze shows a breakout (price at $272.41 above upper band at $271.56), the setup fails on volume. Volume is weak (0.83x) — the strategy requires > 1.5x average volume to confirm the breakout. RSI(14) at 69.61 is high but not overbought (< 70). MA Crossover criteria are partially met but price is $24.52 above the 10 EMA—well outside the pullback zone. The resistance at $273.50 is only $1.09 away, making any setup asymmetric. Weak volume across all signals disqualifies any trade. **NO SETUP.**

---

## Ticker: MSFT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $393.11 |
| 20-Day Avg Volume | {data not provided} |
| Today's Volume | {data not provided} |
| Relative Volume | 1.14x |
| ATR(14) | $8.94 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $404.40 | +2.9% |
| Support 1 | $356.28 | -9.4% |
| 200 SMA | $471.56 | +19.9% |
| 50 SMA | $391.94 | -0.3% |
| 10 EMA | $378.12 | -3.8% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|