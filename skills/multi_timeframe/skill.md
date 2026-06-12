# Multi-Timeframe Context

Assemble market context across multiple timeframes for long-horizon decision making.

## Purpose

Support multi-timeframe intelligence and connect higher timeframe structure with entry-timeframe execution.

## Inputs

- `timeframes`: list of timeframe labels.
- `data_by_timeframe`: market data keyed by timeframe.

## Outputs

- `context`: assembled multi-timeframe dataset.

## Examples

```json
{
  "input": {"timeframes": ["1h", "4h", "1d"], "data_by_timeframe": {"1h": {"price": 1.12}, "4h": {"price": 1.14}, "1d": {"price": 1.15}}},
  "output": {"1h": {"price": 1.12}, "4h": {"price": 1.14}, "1d": {"price": 1.15}}
}
```
