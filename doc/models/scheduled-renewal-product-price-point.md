
# Scheduled Renewal Product Price Point

Custom pricing for a product within a scheduled renewal.

## Structure

`ScheduledRenewalProductPricePoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | (Optional) |
| `handle` | `str` | Optional | (Optional) |
| `price_in_cents` | str \| int | Required | This is a container for one-of cases. |
| `interval` | str \| int | Required | This is a container for one-of cases. |
| `interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Required | Required if using `custom_price` attribute. |
| `tax_included` | `bool` | Optional | (Optional) |
| `initial_charge_in_cents` | `int` | Optional | The product price point initial charge, in integer cents. |
| `expiration_interval` | `int` | Optional | The numerical expiration interval. i.e. an expiration_interval of ‘30’ coupled with an expiration_interval_unit of day would mean this product price point would expire after 30 days. |
| `expiration_interval_unit` | [`ExpirationIntervalUnit`](../../doc/models/expiration-interval-unit.md) | Optional | A string representing the expiration interval unit for this product price point, either month, day or never |

## Example (as JSON)

```json
{
  "name": "name4",
  "handle": "handle0",
  "price_in_cents": "String3",
  "interval": "String9",
  "interval_unit": "day",
  "tax_included": false,
  "initial_charge_in_cents": 86,
  "expiration_interval": 108
}
```

