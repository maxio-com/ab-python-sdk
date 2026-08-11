
# Payment Method Credit Card

## Structure

`PaymentMethodCreditCard`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_brand` | `str` | Required | - |
| `card_expiration` | `str` | Optional | - |
| `last_four` | `str` | Optional | - |
| `masked_card_number` | `str` | Required | - |
| `mtype` | [`InvoiceEventPaymentMethod`](../../doc/models/invoice-event-payment-method.md) | Required | - |

## Example

```python
from advancedbilling.models.invoice_event_payment_method import InvoiceEventPaymentMethod
from advancedbilling.models.payment_method_credit_card import PaymentMethodCreditCard

payment_method_credit_card = PaymentMethodCreditCard(
    card_brand='card_brand2',
    masked_card_number='masked_card_number2',
    mtype=InvoiceEventPaymentMethod.CREDIT_CARD,
    card_expiration='card_expiration0',
    last_four='last_four8'
)
```

