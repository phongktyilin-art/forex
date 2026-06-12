"""Signal generation using exponential moving average (EMA) crossovers."""

from typing import List

from skills.shared.skill_metadata import SkillIO, SkillMetadata


def calculate_ema(prices: List[float], period: int) -> List[float]:
    if not prices or period <= 0:
        return []

    alpha = 2.0 / (period + 1)
    ema_values = [prices[0]]
    for price in prices[1:]:
        ema_values.append(price * alpha + ema_values[-1] * (1 - alpha))
    return ema_values


def detect_ema_cross(short_ema: List[float], long_ema: List[float]) -> str:
    if len(short_ema) < 2 or len(long_ema) < 2:
        return "hold"

    if short_ema[-2] <= long_ema[-2] and short_ema[-1] > long_ema[-1]:
        return "buy"
    if short_ema[-2] >= long_ema[-2] and short_ema[-1] < long_ema[-1]:
        return "sell"
    return "hold"


METADATA = SkillMetadata(
    name="skills.signal_engine.ema_cross",
    description="Generate EMA values and detect EMA crossover signals.",
    version="1.0.0",
    category="signal_engine",
    inputs=[
        SkillIO(
            name="prices",
            description="Historical price series for EMA calculation.",
            data_type="List[float]",
            required=True,
            example=[1.0, 1.01, 1.02, 1.03],
        ),
        SkillIO(
            name="period",
            description="EMA lookback period.",
            data_type="int",
            required=True,
            example=14,
        ),
    ],
    outputs=[
        SkillIO(
            name="ema_values",
            description="Calculated EMA values.",
            data_type="List[float]",
            required=True,
            example=[1.0, 1.01, 1.02, 1.03],
        ),
        SkillIO(
            name="signal",
            description="Signal output from the EMA crossover rule.",
            data_type="str",
            required=True,
            example="buy",
        ),
    ],
    dependencies=[],
    examples=[
        {
            "input": {"prices": [1.0, 1.01, 1.02, 1.03], "period": 3},
            "output": "buy",
        }
    ],
    tags=["signal_engine", "ema", "trend"],
)
