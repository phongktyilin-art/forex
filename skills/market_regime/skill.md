# Market Regime Detection

Detect market regimes such as trending, ranging, volatile, and low liquidity.

## Purpose

Support regime-aware strategy selection and signal filtering.

## Inputs

- `prices`: historical price series.
- `volume`: historical volume series.

## Outputs

- `regime`: one of `trending`, `ranging`, `volatile`, `low_liquidity`, or `unknown`.

## Examples

```json
{
  "input": {"prices": [1.0, 1.01, 1.02, 1.03, 1.04], "volume": [1000, 1100, 1200, 1000, 900]},
  "output": "trending"
}
```
