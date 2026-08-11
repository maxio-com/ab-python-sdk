
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

## Example

```python
from advancedbilling.models.breakouts import Breakouts
from advancedbilling.models.mrr import MRR

mrr = MRR(
    amount_in_cents=198,
    amount_formatted='amount_formatted6',
    currency='currency4',
    currency_symbol='currency_symbol2',
    breakouts=Breakouts(
        plan_amount_in_cents=254,
        plan_amount_formatted='plan_amount_formatted0',
        usage_amount_in_cents=106,
        usage_amount_formatted='usage_amount_formatted8'
    )
)
```

