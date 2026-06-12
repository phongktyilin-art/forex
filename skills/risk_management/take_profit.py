from skills.shared.skill_metadata import SkillIO, SkillMetadata
"""Take profit skill to calculate profit target levels."""


def calculate_take_profit(entry_price: float, risk_distance: float, reward_ratio: float = 2.0) -> float:
    return entry_price + abs(risk_distance) * reward_ratio

METADATA = SkillMetadata(
    name='skills.risk_management.take_profit',
    description='Calculate a take profit target based on risk distance and reward ratio.',
    version='1.0.0',
    category='risk_management',
    inputs=[
        SkillIO(name='entry_price', description='Entry price for the trade.', data_type='float', required=True, example=1.2000),
        SkillIO(name='risk_distance', description='Distance from entry to stop loss.', data_type='float', required=True, example=0.01),
        SkillIO(name='reward_ratio', description='Desired reward-to-risk ratio.', data_type='float', required=False, example=2.0),
    ],
    outputs=[
        SkillIO(name='take_profit_price', description='Calculated take profit price level.', data_type='float', required=True),
    ],
    dependencies=[],
    examples=[{'input': {'entry_price': 1.2000, 'risk_distance': 0.01, 'reward_ratio': 2.0}, 'output': 1.2200}],
    tags=['risk_management', 'take_profit'],
)
