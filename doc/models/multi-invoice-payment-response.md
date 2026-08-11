
# Multi Invoice Payment Response

## Structure

`MultiInvoicePaymentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment` | [`MultiInvoicePayment`](../../doc/models/multi-invoice-payment.md) | Required | - |

## Example

```python
from advancedbilling.models.invoice_payment_application import InvoicePaymentApplication
from advancedbilling.models.multi_invoice_payment import MultiInvoicePayment
from advancedbilling.models.multi_invoice_payment_response import MultiInvoicePaymentResponse

multi_invoice_payment_response = MultiInvoicePaymentResponse(
    payment=MultiInvoicePayment(
        transaction_id=224,
        total_amount='total_amount2',
        currency_code='currency_code2',
        applications=[
            InvoicePaymentApplication(
                invoice_uid='invoice_uid8',
                application_uid='application_uid8',
                applied_amount='applied_amount0'
            ),
            InvoicePaymentApplication(
                invoice_uid='invoice_uid8',
                application_uid='application_uid8',
                applied_amount='applied_amount0'
            ),
            InvoicePaymentApplication(
                invoice_uid='invoice_uid8',
                application_uid='application_uid8',
                applied_amount='applied_amount0'
            )
        ]
    )
)
```

