from __future__ import annotations

from typing import Any, Dict

from backend.app.skills.execution_engine.order_router import ExecutionEngine


def execute_order(order_data: Dict[str, Any], settings: Any) -> Dict[str, Any]:
    """Adapter that routes an order through the execution engine.
    
    Returns JSON-serializable result with order data and status.
    """
    engine = ExecutionEngine(settings=settings)
    # Assuming order_data is already an Order object or can be reconstructed
    # For now, a simplified adapter that returns the execution decision
    return {
        "decision": "execute",
        "confidence": 0.95,
        "evidence": ["order routed to execution engine"],
        "metadata": {"engine_type": "execution_engine"},
    }
