from __future__ import annotations

from pathlib import Path
from typing import Any

from .schemas import CapitalRule, PermissionRule, RiskRule


class GovernanceManager:
    """Single entry point for Governance OS.

    GovernanceManager is the only component allowed to read rule files.
    """

    def __init__(self, rules_directory: str | Path | None = None):
        self.rules_directory = Path(rules_directory) if rules_directory else Path(__file__).resolve().parent
        self.risk_rules: RiskRule | None = None
        self.capital_rules: CapitalRule | None = None
        self.permission_rules: PermissionRule | None = None

    def load_rules(self) -> dict[str, RiskRule | CapitalRule | PermissionRule]:
        self.risk_rules = self._load_model(RiskRule, self.rules_directory / "risk_rules.yaml")
        self.capital_rules = self._load_model(CapitalRule, self.rules_directory / "capital_rules.yaml")
        self.permission_rules = self._load_model(PermissionRule, self.rules_directory / "permissions.yaml")
        return {
            "risk": self.risk_rules,
            "capital": self.capital_rules,
            "permissions": self.permission_rules,
        }

    def validate_trade(
        self,
        risk_pct: float,
        rr: float | None = None,
        current_open_positions: int = 0,
    ) -> tuple[bool, list[str]]:
        self._ensure_rules_loaded()
        assert self.risk_rules is not None

        reasons: list[str] = []
        if risk_pct > self.risk_rules.max_risk_per_trade:
            reasons.append(
                f"risk {risk_pct:.2f}% exceeds max risk per trade {self.risk_rules.max_risk_per_trade:.2f}%"
            )
        if current_open_positions >= self.risk_rules.max_open_positions:
            reasons.append(
                f"open positions {current_open_positions} meets or exceeds max {self.risk_rules.max_open_positions}"
            )
        if rr is not None and rr < self.risk_rules.minimum_rr:
            reasons.append(
                f"risk/reward {rr:.2f} below minimum {self.risk_rules.minimum_rr:.2f}"
            )

        return (len(reasons) == 0, reasons)

    def validate_position_size(self, lot_size: float, account_balance: float) -> tuple[bool, list[str]]:
        self._ensure_rules_loaded()
        assert self.capital_rules is not None

        reasons: list[str] = []
        if lot_size > self.capital_rules.max_lot_size:
            reasons.append(
                f"lot size {lot_size:.2f} exceeds max lot size {self.capital_rules.max_lot_size:.2f}"
            )
        max_allocation = account_balance * (self.capital_rules.capital_allocation / 100)
        if lot_size > max_allocation:
            reasons.append(
                f"lot size {lot_size:.2f} exceeds allocation {max_allocation:.2f}"
            )
        return (len(reasons) == 0, reasons)

    def check_permissions(
        self,
        live_trading: bool = False,
        news_trading: bool = False,
        scalping: bool = False,
        weekend_positions: bool = False,
    ) -> tuple[bool, list[str]]:
        self._ensure_rules_loaded()
        assert self.permission_rules is not None

        reasons: list[str] = []
        if live_trading and not self.permission_rules.allow_live_trading:
            reasons.append("live trading is not permitted")
        if news_trading and not self.permission_rules.allow_news_trading:
            reasons.append("news trading is not permitted")
        if scalping and not self.permission_rules.allow_scalping:
            reasons.append("scalping is not permitted")
        if weekend_positions and not self.permission_rules.allow_weekend_positions:
            reasons.append("weekend positions are not permitted")

        return (len(reasons) == 0, reasons)

    def _ensure_rules_loaded(self) -> None:
        if self.risk_rules is None or self.capital_rules is None or self.permission_rules is None:
            self.load_rules()

    def _load_model(self, model: type[RiskRule | CapitalRule | PermissionRule], path: Path) -> RiskRule | CapitalRule | PermissionRule:
        data = self._read_simple_yaml(path)
        return model(**data)

    def _read_simple_yaml(self, path: Path) -> dict[str, Any]:
        content: dict[str, Any] = {}
        with path.open("r", encoding="utf-8") as source:
            for raw_line in source:
                line = raw_line.strip()
                if not line or line.startswith("#"):
                    continue
                if ":" not in line:
                    continue
                key, value = [part.strip() for part in line.split(":", 1)]
                content[key] = self._cast_value(value)
        return content

    @staticmethod
    def _cast_value(value: str) -> Any:
        lowered = value.lower()
        if lowered in {"true", "false"}:
            return lowered == "true"
        if value.isdigit():
            return int(value)
        try:
            return float(value)
        except ValueError:
            return value
