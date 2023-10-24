
# Custom Price Used for Subscription Create Update

(Optional) Used in place of `product_price_point_id` to define a custom price point unique to the subscription

## Structure

`CustomPriceUsedForSubscriptionCreateUpdate`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | (Optional) |
| `handle` | `str` | Optional | (Optional) |
| `price_in_cents` | str \| int \| None | Optional | This is a container for one-of cases. |
| `interval` | str \| int \| None | Optional | This is a container for one-of cases. |
| `interval_unit` | [Interval Unit](../../doc/models/interval-unit.md) \| None | Optional | This is a container for one-of cases. |
| `trial_price_in_cents` | str \| int \| None | Optional | This is a container for one-of cases. |
| `trial_interval` | str \| int \| None | Optional | This is a container for one-of cases. |
| `trial_interval_unit` | [Interval Unit](../../doc/models/interval-unit.md) \| None | Optional | This is a container for one-of cases. |
| `initial_charge_in_cents` | str \| int \| None | Optional | This is a container for one-of cases. |
| `initial_charge_after_trial` | `bool` | Optional | (Optional) |
| `expiration_interval` | str \| int \| None | Optional | This is a container for one-of cases. |
| `expiration_interval_unit` | [Interval Unit](../../doc/models/interval-unit.md) \| None | Optional | This is a container for one-of cases. |
| `tax_included` | `bool` | Optional | (Optional) |

## Example (as JSON)

```json
{
  "name": "name4",
  "handle": "handle0",
  "price_in_cents": "String3",
  "interval": "String3",
  "interval_unit": "day"
}
```

