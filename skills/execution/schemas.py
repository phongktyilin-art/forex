"""Schemas for execution order payloads."""

from dataclasses import dataclass
from typing import Optional


@dataclass
class OrderPayload:
    symbol: str
    quantity: float
    side: str
    type: str
    price: Optional[float] = None
    order_id: Optional[str] = None
