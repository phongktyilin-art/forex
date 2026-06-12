# Skill: Market Analysis

Purpose: Analyze market structure, trend, momentum and volatility. Produces
standardized analysis JSON for downstream skills/agents.

Standard Input: `market_state` (dict containing at least an `ohlcv` table or
recent ticks).
Standard Output: JSON with keys: `decision`, `confidence`, `evidence`, `metadata`.

Constraints: Must not place orders, compute risk sizing, or write journals.
Keep logic focused to analysis and evidence generation.
