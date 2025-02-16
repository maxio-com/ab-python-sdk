
# Product Price Point

## Structure

`ProductPricePoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `name` | `str` | Optional | The product price point name |
| `handle` | `str` | Optional | The product price point API handle |
| `price_in_cents` | `int` | Optional | The product price point price, in integer cents |
| `interval` | `int` | Optional | The numerical interval. i.e. an interval of ‘30’ coupled with an interval_unit of day would mean this product price point would renew every 30 days |
| `interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Optional | A string representing the interval unit for this product price point, either month or day |
| `trial_price_in_cents` | `int` | Optional | The product price point trial price, in integer cents |
| `trial_interval` | `int` | Optional | The numerical trial interval. i.e. an interval of ‘30’ coupled with a trial_interval_unit of day would mean this product price point trial would last 30 days |
| `trial_interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Optional | A string representing the trial interval unit for this product price point, either month or day |
| `trial_type` | `str` | Optional | - |
| `introductory_offer` | `bool` | Optional | reserved for future use |
| `initial_charge_in_cents` | `int` | Optional | The product price point initial charge, in integer cents |
| `initial_charge_after_trial` | `bool` | Optional | - |
| `expiration_interval` | `int` | Optional | The numerical expiration interval. i.e. an expiration_interval of ‘30’ coupled with an expiration_interval_unit of day would mean this product price point would expire after 30 days |
| `expiration_interval_unit` | [`ExpirationIntervalUnit`](../../doc/models/expiration-interval-unit.md) | Optional | A string representing the expiration interval unit for this product price point, either month, day or never |
| `product_id` | `int` | Optional | The product id this price point belongs to |
| `archived_at` | `datetime` | Optional | Timestamp indicating when this price point was archived |
| `created_at` | `datetime` | Optional | Timestamp indicating when this price point was created |
| `updated_at` | `datetime` | Optional | Timestamp indicating when this price point was last updated |
| `use_site_exchange_rate` | `bool` | Optional | Whether or not to use the site's exchange rate or define your own pricing when your site has multiple currencies defined. |
| `mtype` | [`PricePointType`](../../doc/models/price-point-type.md) | Optional | The type of price point |
| `tax_included` | `bool` | Optional | Whether or not the price point includes tax |
| `subscription_id` | `int` | Optional | The subscription id this price point belongs to |
| `currency_prices` | [`List[CurrencyPrice]`](../../doc/models/currency-price.md) | Optional | An array of currency pricing data is available when multiple currencies are defined for the site. It varies based on the use_site_exchange_rate setting for the price point. This parameter is present only in the response of read endpoints, after including the appropriate query parameter. |

## Example (as JSON)

```json
{
  "id": 196,
  "name": "name6",
  "handle": "handle2",
  "price_in_cents": 248,
  "interval": 8
}
```

