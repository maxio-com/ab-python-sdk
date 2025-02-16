
# Allocation

## Structure

`Allocation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `allocation_id` | `int` | Optional | The allocation unique id |
| `component_id` | `int` | Optional | The integer component ID for the allocation. This references a component that you have created in your Product setup |
| `component_handle` | `str` | Optional | The handle of the component. This references a component that you have created in your Product setup |
| `subscription_id` | `int` | Optional | The integer subscription ID for the allocation. This references a unique subscription in your Site |
| `quantity` | int \| str \| None | Optional | This is a container for one-of cases. |
| `previous_quantity` | int \| str \| None | Optional | This is a container for one-of cases. |
| `memo` | `str` | Optional | The memo passed when the allocation was created |
| `timestamp` | `datetime` | Optional | The time that the allocation was recorded, in format and UTC timezone, i.e. 2012-11-20T22:00:37Z |
| `created_at` | `datetime` | Optional | Timestamp indicating when this allocation was created |
| `proration_upgrade_scheme` | `str` | Optional | The scheme used if the proration was an upgrade. This is only present when the allocation was created mid-period. |
| `proration_downgrade_scheme` | `str` | Optional | The scheme used if the proration was a downgrade. This is only present when the allocation was created mid-period. |
| `price_point_id` | `int` | Optional | - |
| `price_point_name` | `str` | Optional | - |
| `price_point_handle` | `str` | Optional | - |
| `interval` | `int` | Optional | The numerical interval. i.e. an interval of ‘30’ coupled with an interval_unit of day would mean this component price point would renew every 30 days. This property is only available for sites with Multifrequency enabled. |
| `interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Optional | A string representing the interval unit for this component price point, either month or day. This property is only available for sites with Multifrequency enabled. |
| `previous_price_point_id` | `int` | Optional | - |
| `accrue_charge` | `bool` | Optional | If the change in cost is an upgrade, this determines if the charge should accrue to the next renewal or if capture should be attempted immediately. |
| `initiate_dunning` | `bool` | Optional | If true, if the immediate component payment fails, initiate dunning for the subscription.<br>Otherwise, leave the charges on the subscription to pay for at renewal. |
| `upgrade_charge` | [`CreditType`](../../doc/models/credit-type.md) | Optional | The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if one is not provided.<br>Available values: `full`, `prorated`, `none`. |
| `downgrade_credit` | [`CreditType`](../../doc/models/credit-type.md) | Optional | The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if one is not provided.<br>Available values: `full`, `prorated`, `none`. |
| `payment` | [`PaymentForAllocation`](../../doc/models/payment-for-allocation.md) | Optional | - |
| `expires_at` | `datetime` | Optional | - |
| `used_quantity` | `int` | Optional | - |
| `charge_id` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "allocation_id": 102,
  "component_id": 144,
  "component_handle": "component_handle0",
  "subscription_id": 144,
  "quantity": 168
}
```

