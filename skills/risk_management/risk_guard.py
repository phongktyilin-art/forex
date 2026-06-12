"""Risk guard logic moved out of backend agent."""

from __future__ import annotations

from app.core.config import Settings
from app.core.models import MarketTick, RiskDecision, RobotState
from skills.shared.skill_metadata import SkillIO, SkillMetadata


def evaluate_risk(state: RobotState, settings: Settings, tick: MarketTick | None = None, api_latency_ms: int = 0) -> RiskDecision:
    reasons: list[str] = []
    action = "ALLOW"

    if state.drawdown_pct >= settings.max_drawdown_pct:
        reasons.append(f"drawdown {state.drawdown_pct:.2f}% >= max {settings.max_drawdown_pct:.2f}%")
        action = "FREEZE"
    if state.equity <= state.balance * (1 - settings.equity_guard_pct / 100):
        reasons.append("equity guard threshold breached")
        action = "CLOSE_RISKY_ORDERS"
    if state.margin_level_pct < settings.min_margin_level_pct:
        reasons.append("margin level below minimum")
        action = "REDUCE_EXPOSURE"
    if state.consecutive_loss >= settings.max_consecutive_loss:
        reasons.append("consecutive loss limit reached")
        action = "COOLDOWN"
    if tick is not None:
        spread_points = tick.spread / settings.tick_size
        if spread_points > settings.max_spread_points:
            reasons.append(f"spread {spread_points:.1f} points > max {settings.max_spread_points:.1f}")
            action = "PAUSE_NEW_ENTRY"
    if api_latency_ms > settings.max_api_latency_ms:
        reasons.append("api latency too high")
        action = "PAUSE_EXECUTION"

    return RiskDecision(allowed=len(reasons) == 0, action=action, reasons=reasons)

METADATA = SkillMetadata(
    name='skills.risk_management.risk_guard',
    description='Evaluate risk state and decide whether to allow, pause, or reduce exposure.',
    version='1.0.0',
    category='risk_management',
    inputs=[
        SkillIO(name='state', description='Current robot state.', data_type='RobotState', required=True, example=None),
        SkillIO(name='settings', description='Risk configuration settings.', data_type='Settings', required=True, example=None),
        SkillIO(name='tick', description='Optional latest market tick.', data_type='MarketTick', required=False, example=None),
        SkillIO(name='api_latency_ms', description='Current API latency in milliseconds.', data_type='int', required=False, example=50),
    ],
    outputs=[
        SkillIO(name='risk_decision', description='Risk decision object indicating whether execution is allowed.', data_type='RiskDecision', required=True),
    ],
    dependencies=['app.core.models.RobotState', 'app.core.models.Settings', 'app.core.models.MarketTick', 'app.core.models.RiskDecision'],
    examples=[{
        'input': {'state': 'robot state', 'settings': 'settings object'},
        'output': {'allowed': True, 'action': 'ALLOW', 'reasons': []},
    }],
    tags=['risk_management', 'risk_guard'],
)
