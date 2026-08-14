
# Change Invoice Collection Method Event

## Structure

`ChangeInvoiceCollectionMethodEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `timestamp` | `datetime` | Required | - |
| `invoice` | [`Invoice`](../../doc/models/invoice.md) | Required | - |
| `event_type` | [`InvoiceEventType`](../../doc/models/invoice-event-type.md) | Required | **Default**: `"change_invoice_collection_method"` |
| `event_data` | [`ChangeInvoiceCollectionMethodEventData`](../../doc/models/change-invoice-collection-method-event-data.md) | Required | Example schema for an `change_invoice_collection_method` event |

## Example

```python
import dateutil.parser

from advancedbilling.models.change_invoice_collection_method_event import ChangeInvoiceCollectionMethodEvent
from advancedbilling.models.change_invoice_collection_method_event_data import ChangeInvoiceCollectionMethodEventData
from advancedbilling.models.invoice import Invoice
from advancedbilling.models.invoice_event_type import InvoiceEventType

change_invoice_collection_method_event = ChangeInvoiceCollectionMethodEvent(
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
    event_type=InvoiceEventType.CHANGE_INVOICE_COLLECTION_METHOD,
    event_data=ChangeInvoiceCollectionMethodEventData(
        from_collection_method='from_collection_method4',
        to_collection_method='to_collection_method8'
    )
)
```

