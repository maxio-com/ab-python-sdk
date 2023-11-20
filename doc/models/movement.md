
# Movement

## Structure

`Movement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `timestamp` | `str` | Optional | - |
| `amount_in_cents` | `long\|int` | Optional | - |
| `amount_formatted` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `category` | `str` | Optional | - |
| `breakouts` | [`Breakouts`](../../doc/models/breakouts.md) | Optional | - |
| `line_items` | [`List[MovementLineItem]`](../../doc/models/movement-line-item.md) | Optional | - |
| `subscription_id` | `int` | Optional | - |
| `subscriber_name` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "timestamp": "timestamp0",
  "amount_in_cents": 174,
  "amount_formatted": "amount_formatted4",
  "description": "description2",
  "category": "category0"
}
```

