from __future__ import annotations

from typing import Any, Callable

from hooks.hook_manager import HookManager
from memory.memory_manager import MemoryManager
from hooks.schemas import HookContext, SignalHookResult, TradeHookResult, CloseHookResult


class EvolutionManager:
    def __init__(self, hooks_directory: str | None = None, memory_path: str | None = None):
        self.hook_manager = HookManager(hooks_directory)
        self.memory_manager = MemoryManager(memory_path or "memory_store.json")

    def discover_patterns(self) -> list[dict[str, Any]]:
        return []

    def update_strategy(self, strategy_payload: dict[str, Any]) -> dict[str, Any]:
        return strategy_payload

    def run_before_signal(self, context: HookContext) -> list[SignalHookResult]:
        return self.hook_manager.run_before_signal(context)

    def run_after_signal(self, context: HookContext) -> list[SignalHookResult]:
        return self.hook_manager.run_after_signal(context)

    def run_before_trade(self, context: HookContext) -> list[TradeHookResult]:
        return self.hook_manager.run_before_trade(context)

    def run_after_trade(self, context: HookContext) -> list[TradeHookResult]:
        return self.hook_manager.run_after_trade(context)

    def run_before_close(self, context: HookContext) -> list[CloseHookResult]:
        return self.hook_manager.run_before_close(context)

    def run_after_close(self, context: HookContext) -> list[CloseHookResult]:
        return self.hook_manager.run_after_close(context)

    def run_after_backtest(self, context: HookContext) -> list[SignalHookResult]:
        return self.hook_manager.run_after_backtest(context)

    def register_before_signal_hook(self, hook: Callable[[HookContext], SignalHookResult]) -> None:
        self.hook_manager.register_before_signal_hook(hook)

    def register_after_signal_hook(self, hook: Callable[[HookContext], SignalHookResult]) -> None:
        self.hook_manager.register_after_signal_hook(hook)

    def register_before_trade_hook(self, hook: Callable[[HookContext], TradeHookResult]) -> None:
        self.hook_manager.register_before_trade_hook(hook)

    def register_after_trade_hook(self, hook: Callable[[HookContext], TradeHookResult]) -> None:
        self.hook_manager.register_after_trade_hook(hook)

    def register_before_close_hook(self, hook: Callable[[HookContext], CloseHookResult]) -> None:
        self.hook_manager.register_before_close_hook(hook)

    def register_after_close_hook(self, hook: Callable[[HookContext], CloseHookResult]) -> None:
        self.hook_manager.register_after_close_hook(hook)

    def register_after_backtest_hook(self, hook: Callable[[HookContext], SignalHookResult]) -> None:
        self.hook_manager.register_after_backtest_hook(hook)

    @property
    def before_signal_hooks(self):
        return self.hook_manager.before_signal_hooks

    @property
    def after_signal_hooks(self):
        return self.hook_manager.after_signal_hooks

    @property
    def before_trade_hooks(self):
        return self.hook_manager.before_trade_hooks

    @property
    def after_trade_hooks(self):
        return self.hook_manager.after_trade_hooks

    @property
    def before_close_hooks(self):
        return self.hook_manager.before_close_hooks

    @property
    def after_close_hooks(self):
        return self.hook_manager.after_close_hooks

    @property
    def after_backtest_hooks(self):
        return self.hook_manager.after_backtest_hooks

    def save_failure(self, content: dict[str, Any], tags: list[str] | None = None):
        return self.memory_manager.save_failure(content, tags)

    def save_evidence(self, content: dict[str, Any], tags: list[str] | None = None):
        return self.memory_manager.save_evidence(content, tags)
