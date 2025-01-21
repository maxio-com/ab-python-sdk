
# MRR

## Structure

`MRR`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount_in_cents` | `int` | Optional | - |
| `amount_formatted` | `str` | Optional | - |
| `currency` | `str` | Optional | - |
| `currency_symbol` | `str` | Optional | - |
| `breakouts` | [`Breakouts`](../../doc/models/breakouts.md) | Optional | - |
| `at_time` | `datetime` | Optional | ISO8601 timestamp |

## Example (as JSON)

```json
{
  "amount_in_cents": 208,
  "amount_formatted": "amount_formatted2",
  "currency": "currency0",
  "currency_symbol": "currency_symbol8",
  "breakouts": {
    "plan_amount_in_cents": 254,
    "plan_amount_formatted": "plan_amount_formatted0",
    "usage_amount_in_cents": 106,
    "usage_amount_formatted": "usage_amount_formatted8"
  }
}
```

