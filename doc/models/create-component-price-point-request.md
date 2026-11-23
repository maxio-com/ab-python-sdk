
# Create Component Price Point Request

## Structure

`CreateComponentPricePointRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_point` | [Create Component Price Point](../../doc/models/create-component-price-point.md) \| [Create Prepaid Usage Component Price Point](../../doc/models/create-prepaid-usage-component-price-point.md) | Required | This is a container for any-of cases. |

## Example

```python
from advancedbilling.models.create_component_price_point import CreateComponentPricePoint
from advancedbilling.models.create_component_price_point_request import CreateComponentPricePointRequest
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.secondary_pricing import SecondaryPricing

create_component_price_point_request = CreateComponentPricePointRequest(
    price_point=CreateComponentPricePoint(
        name='name0',
        pricing_scheme=PricingScheme.PER_UNIT,
        prices=[
            Price(
                starting_quantity=242,
                unit_price=23.26,
                ending_quantity=40
            )
        ],
        handle='handle6',
        secondary_pricing=SecondaryPricing(
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
        ),
        secondary_pricing_scheme=PricingScheme.STAIRSTEP,
        use_site_exchange_rate=True,
        tax_included=False
    )
)
```

