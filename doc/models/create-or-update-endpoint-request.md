
# Create or Update Endpoint Request

Used to Create or Update Endpoint.

## Structure

`CreateOrUpdateEndpointRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `endpoint` | [`CreateOrUpdateEndpoint`](../../doc/models/create-or-update-endpoint.md) | Required | Used to Create or Update Endpoint. |

## Example

```python
from advancedbilling.models.create_or_update_endpoint import CreateOrUpdateEndpoint
from advancedbilling.models.create_or_update_endpoint_request import CreateOrUpdateEndpointRequest
from advancedbilling.models.webhook_subscription import WebhookSubscription

create_or_update_endpoint_request = CreateOrUpdateEndpointRequest(
    endpoint=CreateOrUpdateEndpoint(
        url='url2',
        webhook_subscriptions=[
            WebhookSubscription.STATEMENT_CLOSED
        ]
    )
)
```

