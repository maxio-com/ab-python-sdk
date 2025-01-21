
# Created Prepayment

## Structure

`CreatedPrepayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | **Constraints**: `>= 1` |
| `subscription_id` | `int` | Optional | **Constraints**: `>= 1` |
| `amount_in_cents` | `int` | Optional | **Constraints**: `>= 0.01` |
| `memo` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `starting_balance_in_cents` | `int` | Optional | **Constraints**: `>= 0` |
| `ending_balance_in_cents` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "id": 110,
  "subscription_id": 220,
  "amount_in_cents": 196,
  "memo": "memo6",
  "created_at": "2016-03-13T12:52:32.123Z"
}
```

