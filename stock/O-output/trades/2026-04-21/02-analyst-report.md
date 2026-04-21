# Technical Analysis Report — 2026-04-21

## Ticker: TXN

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $233.70 |
| 20-Day Avg Volume | Baseline |
| Today's Relative Volume | 1.08x |
| ATR(14) | $5.98 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $233.97 | +0.1% |
| Support 1 | $184.95 | -20.9% |
| 200 SMA | $189.12 | -19.1% |
| 50 EMA | $206.83 | -11.5% |
| 10 EMA | $218.68 | -6.4% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | OVERBOUGHT | RSI(2)=96.6, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | OVERBOUGHT | MACD cross=NO, RSI(14)=76.2 (>75) | NO SETUP |
| Bollinger Squeeze | NO SQUEEZE | BW=27.24 (vs 6m low=5.41), Breakout=YES, Volume=1.08x (weak) | NO SETUP |
| MA Crossover | EMA BULLISH | 10 EMA vs 50 EMA=BULLISH, but price not in pullback zone, RSI(14)=76.2 | NO SETUP |
| VIX Fear | N/A | Not applicable to single-stock analysis | N/A |

### Decision
**NO SETUP** — All strategies fail confirmation criteria. RSI(14) is overbought (76.2), RSI(2) is extreme (96.6), and price has extended significantly from moving averages without pullback zone. No entry warranted.

---

## Ticker: LRCX

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $263.16 |
| 20-Day Avg Volume | Baseline |
| Today's Relative Volume | 0.66x |
| ATR(14) | $11.10 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $273.50 | +3.9% |
| Support 1 | $198.60 | -24.5% |
| 200 SMA | $166.80 | -36.6% |
| 50 EMA | $232.59 | -11.6% |
| 10 EMA | $256.91 | -2.4% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NEUTRAL | RSI(2)=38.6, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | BULLISH BIAS | MACD cross=NO, RSI(14)=61.7 (in range), Volume=0.66x (WEAK) | NO SETUP |
| Bollinger Squeeze | NO SQUEEZE | BW=38.31 (vs 6m low=15.05), Breakout=NO, Volume=0.66x (weak) | NO SETUP |
| MA Crossover | PULLBACK ZONE | 10 EMA=$256.91, Price=$263.16 (within 1.0%), EMA10 vs EMA50=BULLISH, RSI(14)=61.7 | SETUP DETECTED |
| VIX Fear | N/A | Not applicable to single-stock analysis | N/A |

### Suggested Parameters (Pre-Computed)
| Parameter | Value |
|-----------|-------|
| Entry | $263.16 |
| Stop Loss | $246.51 |
| Take Profit | $273.50 |
| Risk/Share | $16.65 |
| Reward/Share | $10.34 |
| R:R Ratio | 0.62:1 |

### Decision
**SETUP DETECTED — MA CROSSOVER (CONDITIONAL REJECTION)** — Price is in pullback zone touching 10 EMA ($256.91), EMA10 vs EMA50 bullish, RSI(14)=61.7 (not overbought). However, **R:R ratio of 0.62:1 falls below minimum requirement of 1.5:1**. Risk ($16.65/share) significantly exceeds reward ($10.34/share). **TRADE REJECTED on risk/reward basis.** Pass to Agent 03 with notation: Setup geometrically valid but position sizing insufficient for swing trade profitability.

---

## Ticker: KLAC

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $1805.32 |
| 20-Day Avg Volume | Baseline |
| Today's Relative Volume | 0.74x |
| ATR(14) | $64.59 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $1806.75 | +0.1% |
| Support 1 | $1374.43 | -23.9% |
| 200 SMA | $1218.28 | -32.5% |
| 50 EMA | $1525.89 | -15.5% |
| 10 EMA | $1724.24 | -4.5% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | OVERBOUGHT | RSI(2)=83.2, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | BULLISH BIAS | MACD cross=NO, RSI(14)=69.7 (in range), Volume=0.74x (weak) | NO SETUP |
| Bollinger Squeeze | NO SQUEEZE | BW=33.45 (vs 6m low=8.90), Breakout=NO, Volume=0.74x (weak) | NO SETUP |
| MA Crossover | NO CROSSOVER | 10 EMA vs 50 EMA=BULLISH, but no crossover within 10 days, pullback zone=NO | NO SETUP |
| VIX Fear | N/A | Not applicable to single-stock analysis | N/A |

### Decision
**NO SETUP** — No active strategy triggers. Price has advanced significantly above 10 EMA ($1724.24), removing pullback zone for MA Crossover. RSI(2) is overbought (83.2). Relative volume weak (0.74x). Stock at resistance ($1806.75). No entry warranted.

---

## Ticker: MTD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $1324.66 |
| 20-Day Avg Volume | Baseline |
| Today's Relative Volume | 0.80x |
| ATR(14) | $36.80 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $1365.79 | +3.1% |
| Support 1 | $1216.63 | -8.2% |
| 200 SMA | $1332.35 | +0.6% |
| 50 EMA | $1306.46 | -1.4% |
| 10 EMA | $1314.15 | -0.8% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NEUTRAL | RSI(2)=50.0, Price vs 200 SMA=BELOW (FAIL) | NO SETUP |
| MACD + RSI | BULLISH BIAS | MACD cross=NO, RSI(14)=55.6 (in range), Volume=0.80x (weak) | NO SETUP |
| Bollinger Squeeze | NO SQUEEZE | BW=11.36 (vs 6m low=3.39), Breakout=NO, Volume=0.80x (weak) | NO SETUP |
| MA Crossover | PULLBACK ZONE | 10 EMA=$1314.15, Price=$1324.66 (within 1.0%), EMA10 vs EMA50=BULLISH (recent crossover), RSI(14)=55.6 | SETUP DETECTED |
| VIX Fear | N/A | Not applicable to single-stock analysis | N/A |

