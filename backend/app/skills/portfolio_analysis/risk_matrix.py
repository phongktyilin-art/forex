from __future__ import annotations

from enum import Enum
from typing import Dict, Any


class RiskLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


def assess_portfolio_risk(metrics: Dict[str, Any]) -> Dict[str, Any]:
    """Basic heuristic to assess portfolio risk from metrics.

    Expects metrics to contain `concentration_score` (0..1) and `margin_usage` (0..1) optionally.
    """
    concentration = float(metrics.get("concentration_score", 0))
    margin = float(metrics.get("margin_usage", 0))

    score = concentration * 0.7 + margin * 0.3
    if score < 0.25:
        level = RiskLevel.LOW
    elif score < 0.5:
        level = RiskLevel.MEDIUM
    elif score < 0.75:
        level = RiskLevel.HIGH
    else:
        level = RiskLevel.CRITICAL

    return {"risk_level": level.value, "risk_score": round(score, 4)}
