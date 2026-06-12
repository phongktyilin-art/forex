from skills.shared.skill_metadata import SkillIO, SkillMetadata
"""Risk/reward ratio calculation skill."""


def calculate_risk_reward(stop_distance: float, profit_distance: float) -> float:
    if stop_distance <= 0:
        return 0.0
    return profit_distance / stop_distance

METADATA = SkillMetadata(
    name='skills.risk_management.risk_reward',
    description='Calculate the risk/reward ratio for a trade setup.',
    version='1.0.0',
    category='risk_management',
    inputs=[
        SkillIO(name='stop_distance', description='Distance from entry to stop loss.', data_type='float', required=True, example=0.01),
        SkillIO(name='profit_distance', description='Distance from entry to take profit.', data_type='float', required=True, example=0.02),
    ],
    outputs=[
        SkillIO(name='risk_reward_ratio', description='Calculated ratio of profit distance to stop distance.', data_type='float', required=True),
    ],
    dependencies=[],
    examples=[{'input': {'stop_distance': 0.01, 'profit_distance': 0.02}, 'output': 2.0}],
    tags=['risk_management', 'risk_reward'],
)
