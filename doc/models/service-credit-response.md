
# Service Credit Response

## Structure

`ServiceCreditResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_credit` | [`ServiceCredit`](../../doc/models/service-credit.md) | Required | - |

## Example

```python
from advancedbilling.models.service_credit import ServiceCredit
from advancedbilling.models.service_credit_response import ServiceCreditResponse
from advancedbilling.models.service_credit_type import ServiceCreditType

service_credit_response = ServiceCreditResponse(
    service_credit=ServiceCredit(
        id=38,
        amount_in_cents=124,
        ending_balance_in_cents=164,
        entry_type=ServiceCreditType.CREDIT,
        memo='memo0'
    )
)
```

