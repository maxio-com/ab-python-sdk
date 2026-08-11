
# Deduct Service Credit Request

## Structure

`DeductServiceCreditRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `deduction` | [`DeductServiceCredit`](../../doc/models/deduct-service-credit.md) | Required | - |

## Example

```python
from advancedbilling.models.deduct_service_credit import DeductServiceCredit
from advancedbilling.models.deduct_service_credit_request import DeductServiceCreditRequest

deduct_service_credit_request = DeductServiceCreditRequest(
    deduction=DeductServiceCredit(
        amount='String9',
        memo='memo0'
    )
)
```

