from __future__ import annotations

from typing import Any

from fastapi import APIRouter
from pydantic import BaseModel, Field

from app.core.runtime import memory_agent
from memory.schemas import MemoryQuery, MemoryType

router = APIRouter(prefix="/api/v1/memory", tags=["memory"])


class MemorySaveRequest(BaseModel):
    kind: str = Field(default="generic", description="Type of memory record")
    content: dict[str, Any] = Field(default_factory=dict)
    memory_type: MemoryType = Field(default=MemoryType.LONG_TERM)
    tags: list[str] = Field(default_factory=list)


class TradeContextRequest(BaseModel):
    symbol: str
    timeframe: str
    trade_context: dict[str, Any]
    tags: list[str] = Field(default_factory=list)


class MemoryQueryRequest(BaseModel):
    query: str
    tags: list[str] = Field(default_factory=list)
    memory_type: MemoryType | None = None


class ShortTermMemoryRequest(BaseModel):
    content: dict[str, Any] = Field(default_factory=dict)
    tags: list[str] = Field(default_factory=list)


@router.post("/save")
def save_memory(record: MemorySaveRequest):
    saved = memory_agent.remember(
        {"kind": record.kind, "content": record.content},
        memory_type=record.memory_type,
        tags=record.tags,
    )
    return {"saved_memory": saved.to_dict()}


@router.post("/save-trade-context")
def save_trade_context_endpoint(payload: TradeContextRequest):
    saved = memory_agent.save_trade_context(
        symbol=payload.symbol,
        timeframe=payload.timeframe,
        trade_context=payload.trade_context,
        tags=payload.tags,
    )
    return {"saved_memory": saved.to_dict()}


@router.post("/query")
def query_memory(payload: MemoryQueryRequest):
    results = memory_agent.query(
        payload.query,
        tags=payload.tags,
        memory_type=payload.memory_type,
    )
    return {"results": [record.to_dict() for record in results]}


@router.get("/all")
def get_all_memory():
    records = memory_agent.load_memory()
    return {"records": [record.to_dict() for record in records]}


@router.post("/short-term/save")
def save_short_term_memory(payload: ShortTermMemoryRequest):
    record = memory_agent.save_short_term(payload.content, payload.tags)
    return {"saved_memory": record.to_dict()}


@router.get("/short-term/recent")
def recent_short_term_memory(limit: int = 10):
    records = memory_agent.recent_short_term(limit)
    return {"recent_memories": [record.to_dict() for record in records]}


@router.post("/market-insight")
def query_market_insight_endpoint(payload: MemoryQueryRequest):
    results = memory_agent.query_market_insight(payload.query, payload.tags)
    return {"market_insights": [record.to_dict() for record in results]}


class EvidenceRequest(BaseModel):
    content: dict[str, Any] = Field(default_factory=dict)
    tags: list[str] = Field(default_factory=list)


class FailureRequest(BaseModel):
    content: dict[str, Any] = Field(default_factory=dict)
    tags: list[str] = Field(default_factory=list)


@router.post("/evidence")
def save_evidence_endpoint(payload: EvidenceRequest):
    saved = memory_agent.save_evidence(payload.content, payload.tags)
    return {"saved_memory": saved.to_dict()}


@router.post("/failure")
def save_failure_endpoint(payload: FailureRequest):
    saved = memory_agent.save_failure(payload.content, payload.tags)
    return {"saved_memory": saved.to_dict()}
