# PORTFOLIO ANALYSIS — COMPLETE MODULE

## Path

```text
backend/app/skills/portfolio-analysis/
```

---

# Folder Structure

```text
portfolio-analysis/

__init__.py

portfolio_engine.py
risk_matrix.py

config.json
skill.md

examples/
    healthy_portfolio.json
    over_exposure.json
    high_correlation.json

metrics/
    portfolio_metrics.json

tests/
    test_portfolio_analysis.py
```

---

# **init**.py

Exports:

```python
PortfolioEngine
RiskMatrix
```

---

# portfolio_engine.py

## Purpose

Đánh giá toàn bộ danh mục.

Không đánh giá từng lệnh riêng lẻ.

Flow:

```text
Portfolio
↓
Risk
↓
Capital Protection
```

---

## Responsibilities

### Exposure Analysis

Tính:

* total exposure;
* symbol exposure;
* currency exposure;
* margin usage.

---

### Correlation Analysis

Ví dụ:

```text
EURUSD ↔ GBPUSD
NAS100 ↔ SP500
XAUUSD ↔ USDJPY
```

---

### Diversification Analysis

Đánh giá:

* symbol overlap;
* sector overlap;
* concentration risk.

---

### Portfolio Health Score

Trả về:

```json
{
  "health_score": 87,
  "risk_level": "MEDIUM",
  "warnings": []
}
```

---

## Output Standard

```json
{
  "health_score": 87,

  "risk_level": "MEDIUM",

  "exposure_score": 72,

  "correlation_risk": "LOW",

  "concentration_risk": "MEDIUM",

  "warnings": []
}
```

---

# risk_matrix.py

## Risk Levels

```text
LOW
MEDIUM
HIGH
CRITICAL
```

---

## Exposure Risk

| Risk % | Level    |
| ------ | -------- |
| <1     | LOW      |
| 1–2    | MEDIUM   |
| 2–3    | HIGH     |
| >3     | CRITICAL |

---

## Correlation Risk

Theo:

* duplicated exposure;
* correlation coefficient.

---

## Concentration Risk

Theo:

* cùng symbol;
* cùng currency;
* cùng sector;
* cùng direction.

---

## Margin Risk

Theo:

* margin usage;
* free margin.

---

# config.json

```json
{
  "max_portfolio_risk": 3,
  "max_symbol_risk": 1,
  "max_correlation_score": 0.8,
  "max_margin_usage": 50
}
```

---

# skill.md

## Philosophy

Robot không tối ưu:

```text
Trade
↓
Profit
```

Robot tối ưu:

```text
Portfolio
↓
Risk
↓
Capital Protection
↓
Survival
↓
Compounding
```

---

## Principles

* Portfolio First
* Risk First
* Evidence First
* Long Horizon

---

# examples/

## healthy_portfolio.json

Danh mục phân tán tốt.

---

## over_exposure.json

Risk tập trung quá mức.

---

## high_correlation.json

Correlation cao giữa các vị thế.

---

# metrics/

## portfolio_metrics.json

Theo dõi:

```json
{
  "health_score": 0,
  "correlation_score": 0,
  "diversification_score": 0,
  "margin_usage": 0,
  "exposure_score": 0
}
```

---

# tests/

## test_portfolio_analysis.py

Kiểm tra:

### exposure calculation

### symbol overlap

### sector overlap

### correlation detection

### health score

### risk classification

---

# Integration

Skill này nhận dữ liệu từ:

```text
execution-engine
journal-engine
```

và cung cấp dữ liệu cho:

```text
Governance OS
Memory OS
Evolution OS
```

---

# Long Horizon Flow

```text
Trade
↓
Journal
↓
Portfolio Analysis
↓
Capital Protection
↓
Survival
↓
Compounding
```

---

# Status

Sau khi module này được thêm vào source code:

```text
Journal Engine ✓
Portfolio Analysis ✓
Backtesting ✓
```

Robot sẽ sẵn sàng chuyển sang:

```text
Phase C — Memory OS
```

theo kiến trúc MiMo Long Horizon.
