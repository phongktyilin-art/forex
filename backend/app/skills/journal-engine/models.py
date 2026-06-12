from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any
from uuid import uuid4


class SetupRecord(str, Enum):
    BREAKOUT = "breakout"
    PULLBACK = "pullback"
    REVERSAL = "reversal"
    CONTINUATION = "continuation"
    UNKNOWN = "unknown"


class RegimeRecord(str, Enum):
    TRENDING = "Trending"
    RANGING = "Ranging"
    VOLATILE = "Volatile"
    NEWS = "News"
    LOW_LIQUIDITY = "Low Liquidity"
    UNKNOWN = "Unknown"


class SessionRecord(str, Enum):
    ASIAN = "Asian"
    LONDON = "London"
    NEW_YORK = "New York"
    OVERLAP = "Overlap"
    UNKNOWN = "Unknown"


class ResultType(str, Enum):
    WINNER = "winner"
    LOSER = "loser"
    BREAKEVEN = "breakeven"
    MANUAL_CLOSE = "manual_close"
    PARTIAL_CLOSE = "partial_close"
    UNKNOWN = "unknown"


@dataclass
class EvidenceRecord:
    screenshots: list[str] = field(default_factory=list)
    indicators: dict[str, Any] = field(default_factory=dict)
    notes: list[str] = field(default_factory=list)
    confidence: float = 0.0
    metadata: dict[str, Any] = field(default_factory=dict)

    def validate(self) -> None:
        if isinstance(self.notes, str):
            raise ValueError("Evidence notes must be structured as a list, not raw text.")
        if not 0.0 <= float(self.confidence) <= 1.0:
            raise ValueError("Evidence confidence must be between 0 and 1.")

    def to_dict(self) -> dict[str, Any]:
        self.validate()
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "EvidenceRecord":
        notes = data.get("notes") or []
        return cls(
            screenshots=list(data.get("screenshots") or []),
            indicators=dict(data.get("indicators") or {}),
            notes=notes if isinstance(notes, list) else notes,
            confidence=float(data.get("confidence", 0.0) or 0.0),
            metadata=dict(data.get("metadata") or {}),
        )


@dataclass
class TradeRecord:
    trade_id: str
    symbol: str
    direction: str
    entry_price: float
    exit_price: float
    stop_loss: float | None = None
    take_profit: float | None = None
    lot_size: float = 0.0
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())

    @classmethod
    def from_payload(cls, market_state: dict[str, Any], trade_result: dict[str, Any]) -> "TradeRecord":
        return cls(
            trade_id=str(trade_result.get("trade_id") or uuid4()),
            symbol=str(trade_result.get("symbol") or market_state.get("symbol") or "UNKNOWN"),
            direction=str(trade_result.get("direction") or market_state.get("direction") or "unknown"),
            entry_price=float(trade_result.get("entry_price", trade_result.get("entry", 0.0)) or 0.0),
            exit_price=float(trade_result.get("exit_price", trade_result.get("exit", 0.0)) or 0.0),
            stop_loss=_optional_float(trade_result.get("stop_loss")),
            take_profit=_optional_float(trade_result.get("take_profit")),
            lot_size=float(trade_result.get("lot_size", trade_result.get("lot", 0.0)) or 0.0),
            timestamp=str(trade_result.get("timestamp") or datetime.now(timezone.utc).isoformat()),
        )

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)


@dataclass
class JournalRecord:
    trade: TradeRecord
    setup: SetupRecord = SetupRecord.UNKNOWN
    regime: RegimeRecord = RegimeRecord.UNKNOWN
    session: SessionRecord = SessionRecord.UNKNOWN
    result: ResultType = ResultType.UNKNOWN
    evidence: list[EvidenceRecord] = field(default_factory=list)
    metadata: dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "trade_id": self.trade.trade_id,
            "symbol": self.trade.symbol,
            "direction": self.trade.direction,
            "entry_price": self.trade.entry_price,
            "exit_price": self.trade.exit_price,
            "stop_loss": self.trade.stop_loss,
            "take_profit": self.trade.take_profit,
            "lot_size": self.trade.lot_size,
            "timestamp": self.trade.timestamp,
            "setup": self.setup.value,
            "regime": self.regime.value,
            "session": self.session.value,
            "result": self.result.value,
            "evidence": [item.to_dict() for item in self.evidence],
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "JournalRecord":
        trade = TradeRecord(
            trade_id=str(data["trade_id"]),
            symbol=str(data["symbol"]),
            direction=str(data.get("direction", "unknown")),
            entry_price=float(data.get("entry_price", 0.0) or 0.0),
            exit_price=float(data.get("exit_price", 0.0) or 0.0),
            stop_loss=_optional_float(data.get("stop_loss")),
            take_profit=_optional_float(data.get("take_profit")),
            lot_size=float(data.get("lot_size", 0.0) or 0.0),
            timestamp=str(data.get("timestamp") or datetime.now(timezone.utc).isoformat()),
        )
        return cls(
            trade=trade,
            setup=_enum_value(SetupRecord, data.get("setup"), SetupRecord.UNKNOWN),
            regime=_enum_value(RegimeRecord, data.get("regime"), RegimeRecord.UNKNOWN),
            session=_enum_value(SessionRecord, data.get("session"), SessionRecord.UNKNOWN),
            result=_enum_value(ResultType, data.get("result"), ResultType.UNKNOWN),
            evidence=[EvidenceRecord.from_dict(item) for item in data.get("evidence", [])],
            metadata=dict(data.get("metadata") or {}),
        )


def _optional_float(value: Any) -> float | None:
    if value is None or value == "":
        return None
    return float(value)


def _enum_value(enum_type: type[Enum], value: Any, default: Enum):
    try:
        return enum_type(value)
    except ValueError:
        return default
