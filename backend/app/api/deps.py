from __future__ import annotations

from fastapi import Request

from app.memory import MemoryManager


def get_memory_agent(request: Request) -> MemoryManager:
    """FastAPI dependency to retrieve the MemoryManager from app.state."""
    return request.app.state.memory_agent
