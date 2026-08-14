
# Refund Invoice Event

## Structure

`RefundInvoiceEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `timestamp` | `datetime` | Required | - |
| `invoice` | [`Invoice`](../../doc/models/invoice.md) | Required | - |
| `event_type` | [`InvoiceEventType`](../../doc/models/invoice-event-type.md) | Required | **Default**: `"refund_invoice"` |
| `event_data` | [`RefundInvoiceEventData`](../../doc/models/refund-invoice-event-data.md) | Required | Example schema for an `refund_invoice` event |

## Example

```python
import dateutil.parser

from advancedbilling.models.credit_note import CreditNote
from advancedbilling.models.invoice import Invoice
from advancedbilling.models.invoice_consolidation_level import InvoiceConsolidationLevel
from advancedbilling.models.invoice_event_type import InvoiceEventType
from advancedbilling.models.refund_invoice_event import RefundInvoiceEvent
from advancedbilling.models.refund_invoice_event_data import RefundInvoiceEventData

refund_invoice_event = RefundInvoiceEvent(
    id=142,
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
    event_type=InvoiceEventType.REFUND_INVOICE,
    event_data=RefundInvoiceEventData(
        apply_credit=False,
        credit_note_attributes=CreditNote(
            uid='uid2',
            site_id=72,
            customer_id=184,
            subscription_id=0,
            number='number0'
        ),
        payment_id=204,
        refund_amount='refund_amount8',
        refund_id=248,
        transaction_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        consolidation_level=InvoiceConsolidationLevel.CHILD,
        memo='memo0',
        original_amount='original_amount0'
    )
)
```

