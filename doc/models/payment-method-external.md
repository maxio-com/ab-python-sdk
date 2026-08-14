
# Payment Method External

## Structure

`PaymentMethodExternal`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `details` | `str` | Required | - |
| `kind` | `str` | Required | - |
| `memo` | `str` | Required | - |
| `mtype` | [`InvoiceEventPaymentMethod`](../../doc/models/invoice-event-payment-method.md) | Required | - |

## Example

```python
from advancedbilling.models.invoice_event_payment_method import InvoiceEventPaymentMethod
from advancedbilling.models.payment_method_external import PaymentMethodExternal

payment_method_external = PaymentMethodExternal(
    details='details8',
    kind='kind6',
    memo='memo2',
    mtype=InvoiceEventPaymentMethod.EXTERNAL
)
```

