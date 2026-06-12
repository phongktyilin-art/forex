# TUNGNS Trading OS

### Adaptive Trading Operating System

### Inspired by MiMo Long Horizon

---

# Vision

Robot không chỉ giao dịch.

Robot phải:

* quan sát;
* suy luận;
* lập kế hoạch;
* thực thi;
* ghi nhớ;
* học hỏi;
* tiến hóa.

Mục tiêu cuối cùng không phải tạo ra nhiều lệnh hơn.

Mục tiêu là tạo ra một hệ thống có khả năng tồn tại và phát triển lâu dài.

```text
Survival
↓
Consistency
↓
Compounding
↓
Longevity
↓
Evolution
```

---

# Core Philosophy

Trading không phải bài toán dự đoán.

Trading là bài toán quản lý xác suất.

Robot không cố đoán tương lai.

Robot phản ứng với bằng chứng.

Robot không tối đa hóa lợi nhuận ngắn hạn.

Robot tối ưu:

* xác suất sống sót;
* drawdown thấp;
* khả năng phục hồi;
* tăng trưởng dài hạn.

---

# Long Horizon Thinking

Không suy nghĩ:

```text
1 Trade = 1 Decision
```

Robot phải suy nghĩ:

```text
Portfolio
↓
Quarter
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

Mỗi lệnh chỉ là một phần nhỏ trong hành trình dài hạn.

---

# Capability Lifecycle

Mọi capability đều tuân theo:

```text
Observe
↓
Think
↓
Plan
↓
Execute
↓
Review
↓
Store Evidence
↓
Learn
↓
Evolve
```

Không được bỏ qua bước Evidence.

---

# Architecture

```text
Identity
↓
Skill Registry
↓
Memory OS
↓
Governance OS
↓
Evolution OS
↓
Trading OS
```

---

# Agent Philosophy

Agent không chứa logic.

Agent chỉ điều phối.

```text
Market Agent
Signal Agent
Risk Agent
Execution Agent
Journal Agent
Evolution Agent
```

Năng lực thực sự nằm trong:

```text
skills/
memory/
```

---

# Skills First

Một skill chỉ làm một nhiệm vụ.

Ví dụ:

```text
market-analysis
bias-engine
setup-detection
risk-engine
execution-engine
journal-engine
portfolio-analysis
backtesting
```

Mỗi skill phải có:

```text
skill.md
config.json
examples/
tests/
metrics/
```

---

# Memory First

Robot phải nhớ.

Memory không lưu hội thoại.

Memory chỉ lưu:

* evidence;
* winners;
* failures;
* statistics;
* patterns;
* strategies.

```text
Trade
↓
Evidence
↓
Memory
↓
Pattern
↓
Evolution
```

---

# Evidence First

Không có bằng chứng:

* không được học;
* không được tiến hóa;
* không được thay đổi chiến lược.

Evidence luôn quan trọng hơn cảm xúc.

---

# Governance First

Không có chiến lược nào được phép phá vỡ quản trị rủi ro.

Governance luôn đứng trên Signal.

```text
Signal
↓
Risk Rules
↓
Execution
```

---

# Risk Philosophy

Robot không chỉ quản lý:

* SL;
* TP.

Robot phải quản lý:

* Daily Risk;
* Weekly Risk;
* Portfolio Risk;
* Correlation Risk;
* Exposure Risk;
* Drawdown Risk;
* Consecutive Loss Risk.

Ưu tiên:

```text
Capital Protection
↓
Survival
↓
Profit
```

---

# Market Regime Intelligence

Robot phải phân loại thị trường:

```text
Trending
Ranging
Volatile
News
Low Liquidity
```

Mỗi regime kích hoạt skill khác nhau.

Không tồn tại một chiến lược thắng mọi thị trường.

---

# Multi-Timeframe Intelligence

Robot không được nhìn một timeframe duy nhất.

```text
HTF Context
↓
Structure
↓
Entry Timeframe
↓
Execution
```

---

# Portfolio Intelligence

Robot không đánh giá từng lệnh riêng lẻ.

Robot đánh giá:

* toàn bộ danh mục;
* correlation;
* exposure;
* risk concentration.

---

# Journal Intelligence

Mọi lệnh phải để lại:

```text
Market State
Setup
Risk
Entry
Exit
Result
Emotion
Evidence
```

Journal là nguồn dữ liệu của Evolution.

---

# Backtesting Intelligence

Backtest không nhằm chứng minh chiến lược đúng.

Backtest nhằm tìm:

* điểm yếu;
* điều kiện thất bại;
* market regime phù hợp;
* drawdown thực tế.

---

# Hooks First

Mọi capability đều hỗ trợ:

```text
before_signal
after_signal

