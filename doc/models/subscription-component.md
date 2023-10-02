
# Subscription Component

## Structure

`SubscriptionComponent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `name` | `str` | Optional | - |
| `kind` | `str` | Optional | - |
| `unit_name` | `str` | Optional | - |
| `enabled` | `bool` | Optional | (for on/off components) indicates if the component is enabled for the subscription |
| `unit_balance` | `int` | Optional | - |
| `currency` | `str` | Optional | - |
| `allocated_quantity` | `int` | Optional | For Quantity-based components: The current allocation for the component on the given subscription. For On/Off components: Use 1 for on. Use 0 for off. |
| `pricing_scheme` | `str` | Optional | - |
| `component_id` | `int` | Optional | - |
| `component_handle` | `str` | Optional | - |
| `subscription_id` | `int` | Optional | - |
| `recurring` | `bool` | Optional | - |
| `upgrade_charge` | `str` | Optional | - |
| `downgrade_credit` | `str` | Optional | - |
| `archived_at` | `str` | Optional | - |
| `price_point_id` | `int` | Optional | - |
| `price_point_handle` | `str` | Optional | - |
| `price_point_type` | [Price Point Type](../../doc/models/price-point-type-enum.md) \| None | Optional | This is a container for one-of cases. |
| `price_point_name` | `str` | Optional | - |
| `product_family_id` | `int` | Optional | - |
| `product_family_handle` | `str` | Optional | - |
| `created_at` | `str` | Optional | - |
| `updated_at` | `str` | Optional | - |
| `use_site_exchange_rate` | `bool` | Optional | - |
| `description` | `str` | Optional | - |
| `allow_fractional_quantities` | `bool` | Optional | - |
| `subscription` | [`SubscriptionComponentSubscription`](../../doc/models/subscription-component-subscription.md) | Optional | An optional object, will be returned if provided `include=subscription` query param. |

## Example (as JSON)

```json
{
  "id": 20,
  "name": "name8",
  "kind": "kind6",
  "unit_name": "unit_name0",
  "enabled": false
}
```

