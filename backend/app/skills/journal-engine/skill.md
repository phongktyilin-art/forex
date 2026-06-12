# Skill: Journal Engine

Purpose: Record trade evidence for Memory OS and Evolution OS.

Standard Input: JSON with `market_state` and `trade_result`.

Standard Output: JSON with `trade_id`, `symbol`, `setup`, `regime`, `session`, `result`, `evidence`, and `metadata`.

Responsibilities:
- Save entry and exit data.
- Save setup, market regime, session, result, and evidence.
- Persist journal records.
- Publish evidence into Memory OS folders.

Non-responsibilities:
- Do not analyze markets.
- Do not calculate risk.
- Do not send orders.
- Do not optimize strategies.

Constraints:
- Evidence First.
- Memory First.
- Save structured evidence, not raw opinions.
