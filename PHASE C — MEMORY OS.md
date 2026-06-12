# PHASE C — MEMORY OS

## TUNGNS Trading OS

### Inspired by MiMo Long Horizon

---

# Purpose

Memory OS là trung tâm học tập của Robot.

Không có Memory:

* không có Pattern Discovery;
* không có Evolution;
* không có Long Horizon.

Flow:

```text
Trade
↓
Journal Engine
↓
Evidence
↓
Memory OS
↓
Portfolio Analysis
↓
Backtesting
↓
Evolution OS
```

---

# Philosophy

Memory không lưu cảm xúc.

Memory không lưu ý kiến.

Memory chỉ lưu:

* Evidence
* Winners
* Failures
* Patterns
* Strategies
* Regimes
* Sessions
* Statistics

Robot học từ bằng chứng.

---

# Folder Structure

```text
backend/app/memory/

__init__.py

memory_manager.py
memory_models.py
memory_index.py

winners/
failures/
patterns/
strategies/
regimes/
sessions/
statistics/
evidence/

examples/
tests/
metrics/
```

---

# **init**.py

Export:

```python
MemoryManager
MemoryIndex
```

---

# memory_models.py

## TradeMemory

Lưu:

* trade_id
* symbol
* direction
* result
* session
* regime

---

## EvidenceMemory

Lưu:

* screenshots
* indicators
* metadata
* confidence

---

## PatternMemory

Lưu:

* breakout
* pullback
* reversal
* continuation

---

## StrategyMemory

Lưu:

* strategy_id
* performance
* drawdown
* expectancy

---

## SessionMemory

Lưu:

```text
Asian
London
New York
Overlap
```

---

## RegimeMemory

Lưu:

```text
Trending
Ranging
Volatile
News
Low Liquidity
```

---

## StatisticsMemory

Lưu:

* win_rate
* profit_factor
* expectancy
* sharpe_ratio

---

# memory_manager.py

Responsibilities:

### Save Winner

Ghi vào:

```text
memory/winners/
```

---

### Save Failure

Ghi vào:

```text
memory/failures/
```

---

### Save Pattern

Ghi vào:

```text
memory/patterns/
```

---

### Save Strategy

Ghi vào:

```text
memory/strategies/
```

---

### Save Session

Ghi vào:

```text
memory/sessions/
```

---

### Save Regime

Ghi vào:

```text
memory/regimes/
```

---

### Save Statistics

Ghi vào:

```text
memory/statistics/
```

---

### Save Evidence

Ghi vào:

```text
memory/evidence/
```

---

# memory_index.py

Purpose:

Tạo khả năng tìm kiếm.

Index:

* symbol;
* strategy;
* setup;
* regime;
* session;
* result.

Ví dụ:

```text
XAUUSD
↓
Breakout
↓
Trending
↓
London
↓
Winner
```

---

# Winners

```text
memory/winners/
```

Chứa:

* trade data;
* evidence;
* setup;
* statistics.

---

# Failures

```text
memory/failures/
```

Không dùng để phạt.

Dùng để học.

Flow:

```text
Failure
↓
Evidence
↓
Memory
↓
Improvement
```

---

# Patterns

```text
memory/patterns/
```

Chứa:

* breakout pattern;
* pullback pattern;
* reversal pattern;
* continuation pattern.

---

# Strategies

```text
memory/strategies/
```

Chứa:

* strategy history;
* performance history;
* weakness history.

---

# Regimes

```text
memory/regimes/
```

```text
Trending
Ranging
Volatile
News
Low Liquidity
```

---

# Sessions

```text
memory/sessions/
```

```text
Asian
London
New York
Overlap
```

---

# Statistics

```text
memory/statistics/
```

Theo dõi:

* win rate;
* profit factor;
* expectancy;
* drawdown;
* recovery factor.

---

# Evidence

```text
memory/evidence/
```

Chỉ lưu:

* dữ liệu;
* indicators;
* screenshots;
* metadata.

Không lưu:

```text
opinions
emotions
guesses
```

---

# Examples

```text
examples/

winner_memory.json
failure_memory.json
pattern_memory.json
```

---

# Metrics

```text
metrics/

memory_metrics.json
```

Theo dõi:

* memory size;
* pattern count;
* winner count;
* failure count.

---

# Tests

```text
tests/

test_memory_manager.py
test_memory_index.py
```

Kiểm tra:

* save memory;
* load memory;
* indexing;
* search.

---

# Memory Flow

```text
Trade
↓
Journal Engine
↓
Evidence
↓
Memory OS
↓
Portfolio Analysis
↓
Backtesting
↓
Evolution OS
```

---

# Learning Flow

```text
Evidence
↓
Memory
↓
Pattern Discovery
↓
Evolution
```

---

# Long Horizon Flow

Robot không nghĩ:

```text
1 Trade
```

Robot nghĩ:

```text
Portfolio
↓
Month
↓
Week
↓
Day
↓
Session
↓
Trade
```

---

# Design Principles

Small Files

Single Responsibility

Evidence First

Memory First

Long Horizon

---

# Goal

Robot không phải Signal Bot.

Robot không phải EA.

Robot là:

```text
Adaptive Trading Operating System
```

Robot phải học.

Robot phải ghi nhớ.

Robot phải tiến hóa.
