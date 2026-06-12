from __future__ import annotations

from app.core.models import MarketTick
from skills.shared.mock_market import generate_tick, validate_independent_source


class MockMarketDataAgent:
    def __init__(self, start_price: float = 1.08000, spread: float = 0.00010):
        self.price = start_price
        self.spread = spread

    def fetch_tick(self, symbol: str) -> MarketTick:
        tick = generate_tick(symbol=symbol, start_price=self.price, spread=self.spread)
        self.price = tick.mid
        return tick

    def validate_independent_source(self, tick: MarketTick) -> bool:
        # MVP: simulated independent feed. Real version compares broker vs paid feed.
        return validate_independent_source(tick)
