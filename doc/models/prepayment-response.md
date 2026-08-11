
# Prepayment Response

## Structure

`PrepaymentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `prepayment` | [`Prepayment`](../../doc/models/prepayment.md) | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.prepayment import Prepayment
from advancedbilling.models.prepayment_method import PrepaymentMethod
from advancedbilling.models.prepayment_response import PrepaymentResponse

prepayment_response = PrepaymentResponse(
    prepayment=Prepayment(
        id=38,
        subscription_id=148,
        amount_in_cents=124,
        remaining_amount_in_cents=182,
        external=False,
        memo='memo2',
        created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        refunded_amount_in_cents=132,
        details='details8',
        payment_type=PrepaymentMethod.CREDIT_CARD
    )
)
```

