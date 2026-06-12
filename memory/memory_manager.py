from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from uuid import uuid4

from memory.schemas import MemoryQuery, MemoryRecord, MemoryType


@dataclass
class MemoryManager:
    path: str
    short_term: list[MemoryRecord]

    def __init__(self, path: str):
        self.path = path
        self.short_term = []
        store_path = Path(path)
        store_path.parent.mkdir(parents=True, exist_ok=True)
        if not store_path.exists():
            store_path.write_text("[]", encoding="utf-8")

    def _read_store(self) -> list[MemoryRecord]:
        store_path = Path(self.path)
        if not store_path.exists():
            return []
        raw = json.loads(store_path.read_text(encoding="utf-8"))
        return [MemoryRecord.from_dict(item) for item in raw]

    def _write_store(self, records: list[MemoryRecord]) -> None:
        store_path = Path(self.path)
        store_path.parent.mkdir(parents=True, exist_ok=True)
        store_path.write_text(json.dumps([record.to_dict() for record in records], indent=2, default=str), encoding="utf-8")

    def _record(self, content: dict[str, Any], memory_type: MemoryType, tags: list[str] | None = None) -> MemoryRecord:
        return MemoryRecord(
            memory_id=str(uuid4()),
            created_at=datetime.now(timezone.utc).isoformat(),
            memory_type=memory_type,
            content=content,
            tags=tags or [],
        )

    def remember(self, content: dict[str, Any], memory_type: MemoryType = MemoryType.LONG_TERM, tags: list[str] | None = None) -> MemoryRecord:
        record = self._record(content, memory_type, tags)
        records = self._read_store()
        records.append(record)
        self._write_store(records)
        return record

    def save_winner(self, content: dict[str, Any], tags: list[str] | None = None) -> MemoryRecord:
        return self.remember(
            {"kind": "winner", "content": content},
            memory_type=MemoryType.LONG_TERM,
            tags=(tags or ["winner"]),
        )

    def save_failure(self, content: dict[str, Any], tags: list[str] | None = None) -> MemoryRecord:
        return self.remember(
            {"kind": "failure", "content": content},
            memory_type=MemoryType.LONG_TERM,
            tags=(tags or ["failure"]),
        )

    def save_evidence(self, content: dict[str, Any], tags: list[str] | None = None) -> MemoryRecord:
        return self.remember(
            {"kind": "evidence", "content": content},
            memory_type=MemoryType.LONG_TERM,
            tags=(tags or ["evidence"]),
        )

    def query_evidence(self, query_value: str, tags: list[str] | None = None) -> list[MemoryRecord]:
        return self.query(query_value, tags=(tags or ["evidence"]), memory_type=MemoryType.LONG_TERM)

    def save_strategy(self, content: dict[str, Any], tags: list[str] | None = None) -> MemoryRecord:
        return self.remember(
            {"kind": "strategy", "content": content},
            memory_type=MemoryType.LONG_TERM,
            tags=(tags or ["strategy"]),
        )

    def save_pattern(self, content: dict[str, Any], tags: list[str] | None = None) -> MemoryRecord:
        return self.remember(
            {"kind": "pattern", "content": content},
            memory_type=MemoryType.LONG_TERM,
            tags=(tags or ["pattern"]),
        )

    def save_short_term(self, content: dict[str, Any], tags: list[str] | None = None) -> MemoryRecord:
        record = self._record(content, MemoryType.SHORT_TERM, tags)
        self.short_term.append(record)
        return record

    def load_memory(self, memory_type: MemoryType | None = None) -> list[MemoryRecord]:
        records = self._read_store()
        if memory_type is None:
            return records
        return [record for record in records if record.memory_type is memory_type]

    def query(self, query_value: str, tags: list[str] | None = None, memory_type: MemoryType | None = None) -> list[MemoryRecord]:
        records = self.load_memory(memory_type)
        query_terms = [term.lower() for term in query_value.split() if term]
        tags = [tag.lower() for tag in (tags or [])]

        def matches(record: MemoryRecord) -> bool:
            searchable = f"{json.dumps(record.content, ensure_ascii=False).lower()} {' '.join(record.tags).lower()}"
            return all(term in searchable for term in query_terms) and all(tag in searchable for tag in tags)

        return [record for record in records if matches(record)]

    def recent_short_term(self, limit: int = 10) -> list[MemoryRecord]:
        return list(reversed(self.short_term[-limit:]))

    def save_trade_context(self, symbol: str, timeframe: str, trade_context: dict[str, Any], tags: list[str] | None = None) -> MemoryRecord:
        payload = {
            "kind": "trade_context",
            "symbol": symbol,
            "timeframe": timeframe,
            "saved_at": datetime.now(timezone.utc).isoformat(),
            "trade_context": trade_context,
        }
        return self.remember(
            payload,
            memory_type=MemoryType.LONG_TERM,
            tags=(tags or ["trade_context", symbol, timeframe]),
        )

    def query_market_insight(self, query_value: str, tags: list[str] | None = None) -> list[MemoryRecord]:
        return self.query(query_value, tags or ["market_insight"], MemoryType.LONG_TERM)
