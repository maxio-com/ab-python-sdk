
# Update Secondary Pricing

Hybrid Pricing only. Changes the secondary pricing model of an existing hybrid price point. Send `pricing_scheme` (or the top-level `secondary_pricing_scheme`) every time you send this block; a block without a scheme returns `422`. Brackets sent without an `id` are added to the existing ones rather than replacing them, so to change a bracket set, update existing brackets by `id` and remove the ones you no longer want with `_destroy: true`. See [Hybrid Pricing](page:introduction/basic-concepts/hybrid-pricing).

## Structure

`UpdateSecondaryPricing`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `pricing_scheme` | [`PricingScheme`](../../doc/models/pricing-scheme.md) | Optional | The identifier for the pricing scheme. See [Product Components](https://help.chargify.com/products/product-components.html) for an overview of pricing schemes. |
| `prices` | [`List[UpdatePrice]`](../../doc/models/update-price.md) | Optional | - |

## Example

```python
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.update_price import UpdatePrice
from advancedbilling.models.update_secondary_pricing import UpdateSecondaryPricing

update_secondary_pricing = UpdateSecondaryPricing(
    pricing_scheme=PricingScheme.PER_UNIT,
    prices=[
        UpdatePrice(
            id=18,
            ending_quantity=40,
            unit_price=23.26,
            destroy=False,
            starting_quantity=242
        ),
        UpdatePrice(
            id=18,
            ending_quantity=40,
            unit_price=23.26,
            destroy=False,
            starting_quantity=242
        ),
        UpdatePrice(
            id=18,
            ending_quantity=40,
            unit_price=23.26,
            destroy=False,
            starting_quantity=242
        )
    ]
)
```

