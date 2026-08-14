
# Create Invoice Payment Request

## Structure

`CreateInvoicePaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment` | [`CreateInvoicePayment`](../../doc/models/create-invoice-payment.md) | Required | - |
| `mtype` | [`InvoicePaymentType`](../../doc/models/invoice-payment-type.md) | Optional | The type of payment to be applied to an Invoice. Defaults to external. |

## Example

```python
from advancedbilling.models.create_invoice_payment import CreateInvoicePayment
from advancedbilling.models.create_invoice_payment_request import CreateInvoicePaymentRequest
from advancedbilling.models.invoice_payment_method_type import InvoicePaymentMethodType
from advancedbilling.models.invoice_payment_type import InvoicePaymentType

create_invoice_payment_request = CreateInvoicePaymentRequest(
    payment=CreateInvoicePayment(
        amount='String9',
        memo='memo0',
        method=InvoicePaymentMethodType.ACH,
        details='details6',
        payment_profile_id=42
    ),
    mtype=InvoicePaymentType.SERVICE_CREDIT
)
```

