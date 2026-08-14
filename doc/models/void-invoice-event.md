
# Void Invoice Event

## Structure

`VoidInvoiceEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `timestamp` | `datetime` | Required | - |
| `invoice` | [`Invoice`](../../doc/models/invoice.md) | Required | - |
| `event_type` | [`InvoiceEventType`](../../doc/models/invoice-event-type.md) | Required | **Default**: `"void_invoice"` |
| `event_data` | [`VoidInvoiceEventData`](../../doc/models/void-invoice-event-data.md) | Required | Example schema for an `void_invoice` event |

## Example

```python
import dateutil.parser

from advancedbilling.models.credit_note import CreditNote
from advancedbilling.models.invoice import Invoice
from advancedbilling.models.invoice_event_type import InvoiceEventType
from advancedbilling.models.void_invoice_event import VoidInvoiceEvent
from advancedbilling.models.void_invoice_event_data import VoidInvoiceEventData

void_invoice_event = VoidInvoiceEvent(
    id=220,
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
    event_type=InvoiceEventType.VOID_INVOICE,
    event_data=VoidInvoiceEventData(
        credit_note_attributes=CreditNote(
            uid='uid2',
            site_id=72,
            customer_id=184,
            subscription_id=0,
            number='number0'
        ),
        memo='memo0',
        applied_amount='applied_amount2',
        transaction_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        is_advance_invoice=False,
        reason='reason2'
    )
)
```

