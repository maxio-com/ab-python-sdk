
# Create or Update Endpoint

Used to Create or Update Endpoint.

## Structure

`CreateOrUpdateEndpoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Required | - |
| `webhook_subscriptions` | [`List[WebhookSubscription]`](../../doc/models/webhook-subscription.md) | Required | - |

## Example

```python
from advancedbilling.models.create_or_update_endpoint import CreateOrUpdateEndpoint
from advancedbilling.models.webhook_subscription import WebhookSubscription

create_or_update_endpoint = CreateOrUpdateEndpoint(
    url='url2',
    webhook_subscriptions=[
        WebhookSubscription.EXPIRATION_DATE_CHANGE
    ]
)
```

