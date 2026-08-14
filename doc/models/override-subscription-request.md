
# Override Subscription Request

## Structure

`OverrideSubscriptionRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription` | [`OverrideSubscription`](../../doc/models/override-subscription.md) | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.override_subscription import OverrideSubscription
from advancedbilling.models.override_subscription_request import OverrideSubscriptionRequest

override_subscription_request = OverrideSubscriptionRequest(
    subscription=OverrideSubscription(
        activated_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        canceled_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        cancellation_message='cancellation_message2',
        expires_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        current_period_starts_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    )
)
```

