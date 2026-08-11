
# Record Payment Request

## Structure

`RecordPaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment` | [`CreatePayment`](../../doc/models/create-payment.md) | Required | - |

## Example

```python
from advancedbilling.models.create_payment import CreatePayment
from advancedbilling.models.invoice_payment_method_type import InvoicePaymentMethodType
from advancedbilling.models.record_payment_request import RecordPaymentRequest

record_payment_request = RecordPaymentRequest(
    payment=CreatePayment(
        amount='amount8',
        memo='memo0',
        payment_details='payment_details6',
        payment_method=InvoicePaymentMethodType.CASH
    )
)
```

