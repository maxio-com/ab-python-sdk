
# Endpoint Response

## Structure

`EndpointResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `endpoint` | [`Endpoint`](../../doc/models/endpoint.md) | Optional | - |

## Example

```python
from advancedbilling.models.endpoint import Endpoint
from advancedbilling.models.endpoint_response import EndpointResponse

endpoint_response = EndpointResponse(
    endpoint=Endpoint(
        id=202,
        url='url2',
        site_id=128,
        status='status0',
        webhook_subscriptions=[
            'webhook_subscriptions4'
        ]
    )
)
```

