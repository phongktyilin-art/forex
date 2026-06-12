"""Schemas for risk management results."""

from dataclasses import dataclass


@dataclass
class PositionSizeResult:
    size: float
    risk_amount: float


@dataclass
class RiskManagementRecommendation:
    suggested_size: float
    stop_loss: float
    take_profit: float
    risk_reward_ratio: float
