
# Subscription Product Migration

## Structure

`SubscriptionProductMigration`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `int` | Optional | The ID of the target Product. Either a product_id or product_handle must be present. A Subscription can be migrated to another product for both the current Product Family and another Product Family. Note: Going to another Product Family, components will not be migrated as well. |
| `product_price_point_id` | `int` | Optional | The ID of the specified product's price point. This can be passed to migrate to a non-default price point. |
| `include_trial` | `bool` | Optional | Whether to include the trial period configured for the product price point when starting a new billing period. Note that if preserve_period is set, then include_trial will be ignored.<br><br>**Default**: `False` |
| `include_initial_charge` | `bool` | Optional | If `true` is sent initial charges will be assessed.<br><br>**Default**: `False` |
| `include_coupons` | `bool` | Optional | If `true` is sent, any coupons associated with the subscription will be applied to the migration. If `false` is sent, coupons will not be applied. Note: When migrating to a new product family, the coupon cannot migrate.<br><br>**Default**: `True` |
| `preserve_period` | `bool` | Optional | If `false` is sent, the subscription's billing period will be reset to today and the full price of the new product will be charged. If `true` is sent, the billing period will not change and a prorated charge will be issued for the new product.<br><br>**Default**: `False` |
| `product_handle` | `str` | Optional | The handle of the target Product. Either a product_id or product_handle must be present. A Subscription can be migrated to another product for both the current Product Family and another Product Family. Note: Going to another Product Family, components will not be migrated as well. |
| `product_price_point_handle` | `str` | Optional | The ID or handle of the specified product's price point. This can be passed to migrate to a non-default price point. |
| `proration` | [`Proration`](../../doc/models/proration.md) | Optional | - |

## Example (as JSON)

```json
{
  "include_trial": false,
  "include_initial_charge": false,
  "include_coupons": true,
  "preserve_period": false,
  "product_id": 8,
  "product_price_point_id": 172
}
```

