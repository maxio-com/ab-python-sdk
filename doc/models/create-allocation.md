
# Create Allocation

## Structure

`CreateAllocation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `quantity` | `float` | Required | The allocated quantity to which to set the line-items allocated quantity. By default, this is an integer. If decimal allocations are enabled for the component, it will be a decimal number. For On/Off components, use 1for on and 0 for off. |
| `component_id` | `int` | Optional | (required for the multiple allocations endpoint) The id associated with the component for which the allocation is being made |
| `memo` | `str` | Optional | A memo to record along with the allocation |
| `proration_downgrade_scheme` | `str` | Optional | The scheme used if the proration is a downgrade. Defaults to the site setting if one is not provided. |
| `proration_upgrade_scheme` | `str` | Optional | The scheme used if the proration is an upgrade. Defaults to the site setting if one is not provided. |
| `accrue_charge` | `bool` | Optional | If the change in cost is an upgrade, this determines if the charge should accrue to the next renewal or if capture should be attempted immediately. Defaults to the site setting if one is not provided. |
| `downgrade_credit` | [`CreditType`](../../doc/models/credit-type.md) | Optional | The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if one is not provided.<br>Available values: `full`, `prorated`, `none`. |
| `upgrade_charge` | [`CreditType`](../../doc/models/credit-type.md) | Optional | The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if one is not provided.<br>Available values: `full`, `prorated`, `none`. |
| `initiate_dunning` | `bool` | Optional | If set to true, if the immediate component payment fails, initiate dunning for the subscription.<br>Otherwise, leave the charges on the subscription to pay for at renewal. Defaults to false. |
| `price_point_id` | str \| int \| None | Optional | This is a container for one-of cases. |
| `billing_schedule` | [`BillingSchedule`](../../doc/models/billing-schedule.md) | Optional | This attribute is particularly useful when you need to align billing events for different components on distinct schedules within a subscription. Please note this only works for site with Multifrequency enabled |

## Example (as JSON)

```json
{
  "quantity": 8.06,
  "component_id": 192,
  "memo": "memo4",
  "proration_downgrade_scheme": "proration_downgrade_scheme2",
  "proration_upgrade_scheme": "proration_upgrade_scheme4",
  "accrue_charge": false
}
```

