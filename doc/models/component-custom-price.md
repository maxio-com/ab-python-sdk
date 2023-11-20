
# Component Custom Price

Create or update custom pricing unique to the subscription. Used in place of `price_point_id`.

## Structure

`ComponentCustomPrice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pricing_scheme` | [Pricing Scheme](../../doc/models/pricing-scheme.md) \| None | Optional | This is a container for one-of cases. |
| `prices` | [`List[Price]`](../../doc/models/price.md) | Optional | On/off components only need one price bracket starting at 1 |

## Example (as JSON)

```json
{
  "pricing_scheme": "volume",
  "prices": [
    {
      "starting_quantity": 242,
      "ending_quantity": 40,
      "unit_price": 23.26
    }
  ]
}
```

