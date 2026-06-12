"""Position sizing skill based on account equity and risk tolerance."""

from typing import Optional

from skills.shared.skill_metadata import SkillIO, SkillMetadata


def calculate_position_size(account_balance: float, risk_per_trade: float, stop_distance: float, price: float) -> Optional[float]:
    if account_balance <= 0 or risk_per_trade <= 0 or stop_distance <= 0 or price <= 0:
        return None

    risk_amount = account_balance * risk_per_trade
    position_size = risk_amount / (stop_distance * price)
    return max(position_size, 0.0)


METADATA = SkillMetadata(
    name="skills.risk_management.position_size.calculate_position_size",
    description="Calculate the position size based on account balance, risk ratio, stop loss distance, and price.",
    version="1.0.0",
    category="risk_management",
    inputs=[
        SkillIO(
            name="account_balance",
            description="The available trading capital.",
            data_type="float",
            required=True,
            example=10000.0,
        ),
        SkillIO(
            name="risk_per_trade",
            description="The fraction of capital to risk on the trade.",
            data_type="float",
            required=True,
            example=0.01,
        ),
        SkillIO(
            name="stop_distance",
            description="Stop loss distance in price units.",
            data_type="float",
            required=True,
            example=0.02,
        ),
        SkillIO(
            name="price",
            description="Current market price for the instrument.",
            data_type="float",
            required=True,
            example=1.25,
        ),
    ],
    outputs=[
        SkillIO(
            name="position_size",
            description="Calculated number of lots or units to trade.",
            data_type="Optional[float]",
            required=False,
        )
    ],
    dependencies=[],
    examples=[
        {
            "input": {"account_balance": 10000.0, "risk_per_trade": 0.01, "stop_distance": 0.02, "price": 1.25},
            "output": 4000.0,
        }
    ],
    tags=["risk_management", "position_sizing", "trade_risk"],
)
