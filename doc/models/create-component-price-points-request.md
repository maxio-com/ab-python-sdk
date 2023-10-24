
# Create Component Price Points Request

## Structure

`CreateComponentPricePointsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_points` | List[[Create Component Price Point](../../doc/models/create-component-price-point.md) \| [Create Prepaid Usage Component Price Point](../../doc/models/create-prepaid-usage-component-price-point.md)] | Required | This is List of a container for any-of cases. |

## Example (as JSON)

```json
{
  "price_points": [
    {
      "name": "name0",
      "handle": "handle6",
      "pricing_scheme": "pricing_scheme8",
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
      ],
      "use_site_exchange_rate": false
    },
    {
      "name": "name0",
      "handle": "handle6",
      "pricing_scheme": "pricing_scheme8",
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
      ],
      "use_site_exchange_rate": false
    }
  ]
}
```

