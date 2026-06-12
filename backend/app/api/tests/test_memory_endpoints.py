from __future__ import annotations

from fastapi.testclient import TestClient

from backend.app.main import app
from memory.memory_manager import MemoryManager as FileMemoryManager


def test_save_evidence_and_failure_and_short_term(tmp_path):
    client = TestClient(app)
    # use isolated memory store for test
    store_path = tmp_path / "mem.json"
    client.app.state.memory_agent = FileMemoryManager(str(store_path))

    # evidence
    ev_payload = {"content": {"note": "evidence-note"}, "tags": ["test"]}
    r = client.post("/api/v1/memory/evidence", json=ev_payload)
    assert r.status_code == 200
    data = r.json()["saved_memory"]
    assert data["content"]["kind"] == "evidence"

    # failure
    fail_payload = {"content": {"reason": "bad-trade"}, "tags": ["test"]}
    r2 = client.post("/api/v1/memory/failure", json=fail_payload)
    assert r2.status_code == 200
    data2 = r2.json()["saved_memory"]
    assert data2["content"]["kind"] == "failure"

    # short term
    st_payload = {"content": {"temp": 1}, "tags": ["ephemeral"]}
    r3 = client.post("/api/v1/memory/short-term/save", json=st_payload)
    assert r3.status_code == 200
    data3 = r3.json()["saved_memory"]
    assert data3["memory_type"] == "short_term"
