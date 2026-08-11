
# Change Invoice Status Event

## Structure

`ChangeInvoiceStatusEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `timestamp` | `datetime` | Required | - |
| `invoice` | [`Invoice`](../../doc/models/invoice.md) | Required | - |
| `event_type` | [`InvoiceEventType`](../../doc/models/invoice-event-type.md) | Required | **Default**: `"change_invoice_status"` |
| `event_data` | [`ChangeInvoiceStatusEventData`](../../doc/models/change-invoice-status-event-data.md) | Required | Example schema for an `change_invoice_status` event |

## Example

```python
import dateutil.parser

from advancedbilling.models.change_invoice_status_event import ChangeInvoiceStatusEvent
from advancedbilling.models.change_invoice_status_event_data import ChangeInvoiceStatusEventData
from advancedbilling.models.invoice import Invoice
from advancedbilling.models.invoice_consolidation_level import InvoiceConsolidationLevel
from advancedbilling.models.invoice_event_type import InvoiceEventType
from advancedbilling.models.invoice_status import InvoiceStatus

change_invoice_status_event = ChangeInvoiceStatusEvent(
    id=36,
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
    event_type=InvoiceEventType.CHANGE_INVOICE_STATUS,
    event_data=ChangeInvoiceStatusEventData(
        from_status=InvoiceStatus.OPEN,
        to_status=InvoiceStatus.PENDING,
        gateway_trans_id='gateway_trans_id2',
        amount='amount8',
        consolidation_level=InvoiceConsolidationLevel.CHILD
    )
)
```

