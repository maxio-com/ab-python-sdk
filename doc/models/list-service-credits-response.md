
# List Service Credits Response

## Structure

`ListServiceCreditsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_credits` | [`List[ServiceCredit1]`](../../doc/models/service-credit-1.md) | Optional | - |

## Example

```python
from advancedbilling.models.list_service_credits_response import ListServiceCreditsResponse
from advancedbilling.models.service_credit_1 import ServiceCredit1
from advancedbilling.models.service_credit_type import ServiceCreditType

list_service_credits_response = ListServiceCreditsResponse(
    service_credits=[
        ServiceCredit1(
            id=224,
            amount_in_cents=54,
            ending_balance_in_cents=94,
            entry_type=ServiceCreditType.CREDIT,
            memo='memo2'
        )
    ]
)
```

