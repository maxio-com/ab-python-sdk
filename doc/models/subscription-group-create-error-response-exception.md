
# Subscription Group Create Error Response Exception

## Structure

`SubscriptionGroupCreateErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [Subscription Group Members Array Error](../../doc/models/subscription-group-members-array-error.md) \| [Subscription Group Single Error](../../doc/models/subscription-group-single-error.md) \| str | Required | This is a container for one-of cases. |

## Example (as JSON)

```json
{
  "errors": {
    "members": [
      "members6"
    ]
  }
}
```

