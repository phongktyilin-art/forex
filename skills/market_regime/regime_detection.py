from typing import List

from skills.shared.skill_metadata import SkillIO, SkillMetadata


def detect_market_regime(prices: List[float], volume: List[float]) -> str:
    """Detect the current market regime based on price and volume behavior."""
    if len(prices) < 5 or len(volume) < 5:
        return "unknown"

    volatility = max(prices) - min(prices)
    avg_volume = sum(volume) / len(volume)
    latest_volume = volume[-1]

    if volatility > 0.02 and latest_volume > avg_volume * 1.5:
        return "volatile"
    if volatility < 0.005:
        return "ranging"
    if latest_volume < avg_volume * 0.5:
        return "low_liquidity"
    return "trending"


METADATA = SkillMetadata(
    name="skills.market_regime.regime_detection.detect_market_regime",
    description="Detect the current market regime for regime-specific strategy selection.",
    version="1.0.0",
    category="market_regime",
    inputs=[
        SkillIO(name="prices", description="Recent prices.", data_type="List[float]", required=True, example=[1.0, 1.01, 1.02, 1.03, 1.04]),
        SkillIO(name="volume", description="Recent volumes.", data_type="List[float]", required=True, example=[1000.0, 1200.0, 900.0, 1100.0, 950.0]),
    ],
    outputs=[
        SkillIO(name="regime", description="Detected market regime.", data_type="str", required=True, example="trending"),
    ],
    dependencies=[],
    examples=[
        {
            "input": {"prices": [1.0, 1.01, 1.02, 1.03, 1.04], "volume": [1000.0, 1100.0, 1200.0, 1000.0, 900.0]},
            "output": "trending",
        }
    ],
    tags=["market_regime", "regime_detection"],
)
