from __future__ import annotations

from pydantic import BaseModel, Field


class RiskRule(BaseModel):
    max_risk_per_trade: float = Field(default=1.0)
    max_daily_loss: float = Field(default=3.0)
    max_weekly_loss: float = Field(default=10.0)
    max_open_positions: int = Field(default=5)
    minimum_rr: float = Field(default=2.0)


class CapitalRule(BaseModel):
    starting_balance: float = Field(default=10000.0)
    max_lot_size: float = Field(default=1.0)
    compounding_enabled: bool = Field(default=True)
    capital_allocation: float = Field(default=100.0)


class PermissionRule(BaseModel):
    allow_live_trading: bool = Field(default=False)
    allow_news_trading: bool = Field(default=False)
    allow_scalping: bool = Field(default=True)
    allow_weekend_positions: bool = Field(default=False)
