
# Allocation Preview Item

## Structure

`AllocationPreviewItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Optional | - |
| `subscription_id` | `int` | Optional | - |
| `quantity` | float \| int \| None | Optional | This is a container for one-of cases. |
| `previous_quantity` | `int` | Optional | - |
| `memo` | `str` | Optional | - |
| `timestamp` | `str` | Optional | - |
| `proration_upgrade_scheme` | `str` | Optional | - |
| `proration_downgrade_scheme` | `str` | Optional | - |
| `accrue_charge` | `bool` | Optional | - |
| `upgrade_charge` | `str` | Optional | - |
| `downgrade_credit` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "component_id": 54,
  "subscription_id": 54,
  "quantity": 159.62,
  "previous_quantity": 14,
  "memo": "memo6"
}
```

