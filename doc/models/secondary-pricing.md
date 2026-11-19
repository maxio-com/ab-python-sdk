
# Secondary Pricing

Hybrid Pricing only. The secondary pricing model that takes over once usage passes the primary model's included threshold. Applies to Quantity-Based and Metered Components on Sites with Hybrid Pricing enabled; ignored otherwise. Its `prices` brackets start at `1`, not at the primary model's highest `ending_quantity`. See [Hybrid Pricing](page:introduction/basic-concepts/hybrid-pricing).

## Structure

`SecondaryPricing`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pricing_scheme` | [`PricingScheme`](../../doc/models/pricing-scheme.md) | Optional | Required, unless you send the top-level `secondary_pricing_scheme` instead (Create and Update Component Price Point only). A block with neither returns `422` (`Secondary pricing scheme must be defined`). |
| `prices` | [`List[Price]`](../../doc/models/price.md) | Optional | - |

## Example

```python
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.secondary_pricing import SecondaryPricing

secondary_pricing = SecondaryPricing(
    pricing_scheme=PricingScheme.STAIRSTEP,
    prices=[
        Price(
            starting_quantity=242,
            unit_price=23.26,
            ending_quantity=40
        ),
        Price(
            starting_quantity=242,
            unit_price=23.26,
            ending_quantity=40
        )
    ]
)
```

