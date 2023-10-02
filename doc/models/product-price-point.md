
# Product Price Point

## Structure

`ProductPricePoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `name` | `str` | Optional | - |
| `handle` | `str` | Optional | - |
| `price_in_cents` | `int` | Optional | - |
| `interval` | `int` | Optional | - |
| `interval_unit` | `str` | Optional | - |
| `trial_price_in_cents` | `int` | Optional | - |
| `trial_interval` | `int` | Optional | - |
| `trial_interval_unit` | `str` | Optional | - |
| `trial_type` | `str` | Optional | - |
| `introductory_offer` | `bool` | Optional | reserved for future use |
| `initial_charge_in_cents` | `int` | Optional | - |
| `initial_charge_after_trial` | `bool` | Optional | - |
| `expiration_interval` | `int` | Optional | - |
| `expiration_interval_unit` | `str` | Optional | - |
| `product_id` | `int` | Optional | - |
| `archived_at` | `str` | Optional | - |
| `created_at` | `str` | Optional | - |
| `updated_at` | `str` | Optional | - |
| `use_site_exchange_rate` | `bool` | Optional | Whether or not to use the site's exchange rate or define your own pricing when your site has multiple currencies defined. |
| `mtype` | [`PricePointTypeEnum`](../../doc/models/price-point-type-enum.md) | Optional | Price point type. We expose the following types:<br><br>1. **default**: a price point that is marked as a default price for a certain product.<br>2. **custom**: a custom price point.<br>3. **catalog**: a price point that is **not** marked as a default price for a certain product and is **not** a custom one. |
| `tax_included` | `bool` | Optional | - |
| `subscription_id` | `int` | Optional | - |

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

