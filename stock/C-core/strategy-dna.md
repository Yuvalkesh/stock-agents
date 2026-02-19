# Strategy DNA — 5 Verified Trading Strategies

## Strategy 1: Connors RSI(2) Mean Reversion

### Theory
When a stock in a long-term uptrend pulls back sharply (RSI(2) < 20), it tends to snap back. We buy the dip and exit on the first sign of recovery.

### Entry Conditions (ALL must be true)
- RSI(2) < 20 (short-term oversold)
- Price > 200-day SMA (confirming long-term uptrend)
- Stock is above $10 (liquidity filter)
- Relative volume > 1.0x (some activity)

### Exit Conditions
- Price closes above 5-day SMA (mean reversion complete)
- OR stop loss hit (ATR-based, 2x ATR(14) below entry)

### Parameters
| Parameter | Value |
|-----------|-------|
| RSI Period | 2 |
| RSI Threshold | < 20 |
| Trend Filter | 200 SMA |
| Exit Signal | Close > 5-day SMA |
| Stop Loss | 2x ATR(14) below entry |
| Typical Hold | 2-5 days |
| Historical Win Rate | ~75% |

### Best Market Conditions
- Trending markets with shallow pullbacks
- Low-to-moderate VIX (< 25)
- Strong sector support

### Worst Market Conditions
- Bear markets (price below 200 SMA = no trade)
- High volatility environments (VIX > 30)
- Earnings season for the specific stock

---

## Strategy 2: MACD + RSI Momentum

### Theory
When MACD crosses bullish AND RSI is in the "sweet spot" (35-75), the stock has momentum but isn't overbought. Ride the wave.

### Entry Conditions (ALL must be true)
- MACD line crosses above Signal line (bullish crossover)
- MACD histogram turns positive
- RSI(14) between 35 and 75 (momentum without overextension)
- Price > 50-day SMA (medium-term uptrend)
- Volume on crossover day > 20-day average volume

### Exit Conditions
- MACD line crosses below Signal line (bearish crossover)
- OR RSI(14) > 80 (overbought — take profits)
- OR stop loss hit (1.5x ATR(14) below entry)

### Parameters
| Parameter | Value |
|-----------|-------|
| MACD Fast | 12 |
| MACD Slow | 26 |
| MACD Signal | 9 |
| RSI Period | 14 |
| RSI Range | 35-75 |
| Trend Filter | 50 SMA |
| Stop Loss | 1.5x ATR(14) below entry |
| Typical Hold | 3-8 days |
| Historical Win Rate | ~73% |

### Best Market Conditions
- Early-to-mid trend moves
- Sector rotation into stock's sector
- Moderate volume environment

### Worst Market Conditions
- Choppy, range-bound markets
- Low volume / summer doldrums
- Conflicting macro signals

---

## Strategy 3: Bollinger Band Squeeze Breakout

### Theory
When Bollinger Bandwidth hits a 3-month low, volatility is compressed. When price breaks out of the upper band with volume, a significant move is starting.

### Entry Conditions (ALL must be true)
- Bollinger Bandwidth (20,2) at 3-month low (volatility squeeze)
- Price breaks above upper Bollinger Band
- Volume on breakout > 1.2x 20-day average volume
- RSI(14) > 50 (confirming bullish bias)

### Exit Conditions
- Price closes below middle Bollinger Band (20 SMA)
- OR price reaches 2x the bandwidth distance from entry
- OR stop loss hit (lower Bollinger Band at time of entry)

### Parameters
| Parameter | Value |
|-----------|-------|
| BB Period | 20 |
| BB Std Dev | 2 |
| Squeeze Lookback | 63 days (3 months) |
| Volume Threshold | 1.2x average |
| Stop Loss | Lower BB at entry |
| Typical Hold | 3-10 days |
| Historical Win Rate | ~65% |

### Best Market Conditions
- Pre-breakout consolidation periods
- Sector catalysts approaching
- Low overall market volatility transitioning higher

### Worst Market Conditions
- Already-extended moves (false breakouts)
- Market-wide volatility compression (everything squeezing)
- No clear catalyst

---

## Strategy 4: MA Crossover (10 EMA / 50 EMA)

### Theory
When the faster moving average (10 EMA) crosses above the slower (50 EMA), a new trend is forming. We wait for a pullback to the 10 EMA for a better entry.

### Entry Conditions (ALL must be true)
- 10 EMA crosses above 50 EMA (bullish crossover within last 10 days)
- Price pulls back to touch or approach 10 EMA (within 1.5% of 10 EMA)
- Price bounces — closes above 10 EMA after the pullback
- Volume on bounce > 1.0x average (some confirmation)
- RSI(14) > 45 (not in bearish territory)

### Exit Conditions
- 10 EMA crosses below 50 EMA (bearish crossover)
- OR price closes below 50 EMA (trend broken)
- OR stop loss hit (1.5x ATR(14) below entry or below 50 EMA, whichever is tighter)

### Parameters
| Parameter | Value |
|-----------|-------|
| Fast MA | 10 EMA |
| Slow MA | 50 EMA |
| Crossover Recency | Within 10 days |
| Pullback Zone | Within 1.5% of 10 EMA |
| Stop Loss | 1.5x ATR(14) or below 50 EMA |
| Typical Hold | 5-15 days |
| Historical Win Rate | ~60% |

### Best Market Conditions
- Trending markets (strong directional moves)
- Post-correction recovery periods
- Sector leadership emerging

### Worst Market Conditions
- Range-bound / choppy markets (whipsaws)
- High VIX environments (false signals)
- End-of-trend moves

---

## Strategy 5: VIX Buy-the-Fear

### Theory
When VIX spikes 15%+ above its 10-day SMA, panic is overdone. Buy SPY/QQQ and hold until fear subsides.

### Entry Conditions (ALL must be true)
- VIX closes 15% or more above its 10-day SMA
- S&P 500 is above its 200-day SMA (not a bear market)
- Only trade SPY or QQQ (liquid, diversified)
- No major systemic risk event (pandemic, financial crisis — use judgment)

### Exit Conditions
- VIX closes below its 10-day SMA (fear has subsided)
- OR stop loss hit (3% below entry for SPY, 4% below for QQQ)

### Parameters
| Parameter | Value |
|-----------|-------|
| VIX SMA Period | 10 days |
| VIX Spike Threshold | 15% above SMA |
| Eligible Tickers | SPY, QQQ only |
| Trend Filter | S&P 500 > 200 SMA |
| Stop Loss | 3% (SPY) / 4% (QQQ) |
| Typical Hold | 2-7 days |
| Historical Win Rate | ~80% |

### Best Market Conditions
- Sudden fear spikes in otherwise healthy markets
- Geopolitical scares without fundamental damage
- Seasonal volatility (October, pre-election)

### Worst Market Conditions
- Actual bear markets (below 200 SMA)
- Systemic crises (2008, COVID crash)
- Sustained high volatility regime (VIX consistently > 30)

---

## Strategy Selection by Market Regime

| Regime | Best Strategies | Avoid |
|--------|----------------|-------|
| RISK-ON (trending up) | MA Crossover, MACD+RSI | VIX Fear (no signal) |
| RISK-OFF (trending down) | Connors RSI(2) on pullbacks | MA Crossover (whipsaw) |
| HIGH VOLATILITY | VIX Fear, Connors RSI(2) | Bollinger Squeeze |
| LOW VOLATILITY | Bollinger Squeeze | VIX Fear (no signal) |
| MIXED/CHOPPY | Connors RSI(2) only | MA Crossover, MACD+RSI |
