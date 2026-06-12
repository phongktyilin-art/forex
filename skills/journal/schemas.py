"""Schemas for trade journal entries."""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class TradeEntry:
    symbol: str
    entry_price: float
    exit_price: float
    quantity: float
    entry_time: datetime
    exit_time: datetime
    profit_loss: float
