from governance.governance_manager import GovernanceManager


def test_governance_manager_loads_rules():
    manager = GovernanceManager()
    rules = manager.load_rules()

    assert rules["risk"].max_risk_per_trade == 1.0
    assert rules["risk"].max_open_positions == 5
    assert rules["capital"].starting_balance == 10000.0
    assert rules["capital"].compounding_enabled is True
    assert rules["permissions"].allow_live_trading is False
    assert rules["permissions"].allow_scalping is True


def test_governance_manager_validate_trade():
    manager = GovernanceManager()
    allowed, reasons = manager.validate_trade(risk_pct=0.8, rr=2.5, current_open_positions=1)
    assert allowed
    assert reasons == []

    allowed, reasons = manager.validate_trade(risk_pct=1.2, rr=1.5, current_open_positions=6)
    assert not allowed
    assert any("risk" in reason for reason in reasons)
    assert any("open positions" in reason for reason in reasons)
    assert any("risk/reward" in reason for reason in reasons)


def test_governance_manager_validate_position_size():
    manager = GovernanceManager()
    allowed, reasons = manager.validate_position_size(lot_size=0.5, account_balance=10000.0)
    assert allowed
    assert reasons == []

    allowed, reasons = manager.validate_position_size(lot_size=2.0, account_balance=10000.0)
    assert not allowed
    assert any("lot size" in reason for reason in reasons)


def test_governance_manager_check_permissions():
    manager = GovernanceManager()
    allowed, reasons = manager.check_permissions(live_trading=True, news_trading=False, scalping=True)
    assert not allowed
    assert "live trading is not permitted" in reasons
