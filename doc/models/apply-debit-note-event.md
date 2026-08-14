
# Apply Debit Note Event

## Structure

`ApplyDebitNoteEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `timestamp` | `datetime` | Required | - |
| `invoice` | [`Invoice`](../../doc/models/invoice.md) | Required | - |
| `event_type` | [`InvoiceEventType`](../../doc/models/invoice-event-type.md) | Required | **Default**: `"apply_debit_note"` |
| `event_data` | [`ApplyDebitNoteEventData`](../../doc/models/apply-debit-note-event-data.md) | Required | Example schema for an `apply_debit_note` event |

## Example

```python
import dateutil.parser

from advancedbilling.models.apply_debit_note_event import ApplyDebitNoteEvent
from advancedbilling.models.apply_debit_note_event_data import ApplyDebitNoteEventData
from advancedbilling.models.invoice import Invoice
from advancedbilling.models.invoice_event_type import InvoiceEventType

apply_debit_note_event = ApplyDebitNoteEvent(
    id=216,
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
    event_type=InvoiceEventType.APPLY_DEBIT_NOTE,
    event_data=ApplyDebitNoteEventData(
        debit_note_number='debit_note_number6',
        debit_note_uid='debit_note_uid2',
        original_amount='original_amount0',
        applied_amount='applied_amount2',
        memo='memo0',
        transaction_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    )
)
```

