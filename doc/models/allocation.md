
# Allocation

## Structure

`Allocation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Optional | The integer component ID for the allocation. This references a component that you have created in your Product setup |
| `subscription_id` | `int` | Optional | The integer subscription ID for the allocation. This references a unique subscription in your Site |
| `quantity` | `int` | Optional | The allocated quantity set in to effect by the allocation |
| `previous_quantity` | `int` | Optional | The allocated quantity that was in effect before this allocation was created |
| `memo` | `str` | Optional | The memo passed when the allocation was created |
| `timestamp` | `str` | Optional | The time that the allocation was recorded, in  format and UTC timezone, i.e. 2012-11-20T22:00:37Z |
| `proration_upgrade_scheme` | `str` | Optional | The scheme used if the proration was an upgrade. This is only present when the allocation was created mid-period. |
| `proration_downgrade_scheme` | `str` | Optional | The scheme used if the proration was a downgrade. This is only present when the allocation was created mid-period. |
| `price_point_id` | `int` | Optional | - |
| `price_point_name` | `str` | Optional | - |
| `price_point_handle` | `str` | Optional | - |
| `previous_price_point_id` | `int` | Optional | - |
| `accrue_charge` | `bool` | Optional | If the change in cost is an upgrade, this determines if the charge should accrue to the next renewal or if capture should be attempted immediately. |
| `upgrade_charge` | `str` | Optional | The type of charge to be created if the change in cost is an upgrade. |
| `downgrade_credit` | `str` | Optional | The type of credit to be created if the change in cost is a downgrade. |
| `payment` | [Allocation Payment](../../doc/models/allocation-payment.md) \| None | Optional | This is a container for one-of cases. |

## Example (as JSON)

```json
{
  "component_id": 144,
  "subscription_id": 144,
  "quantity": 246,
  "previous_quantity": 180,
  "memo": "memo4"
}
```

