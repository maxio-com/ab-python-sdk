
# Payment Method Apple Pay

## Structure

`PaymentMethodApplePay`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | [`InvoiceEventPaymentMethod`](../../doc/models/invoice-event-payment-method.md) | Required | - |

## Example

```python
from advancedbilling.models.invoice_event_payment_method import InvoiceEventPaymentMethod
from advancedbilling.models.payment_method_apple_pay import PaymentMethodApplePay

payment_method_apple_pay = PaymentMethodApplePay(
    mtype=InvoiceEventPaymentMethod.APPLE_PAY
)
```

