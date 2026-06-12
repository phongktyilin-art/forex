"""Break of structure (BOS) signal generation skill."""

from typing import List
from skills.shared.skill_metadata import SkillIO, SkillMetadata


def detect_break_of_structure(highs: List[float], lows: List[float]) -> str:
    if len(highs) < 2 or len(lows) < 2:
        return "hold"

    if highs[-1] > highs[-2]:
        return "bullish"
    if lows[-1] < lows[-2]:
        return "bearish"
    return "hold"

METADATA = SkillMetadata(
    name='skills.signal_engine.bos',
    description='Detect breaks of market structure from highs and lows to classify trend direction.',
    version='1.0.0',
    category='signal_engine',
    inputs=[
        SkillIO(name='highs', description='Sequence of recent high prices.', data_type='List[float]', required=True, example=[1.2, 1.25, 1.3]),
        SkillIO(name='lows', description='Sequence of recent low prices.', data_type='List[float]', required=True, example=[1.1, 1.15, 1.18]),
    ],
    outputs=[
        SkillIO(name='signal', description='Structure break signal: bullish, bearish, or hold.', data_type='str', required=True),
    ],
    dependencies=[],
    examples=[{'input': {'highs': [1.2, 1.3], 'lows': [1.1, 1.18]}, 'output': 'bullish'}],
    tags=['signal_engine', 'structure_break'],
)
