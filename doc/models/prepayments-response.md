
# Prepayments Response

## Structure

`PrepaymentsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `prepayments` | [`List[Prepayment]`](../../doc/models/prepayment.md) | Optional | **Constraints**: *Unique Items Required* |

## Example

```python
import dateutil.parser

from advancedbilling.models.prepayment import Prepayment
from advancedbilling.models.prepayment_method import PrepaymentMethod
from advancedbilling.models.prepayments_response import PrepaymentsResponse

prepayments_response = PrepaymentsResponse(
    prepayments=[
        Prepayment(
            id=76,
            subscription_id=186,
            amount_in_cents=94,
            remaining_amount_in_cents=220,
            external=False,
            memo='memo0',
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            refunded_amount_in_cents=170,
            details='details6',
            payment_type=PrepaymentMethod.CASH
        ),
        Prepayment(
            id=76,
            subscription_id=186,
            amount_in_cents=94,
            remaining_amount_in_cents=220,
            external=False,
            memo='memo0',
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            refunded_amount_in_cents=170,
            details='details6',
            payment_type=PrepaymentMethod.CASH
        ),
        Prepayment(
            id=76,
            subscription_id=186,
            amount_in_cents=94,
            remaining_amount_in_cents=220,
            external=False,
            memo='memo0',
            created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
            refunded_amount_in_cents=170,
            details='details6',
            payment_type=PrepaymentMethod.CASH
        )
    ]
)
```

