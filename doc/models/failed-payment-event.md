
# Failed Payment Event

## Structure

`FailedPaymentEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `timestamp` | `datetime` | Required | - |
| `invoice` | [`Invoice`](../../doc/models/invoice.md) | Required | - |
| `event_type` | [`InvoiceEventType`](../../doc/models/invoice-event-type.md) | Required | **Default**: `"failed_payment"` |
| `event_data` | [`FailedPaymentEventData`](../../doc/models/failed-payment-event-data.md) | Required | Example schema for an `failed_payment` event |

## Example

```python
import dateutil.parser

from advancedbilling.models.failed_payment_event import FailedPaymentEvent
from advancedbilling.models.failed_payment_event_data import FailedPaymentEventData
from advancedbilling.models.invoice import Invoice
from advancedbilling.models.invoice_event_type import InvoiceEventType
from advancedbilling.models.invoice_payment_method_type import InvoicePaymentMethodType

failed_payment_event = FailedPaymentEvent(
    id=140,
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
    event_type=InvoiceEventType.FAILED_PAYMENT,
    event_data=FailedPaymentEventData(
        amount_in_cents=220,
        applied_amount=194,
        payment_method=InvoicePaymentMethodType.CASH,
        transaction_id=78,
        memo='memo0'
    )
)
```

