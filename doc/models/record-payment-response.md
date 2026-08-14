
# Record Payment Response

## Structure

`RecordPaymentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `paid_invoices` | [`List[PaidInvoice]`](../../doc/models/paid-invoice.md) | Optional | - |
| `prepayment` | [`InvoicePrePayment`](../../doc/models/invoice-pre-payment.md) | Optional | - |

## Example

```python
from advancedbilling.models.invoice_pre_payment import InvoicePrePayment
from advancedbilling.models.invoice_status import InvoiceStatus
from advancedbilling.models.paid_invoice import PaidInvoice
from advancedbilling.models.record_payment_response import RecordPaymentResponse

record_payment_response = RecordPaymentResponse(
    paid_invoices=[
        PaidInvoice(
            invoice_id='invoice_id8',
            status=InvoiceStatus.DRAFT,
            due_amount='due_amount0',
            paid_amount='paid_amount0'
        )
    ],
    prepayment=InvoicePrePayment(
        subscription_id=148,
        amount_in_cents=124,
        ending_balance_in_cents=164
    )
)
```

