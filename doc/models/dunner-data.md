
# Dunner Data

## Structure

`DunnerData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `state` | `str` | Required | - |
| `subscription_id` | `int` | Required | - |
| `revenue_at_risk_in_cents` | `long\|int` | Required | - |
| `created_at` | `datetime` | Required | - |
| `attempts` | `int` | Required | - |
| `last_attempted_at` | `datetime` | Required | - |

## Example (as JSON)

```json
{
  "state": "state4",
  "subscription_id": 126,
  "revenue_at_risk_in_cents": 30,
  "created_at": "2016-03-13T12:52:32.123Z",
  "attempts": 110,
  "last_attempted_at": "2016-03-13T12:52:32.123Z"
}
```

