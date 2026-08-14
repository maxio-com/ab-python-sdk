
# Upsert Prepaid Configuration

## Structure

`UpsertPrepaidConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `initial_funding_amount_in_cents` | `int` | Optional | - |
| `replenish_to_amount_in_cents` | `int` | Optional | - |
| `auto_replenish` | `bool` | Optional | - |
| `replenish_threshold_amount_in_cents` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.upsert_prepaid_configuration import UpsertPrepaidConfiguration

upsert_prepaid_configuration = UpsertPrepaidConfiguration(
    initial_funding_amount_in_cents=104,
    replenish_to_amount_in_cents=106,
    auto_replenish=False,
    replenish_threshold_amount_in_cents=206
)
```

