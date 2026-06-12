# Portfolio Exposure

Calculate portfolio exposure and support portfolio-level risk management.

## Purpose

Enable portfolio intelligence by measuring exposure relative to account balance.

## Inputs

- `positions`: open positions with market value.
- `account_balance`: current account balance.

## Outputs

- `exposure_pct`: portfolio exposure as a fraction of account balance.

## Examples

```json
{
  "input": {"positions": [{"symbol": "EURUSD", "value": 10000.0}], "account_balance": 100000.0},
  "output": 0.1
}
```
