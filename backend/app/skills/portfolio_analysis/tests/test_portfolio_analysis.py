from __future__ import annotations

import math

from app.skills.portfolio_analysis import analyze_portfolio
from app.skills.portfolio_analysis.risk_matrix import assess_portfolio_risk


def test_analyze_portfolio_with_prices():
    portfolio = {
        "holdings": [
            {"symbol": "A", "value": 50000, "prices": [1, 1.1, 1.05, 1.08, 1.07]},
            {"symbol": "B", "value": 30000, "prices": [2, 2.05, 2.1, 2.08, 2.09]},
            {"symbol": "C", "value": 20000, "prices": [3, 2.9, 3.05, 3.1, 3.0]},
        ]
    }

    res = analyze_portfolio(portfolio)
    assert "exposure" in res
    assert "diversification" in res
    assert "correlation" in res
    assert "concentration" in res

    # diversification score between 0 and 1
    div_score = res["diversification"]["diversification_score"]
    assert 0.0 <= div_score <= 1.0

    # correlation score between 0 and 1
    corr_score = res["correlation"].get("correlation_score", 0.0)
    assert 0.0 <= corr_score <= 1.0


def test_assess_portfolio_risk():
    metrics = {"concentration_score": 0.8, "margin_usage": 0.2}
    r = assess_portfolio_risk(metrics)
    assert r["risk_level"] in ("LOW", "MEDIUM", "HIGH", "CRITICAL")
    assert 0.0 <= r["risk_score"] <= 1.0
