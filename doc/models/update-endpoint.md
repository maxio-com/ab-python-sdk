
# Update Endpoint

Used to Create or Update Endpoint

## Structure

`UpdateEndpoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `url` | `str` | Required | - |
| `webhook_subscriptions` | [`List[WebhookSubscriptionEnum]`](../../doc/models/webhook-subscription-enum.md) | Required | - |

## Example (as JSON)

```json
{
  "url": "url8",
  "webhook_subscriptions": [
    "payment_success"
  ]
}
```

