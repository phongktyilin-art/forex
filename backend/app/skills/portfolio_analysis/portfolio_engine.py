from __future__ import annotations

from typing import Any, Dict, List


class PortfolioEngine:
    """Simple portfolio analysis engine (stub).

    Responsibilities:
    - exposure analysis
    - correlation analysis
    - diversification analysis
    - concentration analysis

    This is intentionally lightweight — replace with real implementations later.
    """

    def __init__(self, holdings: List[Dict[str, Any]] | None = None):
        self.holdings = holdings or []

    def exposure_analysis(self) -> Dict[str, float]:
        total = sum(h.get("value", 0) for h in self.holdings)
        exposures: Dict[str, float] = {}
        for h in self.holdings:
            sym = h.get("symbol", "UNKNOWN")
            exposures[sym] = round(h.get("value", 0) / total, 4) if total > 0 else 0.0
        return {"total_value": total, "exposures": exposures}

    def diversification_analysis(self) -> Dict[str, Any]:
        exposures = self.exposure_analysis().get("exposures", {})
        n_positions = len(exposures)
        concentration = max(exposures.values()) if exposures else 0.0
        # Use Herfindahl–Hirschman Index (HHI) as concentration measure; diversification = 1 - HHI
        hhi = sum((v ** 2) for v in exposures.values()) if exposures else 0.0
        diversification_score = round(1.0 - hhi, 4)
        return {
            "n_positions": n_positions,
            "concentration": round(concentration, 4),
            "hhi": round(hhi, 4),
            "diversification_score": diversification_score,
        }

    def correlation_analysis(self) -> Dict[str, Any]:
        # If holdings include historical `prices` series, compute correlation of returns
        try:
            import pandas as pd
            import numpy as np
        except Exception:
            return {"note": "pandas not available", "correlation_score": 0.0}

        price_series = {}
        for h in self.holdings:
            sym = h.get("symbol")
            prices = h.get("prices")
            if sym and prices and isinstance(prices, (list, tuple)) and len(prices) > 1:
                price_series[sym] = pd.Series(prices)

        if len(price_series) < 2:
            return {"note": "not enough price series to compute correlation", "correlation_score": 0.0}

        df = pd.DataFrame(price_series)
        # compute log returns (or simple pct_change) and correlation matrix
        returns = df.pct_change().dropna()
        if returns.empty:
            return {"note": "insufficient data after returns calculation", "correlation_score": 0.0}

        corr = returns.corr()
        # average absolute pairwise correlation (upper triangle)
        triu = corr.where(~np.tril(np.ones(corr.shape, dtype=bool)))
        abs_vals = triu.abs().values[np.triu_indices_from(triu.values, k=1)]
        correlation_score = float(round(float(abs_vals.mean()) if abs_vals.size else 0.0, 4))
        # convert matrix to nested dict for inspectability
        corr_dict = {col: corr[col].to_dict() for col in corr.columns}
        return {"correlation_matrix": corr_dict, "correlation_score": correlation_score}

    def concentration_analysis(self) -> Dict[str, Any]:
        exposures = self.exposure_analysis().get("exposures", {})
        concentration_score = round(max(exposures.values()) if exposures else 0.0, 4)
        return {"concentration_score": concentration_score}


def analyze_portfolio(portfolio: Dict[str, Any]) -> Dict[str, Any]:
    engine = PortfolioEngine(portfolio.get("holdings", []))
    return {
        "exposure": engine.exposure_analysis(),
        "diversification": engine.diversification_analysis(),
        "correlation": engine.correlation_analysis(),
        "concentration": engine.concentration_analysis(),
    }


# compatibility alias
run_portfolio_analysis = analyze_portfolio
