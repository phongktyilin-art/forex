from __future__ import annotations

from backend.app.skills.optimization_engine.gene_search import BacktestOptimizer


class BacktestOptimizationAgent:
    """Deterministic enough fake optimizer for MVP API wiring.

    Replace with vectorbt/backtrader engine before using real capital.
    """

    def __init__(self):
        self.optimizer = BacktestOptimizer()

    def run(self, symbol: str, timeframe: str, step_range: list[float], x_range: list[int], risk_range: list[float]):
        return self.optimizer.run(symbol=symbol, timeframe=timeframe, step_range=step_range, x_range=x_range, risk_range=risk_range)
