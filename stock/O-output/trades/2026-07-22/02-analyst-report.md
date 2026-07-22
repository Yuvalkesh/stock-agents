# Technical Analysis Report — 2026-07-22

## Ticker: PANW

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $342.15 |
| 200-Day SMA | $209.82 |
| 50-Day SMA | $290.09 |
| 10-Day EMA | $343.96 |
| ATR(14) | $16.72 |
| 20-Day Avg Volume | Baseline |
| Relative Volume | 0.92x |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $368.80 | +7.8% |
| Support 1 | $282.52 | -17.4% |
| 200 SMA | $209.82 | -38.7% |
| 50 EMA | $290.09 | -15.2% |
| 10 EMA | $343.96 | +0.5% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO | RSI(2)=15.2, Price > 200 SMA (ABOVE) | NO SETUP |
| MACD + RSI | NO | MACD=-1.76 (neg histogram), RSI(14)=58.8, Vol=0.92x | NO SETUP |
| Bollinger Squeeze | NO | BW=27.16 (far from 6m low 6.85), RSI(14)=58.8 | NO SETUP |
| MA Crossover | NO | 10 EMA > 50 EMA (bullish), Price < 10 EMA (no bounce confirmation) | NO SETUP |
| VIX Fear | N/A | Not applicable to individual equity | N/A |

### Decision
**NO SETUP** — No strategy triggers valid entry conditions. Connors RSI(2) fails (15.2 >= 10). MACD histogram negative, no crossover. Bollinger Bands show no squeeze. MA Crossover bullish but price fails to confirm bounce above 10 EMA. Relative volume weak at 0.92x.

---

## Ticker: CRWD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $191.15 |
| 200-Day SMA | $130.27 |
| 50-Day SMA | $174.89 |
| 5-Day SMA | $200.65 |
| ATR(14) | $10.38 |
| 20-Day Avg Volume | Baseline |
| Relative Volume | 0.96x |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $217.50 | +13.8% |
| Support 1 | $165.50 | -13.5% |
| 200 SMA | $130.27 | -31.9% |
| 50 SMA | $174.89 | -8.5% |
| 5 SMA | $200.65 | +5.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | YES* | RSI(2)=6.71 (< 10 OVERSOLD), Price > 200 SMA (ABOVE) | SETUP CONFIRMED |
| MACD + RSI | NO | MACD=-0.94 (negative histogram), RSI(14)=52.9, Vol=0.96x | NO SETUP |
| Bollinger Squeeze | NO | BW=25.04 (far from 6m low 8.62), RSI(14)=52.9 | NO SETUP |
| MA Crossover | NO | 10 EMA > 50 EMA (bullish), Price < 10 EMA (no bounce confirmation) | NO SETUP |
| VIX Fear | N/A | Not applicable to individual equity | N/A |

### Suggested Parameters (use Pre-Computed values)
| Parameter | Value |
|-----------|-------|
| Entry | $191.15 |
| Stop Loss | $170.39 (2x ATR below entry) |
| Take Profit | $200.65 (above 5-day SMA) |
| Risk/Share | $20.76 |
| Reward/Share | $9.50 |
| R:R Ratio | 0.46:1 |
| Min Required | 0.5:1 |

### Decision
**SETUP CONFIRMED — Connors RSI(2)** ⚠️ **RISK WARNING: R:R RATIO FAILS MINIMUM THRESHOLD**

Connors RSI(2) entry conditions satisfied: RSI(2)=6.71 (< 10), price $191.15 is well above 200 SMA at $130.27. Mean reversion setup valid. However, **R:R ratio of 0.46:1 FAILS the strategy minimum of 0.5:1**. Risk ($20.76) exceeds reward ($9.50). **TRADE REJECTED** — Risk/reward imbalance does not justify entry despite valid technical setup.

---

