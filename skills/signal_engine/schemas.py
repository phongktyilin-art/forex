"""Schemas for signal engine skill outputs."""

from dataclasses import dataclass
from enum import Enum


class SignalType(Enum):
    BUY = "buy"
    SELL = "sell"
    HOLD = "hold"
    BULLISH = "bullish"
    BEARISH = "bearish"


@dataclass
class SignalResult:
    signal: SignalType
    strength: float = 0.0
    metadata: dict = None
