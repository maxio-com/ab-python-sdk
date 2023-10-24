
# Overage Pricing

## Structure

`OveragePricing`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pricing_scheme` | [Pricing Scheme](../../doc/models/pricing-scheme.md) | Required | This is a container for one-of cases. |
| `prices` | [`List[Price]`](../../doc/models/price.md) | Optional | - |

## Example (as JSON)

```json
{
  "pricing_scheme": "volume",
  "prices": [
    {
      "starting_quantity": 242,
      "ending_quantity": 40,
      "unit_price": 23.26
    },
    {
      "starting_quantity": 242,
      "ending_quantity": 40,
      "unit_price": 23.26
    },
    {
      "starting_quantity": 242,
      "ending_quantity": 40,
      "unit_price": 23.26
    }
  ]
}
```

