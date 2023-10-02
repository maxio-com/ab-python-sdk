
# Event

## Structure

`Event`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `float` | Required | - |
| `key` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `message` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `subscription_id` | `float` | Required | - |
| `created_at` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `event_specific_data` | [Event Data](../../doc/models/event-data.md) \| None | Required | This is a container for one-of cases. |

## Example (as JSON)

```json
{
  "id": 159.12,
  "key": "key2",
  "message": "message8",
  "subscription_id": 185.82,
  "created_at": "created_at0",
  "event_specific_data": {
    "previous_subscription_state": "previous_subscription_state4",
    "new_subscription_state": "new_subscription_state8"
  }
}
```

