
# Payment Method Paypal

## Structure

`PaymentMethodPaypal`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Required | - |
| `mtype` | [`InvoiceEventPaymentMethod`](../../doc/models/invoice-event-payment-method.md) | Required | - |

## Example

```python
from advancedbilling.models.invoice_event_payment_method import InvoiceEventPaymentMethod
from advancedbilling.models.payment_method_paypal import PaymentMethodPaypal

payment_method_paypal = PaymentMethodPaypal(
    email='email6',
    mtype=InvoiceEventPaymentMethod.PAYPAL_ACCOUNT
)
```

