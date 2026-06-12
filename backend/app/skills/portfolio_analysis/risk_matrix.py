from __future__ import annotations

from enum import Enum
from typing import Dict, Any


class RiskLevel(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


def assess_portfolio_risk(metrics: Dict[str, Any]) -> Dict[str, Any]:
    """Heuristic risk assessment across portfolio dimensions."""
    concentration = max(0.0, min(1.0, float(metrics.get("concentration_score", 0.0))))
    correlation = max(0.0, min(1.0, float(metrics.get("correlation_score", 0.0))))
    exposure = max(0.0, min(1.0, float(metrics.get("exposure_score", 0.0))))
    margin = max(0.0, min(1.0, float(metrics.get("margin_usage", 0.0))))
    drawdown = max(0.0, min(1.0, float(metrics.get("drawdown", 0.0))))

    dimensions = [concentration, correlation, exposure, margin]
    if drawdown > 0.0:
        dimensions.append(drawdown)

    score = sum(dimensions) / len(dimensions) if dimensions else 0.0
    if score < 0.25:
        level = RiskLevel.LOW
    elif score < 0.5:
        level = RiskLevel.MEDIUM
    elif score < 0.75:
        level = RiskLevel.HIGH
    else:
        level = RiskLevel.CRITICAL

    return {
        "risk_level": level.value,
        "risk_score": round(score, 4),
        "dimensions": {
            "exposure": exposure,
            "concentration": concentration,
            "correlation": correlation,
            "margin_usage": margin,
            "drawdown": drawdown,
        },
    }
