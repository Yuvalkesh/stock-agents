# Technical Analysis Report — 2026-08-12

## Ticker: GOOGL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $343.80 |
| Support | $314.90 |
| Resistance | $384.48 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.87x |
| ATR(14) | $12.42 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $384.48 | +11.8% |
| Support 1 | $314.90 | -8.4% |
| 200 SMA | $329.83 | -4.0% |
| 50 EMA | $355.10 | +3.3% |
| 10 EMA | $353.05 | +2.7% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=12.02 | Above threshold (≥10); Price above 200 SMA | **NO SETUP** |
| MACD + RSI | MACD=0.27, Signal=-1.06 | No crossover; RSI=45.86 in range; Price below 50 SMA | **NO SETUP** |
| Bollinger Squeeze | BW=18.84, 6M Low=5.06 | No squeeze (BW >> min); No breakout; Volume weak (0.87x) | **NO SETUP** |
| MA Crossover | 10 EMA=353.05, 50 EMA=353.61 | EMA10 below EMA50 (bearish); Price below 10 EMA | **NO SETUP** |
| VIX Fear | — | Not applicable to single stock | — |

### Decision
**NO SETUP**

All strategies fail entry criteria. Price trapped below both EMAs with weak volume confirmation. Bearish MA alignment disqualifies crossover setup.

---

## Ticker: AMZN

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $272.27 |
| Support | $226.16 |
| Resistance | $287.20 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.63x |
| ATR(14) | $9.02 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $287.20 | +5.5% |
| Support 1 | $226.16 | -17.0% |
| 200 SMA | $237.09 | -13.0% |
| 50 EMA | $251.99 | -7.4% |
| 10 EMA | $267.16 | -1.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=31.02 | Above threshold (≥10); Price above 200 SMA | **NO SETUP** |
| MACD + RSI | MACD=8.43, Signal=5.26 | No crossover; RSI=60.97 in range; Volume weak (0.63x) | **NO SETUP** |
| Bollinger Squeeze | BW=29.43, 6M Low=5.81 | No squeeze; No breakout; Volume weak (0.63x) | **NO SETUP** |
| MA Crossover | 10 EMA=267.16, 50 EMA=251.99 | **Crossover YES; EMA10 > EMA50 (bullish); Pullback zone YES; Price > EMA10; RSI=60.97** | **SETUP CONFIRMED** |
| VIX Fear | — | Not applicable to single stock | — |

### Suggested Parameters (use Pre-Computed values)
| Parameter | Value |
|-----------|-------|
| Entry | $272.27 |
| Stop Loss | $258.74 (1.5x ATR below entry) |
| Target | $287.20 |
| R:R Ratio | 1.1:1 |
| Risk/Share | $13.53 |
| Reward/Share | $14.93 |

### Decision
**SETUP CONFIRMED — MA Crossover**

✓ 10 EMA ($267.16) crossed above 50 EMA ($251.99) — bullish crossover active
✓ Price ($272.27) within pullback zone (1.9% above 10 EMA)
✓ RSI(14) = 60.97 — in bullish sweet spot (35–75 range)
✓ Relative volume 0.63x — acceptable
✓ Price above 50 EMA ($251.99) confirms medium-term uptrend

**CAVEAT:** R:R ratio of 1.1:1 **FAILS minimum 1.5:1 threshold** for this strategy. Setup technically valid but insufficient reward-to-risk geometry. Proceed with caution.

---

## Ticker: MSFT

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $503.81 |
| Support | $377.39 |
| Resistance | $513.73 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.58x |
| ATR(14) | $15.01 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $513.73 | +1.9% |
| Support 1 | $377.39 | -25.0% |
| 200 SMA | $431.72 | -14.3% |
| 50 EMA | $409.66 | -18.7% |
| 10 EMA | $477.97 | -5.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=67.92 | Above threshold (≥10); Price above 200 SMA | **NO SETUP** |
| MACD + RSI | MACD=30.31, Signal=21.19 | No crossover; RSI=77.72 **OUT OF RANGE (>75)** | **NO SETUP** |
| Bollinger Squeeze | BW=45.26, 6M Low=5.20 | No squeeze; No breakout; Volume weak (0.58x) | **NO SETUP** |
| MA Crossover | 10 EMA=477.97, 50 EMA=423.10 | Crossover YES; EMA10 > EMA50 (bullish); **No pullback zone** (price $5.84 above 10 EMA); RSI overbought | **NO SETUP** |
| VIX Fear | — | Not applicable to single stock | — |

### Decision
**NO SETUP**

MACD momentum rules fail — RSI(14) = 77.72 is overbought (>75 threshold). MA crossover fails pullback requirement; price too extended above 10 EMA. High overextension risk. Volume weakness (0.58x) adds caution.

---

## Ticker: META

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $599.12 |
| Support | $524.49 |
| Resistance | $686.08 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.78x |
| ATR(14) | $22.46 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $686.08 | +14.5% |
| Support 1 | $524.49 | -12.5% |
| 200 SMA | $629.09 | +5.0% |
| 50 EMA | $598.17 | -0.2% |
| 10 EMA | $592.42 | -1.1% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=96.21 | Above threshold; **Price BELOW 200 SMA** | **NO SETUP** |
| MACD + RSI | MACD=-5.68, Signal=-5.42 | No crossover; RSI=49.93 in range; Price above 50 EMA; Volume weak | **NO SETUP** |
| Bollinger Squeeze | BW=22.58, 6M Low=5.03 | No squeeze; No breakout; Volume weak (0.78x); RSI=49.93 | **NO SETUP** |
| MA Crossover | 10 EMA=592.42, 50 EMA=603.24 | **No crossover; EMA10 < EMA50 (bearish); Price in pullback zone; But above 10 EMA** | **NO SETUP** |
| VIX Fear | — | Not applicable to single stock | — |

### Decision
**NO SETUP**

Connors fails — price below 200 SMA disqualifies mean reversion in uptrend. MACD shows no momentum crossover. MA crossover fails — no recent crossover event and EMA10 below EMA50 (bearish alignment). Meta is extended off 50 EMA with conflicting signals.

---

## Ticker: XOM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $159.80 |
| Support | $142.03 |
| Resistance | $161.67 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.94x |
| ATR(14) | $3.92 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $161.67 | +1.2% |
| Support 1 | $142.03 | -11.1% |
| 200 SMA | $139.62 | -12.6% |
| 50 EMA | $147.03 | -8.0% |
| 10 EMA | $155.66 | -2.6% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | RSI(2)=85.36 | Above threshold (≥10); Price above 200 SMA | **NO SETUP** |
| MACD + RSI | MACD=3.17, Signal=2.93 | **MACD crossover YES; RSI=65.10 in range; Price above 50 EMA; Volume 0.94x** | **SETUP CONFIRMED** |
| Bollinger Squeeze | BW=10.82, 6M Low=5.21 | Approaching squeeze but not confirmed; No breakout; Volume weak | **NO SETUP** |
| MA Crossover | 10 EMA=155.66, 50 EMA=149.80 | Crossover NO; EMA10 > EMA50 (bullish); **Price not in pullback zone** (4.14 above 10 EMA) | **NO SETUP** |
| VIX Fear | — | Not applicable to single stock | — |

### Suggested Parameters (use Pre-Computed values)
| Parameter | Value |
|-----------|-------|
| Entry | $159.80 |
| Stop Loss | $153.92 (1.5x ATR below entry) |
| Target | $161.67 |