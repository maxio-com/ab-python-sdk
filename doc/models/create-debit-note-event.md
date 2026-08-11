
# Create Debit Note Event

## Structure

`CreateDebitNoteEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `timestamp` | `datetime` | Required | - |
| `invoice` | [`Invoice`](../../doc/models/invoice.md) | Required | - |
| `event_type` | [`InvoiceEventType`](../../doc/models/invoice-event-type.md) | Required | **Default**: `"create_debit_note"` |
| `event_data` | [`DebitNote`](../../doc/models/debit-note.md) | Required | Example schema for an `create_debit_note` event |

## Example

```python
import dateutil.parser

from advancedbilling.models.create_debit_note_event import CreateDebitNoteEvent
from advancedbilling.models.debit_note import DebitNote
from advancedbilling.models.invoice import Invoice
from advancedbilling.models.invoice_event_type import InvoiceEventType

create_debit_note_event = CreateDebitNoteEvent(
    id=246,
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
    event_type=InvoiceEventType.CREATE_DEBIT_NOTE,
    event_data=DebitNote(
        uid='uid6',
        site_id=132,
        customer_id=244,
        subscription_id=60,
        number=64
    )
)
```

