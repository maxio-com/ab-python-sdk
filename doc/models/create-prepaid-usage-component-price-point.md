
# Create Prepaid Usage Component Price Point

## Structure

`CreatePrepaidUsageComponentPricePoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `handle` | `str` | Optional | - |
| `pricing_scheme` | `str` | Required | - |
| `prices` | [`List[Price]`](../../doc/models/price.md) | Required | - |
| `overage_pricing` | [`OveragePricing`](../../doc/models/overage-pricing.md) | Required | - |
| `use_site_exchange_rate` | `bool` | Optional | Whether to use the site level exchange rate or define your own prices for each currency if you have multiple currencies defined on the site.<br>**Default**: `True` |
| `rollover_prepaid_remainder` | `bool` | Optional | Boolean which controls whether or not remaining units should be rolled over to the next period |
| `renew_prepaid_allocation` | `bool` | Optional | Boolean which controls whether or not the allocated quantity should be renewed at the beginning of each period |
| `expiration_interval` | `float` | Optional | (only for prepaid usage components where rollover_prepaid_remainder is true) The number of `expiration_interval_unit`s after which rollover amounts should expire |
| `expiration_interval_unit` | [Interval Unit](../../doc/models/interval-unit.md) \| None | Optional | This is a container for one-of cases. |

## Example (as JSON)

```json
{
  "name": "name0",
  "pricing_scheme": "pricing_scheme8",
  "prices": [
    {
      "starting_quantity": 242,
      "ending_quantity": 40,
      "unit_price": 23.26
    }
  ],
  "overage_pricing": {
    "pricing_scheme": "volume",
    "prices": [
      {
        "starting_quantity": 242,
        "ending_quantity": 40,
        "unit_price": 23.26
      }
    ]
  },
  "use_site_exchange_rate": true,
  "handle": "handle6",
  "rollover_prepaid_remainder": false,
  "renew_prepaid_allocation": false,
  "expiration_interval": 101.18
}
```

