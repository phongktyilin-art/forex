from __future__ import annotations

from app.core.models import Order, RobotState
from backend.app.skills.sweep_engine.sweep_engine_module import SweepEngine


class SweepAgent:
    def __init__(self):
        self.engine = SweepEngine()

    def detect_orphans(self, state: RobotState, broker_orders: list[Order]) -> list[Order]:
        return self.engine.detect_orphans(state=state, broker_orders=broker_orders)

    def sweep(self, orphans: list[Order]) -> list[Order]:
        return self.engine.sweep(orphans)
