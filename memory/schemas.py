from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class MemoryType(Enum):
    SHORT_TERM = "short_term"
    LONG_TERM = "long_term"
    EPHEMERAL = "ephemeral"


@dataclass
class MemoryRecord:
    memory_id: str
    created_at: str
    memory_type: MemoryType
    content: dict[str, Any]
    tags: list[str] = field(default_factory=list)

    def to_dict(self) -> dict[str, Any]:
        return {
            "memory_id": self.memory_id,
            "created_at": self.created_at,
            "memory_type": self.memory_type.value,
            "content": self.content,
            "tags": self.tags,
        }

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "MemoryRecord":
        return MemoryRecord(
            memory_id=data["memory_id"],
            created_at=data["created_at"],
            memory_type=MemoryType(data["memory_type"]),
            content=data["content"],
            tags=data.get("tags", []),
        )


@dataclass
class MemoryQuery:
    query: str
    tags: list[str] = field(default_factory=list)
    memory_type: MemoryType | None = None
