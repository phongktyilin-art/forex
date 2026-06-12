from __future__ import annotations

import sys
from pathlib import Path


SKILL_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL_DIR))

from journal_engine import JournalEngine
from models import EvidenceRecord, JournalRecord


def _payload(result: str = "winner"):
    return {
        "market_state": {"symbol": "XAUUSD", "setup": "breakout", "regime": "Trending", "session": "London"},
        "trade_result": {
            "trade_id": "trade-1",
            "direction": "buy",
            "entry_price": 100.0,
            "exit_price": 110.0,
            "stop_loss": 95.0,
            "take_profit": 110.0,
            "lot_size": 0.1,
            "result": result,
            "evidence": [{"notes": ["confirmed breakout"], "confidence": 0.8, "metadata": {"source": "test"}}],
            "metadata": {"rr": 2.0},
        },
    }


def test_journal_record_serialization_round_trip():
    payload = _payload()
    engine = JournalEngine()
    record = engine.build_record(payload["market_state"], payload["trade_result"])
    restored = JournalRecord.from_dict(record.to_dict())

    assert restored.to_dict()["trade_id"] == "trade-1"
    assert restored.to_dict()["setup"] == "breakout"
    assert restored.to_dict()["result"] == "winner"


def test_journal_engine_saves_and_loads_records(tmp_path):
    payload = _payload()
    engine = JournalEngine(journal_path=tmp_path / "journal.jsonl", memory_root=tmp_path / "memory")

    saved = engine.record(payload["market_state"], payload["trade_result"])
    loaded = engine.load_records()

    assert saved["trade_id"] == "trade-1"
    assert len(loaded) == 1
    assert loaded[0]["symbol"] == "XAUUSD"
    assert (tmp_path / "memory" / "winners" / "trade-1.json").exists()
    assert (tmp_path / "memory" / "patterns" / "trade-1.json").exists()
    assert (tmp_path / "memory" / "strategies" / "trade-1.json").exists()


def test_evidence_rejects_raw_string_notes():
    evidence = EvidenceRecord(notes="emotional note", confidence=0.5)

    try:
        evidence.validate()
    except ValueError as exc:
        assert "structured" in str(exc)
    else:
        raise AssertionError("Expected evidence validation to reject string notes")
