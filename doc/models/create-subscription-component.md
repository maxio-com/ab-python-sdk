
# Create Subscription Component

## Structure

`CreateSubscriptionComponent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | int \| str \| None | Optional | This is a container for one-of cases. |
| `enabled` | `bool` | Optional | Used for on/off components only. |
| `unit_balance` | `int` | Optional | Used for metered and events based components. |
| `allocated_quantity` | int \| str \| None | Optional | This is a container for one-of cases. |
| `quantity` | `int` | Optional | Deprecated. Use `allocated_quantity` instead. |
| `price_point_id` | int \| str \| None | Optional | This is a container for one-of cases. |
| `custom_price` | [`ComponentCustomPrice`](../../doc/models/component-custom-price.md) | Optional | Create or update custom pricing unique to the subscription. Used in place of `price_point_id`. |

## Example (as JSON)

```json
{
  "component_id": 8,
  "enabled": false,
  "unit_balance": 144,
  "allocated_quantity": 102,
  "quantity": 188
}
```