### Suggested Parameters (Pre-Computed)
| Parameter | Value |
|-----------|-------|
| Entry | $1324.66 |
| Stop Loss | $1269.46 |
| Take Profit | $1365.79 |
| Risk/Share | $55.20 |
| Reward/Share | $41.13 |
| R:R Ratio | 0.75:1 |

### Decision
**SETUP DETECTED — MA CROSSOVER (CONDITIONAL REJECTION)** — Price is in pullback zone ($1324.66 vs 10 EMA=$1314.15, within 1.0%), 10 EMA recently crossed above 50 EMA (bullish), RSI(14)=55.6 (neutral, not overbought). However, **R:R ratio of 0.75:1 falls significantly below minimum requirement of 1.5:1**. Risk ($55.20/share) substantially exceeds reward ($41.13/share). **TRADE REJECTED on risk/reward basis.** The setup is geometrically valid but position economics are unfavorable for swing trading. Pass to Agent 03 with notation.

---

## Ticker: AI

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $9.38 |
| 20-Day Avg Volume | Baseline |
| Today's Relative Volume | 0.56x |
| ATR(14) | $0.55 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $9.94 | +5.9% |
| Support 1 | $7.68 | -18.1% |
| 200 SMA | $15.38 | +63.8% |
| 50 EMA | $9.24 | -1.5% |
| 10 EMA | $8.97 | -4.4% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | OVERBOUGHT | RSI(2)=74.0, Price vs 200 SMA=BELOW (FAIL) | NO SETUP |
| MACD + RSI | NEUTRAL BEARISH | MACD cross=NO, RSI(14)=56.8 (in range), Price vs 50 SMA=ABOVE, Volume=0.56x (VERY WEAK) | NO SETUP |
| Bollinger Squeeze | NO SQUEEZE | BW=21.62 (vs 6m low=7.95), Breakout=NO, Volume=0.56x (very weak) | NO SETUP |
| MA Crossover | BEARISH | 10 EMA vs 50 EMA=BEARISH (EMA10 $8.97 < EMA50 $9.24), no pullback zone | NO SETUP |
| VIX Fear | N/A | Not applicable to single-stock analysis | N/A |

### Decision
**NO SETUP** — Multiple rejection criteria triggered. Price is 63.8% below 200 SMA (Connors fails trend filter). MA Crossover shows bearish divergence (EMA10 < EMA50). Relative volume extremely weak (0.56x). RSI(2) elevated (74.0) but price in downtrend. No entry warranted.

---

## Ticker: HD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $350.99 |
| 20-Day Avg Volume | Baseline |
| Today's Relative Volume | 0.83x |
| ATR(14) | $9.02 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $352.02 | +0.3% |
| Support 1 | $315.31 | -10.2% |
| 200 SMA | $368.35 | +4.9% |
| 50 EMA | $351.75 | +0.2% |
| 10 EMA | $340.71 | -2.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | OVERBOUGHT | RSI(2)=89.2, Price vs 200 SMA=BELOW (FAIL) | NO SETUP |
| MACD + RSI | WEAK BEARISH | MACD cross=NO, RSI(14)=58.4 (in range), Price vs 50 SMA=BELOW, Volume=0.83x (weak) | NO SETUP |
| Bollinger Squeeze | NO SQUEEZE | BW=10.48 (vs 6m low=4.43), Breakout=YES but at resistance, Volume=0.83x (weak) | NO SETUP |
| MA Crossover | BEARISH | 10 EMA vs 50 EMA=BEARISH (EMA10 $340.71 < EMA50 $351.75), pullback zone=NO | NO SETUP |
| VIX Fear | N/A | Not applicable to single-stock analysis | N/A |

### Decision
**NO SETUP** — Multiple rejection criteria. Price is 4.9% above 200 SMA (below medium-term trend). MA Crossover is bearish (10 EMA < 50 EMA). MACD is not crossed bullish. Price is near resistance ($352.02) with weak relative volume (0.83x). Bollinger Squeeze breakout is present but lacks volume confirmation. No entry warranted.

---

## Ticker: UNH

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $323.48 |
| 20-Day Avg Volume | Baseline |
| Today's Relative Volume | 1.11x |
| ATR(14) | $8.20 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $325.40 | +0.6% |
| Support 1 | $255.97 | -20.9% |
| 200 SMA | $309.02 | -4.5% |
| 50 EMA | $286.55 | -11.4% |
| 10 EMA | $310.84 | -3.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | OVERBOUGHT | RSI(2)=80.8, Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | OVERBOUGHT | MACD cross=NO, RSI(14)=72.1 (>70, near overbought), Volume=1.11x (confirms) | NO SETUP |
| Bollinger Squeeze | NO SQUEEZE | BW=30.55 (vs 6m low=5.04), Breakout=NO, Volume=1.11x | NO SETUP |
| MA Crossover | EMA BULLISH | 10 EMA vs 50 EMA=BULLISH (recent crossover), but price not in pullback zone (advanced to $323.48 vs $310.84), RSI(14)=72.1 (near overbought) | NO SETUP |
| VIX Fear | N/A | Not applicable to single-stock analysis | N/A |

### Decision
**NO SETUP** — Price has extended well above 10 EMA ($310.84), removing pullback zone for MA Crossover entry. RSI(