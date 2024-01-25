
# Create Component Price Point Request

## Structure

`CreateComponentPricePointRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_point` | [Create Component Price Point](../../doc/models/create-component-price-point.md) \| [Create Prepaid Usage Component Price Point](../../doc/models/create-prepaid-usage-component-price-point.md) | Required | This is a container for any-of cases. |

## Example (as JSON)

```json
{
  "price_point": {
    "name": "name0",
    "pricing_scheme": "per_unit",
    "prices": [
      {
        "starting_quantity": 242,
        "ending_quantity": 40,
        "unit_price": 23.26
      }
    ],
    "use_site_exchange_rate": true,
    "handle": "handle6",
    "tax_included": false,
    "interval": 24,
    "interval_unit": "day"
  }
}
```

