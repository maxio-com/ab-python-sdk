
# Create Prepayment

## Structure

`CreatePrepayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `float` | Required | - |
| `details` | `str` | Required | - |
| `memo` | `str` | Required | - |
| `method` | [`CreatePrepaymentMethod`](../../doc/models/create-prepayment-method.md) | Required | When the `method` specified is `"credit_card_on_file"`, the prepayment amount will be collected using the default credit card payment profile and applied to the prepayment account balance. This is especially useful for manual replenishment of prepaid subscriptions. |
| `payment_profile_id` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.create_prepayment import CreatePrepayment
from advancedbilling.models.create_prepayment_method import CreatePrepaymentMethod

create_prepayment = CreatePrepayment(
    amount=14.84,
    details='details2',
    memo='memo6',
    method=CreatePrepaymentMethod.MONEY_ORDER,
    payment_profile_id=204
)
```

