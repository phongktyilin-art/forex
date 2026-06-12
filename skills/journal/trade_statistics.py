"""Trade statistics calculation skill."""

from typing import List
from skills.shared.skill_metadata import SkillIO, SkillMetadata


def calculate_win_rate(results: List[bool]) -> float:
    if not results:
        return 0.0
    return sum(1 for r in results if r) / len(results)


def average_return(returns: List[float]) -> float:
    if not returns:
        return 0.0
    return sum(returns) / len(returns)

METADATA = SkillMetadata(
    name='skills.journal.trade_statistics',
    description='Calculate trade statistics such as win rate and average return.',
    version='1.0.0',
    category='journal',
    inputs=[
        SkillIO(name='results', description='List of trade win/loss results.', data_type='List[bool]', required=True, example=[True, False, True]),
        SkillIO(name='returns', description='List of trade returns.', data_type='List[float]', required=False, example=[0.01, 0.02, -0.005]),
    ],
    outputs=[
        SkillIO(name='win_rate', description='Win rate across trades.', data_type='float', required=True),
        SkillIO(name='average_return', description='Average return across trades.', data_type='float', required=True),
    ],
    dependencies=[],
    examples=[{'input': {'results': [True, False, True], 'returns': [0.01, 0.02, -0.005]}, 'output': {'win_rate': 0.6667, 'average_return': 0.008333}}],
    tags=['journal', 'statistics'],
)
