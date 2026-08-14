
# Enable Webhooks Request

## Structure

`EnableWebhooksRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `webhooks_enabled` | `bool` | Required | - |

## Example

```python
from advancedbilling.models.enable_webhooks_request import EnableWebhooksRequest

enable_webhooks_request = EnableWebhooksRequest(
    webhooks_enabled=False
)
```

