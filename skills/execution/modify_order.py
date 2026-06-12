"""Modify order execution skill."""

from typing import Dict, Optional
from skills.shared.skill_metadata import SkillIO, SkillMetadata


def build_modify_order(order_id: str, new_price: Optional[float] = None, new_quantity: Optional[float] = None) -> Dict[str, object]:
    payload = {"order_id": order_id}
    if new_price is not None:
        payload["price"] = new_price
    if new_quantity is not None:
        payload["quantity"] = new_quantity
    return payload

METADATA = SkillMetadata(
    name='skills.execution.modify_order',
    description='Build a modify order payload for updating order price or quantity.',
    version='1.0.0',
    category='execution',
    inputs=[
        SkillIO(name='order_id', description='Identifier of the order to modify.', data_type='str', required=True, example='MOCK-1234'),
        SkillIO(name='new_price', description='New price for the order.', data_type='float', required=False, example=1.2345),
        SkillIO(name='new_quantity', description='New quantity for the order.', data_type='float', required=False, example=1.5),
    ],
    outputs=[
        SkillIO(name='payload', description='Order modification payload.', data_type='Dict[str, object]', required=True),
    ],
    dependencies=[],
    examples=[{'input': {'order_id': 'MOCK-1234', 'new_price': 1.23}, 'output': {'order_id': 'MOCK-1234', 'price': 1.23}}],
    tags=['execution', 'modify_order'],
)
