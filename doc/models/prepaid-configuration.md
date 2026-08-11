
# Prepaid Configuration

## Structure

`PrepaidConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `initial_funding_amount_in_cents` | `int` | Optional | - |
| `replenish_to_amount_in_cents` | `int` | Optional | - |
| `auto_replenish` | `bool` | Optional | - |
| `replenish_threshold_amount_in_cents` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.prepaid_configuration import PrepaidConfiguration

prepaid_configuration = PrepaidConfiguration(
    id=142,
    initial_funding_amount_in_cents=74,
    replenish_to_amount_in_cents=76,
    auto_replenish=False,
    replenish_threshold_amount_in_cents=20
)
```

