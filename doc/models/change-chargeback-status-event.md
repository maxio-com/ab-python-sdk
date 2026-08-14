
# Change Chargeback Status Event

## Structure

`ChangeChargebackStatusEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `timestamp` | `datetime` | Required | - |
| `invoice` | [`Invoice`](../../doc/models/invoice.md) | Required | - |
| `event_type` | [`InvoiceEventType`](../../doc/models/invoice-event-type.md) | Required | **Default**: `"change_chargeback_status"` |
| `event_data` | [`ChangeChargebackStatusEventData`](../../doc/models/change-chargeback-status-event-data.md) | Required | Example schema for an `change_chargeback_status` event |

## Example

```python
import dateutil.parser

from advancedbilling.models.change_chargeback_status_event import ChangeChargebackStatusEvent
from advancedbilling.models.change_chargeback_status_event_data import ChangeChargebackStatusEventData
from advancedbilling.models.chargeback_status import ChargebackStatus
from advancedbilling.models.invoice import Invoice
from advancedbilling.models.invoice_event_type import InvoiceEventType

change_chargeback_status_event = ChangeChargebackStatusEvent(
    id=114,
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
    event_type=InvoiceEventType.CHANGE_CHARGEBACK_STATUS,
    event_data=ChangeChargebackStatusEventData(
        chargeback_status=ChargebackStatus.WON
    )
)
```

