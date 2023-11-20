
# Create Product Price Point

## Structure

`CreateProductPricePoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `handle` | `str` | Optional | - |
| `price_in_cents` | `long\|int` | Required | - |
| `interval` | `int` | Required | - |
| `interval_unit` | `str` | Required | - |
| `trial_price_in_cents` | `long\|int` | Optional | - |
| `trial_interval` | `int` | Optional | - |
| `trial_interval_unit` | `str` | Optional | - |
| `trial_type` | `str` | Optional | - |
| `initial_charge_in_cents` | `long\|int` | Optional | - |
| `initial_charge_after_trial` | `bool` | Optional | - |
| `expiration_interval` | `int` | Optional | - |
| `expiration_interval_unit` | `str` | Optional | - |
| `use_site_exchange_rate` | `bool` | Optional | Whether or not to use the site's exchange rate or define your own pricing when your site has multiple currencies defined.<br>**Default**: `True` |

## Example (as JSON)

```json
{
  "name": "name6",
  "price_in_cents": 216,
  "interval": 200,
  "interval_unit": "interval_unit6",
  "use_site_exchange_rate": true,
  "handle": "handle2",
  "trial_price_in_cents": 48,
  "trial_interval": 102,
  "trial_interval_unit": "trial_interval_unit0",
  "trial_type": "trial_type0"
}
```

