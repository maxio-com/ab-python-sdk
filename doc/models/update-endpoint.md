
# Update Endpoint

Used to Create or Update Endpoint

## Structure

`UpdateEndpoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Required | - |
| `webhook_subscriptions` | [`List[WebhookSubscription]`](../../doc/models/webhook-subscription.md) | Required | - |

## Example (as JSON)

```json
{
  "url": "url8",
  "webhook_subscriptions": [
    "payment_success"
  ]
}
```

