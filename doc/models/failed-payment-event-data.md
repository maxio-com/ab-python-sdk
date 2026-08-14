
# Failed Payment Event Data

Example schema for an `failed_payment` event

## Structure

`FailedPaymentEventData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount_in_cents` | `int` | Required | The monetary value of the payment, expressed in cents. |
| `applied_amount` | `int` | Required | The monetary value of the payment, expressed in dollars. |
| `memo` | `str` | Optional | The memo passed when the payment was created. |
| `payment_method` | [`InvoicePaymentMethodType`](../../doc/models/invoice-payment-method-type.md) | Required | - |
| `transaction_id` | `int` | Required | The transaction ID of the failed payment. |

## Example

```python
from advancedbilling.models.failed_payment_event_data import FailedPaymentEventData
from advancedbilling.models.invoice_payment_method_type import InvoicePaymentMethodType

failed_payment_event_data = FailedPaymentEventData(
    amount_in_cents=46,
    applied_amount=20,
    payment_method=InvoicePaymentMethodType.CASH,
    transaction_id=252,
    memo='memo2'
)
```

