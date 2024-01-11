
# Allocation Preview Item

## Structure

`AllocationPreviewItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Optional | - |
| `subscription_id` | `int` | Optional | - |
| `quantity` | int \| str \| None | Optional | This is a container for one-of cases. |
| `previous_quantity` | int \| str \| None | Optional | This is a container for one-of cases. |
| `memo` | `str` | Optional | - |
| `timestamp` | `str` | Optional | - |
| `proration_upgrade_scheme` | `str` | Optional | - |
| `proration_downgrade_scheme` | `str` | Optional | - |
| `accrue_charge` | `bool` | Optional | - |
| `upgrade_charge` | [`CreditType`](../../doc/models/credit-type.md) | Optional | The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if one is not provided.<br>Available values: `full`, `prorated`, `none`. |
| `downgrade_credit` | [`CreditType`](../../doc/models/credit-type.md) | Optional | The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if one is not provided.<br>Available values: `full`, `prorated`, `none`. |
| `price_point_id` | `int` | Optional | - |
| `previous_price_point_id` | `int` | Optional | - |
| `price_point_handle` | `str` | Optional | - |
| `price_point_name` | `str` | Optional | - |
| `component_handle` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "component_id": 54,
  "subscription_id": 54,
  "quantity": 78,
  "previous_quantity": 192,
  "memo": "memo6"
}
```

