from typing import List

from skills.shared.skill_metadata import SkillIO, SkillMetadata


def calculate_exposure(positions: List[dict[str, float]], account_balance: float) -> float:
    """Calculate portfolio exposure as a percentage of account balance."""
    total_value = sum(abs(pos.get("value", 0.0)) for pos in positions)
    return total_value / account_balance if account_balance else 0.0


METADATA = SkillMetadata(
    name="skills.portfolio.exposure.calculate_exposure",
    description="Calculate portfolio exposure relative to account balance.",
    version="1.0.0",
    category="portfolio",
    inputs=[
        SkillIO(name="positions", description="Current open positions with market value.", data_type="List[dict]", required=True, example=[{"symbol": "EURUSD", "value": 10000.0}]),
        SkillIO(name="account_balance", description="Current trading account balance.", data_type="float", required=True, example=100000.0),
    ],
    outputs=[
        SkillIO(name="exposure_pct", description="Portfolio exposure as a fraction of account balance.", data_type="float", required=True, example=0.1),
    ],
    dependencies=[],
    examples=[
        {
            "input": {"positions": [{"symbol": "EURUSD", "value": 10000.0}], "account_balance": 100000.0},
            "output": 0.1,
        }
    ],
    tags=["portfolio", "exposure", "risk"],
)
