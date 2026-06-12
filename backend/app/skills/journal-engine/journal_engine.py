from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from models import EvidenceRecord, JournalRecord, RegimeRecord, ResultType, SessionRecord, SetupRecord, TradeRecord


class JournalEngine:
    def __init__(self, journal_path: str | Path | None = None, memory_root: str | Path | None = None):
        skill_dir = Path(__file__).resolve().parent
        self.journal_path = Path(journal_path) if journal_path else skill_dir / "metrics" / "journal_records.jsonl"
        self.memory_root = Path(memory_root) if memory_root else skill_dir.parents[4] / "memory"

    def record(self, market_state: dict[str, Any], trade_result: dict[str, Any]) -> dict[str, Any]:
        record = self.build_record(market_state, trade_result)
        self.save_record(record)
        self.publish_memory(record)
        return record.to_dict()

    def build_record(self, market_state: dict[str, Any], trade_result: dict[str, Any]) -> JournalRecord:
        evidence_payload = trade_result.get("evidence") or market_state.get("evidence") or []
        if isinstance(evidence_payload, dict):
            evidence_payload = [evidence_payload]
        record = JournalRecord(
            trade=TradeRecord.from_payload(market_state, trade_result),
            setup=_setup(trade_result.get("setup") or market_state.get("setup")),
            regime=_regime(trade_result.get("regime") or market_state.get("regime")),
            session=_session(trade_result.get("session") or market_state.get("session")),
            result=_result(trade_result.get("result")),
            evidence=[EvidenceRecord.from_dict(item) for item in evidence_payload],
            metadata=dict(trade_result.get("metadata") or {}),
        )
        for evidence in record.evidence:
            evidence.validate()
        return record

    def save_record(self, record: JournalRecord) -> Path:
        self.journal_path.parent.mkdir(parents=True, exist_ok=True)
        with self.journal_path.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record.to_dict(), ensure_ascii=False) + "\n")
        return self.journal_path

    def load_records(self) -> list[dict[str, Any]]:
        if not self.journal_path.exists():
            return []
        records = []
        for line in self.journal_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                records.append(JournalRecord.from_dict(json.loads(line)).to_dict())
        return records

    def publish_memory(self, record: JournalRecord) -> None:
        payload = record.to_dict()
        self._write_memory("strategies", payload)
        if record.setup is not SetupRecord.UNKNOWN:
            self._write_memory("patterns", payload)
        if record.result is ResultType.WINNER:
            self._write_memory("winners", payload)
        elif record.result is ResultType.LOSER:
            self._write_memory("losers", payload)

    def _write_memory(self, folder: str, payload: dict[str, Any]) -> Path:
        destination = self.memory_root / folder
        destination.mkdir(parents=True, exist_ok=True)
        path = destination / f"{payload['trade_id']}.json"
        path.write_text(json.dumps({"kind": "journal_evidence", "content": payload}, indent=2), encoding="utf-8")
        return path


def record_trade(market_state: dict[str, Any], trade_result: dict[str, Any], journal_path: str | Path | None = None) -> dict[str, Any]:
    return JournalEngine(journal_path=journal_path).record(market_state, trade_result)


def _setup(value: Any) -> SetupRecord:
    try:
        return SetupRecord(str(value or "unknown").lower())
    except ValueError:
        return SetupRecord.UNKNOWN


def _regime(value: Any) -> RegimeRecord:
    normalized = str(value or "Unknown")
    for regime in RegimeRecord:
        if regime.value.lower() == normalized.lower():
            return regime
    return RegimeRecord.UNKNOWN


def _session(value: Any) -> SessionRecord:
    normalized = str(value or "Unknown")
    for session in SessionRecord:
        if session.value.lower() == normalized.lower():
            return session
    return SessionRecord.UNKNOWN


def _result(value: Any) -> ResultType:
    normalized = str(value or "unknown").lower().replace(" ", "_")
    try:
        return ResultType(normalized)
    except ValueError:
        return ResultType.UNKNOWN
