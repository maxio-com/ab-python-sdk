
# Payment Method Bank Account

## Structure

`PaymentMethodBankAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `masked_account_number` | `str` | Required | - |
| `masked_routing_number` | `str` | Required | - |
| `mtype` | [`InvoiceEventPaymentMethod`](../../doc/models/invoice-event-payment-method.md) | Required | - |

## Example

```python
from advancedbilling.models.invoice_event_payment_method import InvoiceEventPaymentMethod
from advancedbilling.models.payment_method_bank_account import PaymentMethodBankAccount

payment_method_bank_account = PaymentMethodBankAccount(
    masked_account_number='masked_account_number6',
    masked_routing_number='masked_routing_number6',
    mtype=InvoiceEventPaymentMethod.BANK_ACCOUNT
)
```

