# Technical Analysis Report — 2026-05-25

## Ticker: AI

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $9.29 |
| 200-Day SMA | $13.35 |
| 50-Day SMA | $8.85 |
| 5-Day SMA | $9.10 |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 1.03x |
| ATR(14) | $0.49 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance | $9.88 | +6.4% |
| Support | $8.32 | -10.5% |
| 200 SMA | $13.35 | -43.6% |
| 50 SMA | $8.85 | -4.7% |
| 10 EMA | $9.12 | -1.8% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=73.9 (≥10), Price BELOW 200 SMA | NO SETUP |
| MACD + RSI | SETUP | MACD cross=YES, RSI(14)=53.6 (in range), Price ABOVE 50 SMA, Volume=1.03x | CONDITIONAL |
| Bollinger Squeeze | FAILED | Bandwidth=15.17 (above 6m low=7.95), No squeeze, Volume weak | NO SETUP |
| MA Crossover | FAILED | 10 EMA=9.12 > 50 EMA=9.28, BEARISH cross, pullback zone met but EMA bearish | NO SETUP |
| VIX Fear | N/A | N/A | NO SETUP |

### Assessment: MACD + RSI Setup Status
The MACD + RSI strategy shows a bullish setup with all core conditions met: MACD crossover confirmed, RSI(14) in ideal range (53.6), price above 50 SMA, and volume confirmation. However, **the Pre-Computed Trade Parameters show R:R Ratio of 0.8:1, which fails the minimum 1.0:1 requirement for this strategy**.

### Suggested Parameters (Pre-Computed — Use These Values)
| Parameter | Value |
|-----------|-------|
| Entry | $9.29 |
| Stop Loss | $8.55 (1.5x ATR below entry) |
| Take Profit | $9.88 (resistance) |
| Risk/Share | $0.74 |
| Reward/Share | $0.59 |
| R:R Ratio | 0.8:1 |
| Minimum R:R Required | 1.0:1 |

### Decision
**NO SETUP** — MACD + RSI triggers technically, but risk/reward ratio (0.8:1) does not meet the strategy's minimum threshold of 1.0:1. Trade is rejected on risk management grounds.

---

## Ticker: LLY

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $1065.00 |
| 200-Day SMA | $925.28 |
| 50-Day SMA | $941.92 |
| 5-Day SMA | $1027.00 |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 1.01x |
| ATR(14) | $30.18 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance | $1070.34 | +0.5% |
| Support | $849.05 | -20.3% |
| 200 SMA | $925.28 | -13.1% |
| 50 SMA | $941.92 | -11.5% |
| 10 EMA | $1014.12 | -4.8% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=95.5 (>>10), extreme overextension | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO (9-bar histogram positive but no crossover signal), RSI(14)=68.6 (in range) | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=22.76 (well above 6m low=5.51), no squeeze, volume weak | NO SETUP |
| MA Crossover | FAILED | 10 EMA=1014.12 ABOVE 50 EMA=968.29 (bullish), but NO recent crossover, no pullback zone | NO SETUP |
| VIX Fear | N/A | N/A | NO SETUP |

### Assessment
All five strategies fail. LLY shows an extended rally with RSI(2) at extreme levels (95.5), indicating price has run sharply higher without pullback support. MACD is strong but shows no fresh crossover signal. No momentum reversion or technical setup available.

### Decision
**NO SETUP** — No strategy triggers. Stock shows overextension with no actionable entry.

---

## Ticker: ENPH

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $64.03 |
| 200-Day SMA | $37.03 |
| 50-Day SMA | $38.98 |
| 5-Day SMA | $55.19 |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 1.12x |
| ATR(14) | $4.37 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance | $64.94 | +1.4% |
| Support | $29.90 | -53.3% |
| 200 SMA | $37.03 | -42.2% |
| 50 SMA | $38.98 | -39.1% |
| 10 EMA | $51.29 | -19.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=93.5 (>>10), extreme overextension | NO SETUP |
| MACD + RSI | FAILED | RSI(14)=78.3 (ABOVE 75 threshold), overbought, MACD cross=NO | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=93.22 (far above 6m low=10.19), no squeeze, volume weak, RSI overbought | NO SETUP |
| MA Crossover | FAILED | 10 EMA=51.29 BELOW 50 EMA=41.05 (bullish crossover exists), but price=64.03 is FAR above both MAs (not in pullback zone), RSI overbought=78.3 | NO SETUP |
| VIX Fear | N/A | N/A | NO SETUP |

### Assessment
ENPH is in a strong extended rally with RSI(2) at 93.5 and RSI(14) at 78.3, both indicating extreme overbought conditions. While the MA crossover is bullish, the price has already moved significantly above the pullback zone, violating the core entry requirement. No setup available.

### Decision
**NO SETUP** — Stock is overextended. All strategies rejected due to overbought conditions and lack of pullback entry opportunity.

---

