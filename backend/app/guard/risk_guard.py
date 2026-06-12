from __future__ import annotations

from app.core.config import Settings
from app.core.models import MarketTick, RiskDecision, RobotState
from backend.app.skills.risk_engine.risk_guard import evaluate_risk


class RiskGuardAgent:
    def __init__(self, settings: Settings):
        self.settings = settings

    def evaluate(self, state: RobotState, tick: MarketTick | None = None, api_latency_ms: int = 0) -> RiskDecision:
        return evaluate_risk(state=state, settings=self.settings, tick=tick, api_latency_ms=api_latency_ms)
