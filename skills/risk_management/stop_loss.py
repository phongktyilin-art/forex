from skills.shared.skill_metadata import SkillIO, SkillMetadata
"""Stop loss skill to calculate stop placement."""


def calculate_stop_loss(entry_price: float, volatility: float, multiplier: float = 1.5) -> float:
    return entry_price - abs(volatility * multiplier)

METADATA = SkillMetadata(
    name='skills.risk_management.stop_loss',
    description='Calculate a stop loss level based on entry price and volatility.',
    version='1.0.0',
    category='risk_management',
    inputs=[
        SkillIO(name='entry_price', description='Entry price for the trade.', data_type='float', required=True, example=1.2000),
        SkillIO(name='volatility', description='Estimated market volatility.', data_type='float', required=True, example=0.005),
        SkillIO(name='multiplier', description='Volatility multiplier for stop placement.', data_type='float', required=False, example=1.5),
    ],
    outputs=[
        SkillIO(name='stop_loss_price', description='Calculated stop loss price level.', data_type='float', required=True),
    ],
    dependencies=[],
    examples=[{'input': {'entry_price': 1.2000, 'volatility': 0.005}, 'output': 1.1925}],
    tags=['risk_management', 'stop_loss'],
)
