
# Create Product Price Point

## Structure

`CreateProductPricePoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | The product price point name |
| `handle` | `str` | Optional | The product price point API handle |
| `price_in_cents` | `long\|int` | Required | The product price point price, in integer cents |
| `interval` | `int` | Required | The numerical interval. i.e. an interval of ‘30’ coupled with an interval_unit of day would mean this product price point would renew every 30 days |
| `interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Required | A string representing the interval unit for this product price point, either month or day |
| `trial_price_in_cents` | `long\|int` | Optional | The product price point trial price, in integer cents |
| `trial_interval` | `int` | Optional | The numerical trial interval. i.e. an interval of ‘30’ coupled with an trial_interval_unit of day would mean this product price point would renew every 30 days |
| `trial_interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Optional | A string representing the trial interval unit for this product price point, either month or day |
| `trial_type` | `str` | Optional | - |
| `initial_charge_in_cents` | `long\|int` | Optional | The product price point initial charge, in integer cents |
| `initial_charge_after_trial` | `bool` | Optional | - |
| `expiration_interval` | `int` | Optional | The numerical expiration interval. i.e. an expiration_interval of ‘30’ coupled with an expiration_interval_unit of day would mean this product price point would expire every 30 days |
| `expiration_interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Optional | A string representing the expiration interval unit for this product price point, either month or day |
| `use_site_exchange_rate` | `bool` | Optional | Whether or not to use the site's exchange rate or define your own pricing when your site has multiple currencies defined.<br>**Default**: `True` |

## Example (as JSON)

```json
{
  "name": "name6",
  "price_in_cents": 216,
  "interval": 200,
  "interval_unit": "day",
  "use_site_exchange_rate": true,
  "handle": "handle2",
  "trial_price_in_cents": 48,
  "trial_interval": 102,
  "trial_interval_unit": "day",
  "trial_type": "trial_type0"
}
```

