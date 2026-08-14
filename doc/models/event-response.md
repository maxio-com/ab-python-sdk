
# Event Response

## Structure

`EventResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event` | [`Event`](../../doc/models/event.md) | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.event import Event
from advancedbilling.models.event_key import EventKey
from advancedbilling.models.event_response import EventResponse
from advancedbilling.models.subscription_product_change import SubscriptionProductChange

event_response = EventResponse(
    event=Event(
        id=242,
        key=EventKey.SUBSCRIPTION_REMOVED_FROM_GROUP,
        message='message0',
        subscription_id=96,
        customer_id=24,
        created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        event_specific_data=SubscriptionProductChange(
            previous_product_id=126,
            new_product_id=12,
            previous_product_price_point_id=250,
            new_product_price_point_id=244,
            effective_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        )
    )
)
```

