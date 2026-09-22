# Technical Analysis Report — 2026-09-22

## Ticker: AMD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $617.59 |
| 52-Week Support | $440.50 |
| 52-Week Resistance | $622.00 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 0.59x |
| ATR(14) | $25.59 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $622.00 | +0.71% |
| Support 1 | $440.50 | -28.64% |
| 200 SMA | $358.63 | -41.88% |
| 50 SMA | $498.66 | -19.24% |
| 10 EMA | $549.47 | -10.97% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | REJECTED | RSI(2)=98.91 (threshold <10), Price=$617.59 above 200 SMA | NO SETUP |
| MACD + RSI | REJECTED | MACD histogram=14.59 (no cross), RSI(14)=73.2 (range OK), Volume=0.59x (WEAK) | NO SETUP |
| Bollinger Squeeze | REJECTED | Bandwidth=36.38 (6-month low=9.53, squeeze=NO), Breakout=YES but Volume=0.59x (WEAK) | NO SETUP |
| MA Crossover | REJECTED | 10 EMA=$549.47 vs 50 EMA=$501.26 (BULLISH cross present), Price=$617.59 NOT in pullback zone | NO SETUP |
| VIX Fear | N/A | Ticker is not SPY/QQQ | N/A |

### Analysis Notes
AMD is extended above all short-term moving averages with RSI(2) at extreme overbought (98.91). While price remains above 200 SMA in a long-term uptrend, no entry signal meets threshold criteria. Volume confirmation is weak (0.59x). The 10 EMA/50 EMA crossover exists but price has not pulled back into the optimal entry zone.

### Decision
**NO SETUP**

---

## Ticker: CRWD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $246.88 |
| 52-Week Support | $181.24 |
| 52-Week Resistance | $250.32 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 0.28x |
| ATR(14) | $12.74 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $250.32 | +1.40% |
| Support 1 | $181.24 | -26.58% |
| 200 SMA | $148.15 | -39.96% |
| 50 SMA | $209.51 | -15.12% |
| 10 EMA | $235.46 | -4.62% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | REJECTED | RSI(2)=60.71 (threshold <10), Price above 200 SMA | NO SETUP |
| MACD + RSI | REJECTED | MACD histogram=3.04 (no cross), RSI(14)=63.11 (range OK), Volume=0.28x (WEAK) | NO SETUP |
| Bollinger Squeeze | REJECTED | Bandwidth=33.69 (6-month low=15.44, squeeze=NO), No breakout above upper band | NO SETUP |
| MA Crossover | REJECTED | 10 EMA=$235.46 vs 50 EMA=$209.93 (BULLISH), Price=$246.88 NOT in pullback zone, no recent crossover | NO SETUP |
| VIX Fear | N/A | Ticker is not SPY/QQQ | N/A |

### Analysis Notes
CRWD is trading near resistance with weak volume (0.28x). No MACD crossover is present, and while the 10/50 EMA relationship is bullish, price has not pulled back to the 10 EMA for entry. RSI(14) is neutral at 63.11. No actionable setup exists.

### Decision
**NO SETUP**

---

## Ticker: FTNT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $172.15 |
| 52-Week Support | $149.50 |
| 52-Week Resistance | $176.10 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 0.23x |
| ATR(14) | $7.10 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $176.10 | +2.29% |
| Support 1 | $149.50 | -13.14% |
| 200 SMA | $114.79 | -33.31% |
| 50 SMA | $160.75 | -6.59% |
| 10 EMA | $168.82 | -1.94% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | REJECTED | RSI(2)=44.73 (threshold <10), Price above 200 SMA | NO SETUP |
| MACD + RSI | REJECTED | MACD histogram=1.28 (no cross), RSI(14)=58.62 (range OK), Volume=0.23x (WEAK) | NO SETUP |
| Bollinger Squeeze | REJECTED | Bandwidth=18.36 (6-month low=9.03, squeeze=NO), No breakout above upper band | NO SETUP |
| MA Crossover | **FLAGGED** | Crossover=NO recent, EMA10=$168.82 vs EMA50=$159.10 (BULLISH), Pullback zone=YES (within 1.0% of EMA10), Price=$172.15 ABOVE EMA10, RSI(14)=58.62 | **CONDITIONAL** |
| VIX Fear | N/A | Ticker is not SPY/QQQ | N/A |

