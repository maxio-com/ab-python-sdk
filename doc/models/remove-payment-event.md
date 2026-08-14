
# Remove Payment Event

## Structure

`RemovePaymentEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `timestamp` | `datetime` | Required | - |
| `invoice` | [`Invoice`](../../doc/models/invoice.md) | Required | - |
| `event_type` | [`InvoiceEventType`](../../doc/models/invoice-event-type.md) | Required | **Default**: `"remove_payment"` |
| `event_data` | [`RemovePaymentEventData`](../../doc/models/remove-payment-event-data.md) | Required | Example schema for an `remove_payment` event |

## Example

```python
import dateutil.parser

from advancedbilling.models.invoice import Invoice
from advancedbilling.models.invoice_event_payment_method import InvoiceEventPaymentMethod
from advancedbilling.models.invoice_event_type import InvoiceEventType
from advancedbilling.models.payment_method_apple_pay import PaymentMethodApplePay
from advancedbilling.models.remove_payment_event import RemovePaymentEvent
from advancedbilling.models.remove_payment_event_data import RemovePaymentEventData

remove_payment_event = RemovePaymentEvent(
    id=4,
    timestamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    invoice=Invoice(
        id=166,
        uid='uid6',
        site_id=92,
        customer_id=204,
        subscription_id=20,
        issue_date=dateutil.parser.parse('2024-01-01').date(),
        due_date=dateutil.parser.parse('2024-01-01').date(),
        paid_date=dateutil.parser.parse('2024-01-01').date(),
        public_url_expires_on=dateutil.parser.parse('2024-01-21').date()
    ),
    event_type=InvoiceEventType.REMOVE_PAYMENT,
    event_data=RemovePaymentEventData(
        transaction_id=78,
        memo='memo0',
        applied_amount='applied_amount2',
        transaction_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        payment_method=PaymentMethodApplePay(
            mtype=InvoiceEventPaymentMethod.APPLE_PAY
        ),
        prepayment=False,
        original_amount='original_amount0'
    )
)
```

