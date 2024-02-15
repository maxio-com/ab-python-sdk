
# Subscription Component

## Structure

`SubscriptionComponent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `name` | `str` | Optional | - |
| `kind` | [`ComponentKind`](../../doc/models/component-kind.md) | Optional | A handle for the component type |
| `unit_name` | `str` | Optional | - |
| `enabled` | `bool` | Optional | (for on/off components) indicates if the component is enabled for the subscription |
| `unit_balance` | `int` | Optional | - |
| `currency` | `str` | Optional | - |
| `allocated_quantity` | int \| str \| None | Optional | This is a container for one-of cases. |
| `pricing_scheme` | [Pricing Scheme](../../doc/models/pricing-scheme.md) \| None | Optional | This is a container for one-of cases. |
| `component_id` | `int` | Optional | - |
| `component_handle` | `str` | Optional | - |
| `subscription_id` | `int` | Optional | - |
| `recurring` | `bool` | Optional | - |
| `upgrade_charge` | [`CreditType`](../../doc/models/credit-type.md) | Optional | The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if one is not provided.<br>Available values: `full`, `prorated`, `none`. |
| `downgrade_credit` | [`CreditType`](../../doc/models/credit-type.md) | Optional | The type of credit to be created when upgrading/downgrading. Defaults to the component and then site setting if one is not provided.<br>Available values: `full`, `prorated`, `none`. |
| `archived_at` | `datetime` | Optional | - |
| `price_point_id` | `int` | Optional | - |
| `price_point_handle` | `str` | Optional | - |
| `price_point_type` | [Price Point Type](../../doc/models/price-point-type.md) \| None | Optional | This is a container for one-of cases. |
| `price_point_name` | `str` | Optional | - |
| `product_family_id` | `int` | Optional | - |
| `product_family_handle` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `use_site_exchange_rate` | `bool` | Optional | - |
| `description` | `str` | Optional | - |
| `allow_fractional_quantities` | `bool` | Optional | - |
| `subscription` | [`SubscriptionComponentSubscription`](../../doc/models/subscription-component-subscription.md) | Optional | An optional object, will be returned if provided `include=subscription` query param. |
| `display_on_hosted_page` | `bool` | Optional | - |
| `interval` | `int` | Optional | The numerical interval. i.e. an interval of '30' coupled with an interval_unit of day would mean this component price point would renew every 30 days. This property is only available for sites with Multifrequency enabled. |
| `interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Optional | A string representing the interval unit for this component price point, either month or day. This property is only available for sites with Multifrequency enabled. |

## Example (as JSON)

```json
{
  "id": 20,
  "name": "name8",
  "kind": "quantity_based_component",
  "unit_name": "unit_name0",
  "enabled": false
}
```

