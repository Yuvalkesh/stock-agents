# Technical Analysis Report — 2026-09-07

## Ticker: AAPL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $319.97 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.0x |
| ATR(14) | $7.63 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $330.81 | +3.4% |
| Support 1 | $300.57 | -6.1% |
| 200 SMA | $283.44 | -11.4% |
| 50 EMA | $314.99 | -1.6% |
| 10 EMA | $319.51 | -0.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=25.3 (threshold: <10), Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO (MACD 2.64 vs Signal 1.09), RSI(14)=54.0, Volume=WEAK (1.0x) | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=9.3 (6m low: 4.9), Squeeze=NO, Volume=WEAK | NO SETUP |
| MA Crossover | MARGINAL | 10 EMA (319.51) vs 50 EMA (312.39)=BULLISH, Price in pullback zone, RSI(14)=54.0 | SETUP FLAGGED |
| VIX Fear | N/A | Strategy not applicable to individual equities | N/A |

### Suggested Parameters (Pre-Computed)
| Parameter | Value |
|-----------|-------|
| Entry | $319.97 |
| Stop Loss | $308.53 (1.5x ATR below entry) |
| Take Profit | $330.81 (resistance level) |
| Risk/Share | $11.44 |
| Reward/Share | $10.84 |
| R:R Ratio | 0.95:1 |
| Min R:R Threshold | 1.5:1 |

### Decision
**NO SETUP — MA Crossover fails R:R minimum (0.95:1 vs required 1.5:1)**

The MA Crossover shows structural bullish setup (10 EMA above 50 EMA, price in pullback zone, RSI neutral), but the reward-to-risk ratio (0.95:1) is below the 1.5:1 minimum threshold for this strategy. Stop loss is too tight relative to target. Risk-adjusted entry rejected.

---

## Ticker: MSFT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $499.70 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.79x |
| ATR(14) | $11.82 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $517.78 | +3.6% |
| Support 1 | $476.25 | -4.7% |
| 200 SMA | $429.37 | -14.1% |
| 50 EMA | $443.56 | -11.2% |
| 10 EMA | $499.80 | +0.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=36.0 (threshold: <10), Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO (histogram negative -2.4), RSI(14)=59.6, Volume=WEAK (0.79x) | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=8.2 (6m low: 5.2), Squeeze=NO, Volume=WEAK | NO SETUP |
| MA Crossover | FAIL | 10 EMA (499.80) vs 50 EMA (460.02)=BULLISH but price BELOW 10 EMA, pullback incomplete | NO SETUP |
| VIX Fear | N/A | Strategy not applicable to individual equities | N/A |

### Decision
**NO SETUP**

All five strategies reject. MA Crossover fails because price ($499.70) is below the 10 EMA ($499.80)—no bounce confirmation. MACD histogram is negative. RSI(2) is too high. Volume is subthreshold (0.79x). No entry warranted.

---

## Ticker: GOOGL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $338.46 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.04x |
| ATR(14) | $8.11 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $357.38 | +5.6% |
| Support 1 | $332.61 | -1.7% |
| 200 SMA | $335.50 | -0.9% |
| 50 EMA | $348.35 | +2.9% |
| 10 EMA | $340.85 | +0.7% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=41.2 (threshold: <10), Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO (negative histogram -0.37), RSI(14)=45.0, Price BELOW 50 EMA | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=5.4 (6m low: 5.1), Near squeeze but no breakout, Volume=WEAK | NO SETUP |
| MA Crossover | FAIL | 10 EMA (340.85) vs 50 EMA (348.35)=BEARISH crossover, Price below both MAs | NO SETUP |
| VIX Fear | N/A | Strategy not applicable to individual equities | N/A |

### Decision
**NO SETUP**

Bearish technical setup across all filters. 10 EMA below 50 EMA indicates downtrend formation. Price trades below 50 EMA. MACD histogram is negative. RSI(14) at 45.0 approaching oversold but not yet in Connors RSI(2) territory. No entry signal.

---

## Ticker: XOM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $159.47 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 1.15x |
| ATR(14) | $3.39 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $168.64 | +5.8% |
| Support 1 | $153.46 | -3.8% |
| 200 SMA | $143.07 | -10.2% |
| 50 EMA | $152.29 | -4.5% |
| 10 EMA | $161.16 | +1.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=15.8 (threshold: <10), Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO (histogram negative -0.56), RSI(14)=51.6, Volume=CONFIRMS but cross missing | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=7.7 (6m low: 5.2), Squeeze=NO, Volume=WEAK | NO SETUP |
| MA Crossover | FAIL | 10 EMA (161.16) vs 50 EMA (155.30)=BULLISH, but price BELOW 10 EMA, bounce not confirmed | NO SETUP |
| VIX Fear | N/A | Strategy not applicable to individual equities | N/A |

### Decision
**NO SETUP**

MA Crossover shows bullish structure (10 EMA above 50 EMA) but price ($159.47) is below the 10 EMA ($161.16)—pullback incomplete, bounce not yet confirmed. MACD histogram is negative. Volume is present (1.15x) but cross signal is absent. No entry.

---

## Ticker: CVX

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $208.60 |
| Day Change | — |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.70x |
| ATR(14) | $3.92 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $213.20 | +2.2% |
| Support 1 | $187.25 | -10.2% |
| 200 SMA | $178.23 | -14.5% |
| 50 EMA | $194.65 | -6.7% |
| 10 EMA | $206.55 | -1.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=27.6 (threshold: <10), Price vs 200 SMA=ABOVE | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO (histogram positive +0.33), RSI(14)=64.9 (approaching overbought), Volume=WEAK (0.70x) | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=10.8 (6m low: 6.5), Squeeze=NO, Volume=WEAK | NO SETUP |
| MA Crossover | MARGINAL | 10 EMA (206.55) vs 50 EMA (194.65)=BULLISH, Price in pullback zone (208.60 near 206.55), RSI(14)=64.9 (elevated) | SETUP FLAGGED |
| VIX Fear | N/A | Strategy not applicable to individual equities | N/A |

### Suggested Parameters (Pre-Computed)
| Parameter | Value |
|-----------|-------|
| Entry | $208.60 |
| Stop Loss | $202.72 (1.5x ATR below entry) |
| Take Profit | $213.20 (resistance level) |
| Risk/Share | $5.88 |
| Reward/Share | $4.60 |
| R:R Ratio | 0.78:1 |
| Min R:R Threshold | 1.5:1 |

### Decision
**NO SETUP — MA Crossover fails R:R minimum (0.78:1 vs required 1.5:1) and volume is subthreshold (0.70x)**

MA Crossover setup is structurally present (10 EMA bullish, price near 10 EMA) but fails on two