from __future__ import annotations

from app.core.config import Settings
from app.core.models import Order
from backend.app.skills.execution_engine.order_router import ExecutionEngine


class ExecutionAdapterAgent:
    def __init__(self, settings: Settings):
        self.settings = settings
        self.engine = ExecutionEngine(settings=settings)

    def execute(self, order: Order) -> Order:
        return self.engine.execute(order)
