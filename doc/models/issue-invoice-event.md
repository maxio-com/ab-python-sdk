
# Issue Invoice Event

## Structure

`IssueInvoiceEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `timestamp` | `datetime` | Required | - |
| `invoice` | [`Invoice`](../../doc/models/invoice.md) | Required | - |
| `event_type` | [`InvoiceEventType`](../../doc/models/invoice-event-type.md) | Required | **Default**: `"issue_invoice"` |
| `event_data` | [`IssueInvoiceEventData`](../../doc/models/issue-invoice-event-data.md) | Required | Example schema for an `issue_invoice` event |

## Example

```python
import dateutil.parser

from advancedbilling.models.invoice import Invoice
from advancedbilling.models.invoice_consolidation_level import InvoiceConsolidationLevel
from advancedbilling.models.invoice_event_type import InvoiceEventType
from advancedbilling.models.invoice_status import InvoiceStatus
from advancedbilling.models.issue_invoice_event import IssueInvoiceEvent
from advancedbilling.models.issue_invoice_event_data import IssueInvoiceEventData

issue_invoice_event = IssueInvoiceEvent(
    id=238,
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
    event_type=InvoiceEventType.ISSUE_INVOICE,
    event_data=IssueInvoiceEventData(
        consolidation_level=InvoiceConsolidationLevel.CHILD,
        from_status=InvoiceStatus.OPEN,
        to_status=InvoiceStatus.PENDING,
        due_amount='due_amount8',
        total_amount='total_amount2'
    )
)
```

