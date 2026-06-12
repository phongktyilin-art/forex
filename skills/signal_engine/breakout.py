"""Breakout signal generation skill."""

from typing import List
from skills.shared.skill_metadata import SkillIO, SkillMetadata


def detect_breakout(prices: List[float], lookback: int = 20) -> str:
    if len(prices) < lookback + 1:
        return "hold"

    recent = prices[-lookback:]
    high = max(recent)
    low = min(recent)
    current = prices[-1]

    if current > high:
        return "buy"
    if current < low:
        return "sell"
    return "hold"

METADATA = SkillMetadata(
    name='skills.signal_engine.breakout',
    description='Detect breakout signals when price moves beyond a recent high or low.',
    version='1.0.0',
    category='signal_engine',
    inputs=[
        SkillIO(name='prices', description='Price history for breakout detection.', data_type='List[float]', required=True, example=[1.0, 1.01, 1.02, 1.03]),
        SkillIO(name='lookback', description='Lookback window for breakout detection.', data_type='int', required=False, example=20),
    ],
    outputs=[
        SkillIO(name='signal', description='Breakout signal: buy, sell, or hold.', data_type='str', required=True),
    ],
    dependencies=[],
    examples=[{'input': {'prices': [1.0, 1.1, 1.2, 1.3], 'lookback': 3}, 'output': 'buy'}],
    tags=['signal_engine', 'breakout'],
)
