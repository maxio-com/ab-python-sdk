
# Replay Webhooks Request

## Structure

`ReplayWebhooksRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | `List[int]` | Required | - |

## Example

```python
from advancedbilling.models.replay_webhooks_request import ReplayWebhooksRequest

replay_webhooks_request = ReplayWebhooksRequest(
    ids=[
        233,
        234,
        235
    ]
)
```

