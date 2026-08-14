
# Multi Invoice Payment

## Structure

`MultiInvoicePayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `int` | Optional | The numeric ID of the transaction. |
| `total_amount` | `str` | Optional | Dollar amount of the sum of the paid invoices. |
| `currency_code` | `str` | Optional | The ISO 4217 currency code (3 character string) representing the currency of invoice transaction. |
| `applications` | [`List[InvoicePaymentApplication]`](../../doc/models/invoice-payment-application.md) | Optional | - |

## Example

```python
from advancedbilling.models.invoice_payment_application import InvoicePaymentApplication
from advancedbilling.models.multi_invoice_payment import MultiInvoicePayment

multi_invoice_payment = MultiInvoicePayment(
    transaction_id=238,
    total_amount='total_amount0',
    currency_code='currency_code0',
    applications=[
        InvoicePaymentApplication(
            invoice_uid='invoice_uid8',
            application_uid='application_uid8',
            applied_amount='applied_amount0'
        )
    ]
)
```