### Pre-Computed Trade Parameters
_ma_crossover_:
- Entry: $172.15
- Stop Loss: $161.50 (1.5x ATR below entry)
- Take Profit: $176.10 (resistance)
- Risk/Share: $10.65
- Reward/Share: $3.95
- R:R Ratio: 0.37:1
- **Minimum R:R for strategy: 1.5:1 — FAIL**

### Analysis Notes
FTNT shows a bullish EMA structure (10 EMA above 50 EMA) with price near the 10 EMA, meeting pullback zone criteria. However, **the R:R ratio of 0.37:1 falls significantly short of the 1.5:1 minimum requirement** for MA Crossover strategy. Risk ($10.65/share) far exceeds reward ($3.95/share). Volume is extremely weak at 0.23x. Despite technical alignment, risk/reward parameters reject this setup.

### Decision
**NO SETUP** — R:R ratio below minimum threshold (0.37:1 vs 1.5:1 required)

---

## Ticker: NET

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $351.27 |
| 52-Week Support | $269.30 |
| 52-Week Resistance | $353.81 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 0.33x |
| ATR(14) | $17.69 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $353.81 | +0.72% |
| Support 1 | $269.30 | -23.33% |
| 200 SMA | $229.33 | -34.75% |
| 50 SMA | $295.04 | -16.02% |
| 10 EMA | $328.10 | -6.59% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | REJECTED | RSI(2)=82.58 (threshold <10), Price above 200 SMA | NO SETUP |
| MACD + RSI | REJECTED | MACD histogram=4.68 (no cross), RSI(14)=65.23 (range OK), Volume=0.33x (WEAK) | NO SETUP |
| Bollinger Squeeze | REJECTED | Bandwidth=30.66 (6-month low=9.13, squeeze=NO), No breakout above upper band | NO SETUP |
| MA Crossover | REJECTED | No recent crossover, 10 EMA=$328.10 vs 50 EMA=$294.94 (BULLISH), Price=$351.27 NOT in pullback zone | NO SETUP |
| VIX Fear | N/A | Ticker is not SPY/QQQ | N/A |

### Analysis Notes
NET is near all-time resistance with RSI(2) elevated at 82.58, suggesting a recent sharp move without mean reversion conditions. While the 10/50 EMA relationship is bullish, price has moved too far above the 10 EMA to trigger a pullback entry. Volume is weak at 0.33x. No actionable setup.

### Decision
**NO SETUP**

---

## Ticker: QCOM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $195.92 |
| 52-Week Support | $158.22 |
| 52-Week Resistance | $196.00 |
| 20-Day Avg Volume | N/A |
| Relative Volume | 0.21x |
| ATR(14) | $8.59 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $196.00 | +0.04% |
| Support 1 | $158.22 | -19.26% |
| 200 SMA | $167.25 | -14.62% |
| 50 SMA | $168.20 | -14.18% |
| 10 EMA | $184.70 | -5.74% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | REJECTED | RSI(2)=78.35 (threshold <10), Price above 200 SMA | NO SETUP |
| MACD + RSI | REJECTED | MACD histogram=2.22 (no cross), RSI(14)=66.79 (range OK), Volume=0.21x (WEAK) | NO SETUP |
| Bollinger Squeeze | REJECTED | Bandwidth=23.98 (6-month low=5.85, squeeze=NO), No breakout above upper band | NO SETUP |
| MA Crossover | REJECTED | Crossover=YES (10 EMA above 50 EMA), but Price=$195.92 NOT in pullback zone (too extended), Volume=0.21x (WEAK) | NO SETUP |
| VIX Fear | N/A | Ticker is not SPY/QQQ | N/A |

### Analysis Notes
QCOM is at resistance with RSI(