## Ticker: SEDG

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $61.95 |
| 200-Day SMA | $37.18 |
| 50-Day SMA | $45.94 |
| 5-Day SMA | $58.19 |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.86x |
| ATR(14) | $5.43 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance | $65.16 | +5.2% |
| Support | $37.55 | -39.4% |
| 200 SMA | $37.18 | -39.9% |
| 50 SMA | $45.94 | -25.8% |
| 10 EMA | $54.53 | -12.0% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=73.5 (≥10), not in oversold territory | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO, RSI(14)=66.3 (in range), BUT relative volume=0.86x (WEAK, below 1.0x threshold) | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=66.23 (above 6m low=14.04), no squeeze, volume weak, RSI=66.3 | NO SETUP |
| MA Crossover | FAILED | Crossover=YES (10 EMA=54.53 > 50 EMA=45.74), but NO pullback zone (price=61.95 is far above 10 EMA), above 10 EMA condition met, RSI=66.3 OK | NO SETUP |
| VIX Fear | N/A | N/A | NO SETUP |

### Assessment
SEDG shows bullish structure with MA crossover present, but volume is weak (0.86x) which disqualifies MACD + RSI strategy. MA crossover is too far extended with no pullback zone entry. Relative volume weakness is a critical failure point across all volume-dependent strategies.

### Decision
**NO SETUP** — Relative volume too weak (0.86x). No strategy meets all entry requirements.

---

## Ticker: QCOM

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $238.16 |
| 200-Day SMA | $159.38 |
| 50-Day SMA | $156.56 |
| 5-Day SMA | $210.67 |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.95x |
| ATR(14) | $15.14 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance | $247.90 | +4.1% |
| Support | $144.00 | -39.5% |
| 200 SMA | $159.38 | -33.1% |
| 50 SMA | $156.56 | -34.3% |
| 10 EMA | $208.94 | -12.2% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=96.1 (>>10), extreme overextension | NO SETUP |
| MACD + RSI | SETUP | MACD cross=YES, RSI(14)=71.8 (in range), Price ABOVE 50 SMA, BUT relative volume=0.95x (WEAK) | CONDITIONAL |
| Bollinger Squeeze | FAILED | Bandwidth=50.91 (far above 6m low=5.85), no squeeze, volume weak | NO SETUP |
| MA Crossover | FAILED | 10 EMA=208.94 ABOVE 50 EMA=171.11 (bullish), but NO recent crossover within 10 days, no pullback zone | NO SETUP |
| VIX Fear | N/A | N/A | NO SETUP |

### Assessment: MACD + RSI Setup Status
The MACD + RSI strategy shows a bullish signal with MACD crossover confirmed and RSI(14) in the 35-75 range at 71.8. However, **the Pre-Computed Trade Parameters show R:R Ratio of 0.43:1, which significantly fails the minimum 1.0:1 requirement**. Additionally, relative volume at 0.95x is weak (below preferred 1.0x+ threshold).

### Suggested Parameters (Pre-Computed — Use These Values)
| Parameter | Value |
|-----------|-------|
| Entry | $238.16 |
| Stop Loss | $215.45 (1.5x ATR below entry) |
| Take Profit | $247.90 (resistance) |
| Risk/Share | $22.71 |
| Reward/Share | $9.74 |
| R:R Ratio | 0.43:1 |
| Minimum R:R Required | 1.0:1 |

### Decision
**NO SETUP** — MACD + RSI triggers technically, but risk/reward ratio (0.43:1) significantly fails the strategy's minimum threshold of 1.0:1. Unfavorable reward-to-risk profile rejects trade on risk management grounds.

---

## Ticker: CRWD

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $663.46 |
| 200-Day SMA | $465.21 |
| 50-Day SMA | $462.83 |
| 5-Day SMA | $639.50 |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 0.92x |
| ATR(14) | $24.24 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance | $674.84 | +1.7% |
| Support | $432.55 | -34.9% |
| 200 SMA | $465.21 | -29.9% |
| 50 SMA | $462.83 | -30.2% |
| 10 EMA | $604.68 | -8.9% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAILED | RSI(2)=95.6 (>>10), extreme overextension | NO SETUP |
| MACD + RSI | FAILED | MACD cross=NO (histogram=12.40 positive but no fresh cross), RSI(14)=86.9 (ABOVE 75, overbought) | NO SETUP |
| Bollinger Squeeze | FAILED | Bandwidth=55.22 (far above 6m low=7.85), no squeeze, volume weak | NO SETUP |
| MA Crossover | FAILED | 10 EMA=604.68 ABOVE 50 EMA=493.86 (bullish), but NO recent crossover, no pullback zone, RSI overbought=86.9 | NO SETUP |
| VIX Fear | N/A | N/A | NO SETUP |

### Assessment
CRWD exhibits extreme overbought conditions with RSI(2)=95.6 and RSI(14)=86.9, both well above threshold levels. Price has extended significantly above all moving averages without a pullback entry opportunity. Volume is weak at 0.92x. No actionable setup.

### Decision
**NO SETUP** — Stock severely overextended. RSI(14) at 86.9 is overbought. No strategy meets entry criteria.

---

## Ticker: NVDA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $215.33 |
| 200-Day SMA | $187.02 |
| 50-Day SMA | $196.81 |
| 5-Day SMA | $220.25 |
| 20-Day Avg Volume | N/A |
| Today's Volume | N/A |
| Relative Volume | 1.04x |
| ATR(14) | $7.59 |

### Key Levels
| Level