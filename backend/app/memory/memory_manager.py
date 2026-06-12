from __future__ import annotations

import json
import os
import uuid
from pathlib import Path
from typing import Any, Dict


BASE = Path(__file__).resolve().parent


class MemoryManager:
    """Simple filesystem-backed memory manager for Phase C."""

    def __init__(self, root: Path | None = None):
        self.root = (root or BASE / "memory").resolve()
        self._ensure_dirs()

    def _ensure_dirs(self) -> None:
        for sub in (
            "winners",
            "failures",
            "patterns",
            "strategies",
            "regimes",
            "sessions",
            "statistics",
            "evidence",
        ):
            p = self.root / sub
            p.mkdir(parents=True, exist_ok=True)

    def _write(self, subdir: str, data: Dict[str, Any]) -> str:
        fname = f"{uuid.uuid4().hex}.json"
        path = self.root / subdir / fname
        path.write_text(json.dumps(data, default=str, ensure_ascii=False))
        return str(path)

    def save_winner(self, data: Dict[str, Any]) -> str:
        return self._write("winners", data)

    def save_failure(self, data: Dict[str, Any]) -> str:
        return self._write("failures", data)

    def save_pattern(self, data: Dict[str, Any]) -> str:
        return self._write("patterns", data)

    def save_strategy(self, data: Dict[str, Any]) -> str:
        return self._write("strategies", data)

    def save_regime(self, data: Dict[str, Any]) -> str:
        return self._write("regimes", data)

    def save_session(self, data: Dict[str, Any]) -> str:
        return self._write("sessions", data)

    def save_statistics(self, data: Dict[str, Any]) -> str:
        return self._write("statistics", data)

    def save_evidence(self, data: Dict[str, Any]) -> str:
        return self._write("evidence", data)

    def list_entries(self, subdir: str) -> list[str]:
        p = self.root / subdir
        if not p.exists():
            return []
        return [str(x) for x in p.glob("*.json")]

    def load(self, path: str) -> Dict[str, Any]:
        return json.loads(Path(path).read_text())
