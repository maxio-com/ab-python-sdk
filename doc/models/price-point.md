
# Price Point

## Structure

`PricePoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | - |
| `handle` | `str` | Optional | - |
| `pricing_scheme` | `str` | Optional | - |
| `prices` | [`List[Price]`](../../doc/models/price.md) | Optional | - |
| `use_site_exchange_rate` | `bool` | Optional | Whether to use the site level exchange rate or define your own prices for each currency if you have multiple currencies defined on the site.<br>**Default**: `True` |
| `overage_pricing` | [`OveragePricing`](../../doc/models/overage-pricing.md) | Optional | - |
| `rollover_prepaid_remainder` | `bool` | Optional | Boolean which controls whether or not remaining units should be rolled over to the next period |
| `renew_prepaid_allocation` | `bool` | Optional | Boolean which controls whether or not the allocated quantity should be renewed at the beginning of each period |
| `expiration_interval` | `float` | Optional | (only for prepaid usage components where rollover_prepaid_remainder is true) The number of `expiration_interval_unit`s after which rollover amounts should expire |
| `expiration_interval_unit` | [Interval Unit](../../doc/models/interval-unit-enum.md) \| None | Optional | This is a container for one-of cases. |

## Example (as JSON)

```json
{
  "use_site_exchange_rate": true,
  "name": "name0",
  "handle": "handle6",
  "pricing_scheme": "pricing_scheme8",
  "prices": [
    {
      "starting_quantity": 242,
      "ending_quantity": 40,
      "unit_price": 10
    }
  ]
}
```

