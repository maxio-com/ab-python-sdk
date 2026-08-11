
# Overage Pricing

## Structure

`OveragePricing`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pricing_scheme` | [`PricingScheme`](../../doc/models/pricing-scheme.md) | Required | The identifier for the pricing scheme. See [Product Components](https://help.chargify.com/products/product-components.html) for an overview of pricing schemes. |
| `prices` | [`List[Price]`](../../doc/models/price.md) | Optional | - |

## Example

```python
from advancedbilling.models.overage_pricing import OveragePricing
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme

overage_pricing = OveragePricing(
    pricing_scheme=PricingScheme.STAIRSTEP,
    prices=[
        Price(
            starting_quantity=242,
            unit_price=23.26,
            ending_quantity=40
        )
    ]
)
```

