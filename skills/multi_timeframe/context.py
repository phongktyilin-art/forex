from typing import Dict, List

from skills.shared.skill_metadata import SkillIO, SkillMetadata


def assemble_multi_timeframe_context(timeframes: List[str], data_by_timeframe: Dict[str, dict]) -> dict:
    """Assemble multi-timeframe market context for strategy decisions."""
    return {tf: data_by_timeframe.get(tf, {}) for tf in timeframes}


METADATA = SkillMetadata(
    name="skills.multi_timeframe.context.assemble_multi_timeframe_context",
    description="Assemble market context across multiple timeframes for higher-level decision making.",
    version="1.0.0",
    category="multi_timeframe",
    inputs=[
        SkillIO(name="timeframes", description="List of timeframes to include in the context.", data_type="List[str]", required=True, example=["1h", "4h", "1d"]),
        SkillIO(name="data_by_timeframe", description="Market data keyed by timeframe.", data_type="Dict[str, dict]", required=True, example={"1h": {"price": 1.12}, "4h": {"price": 1.14}}),
    ],
    outputs=[
        SkillIO(name="context", description="Multi-timeframe context dataset.", data_type="dict", required=True, example={"1h": {"price": 1.12}, "4h": {"price": 1.14}}),
    ],
    dependencies=[],
    examples=[
        {
            "input": {"timeframes": ["1h", "4h", "1d"], "data_by_timeframe": {"1h": {"price": 1.12}, "4h": {"price": 1.14}, "1d": {"price": 1.15}}},
            "output": {"1h": {"price": 1.12}, "4h": {"price": 1.14}, "1d": {"price": 1.15}},
        }
    ],
    tags=["multi_timeframe", "context", "intelligence"],
)
