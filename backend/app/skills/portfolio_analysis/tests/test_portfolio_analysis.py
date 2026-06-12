from __future__ import annotations

from app.skills.portfolio_analysis import analyze_portfolio
from app.skills.portfolio_analysis.risk_matrix import assess_portfolio_risk


def test_analyze_portfolio_with_prices():
    portfolio = {
        "holdings": [
            {"symbol": "A", "value": 50000, "prices": [1, 1.1, 1.05, 1.08, 1.07]},
            {"symbol": "B", "value": 30000, "prices": [2, 2.05, 2.1, 2.08, 2.09]},
            {"symbol": "C", "value": 20000, "prices": [3, 2.9, 3.05, 3.1, 3.0]},
        ],
        "margin_usage": 0.15,
    }

    res = analyze_portfolio(portfolio)
    assert "health_score" in res
    assert "correlation_risk" in res
    assert "exposure_risk" in res
    assert "warnings" in res
    assert "metrics" in res
    assert "analysis" in res
    assert "risk_assessment" in res

    assert 0 <= res["health_score"] <= 100
    assert res["correlation_risk"] in ("LOW", "MEDIUM", "HIGH", "CRITICAL")
    assert res["exposure_risk"] in ("LOW", "MEDIUM", "HIGH", "CRITICAL")
    assert isinstance(res["warnings"], list)

    div_score = res["metrics"]["diversification_score"]
    assert 0.0 <= div_score <= 1.0

    corr_score = res["metrics"].get("correlation_score", 0.0)
    assert 0.0 <= corr_score <= 1.0


def test_analyze_portfolio_warnings_for_over_exposure():
    portfolio = {
        "holdings": [
            {"symbol": "EURUSD", "value": 90000},
            {"symbol": "USDJPY", "value": 5000},
            {"symbol": "GBPUSD", "value": 5000},
        ],
        "margin_usage": 0.9,
    }

    res = analyze_portfolio(portfolio)
    assert "High exposure to a single position" in res["warnings"]
    assert "Margin usage is elevated" in res["warnings"]
    assert res["risk_assessment"]["risk_level"] in ("HIGH", "CRITICAL")


def test_assess_portfolio_risk():
    metrics = {
        "concentration_score": 0.8,
        "margin_usage": 0.2,
        "correlation_score": 0.3,
        "exposure_score": 0.7,
    }
    r = assess_portfolio_risk(metrics)
    assert r["risk_level"] in ("LOW", "MEDIUM", "HIGH", "CRITICAL")
    assert 0.0 <= r["risk_score"] <= 1.0
    assert "dimensions" in r
    assert r["dimensions"]["exposure"] == 0.7
