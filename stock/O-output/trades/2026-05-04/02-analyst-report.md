# Technical Analysis Report — 2026-05-04

## Ticker: AI

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $9.16 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 1.15x |
| ATR(14) | $0.50 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $9.94 | +8.5% |
| Support 1 | $7.90 | -13.8% |
| 200 SMA | $14.59 | +59.2% |
| 50 EMA | $8.87 | -3.2% |
| 10 EMA | $8.94 | -2.4% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=86.6, Price BELOW 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO, RSI(14)=53.7 (in range) | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=15.9 (not at 6m low), Volume=WEAK | NO SETUP |
| MA Crossover | FAILED | EMA10 BELOW EMA50 (bearish), Pullback zone=YES | NO SETUP |
| VIX Fear | N/A | Not applicable for individual stocks | N/A |

### Decision
**NO SETUP** — Price is below 200 SMA, eliminating mean reversion setup. EMA10 below EMA50 eliminates crossover. No MACD cross present. Bandwidth not in squeeze zone. All strategies fail fundamental criteria.

---

## Ticker: UP

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $5.60 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 2.29x |
| ATR(14) | $1.04 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $10.94 | +95.4% |
| Support 1 | $4.69 | -16.3% |
| 200 SMA | $22.40 | +300.0% |
| 50 EMA | $9.81 | +75.2% |
| 10 EMA | $6.66 | +19.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=47.5, Price BELOW 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO, RSI(14)=31.4 (OUT of range <35), Price BELOW 50 SMA | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=83.7 (not squeezed), Breakout=NO, RSI(14)=31.4 (bearish) | NO SETUP |
| MA Crossover | FAILED | EMA10 BELOW EMA50 (bearish), Price NOT above EMA10, RSI(14)=31.4 (bearish) | NO SETUP |
| VIX Fear | N/A | Not applicable for individual stocks | N/A |

### Decision
**NO SETUP** — Price significantly below 200 SMA eliminates mean reversion. EMA10 below EMA50 with price below EMA10 eliminates crossover. RSI(14)=31.4 fails range requirement for MACD setup (needs 35-75). No valid strategy triggers.

---

## Ticker: NVDA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $198.45 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.87x |
| ATR(14) | $6.28 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $216.83 | +9.3% |
| Support 1 | $173.66 | -12.5% |
| 200 SMA | $183.84 | -7.3% |
| 50 EMA | $187.15 | -5.6% |
| 10 EMA | $202.99 | +2.3% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | **TRIGGERED** | RSI(2)=9.9 (<10 OVERSOLD), Price ABOVE 200 SMA | **SETUP CONFIRMED** |
| MACD + RSI | FAILED | MACD cross=NO, RSI(14)=53.0 (in range), Volume=WEAK (0.87x) | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=21.7 (not at 6m low=5.4), Breakout=NO, Volume=WEAK | NO SETUP |
| MA Crossover | FAILED | EMA10 ABOVE EMA50 (bullish), Price NOT above EMA10, Pullback=YES but price below entry zone | NO SETUP |
| VIX Fear | N/A | Not applicable for individual stocks | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $198.45 |
| Stop Loss | $185.89 (2x ATR(14) below entry) |
| Target | $207.41 (close above 5-day SMA) |
| Risk/Share | $12.56 |
| Reward/Share | $8.96 |
| R:R Ratio | 0.71:1 |
| Min R:R Required | 0.5:1 |
| R:R Verdict | **PASS** |

### Decision
**SETUP CONFIRMED — Connors RSI(2) Mean Reversion**

NVDA triggers the Connors RSI(2) setup with textbook conditions: extreme short-term oversold (RSI(2)=9.9) within a long-term uptrend (price $198.45 above 200 SMA of $183.84). Stock is above $10 liquidity threshold. Relative volume of 0.87x is marginally weak but acceptable. Pre-computed parameters meet minimum R:R requirement (0.71:1 vs 0.5:1 needed). Mean reversion target is 5-day SMA at $207.41. Stop loss at $185.89 provides risk definition.

---

## Ticker: HD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $323.88 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 1.09x |
| ATR(14) | $8.24 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $353.55 | +9.2% |
| Support 1 | $315.31 | -2.6% |
| 200 SMA | $367.10 | +13.4% |
| 50 EMA | $342.68 | +5.8% |
| 10 EMA | $331.57 | +2.4% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=29.2, Price BELOW 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO (histogram negative), RSI(14)=40.1 (in range), Price BELOW 50 SMA | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=10.0 (not at 6m low=4.4), Breakout=NO, Volume=WEAK | NO SETUP |
| MA Crossover | FAILED | EMA10 BELOW EMA50 (bearish), Price NOT above EMA10, RSI(14)=40.1 (borderline) | NO SETUP |
| VIX Fear | N/A | Not applicable for individual stocks | N/A |

