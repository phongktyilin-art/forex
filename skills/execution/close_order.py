"""Close order execution skill."""

from typing import Dict
from skills.shared.skill_metadata import SkillIO, SkillMetadata


def build_close_order(symbol: str, quantity: float, side: str) -> Dict[str, object]:
    return {
        "symbol": symbol,
        "quantity": quantity,
        "side": side,
        "type": "market",
    }

METADATA = SkillMetadata(
    name='skills.execution.close_order',
    description='Build a close order payload for market order execution.',
    version='1.0.0',
    category='execution',
    inputs=[
        SkillIO(name='symbol', description='Trading symbol to close.', data_type='str', required=True, example='EURUSD'),
        SkillIO(name='quantity', description='Quantity to close.', data_type='float', required=True, example=1.0),
        SkillIO(name='side', description='Order side for close operation.', data_type='str', required=True, example='sell'),
    ],
    outputs=[
        SkillIO(name='order_payload', description='Order payload ready for broker execution.', data_type='Dict[str, object]', required=True),
    ],
    dependencies=[],
    examples=[{'input': {'symbol': 'EURUSD', 'quantity': 1.0, 'side': 'sell'}, 'output': {'symbol': 'EURUSD', 'quantity': 1.0, 'side': 'sell', 'type': 'market'}}],
    tags=['execution', 'close_order'],
)
