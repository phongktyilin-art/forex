"""Execution adapter decision logic moved out of the backend agent."""

from __future__ import annotations

from app.core.config import Settings
from app.core.models import OrderStatus
from skills.shared.skill_metadata import SkillIO, SkillMetadata


def determine_order_status(settings: Settings) -> OrderStatus:
    if settings.broker_mode != "mock" and not settings.allow_live_execution:
        return OrderStatus.REJECTED
    return OrderStatus.OPEN


def build_broker_order_id() -> str:
    from uuid import uuid4

    return f"MOCK-{uuid4()}"

METADATA = SkillMetadata(
    name='skills.execution.adapter',
    description='Build order status decisions and broker order identifiers based on execution settings.',
    version='1.0.0',
    category='execution',
    inputs=[
        SkillIO(name='settings', description='Runtime execution settings.', data_type='Settings', required=True, example=None),
    ],
    outputs=[
        SkillIO(name='order_status', description='Determined order status.', data_type='OrderStatus', required=True),
        SkillIO(name='broker_order_id', description='Generated broker order identifier.', data_type='str', required=True),
    ],
    dependencies=['app.core.config.Settings', 'app.core.models.OrderStatus'],
    examples=[{'input': {'settings': 'settings object'}, 'output': {'order_status': 'OrderStatus', 'broker_order_id': 'MOCK-...'}}],
    tags=['execution', 'adapter', 'order_routing'],
)
