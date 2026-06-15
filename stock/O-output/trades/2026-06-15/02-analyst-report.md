# Technical Analysis Report — 2026-06-15

## Ticker: NVDA

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $212.50 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.39x |
| ATR(14) | $7.99 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $232.01 | +9.15% |
| Support 1 | $199.34 | -6.18% |
| 200 SMA | $189.19 | -10.92% |
| 50 EMA | $207.41 | -2.39% |
| 10 EMA | $209.54 | -1.39% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=87.51, Price > 200 SMA=YES | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=51.44, Price > 50 SMA=YES | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=12.67, 6M Low=5.37, No squeeze | NO SETUP |
| MA Crossover | PASS | 10 EMA > 50 EMA=YES, Pullback zone=YES, Above 10 EMA=YES | SETUP CONFIRMED |
| VIX Fear | N/A | N/A | N/A |

### Suggested Parameters (if setup confirmed)
| Parameter | Value |
|-----------|-------|
| Entry | $212.50 |
| Stop Loss | $200.51 |
| Take Profit | $232.01 |
| R:R Ratio | 1.63:1 |

### Decision
**SETUP CONFIRMED — MA Crossover**

Price is in pullback zone (within 1.0% of 10 EMA at $209.54), bouncing above 10 EMA with RSI(14)=51.4 confirming non-bearish territory. 10 EMA > 50 EMA bullish alignment intact. R:R ratio of 1.63:1 exceeds 1.5:1 minimum. Volume is weak (0.39x) — acceptable for this structure but requires tight risk management.

---

## Ticker: LRCX

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $390.13 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.55x |
| ATR(14) | $21.31 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $393.07 | +0.75% |
| Support 1 | $263.71 | -32.36% |
| 200 SMA | $205.69 | -47.27% |
| 50 EMA | $289.36 | -25.84% |
| 10 EMA | $345.50 | -11.44% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=96.7, Price > 200 SMA=YES | NO SETUP |
| MACD + RSI | PASS (R:R FAIL) | MACD cross=YES, RSI(14)=72.89, Price > 50 SMA=YES | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=34.41, 6M Low=11.03, Breakout=YES but no squeeze | NO SETUP |
| MA Crossover | FAIL | EMA10 > EMA50=YES, Pullback zone=NO | NO SETUP |
| VIX Fear | N/A | N/A | N/A |

### Decision
**NO SETUP**

MACD + RSI triggered bullish crossover with RSI(14)=72.89 in valid range and price above 50 EMA. However, pre-computed R:R ratio is 0.09:1, which **FAILS** the minimum 1.0:1 requirement. Risk ($31.96/share) vastly exceeds reward ($2.94/share) — take profit at resistance is too tight relative to stop loss placement. This setup is mathematically invalid for trade execution.

---

## Ticker: META

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $599.90 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.47x |
| ATR(14) | $19.65 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $643.00 | +7.18% |
| Support 1 | $557.01 | -7.15% |
| 200 SMA | $656.70 | +9.48% |
| 50 EMA | $622.34 | +3.73% |
| 10 EMA | $590.10 | -1.64% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=89.38, Price < 200 SMA=YES | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=48.53, Price < 50 SMA=YES | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=13.66, 6M Low=4.12, No squeeze | NO SETUP |
| MA Crossover | FAIL | EMA10 < EMA50=BEARISH alignment, Invalid | NO SETUP |
| VIX Fear | N/A | N/A | N/A |

### Decision
**NO SETUP**

Price is below 200 SMA ($656.70) and below 50 EMA ($622.34). 10 EMA < 50 EMA creates bearish MA alignment. MACD histogram is negative (-2.55). No strategy parameters are satisfied. Stock is in correction phase; no mean reversion or momentum setups present.

---

## Ticker: ROKU

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $142.56 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 4.02x |
| ATR(14) | $6.79 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $148.88 | +4.43% |
| Support 1 | $115.00 | -19.31% |
| 200 SMA | $104.43 | -26.78% |
| 50 EMA | $120.16 | -15.72% |
| 10 EMA | $129.32 | -9.27% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=87.4, Price > 200 SMA=YES | NO SETUP |
| MACD + RSI | PASS (R:R FAIL) | MACD cross=YES, RSI(14)=67.64, Price > 50 SMA=YES, Vol=CONFIRMS | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=21.04, 6M Low=5.88, Breakout=YES but no squeeze | NO SETUP |
| MA Crossover | FAIL | EMA10 > EMA50=YES, Pullback zone=NO, Price extended above | NO SETUP |
| VIX Fear | N/A | N/A | N/A |

### Decision
**NO SETUP**

MACD + RSI triggered: bullish crossover with RSI(14)=67.64 (valid range), price above 50 EMA, and **strong volume confirmation (4.02x)**. However, pre-computed R:R ratio is 0.62:1, which **FAILS** the minimum 1.0:1 requirement. Risk ($10.18/share) exceeds reward ($6.32/share). Price is extended above 10 EMA (no pullback zone) — this is a late-stage momentum move with unfavorable risk geometry. Setup is invalid.

---

## Ticker: MRVL

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $299.40 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.41x |
| ATR(14) | $25.92 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $324.20 | +8.27% |
| Support 1 | $162.85 | -45.57% |
| 200 SMA | $109.58 | -63.41% |
| 50 EMA | $186.84 | -37.60% |
| 10 EMA | $271.22 | -9.40% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=86.1, Price > 200 SMA=YES | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(14)=66.31, Price > 50 SMA=YES | NO SETUP |
| Bollinger Squeeze | FAIL | Bandwidth=78.85, 6M Low=10.06, No squeeze (elevated volatility) | NO SETUP |
| MA Crossover | FAIL | EMA10 > EMA50=YES, Pullback zone=NO, Price extended | NO SETUP |
| VIX Fear | N/A | N/A | N/A |

### Decision
**NO SETUP**

Price is extended well above 10 EMA ($271.22) with no pullback zone. MACD histogram is positive (1.70) but line (31.49) has not crossed signal (29.79) — no crossover trigger. RSI(14)=66.31 is strong but momentum structure lacks entry point. Bollinger Bandwidth (78.85) is elevated, indicating volatility expansion without compression setup. No strategy conditions met.

---

## Ticker: GE

### Price Data
| Metric | Value |
|--------|-------|
| Current Price | $345.73 |
| 20-Day Avg Volume | — |
| Today's Volume | — |
| Relative Volume | 0.36x |
| ATR(14) | $10.57 |

### Key Levels
| Level | Price | Distance |
|-------|-------|----------|
| Resistance 1 | $348.90 | +0.92% |
| Support 1 | $282.04 | -18.43% |
| 200 SMA | $303.78 | -12.15% |
| 50 EMA | $304.18 | -12.00% |
| 10 EMA | $328.77 | -4.90% |

### Strategy Scorecard
| Strategy | Status | Key Values | Verdict |
|----------|--------|------------|---------|
| Connors RSI(2) | FAIL | RSI(2)=90.43, Price > 200 SMA=YES | NO SETUP |
| MACD + RSI | FAIL | MACD cross=NO, RSI(