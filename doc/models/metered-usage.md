
# Metered Usage

## Structure

`MeteredUsage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `previous_unit_balance` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `new_unit_balance` | `int` | Required | - |
| `usage_quantity` | `int` | Required | - |
| `component_id` | `int` | Required | - |
| `component_handle` | `str` | Required | - |
| `memo` | `str` | Required | - |

## Example (as JSON)

```json
{
  "previous_unit_balance": "previous_unit_balance6",
  "new_unit_balance": 80,
  "usage_quantity": 42,
  "component_id": 4,
  "component_handle": "component_handle8",
  "memo": "memo2"
}
```

