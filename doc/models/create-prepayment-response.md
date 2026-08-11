
# Create Prepayment Response

## Structure

`CreatePrepaymentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `prepayment` | [`CreatedPrepayment`](../../doc/models/created-prepayment.md) | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.create_prepayment_response import CreatePrepaymentResponse
from advancedbilling.models.created_prepayment import CreatedPrepayment

create_prepayment_response = CreatePrepaymentResponse(
    prepayment=CreatedPrepayment(
        id=38,
        subscription_id=148,
        amount_in_cents=124,
        memo='memo2',
        created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    )
)
```

