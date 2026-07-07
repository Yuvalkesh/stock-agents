# Technical Analysis Report — 2026-07-07

---

## Ticker: AMD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $552.05 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.95x |
| ATR(14) | $37.21 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $584.73 | +5.9% |
| Support 1 | $437.23 | -20.8% |
| 200 SMA | $280.14 | -49.3% |
| 50 SMA | $465.35 | -15.7% |
| 10 EMA | $536.05 | -2.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=64.95 | Price ABOVE 200 SMA, RSI(2) >= 10 (no extreme oversold) | NO SETUP |
| MACD + RSI | MACD=-2.77, RSI(14)=57.35 | MACD histogram negative, no bullish cross | NO SETUP |
| Bollinger Squeeze | BW=23.97, 6m-low=9.53 | Bandwidth expanded, squeeze condition not met, volume=0.95x | NO SETUP |
| MA Crossover | EMA10=536.05, EMA50=461.16 | Bullish EMA alignment but no pullback zone triggered | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stocks | N/A |

### Decision
**NO SETUP**

Data does not support any entry. RSI(2) well above extreme oversold threshold. MACD histogram negative, no bullish crossover. Price above all moving averages but no mean reversion or momentum confirmation. Volume weak at 0.95x. Wait for sharper pullback or clearer momentum signal.

---

## Ticker: AMAT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $592.79 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.65x |
| ATR(14) | $45.95 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $739.67 | +24.8% |
| Support 1 | $452.91 | -23.6% |
| 200 SMA | $340.85 | -42.5% |
| 50 SMA | $493.77 | -16.7% |
| 10 EMA | $624.90 | +5.4% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=14.53 | Price ABOVE 200 SMA, RSI(2)=14.53 (not < 10) | NO SETUP |
| MACD + RSI | MACD=-4.51, RSI(14)=52.69 | MACD histogram negative, no bullish cross, volume=0.65x (WEAK) | NO SETUP |
| Bollinger Squeeze | BW=45.70, 6m-low=8.80 | Bandwidth expanded, squeeze condition not met, volume=0.65x (WEAK) | NO SETUP |
| MA Crossover | EMA10=624.90, EMA50=517.74 | Bullish EMA alignment but price BELOW EMA10 — no pullback trigger | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stocks | N/A |

### Decision
**NO SETUP**

Price above 200 SMA but RSI(2) not extreme (14.53, need <10). MACD histogram negative, no cross. EMA10 > EMA50 but price is below the 10 EMA, which violates pullback zone logic. Volume critically weak at 0.65x. No actionable entry.

---

## Ticker: ABNB

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $147.65 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.65x |
| ATR(14) | $4.52 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $150.19 | +1.7% |
| Support 1 | $127.23 | -13.8% |
| 200 SMA | $130.21 | -11.8% |
| 50 SMA | $137.96 | -6.6% |
| 10 EMA | $144.73 | -1.98% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=53.64 | Price ABOVE 200 SMA, RSI(2)=53.64 (not < 10, no oversold) | NO SETUP |
| MACD + RSI | MACD=0.90, RSI(14)=61.43 | MACD histogram positive but no bullish cross, volume=0.65x (WEAK) | NO SETUP |
| Bollinger Squeeze | BW=17.23, 6m-low=4.49 | Bandwidth expanded, squeeze condition not met, volume=0.65x (WEAK) | NO SETUP |
| MA Crossover | EMA10=144.73, EMA50=138.18 | **Bullish EMA cross, price in pullback zone (within 1.0% of EMA10), RSI(14)=61.43** | **SETUP CONFIRMED** |
| VIX Fear | N/A | Not applicable to individual stocks | N/A |

### Suggested Parameters (MA Crossover)
| Parameter | Value |
|-----------|-------|
| Entry | $147.65 |
| Stop Loss | $140.87 |
| Take Profit | $150.19 |
| Risk/Share | $6.78 |
| Reward/Share | $2.54 |
| R:R Ratio | 0.37:1 |

### Decision
**NO SETUP — RISK/REWARD FAILURE**

Although MA Crossover technical criteria are met (EMA10 > EMA50, price near EMA10, RSI in range), the pre-computed R:R ratio is **0.37:1**, which falls far below the minimum 1.5:1 threshold required for this strategy. Risk ($6.78/share) is 2.67x the reward ($2.54/share). **Trade rejected on risk management grounds.** Resistance is too close; profit target inadequate relative to stop loss distance. Do not trade.

---

## Ticker: ROKU

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $142.26 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.29x |
| ATR(14) | $4.10 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $148.88 | +4.7% |
| Support 1 | $115.00 | -19.2% |
| 200 SMA | $107.09 | -24.7% |
| 50 SMA | $127.94 | -10.0% |
| 10 EMA | $138.32 | -2.8% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=90.42 | Price ABOVE 200 SMA, RSI(2)=90.42 (extreme overbought, not <10) | NO SETUP |
| MACD + RSI | MACD=0.39, RSI(14)=65.25 | MACD histogram positive but no bullish cross, volume=0.29x (CRITICALLY WEAK) | NO SETUP |
| Bollinger Squeeze | BW=24.21, 6m-low=5.88 | Bandwidth expanded, squeeze condition not met, volume=0.29x (CRITICALLY WEAK) | NO SETUP |
| MA Crossover | EMA10=138.32, EMA50=127.35 | Bullish EMA alignment but price above EMA10 — no pullback trigger, volume=0.29x (CRITICALLY WEAK) | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stocks | N/A |

### Decision
**NO SETUP**

RSI(2) at extreme overbought (90.42) — inverse of setup condition. Volume critically weak at 0.29x, invalidates all strategies. Price has already moved above mean reverting range. MACD shows minimal positive histogram but no crossover confirmation. EMA10 > EMA50 bullish but no pullback for entry. Do not trade. Wait for lower volume environment to normalize or sharper pullback.

---

## Ticker: GOOGL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $366.46 |
| Day Change | N/A |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.71x |
| ATR(14) | $11.44 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $376.00 | +2.6% |
| Support 1 | $330.20 | -9.9% |
| 200 SMA | $316.39 | -13.7% |
| 50 SMA | $371.37 | +1.3% |
| 10 EMA | $357.59 | -2.4% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=90.60 | Price ABOVE 200 SMA, RSI(2)=90.60 (extreme overbought, not <10) | NO SETUP |
| MACD + RSI | MACD=1.31, RSI(14)=53.69 | MACD histogram positive, bullish cross detected, **but price BELOW 50 SMA** | NO SETUP |
| Bollinger Squeeze | BW=10.53, 6m-low=5.06 | Bandwidth expanded, squeeze condition not met, volume=0.71x | NO SETUP |
| MA Crossover | EMA10=357.59, EMA50=358.97 | **Bearish EMA alignment** (EMA10 < EMA50) — no bullish crossover setup | NO SETUP |
| VIX Fear | N/A | Not applicable to individual stocks | N/A |

### Decision
**NO SETUP**

RSI(2) at extreme overbought (90.60). MACD shows bullish histogram but price is below 50 SMA, violating momentum entry condition. EMA10 < EMA50 indicates bearish alignment — no MA Crossover buy signal. Price near resistance with weak volume. Risk/reward unfavorable. Do not trade.

---

## Ticker: MSFT

### Price Data
| Metric | Value |
|--------|-------|