
# Created Prepayment

## Structure

`CreatedPrepayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | **Constraints**: `>= 1` |
| `subscription_id` | `int` | Optional | **Constraints**: `>= 1` |
| `amount_in_cents` | `int` | Optional | **Constraints**: `>= 0.01` |
| `memo` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `starting_balance_in_cents` | `int` | Optional | **Constraints**: `>= 0` |
| `ending_balance_in_cents` | `int` | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.created_prepayment import CreatedPrepayment

created_prepayment = CreatedPrepayment(
    id=228,
    subscription_id=82,
    amount_in_cents=198,
    memo='memo6',
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

