
# Prepaid Configuration

## Structure

`PrepaidConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `initial_funding_amount_in_cents` | `int` | Optional | - |
| `replenish_to_amount_in_cents` | `int` | Optional | - |
| `auto_replenish` | `bool` | Optional | - |
| `replenish_threshold_amount_in_cents` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "id": 156,
  "initial_funding_amount_in_cents": 88,
  "replenish_to_amount_in_cents": 166,
  "auto_replenish": false,
  "replenish_threshold_amount_in_cents": 222
}
```

