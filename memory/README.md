# Memory OS Skill Package

This package provides memory operating system primitives for HedgeMath OS.

It contains:
- `skills/memory/short_term.py` — in-memory short-term memory store and recall.
- `skills/memory/long_term.py` — durable long-term memory persistence and query.
- `skills/memory/schemas.py` — typed memory record and query definitions.

The package is intentionally lightweight and uses only standard libraries so it
can be composed into higher-level workflows without backend coupling.
