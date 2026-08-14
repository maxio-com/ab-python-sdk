
# Create Multi Invoice Payment Request

## Structure

`CreateMultiInvoicePaymentRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment` | [`CreateMultiInvoicePayment`](../../doc/models/create-multi-invoice-payment.md) | Required | - |

## Example

```python
from advancedbilling.models.create_invoice_payment_application import CreateInvoicePaymentApplication
from advancedbilling.models.create_multi_invoice_payment import CreateMultiInvoicePayment
from advancedbilling.models.create_multi_invoice_payment_request import CreateMultiInvoicePaymentRequest
from advancedbilling.models.invoice_payment_method_type import InvoicePaymentMethodType

create_multi_invoice_payment_request = CreateMultiInvoicePaymentRequest(
    payment=CreateMultiInvoicePayment(
        amount='String9',
        applications=[
            CreateInvoicePaymentApplication(
                invoice_uid='invoice_uid8',
                amount='amount0'
            )
        ],
        memo='memo0',
        details='details6',
        method=InvoicePaymentMethodType.ACH,
        received_on='received_on8'
    )
)
```

