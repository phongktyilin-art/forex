"""Open order execution skill."""

from typing import Dict
from skills.shared.skill_metadata import SkillIO, SkillMetadata


def build_open_order(symbol: str, quantity: float, side: str, price: float = None) -> Dict[str, object]:
    return {
        "symbol": symbol,
        "quantity": quantity,
        "side": side,
        "type": "market" if price is None else "limit",
        "price": price,
    }

METADATA = SkillMetadata(
    name='skills.execution.open_order',
    description='Build an open order payload for market or limit order execution.',
    version='1.0.0',
    category='execution',
    inputs=[
        SkillIO(name='symbol', description='Trading symbol to open.', data_type='str', required=True, example='EURUSD'),
        SkillIO(name='quantity', description='Order quantity.', data_type='float', required=True, example=1.0),
        SkillIO(name='side', description='Order side to open.', data_type='str', required=True, example='buy'),
        SkillIO(name='price', description='Optional limit price to open with.', data_type='float', required=False, example=1.2345),
    ],
    outputs=[
        SkillIO(name='order_payload', description='Order payload for broker execution.', data_type='Dict[str, object]', required=True),
    ],
    dependencies=[],
    examples=[{'input': {'symbol': 'EURUSD', 'quantity': 1.0, 'side': 'buy'}, 'output': {'symbol': 'EURUSD', 'quantity': 1.0, 'side': 'buy', 'type': 'market'}}],
    tags=['execution', 'open_order'],
)
