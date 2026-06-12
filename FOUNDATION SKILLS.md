# PATCH PACKAGE — FOUNDATION SKILLS

## TUNGNS Trading OS

## Inspired by MiMo Long Horizon

---

# PATCH 01 — JOURNAL ENGINE

## Flow

```text
Trade
↓
Evidence
↓
Journal
```

## Folder

```text
backend/app/skills/journal-engine/

__init__.py
journal_engine.py
models.py

config.json
skill.md

examples/
tests/
metrics/
```

---

## journal_engine.py

Responsibilities:

* save trade record;
* save evidence;
* save setup;
* save session;
* save market regime;
* save result.

Không:

* execution;
* risk;
* signal.

---

## models.py

Models:

### TradeRecord

* trade_id
* symbol
* direction
* entry
* exit
* sl
* tp
* lot_size

### SetupRecord

* breakout
* pullback
* reversal
* continuation

### SessionRecord

* Asian
* London
* New York
* Overlap

### RegimeRecord

* Trending
* Ranging
* Volatile
* News
* Low Liquidity

### EvidenceRecord

* indicators
* screenshots
* metadata
* confidence

---

## metrics/

Theo dõi:

* win_rate
* average_rr
* expectancy
* profit_factor

---

## examples/

```text
winner.json
loser.json
breakeven.json
```

---

## tests/

* serialization
* validation
* save journal

---

# PATCH 02 — PORTFOLIO ANALYSIS

## Flow

```text
Portfolio
↓
Risk
↓
Capital Protection
```

## Folder

```text
backend/app/skills/portfolio-analysis/

__init__.py
portfolio_engine.py
risk_matrix.py

config.json
skill.md

examples/
tests/
metrics/
```

---

## portfolio_engine.py

Responsibilities:

* exposure analysis;
* correlation analysis;
* diversification analysis;
* concentration analysis.

---

## risk_matrix.py

Risk Levels:

```text
LOW
MEDIUM
HIGH
CRITICAL
```

---

## metrics/

Theo dõi:

* exposure_score
* correlation_score
* diversification_score
* margin_usage
* portfolio_health

---

## examples/

```text
healthy_portfolio.json
over_exposure.json
high_correlation.json
```

---

## tests/

* exposure calculation
* overlap detection
* correlation detection

---

# PATCH 03 — BACKTESTING

## Flow

```text
Strategy
↓
Backtest
↓
Weakness Discovery
```

## Folder

```text
backend/app/skills/backtesting/

__init__.py

backtest_engine.py
statistics.py
report_generator.py

config.json
skill.md

examples/
tests/
metrics/
```

---

## backtest_engine.py

Responsibilities:

* replay historical data;
* run strategy;
* collect statistics;
* detect weaknesses.

---

## statistics.py

Theo dõi:

* win_rate;
* expectancy;
* profit_factor;
* recovery_factor;
* sharpe_ratio;
* max_drawdown.

---

## report_generator.py

Sinh:

* summary;
* regime analysis;
* weakness analysis;
* recommendations.

---

## metrics/

Theo dõi:

* drawdown;
* profit_factor;
* expectancy;
* sharpe_ratio.

---

## examples/

```text
trend_strategy.json
breakout_strategy.json
mean_reversion.json
```

---

## tests/

* statistics
* drawdown
* report generation

---

# MEMORY INTEGRATION

Ba skill đều ghi vào:

```text
backend/app/memory/

winners/
failures/
patterns/
strategies/
```

---

# HOOKS

```text
before_trade
after_trade

before_close
after_close

after_backtest
```

---

# SKILL REGISTRY

```text
skills/

market-analysis/
setup-detection/
risk-engine/
execution-engine/
hedge-engine/
optimization-engine/

journal-engine/
portfolio-analysis/
backtesting/
```

---

# Long Horizon Flow

```text
Trade
↓
Journal
↓
Evidence
↓
Memory
↓
Portfolio Analysis
↓
Backtesting
↓
Evolution
```

---

# Goal

Robot không chỉ giao dịch.

Robot phải học và tiến hóa theo thời gian.