### Decision
**NO SETUP** — Price is $13.22 below 200 SMA, eliminating mean reversion. EMA10 below EMA50 with price below EMA10 eliminates crossover. MACD histogram negative (no bullish cross). No strategy parameters met.

---

## Ticker: WMT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $131.60 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.63x |
| ATR(14) | $2.77 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $133.37 | +1.3% |
| Support 1 | $121.33 | -7.8% |
| 200 SMA | $112.05 | -14.8% |
| 50 EMA | $125.62 | -4.5% |
| 10 EMA | $129.34 | -1.7% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=79.6 (NOT <10), Price ABOVE 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO, RSI(14)=61.0 (in range), Price ABOVE 50 SMA, Volume=WEAK (0.63x) | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=8.0 (not at 6m low=4.8), Breakout=NO, Volume=WEAK | NO SETUP |
| MA Crossover | **TRIGGERED** | EMA10 ABOVE EMA50 (bullish), Price ABOVE EMA10, Pullback=YES, RSI(14)=61.0 (in range) | **SETUP TRIGGERED** |
| VIX Fear | N/A | Not applicable for individual stocks | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $131.60 |
| Stop Loss | $127.44 (1.5x ATR(14) below entry) |
| Target | $133.37 (resistance) |
| Risk/Share | $4.16 |
| Reward/Share | $1.77 |
| R:R Ratio | 0.43:1 |
| Min R:R Required | 1.5:1 |
| R:R Verdict | **FAIL** |

### Decision
**NO SETUP** — While WMT triggers the MA Crossover criteria (EMA10 above EMA50, price above EMA10 after pullback, RSI in range), the **R:R ratio of 0.43:1 fails the minimum 1.5:1 requirement** for this strategy. Reward ($1.77) is insufficient relative to risk ($4.16). Distance to resistance is only 1.3%, providing minimal profit potential with technical stop-loss being too wide. Trade does not meet risk/reward threshold.

---

## Ticker: NOTE

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $0.21 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 2.22x |
| ATR(14) | $0.06 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $0.31 | +47.6% |
| Support 1 | $0.16 | -23.8% |
| 200 SMA | $3.00 | +1328.6% |
| 50 EMA | $0.62 | +195.2% |
| 10 EMA | $0.21 | +0.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=67.8 (NOT <10), Price BELOW 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO, RSI(14)=29.5 (OUT of range <35), Price BELOW 50 SMA | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=53.2 (not squeezed), Breakout=NO, RSI(14)=29.5 (bearish) | NO SETUP |
| MA Crossover | FAILED | EMA10 BELOW EMA50 (bearish), Price NOT above EMA10, RSI(14)=29.5 (bearish) | NO SETUP |
| VIX Fear | N/A | Not applicable for individual stocks | N/A |

### Decision
**NO SETUP** — NOTE is a distressed penny stock trading $0.21, drastically below 200 SMA of $3.00. EMA10 equals price but is below EMA50, creating bearish structure. RSI(14)=29.5 fails MACD range requirement. High relative volume (2.22x) does not compensate for complete absence of valid technical setup. Volatility and position risk are excessive for swing trading criteria.

---

## Ticker: SPY

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $720.65 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.80x |
| ATR(14) | $7.78 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $724.87 | +0.6% |
| Support 1 | $651.06 | -9.7% |
| 200 SMA | $667.94 | -7.3% |
| 50 EMA | $679.48 | -5.7% |
| 10 EMA | $710.98 | -1.3% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=91.7 (NOT <10), Price ABOVE 200 SMA | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO, RSI(14)=71.7 (in range but overbought-adjacent), Price ABOVE 50 SMA, Volume=WEAK (0.8x) | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=10.6 (historically not squeezed), Breakout=NO, Volume=WEAK | NO SETUP |
| MA Crossover | **TRIGGERED** | EMA10 ABOVE EMA50 (bullish), Price ABOVE EMA10, Pullback=YES, RSI(14)=71.7 (in range) | **SETUP TRIGGERED** |
| VIX Fear | FAILED | VIX=17.98 vs SMA=18.3 (-1.7%, needs -20% spike), S&P ABOVE 200 SMA | NO SETUP |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |