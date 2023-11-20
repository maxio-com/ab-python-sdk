
# Subscription Group Inlined

## Structure

`SubscriptionGroupInlined`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | The UID for the group |
| `scheme` | `str` | Optional | Whether the group is configured to rely on a primary subscription for billing. At this time, it will always be 1. |
| `primary_subscription_id` | `str` | Optional | The subscription ID of the primary within the group. Applicable to scheme 1. |
| `primary` | `bool` | Optional | A boolean indicating whether the subscription is the primary in the group. Applicable to scheme 1. |

## Example (as JSON)

```json
{
  "uid": "uid2",
  "scheme": "scheme2",
  "primary_subscription_id": "primary_subscription_id8",
  "primary": false
}
```

