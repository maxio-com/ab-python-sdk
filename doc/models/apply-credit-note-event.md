
# Apply Credit Note Event

## Structure

`ApplyCreditNoteEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `timestamp` | `datetime` | Required | - |
| `invoice` | [`Invoice`](../../doc/models/invoice.md) | Required | - |
| `event_type` | [`InvoiceEventType`](../../doc/models/invoice-event-type.md) | Required | **Default**: `"apply_credit_note"` |
| `event_data` | [`ApplyCreditNoteEventData`](../../doc/models/apply-credit-note-event-data.md) | Required | Example schema for an `apply_credit_note` event |

## Example

```python
import dateutil.parser

from advancedbilling.models.applied_credit_note_data import AppliedCreditNoteData
from advancedbilling.models.apply_credit_note_event import ApplyCreditNoteEvent
from advancedbilling.models.apply_credit_note_event_data import ApplyCreditNoteEventData
from advancedbilling.models.invoice import Invoice
from advancedbilling.models.invoice_event_type import InvoiceEventType

apply_credit_note_event = ApplyCreditNoteEvent(
    id=56,
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
    event_type=InvoiceEventType.APPLY_CREDIT_NOTE,
    event_data=ApplyCreditNoteEventData(
        uid='uid6',
        credit_note_number='credit_note_number0',
        credit_note_uid='credit_note_uid0',
        original_amount='original_amount0',
        applied_amount='applied_amount2',
        transaction_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        memo='memo0',
        role='role0',
        consolidated_invoice=False,
        applied_credit_notes=[
            AppliedCreditNoteData(
                uid='uid4',
                number='number8'
            ),
            AppliedCreditNoteData(
                uid='uid4',
                number='number8'
            ),
            AppliedCreditNoteData(
                uid='uid4',
                number='number8'
            )
        ]
    )
)
```

