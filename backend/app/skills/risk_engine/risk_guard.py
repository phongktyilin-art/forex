"""Risk guard skill wrapper that delegates to the canonical implementation.

This module provides a thin wrapper so the new `risk_engine` skill can reuse
the existing `skills.risk_management.risk_guard` implementation while living
under `backend.app.skills.risk_engine` for the Phase B migration.
"""
from __future__ import annotations

from skills.risk_management.risk_guard import evaluate_risk, METADATA as SOURCE_METADATA

# Re-export evaluate_risk under the new skill path
__all__ = ["evaluate_risk", "METADATA"]

METADATA = SOURCE_METADATA
