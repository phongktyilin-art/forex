"""Trade journaling skill."""

from typing import Dict
from skills.shared.skill_metadata import SkillIO, SkillMetadata


def save_trade_entry(entry: Dict[str, object], storage: list) -> None:
    storage.append(entry)

METADATA = SkillMetadata(
    name='skills.journal.save_trade',
    description='Save a trade entry into a journal storage list.',
    version='1.0.0',
    category='journal',
    inputs=[
        SkillIO(name='entry', description='Trade entry data to save.', data_type='Dict[str, object]', required=True, example={'symbol': 'EURUSD', 'profit': 10.0}),
        SkillIO(name='storage', description='Storage list for journal entries.', data_type='list', required=True, example=[]),
    ],
    outputs=[
        SkillIO(name='result', description='No explicit return value; storage list is appended.', data_type='None', required=False),
    ],
    dependencies=[],
    examples=[{
        'input': {'entry': {'symbol': 'EURUSD', 'profit': 10.0}, 'storage': []},
        'output': None,
    }],
    tags=['journal', 'persistence'],
)