## Ticker: FTNT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $158.10 |
| 200-Day SMA | $97.81 |
| 50-Day SMA | $144.25 |
| 10-Day EMA | $160.07 |
| ATR(14) | $6.53 |
| 20-Day Avg Volume | Baseline |
| Relative Volume | 1.05x |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $170.35 | +7.7% |
| Support 1 | $143.47 | -9.2% |
| 200 SMA | $97.81 | -38.1% |
| 50 SMA | $144.25 | -8.8% |
| 10 EMA | $160.07 | +1.2% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO | RSI(2)=11.93 (>= 10, not oversold), Price > 200 SMA (ABOVE) | NO SETUP |
| MACD + RSI | NO | MACD=-1.15 (negative histogram), RSI(14)=55.3, Vol=1.05x | NO SETUP |
| Bollinger Squeeze | NO | BW=13.96 (far from 6m low 9.03), RSI(14)=55.3 | NO SETUP |
| MA Crossover | NO | 10 EMA > 50 EMA (bullish), Price < 10 EMA (no bounce confirmation) | NO SETUP |
| VIX Fear | N/A | Not applicable to individual equity | N/A |

### Decision
**NO SETUP** — Connors RSI(2) fails: 11.93 >= 10 threshold. MACD histogram negative, no crossover signal. Bollinger Bands show no squeeze. MA Crossover bullish structure but price fails to bounce above 10 EMA. Relative volume adequate (1.05x) but no strategy triggers.

---

## Ticker: DDOG

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $254.79 |
| 200-Day SMA | $163.39 |
| 50-Day SMA | $236.92 |
| 10-Day EMA | $259.45 |
| ATR(14) | $13.43 |
| 20-Day Avg Volume | Baseline |
| Relative Volume | 1.04x |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $276.70 | +8.6% |
| Support 1 | $212.73 | -16.5% |
| 200 SMA | $163.39 | -35.9% |
| 50 SMA | $236.92 | -7.0% |
| 10 EMA | $259.45 | +1.8% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO | RSI(2)=20.94 (>= 10, not oversold), Price > 200 SMA (ABOVE) | NO SETUP |
| MACD + RSI | NO | MACD=-1.68 (negative histogram), RSI(14)=53.9, Vol=1.04x | NO SETUP |
| Bollinger Squeeze | NO | BW=23.70 (far from 6m low 14.71), RSI(14)=53.9 | NO SETUP |
| MA Crossover | NO | 10 EMA > 50 EMA (bullish), Price < 10 EMA (no bounce confirmation) | NO SETUP |
| VIX Fear | N/A | Not applicable to individual equity | N/A |

### Decision
**NO SETUP** — Connors RSI(2) fails: 20.94 >= 10. MACD histogram negative with no bullish crossover. Bollinger Bands not squeezed. MA Crossover shows bullish alignment but price fails to confirm bounce above 10 EMA. Relative volume adequate but no valid entry signal across any strategy.

---

## Ticker: NET

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $272.31 |
| 200-Day SMA | $211.30 |
| 50-Day SMA | $237.54 |
| 10-Day EMA | $269.81 |
| ATR(14) | $13.52 |
| 20-Day Avg Volume | Baseline |
| Relative Volume | 1.15x |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $291.00 | +6.9% |
| Support 1 | $214.60 | -21.2% |
| 200 SMA | $211.30 | -22.4% |
| 50 SMA | $237.54 | -12.8% |
| 10 EMA | $269.81 | -0.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | NO | RSI(2)=33.84 (>= 10, not oversold), Price > 200 SMA (ABOVE) | NO SETUP |
| MACD + RSI | NO | MACD=+0.61 (positive but weak), RSI(14)=60.9, Price > 50 SMA | NO SETUP |
| Bollinger Squeeze | NO | BW=29.61 (far from 6m low 12.63), RSI(14)=60.9 | NO SETUP |
| MA Crossover | YES* | 10 EMA > 50 EMA (bullish), Price > 10 EMA (above), RSI(14)=60.9 | SETUP CONFIRMED |
| VIX Fear | N/A | Not applicable to individual equity | N/A |

### Suggested Parameters (use Pre-Computed values)
| Parameter | Value |
|-----------|-------|
| Entry | $272.31 |
| Stop Loss | $252.03 (1.5x ATR below entry) |
| Take Profit | $291.00 (resistance level) |
| Risk/Share | $20.28 |
| Reward/Share | $18.69 |
|