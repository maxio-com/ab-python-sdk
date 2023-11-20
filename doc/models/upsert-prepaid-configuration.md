
# Upsert Prepaid Configuration

## Structure

`UpsertPrepaidConfiguration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `initial_funding_amount_in_cents` | `long\|int` | Optional | - |
| `replenish_to_amount_in_cents` | `long\|int` | Optional | - |
| `auto_replenish` | `bool` | Optional | - |
| `replenish_threshold_amount_in_cents` | `long\|int` | Optional | - |

## Example (as JSON)

```json
{
  "initial_funding_amount_in_cents": 40,
  "replenish_to_amount_in_cents": 42,
  "auto_replenish": false,
  "replenish_threshold_amount_in_cents": 242
}
```

