
# Breakouts

## Structure

`Breakouts`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `plan_amount_in_cents` | `int` | Optional | - |
| `plan_amount_formatted` | `str` | Optional | - |
| `usage_amount_in_cents` | `int` | Optional | - |
| `usage_amount_formatted` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.breakouts import Breakouts

breakouts = Breakouts(
    plan_amount_in_cents=254,
    plan_amount_formatted='plan_amount_formatted0',
    usage_amount_in_cents=106,
    usage_amount_formatted='usage_amount_formatted8'
)
```

