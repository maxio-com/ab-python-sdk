
# Create Credit Note Event

## Structure

`CreateCreditNoteEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `timestamp` | `datetime` | Required | - |
| `invoice` | [`Invoice`](../../doc/models/invoice.md) | Required | - |
| `event_type` | [`InvoiceEventType`](../../doc/models/invoice-event-type.md) | Required | **Default**: `"create_credit_note"` |
| `event_data` | [`CreditNote`](../../doc/models/credit-note.md) | Required | Example schema for an `create_credit_note` event |

## Example

```python
import dateutil.parser

from advancedbilling.models.create_credit_note_event import CreateCreditNoteEvent
from advancedbilling.models.credit_note import CreditNote
from advancedbilling.models.invoice import Invoice
from advancedbilling.models.invoice_event_type import InvoiceEventType

create_credit_note_event = CreateCreditNoteEvent(
    id=166,
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
    event_type=InvoiceEventType.CREATE_CREDIT_NOTE,
    event_data=CreditNote(
        uid='uid6',
        site_id=132,
        customer_id=244,
        subscription_id=60,
        number='number6'
    )
)
```