before_trade
after_trade

before_close
after_close
```

Hook cho phép mở rộng mà không phá vỡ hệ thống.

---

# Evolution Loop

```text
Capability
↓
Execution
↓
Evidence
↓
Memory
↓
Statistics
↓
Pattern Discovery
↓
Strategy Update
↓
Evolution
```

Robot phải ngày càng tốt hơn theo thời gian.

---

# Failure Recovery

Thua lỗ không phải lỗi.

---

## Patch Details

Danh sách các thay đổi thực tế đã triển khai trong repository (thêm / sửa / xóa):

**Added**:
- [backend/app/skills/portfolio_analysis/__init__.py](backend/app/skills/portfolio_analysis/__init__.py)
- [backend/app/skills/portfolio_analysis/portfolio_engine.py](backend/app/skills/portfolio_analysis/portfolio_engine.py)
- [backend/app/skills/portfolio_analysis/risk_matrix.py](backend/app/skills/portfolio_analysis/risk_matrix.py)
- [backend/app/skills/portfolio_analysis/skill.md](backend/app/skills/portfolio_analysis/skill.md)
- [backend/app/skills/portfolio_analysis/config.json](backend/app/skills/portfolio_analysis/config.json)
- [backend/app/skills/portfolio_analysis/examples/healthy_portfolio.json](backend/app/skills/portfolio_analysis/examples/healthy_portfolio.json)
- [backend/app/skills/portfolio_analysis/examples/over_exposure.json](backend/app/skills/portfolio_analysis/examples/over_exposure.json)
- [backend/app/skills/portfolio_analysis/examples/high_correlation.json](backend/app/skills/portfolio_analysis/examples/high_correlation.json)
- [backend/app/skills/portfolio_analysis/metrics/portfolio_metrics.json](backend/app/skills/portfolio_analysis/metrics/portfolio_metrics.json)
- [backend/app/skills/portfolio_analysis/tests/test_portfolio_analysis.py](backend/app/skills/portfolio_analysis/tests/test_portfolio_analysis.py)
- [backend/app/api/routes_portfolio.py](backend/app/api/routes_portfolio.py)
- [backend/app/api/examples/portfolio_demo.sh](backend/app/api/examples/portfolio_demo.sh)
- [backend/app/api/examples/README.md](backend/app/api/examples/README.md)

**Modified**:
- [backend/app/main.py](backend/app/main.py) — đăng ký router `portfolio_router`
- [backend/app/skills/portfolio_analysis/portfolio_engine.py](backend/app/skills/portfolio_analysis/portfolio_engine.py) — cải tiến diversification (HHI) và correlation (tính từ price series khi có)

**Removed**:
- Tài liệu: `TUNGNS_COPILOT_OS_V3_ARCHITECTURE.md`
- Tài liệu: `PATCH 01 — JOURNAL ENGINE.md`
- Tài liệu: `PATCH 02 — PORTFOLIO ANALYSIS.md`
- Tài liệu: `PATCH 03 — BACKTESTING.md`
- Tài liệu: `Phase B — Skill Registry.md`

---

Ghi chú: toàn bộ test backend đã chạy thành công sau thay đổi (`pytest` trên `backend` → 18 passed). Nếu bạn muốn, tôi có thể nhúng nội dung chi tiết (ví dụ `models.py`, `config.json`, `metrics` JSON) trực tiếp vào tài liệu này.

Không học từ thua lỗ mới là lỗi.

```text
Failure
↓
Evidence
↓
Pattern
↓
Memory
↓
Improvement
```

---

# Design Principles

Small Files

Single Responsibility

Skills First

Memory First

Evidence First

Hooks First

Governance First

Generate → Verify → Publish

---

# Ultimate Goal

Robot không phải EA.

Robot không phải Signal Bot.

Robot là:

```text
Adaptive Trading Operating System
```

Robot không chỉ giao dịch.

Robot phải học.

Robot phải tiến hóa.

Robot phải tồn tại lâu dài.
