
# Create Prepayment Request

## Structure

`CreatePrepaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `prepayment` | [`CreatePrepayment`](../../doc/models/create-prepayment.md) | Required | - |

## Example

```python
from advancedbilling.models.create_prepayment import CreatePrepayment
from advancedbilling.models.create_prepayment_method import CreatePrepaymentMethod
from advancedbilling.models.create_prepayment_request import CreatePrepaymentRequest

create_prepayment_request = CreatePrepaymentRequest(
    prepayment=CreatePrepayment(
        amount=11.6,
        details='details8',
        memo='memo2',
        method=CreatePrepaymentMethod.MONEY_ORDER,
        payment_profile_id=240
    )
)
```

