
# Chargify EBB

## Structure

`ChargifyEBB`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timestamp` | `str` | Optional | This timestamp determines what billing period the event will be billed in. If your request payload does not include it, Chargify will add `chargify.timestamp` to the event payload and set the value to `now`. |
| `id` | `str` | Optional | A unique ID set by Chargify. Please note that this field is reserved. If `chargify.id` is present in the request payload, it will be overwritten. |
| `created_at` | `str` | Optional | An ISO-8601 timestamp, set by Chargify at the time each event is recorded. Please note that this field is reserved. If `chargify.created_at` is present in the request payload, it will be overwritten. |
| `uniqueness_token` | `str` | Optional | User-defined string scoped per-stream. Duplicate events within a stream will be silently ignored. Tokens expire after 31 days.<br>**Constraints**: *Maximum Length*: `64` |

## Example (as JSON)

```json
{
  "timestamp": "timestamp8",
  "id": "id4",
  "created_at": "created_at8",
  "uniqueness_token": "uniqueness_token0"
}
```

