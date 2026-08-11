
# MRR Movement

## Structure

`MRRMovement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `int` | Optional | - |
| `category` | `str` | Optional | - |
| `subscriber_delta` | `int` | Optional | - |
| `lead_delta` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.mrr_movement import MRRMovement

mrr_movement = MRRMovement(
    amount=74,
    category='category0',
    subscriber_delta=34,
    lead_delta=62
)
```

