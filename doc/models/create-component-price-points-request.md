
# Create Component Price Points Request

## Structure

`CreateComponentPricePointsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_points` | List[[Create Component Price Point](../../doc/models/create-component-price-point.md) \| [Create Prepaid Usage Component Price Point](../../doc/models/create-prepaid-usage-component-price-point.md)] | Required | This is List of a container for any-of cases. |

## Example

```python
from advancedbilling.models.create_component_price_point import CreateComponentPricePoint
from advancedbilling.models.create_component_price_points_request import CreateComponentPricePointsRequest
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.secondary_pricing import SecondaryPricing

create_component_price_points_request = CreateComponentPricePointsRequest(
    price_points=[
        CreateComponentPricePoint(
            name='name0',
            pricing_scheme=PricingScheme.PER_UNIT,
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
                ),
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
            use_site_exchange_rate=False,
            tax_included=False
        ),
        CreateComponentPricePoint(
            name='name0',
            pricing_scheme=PricingScheme.PER_UNIT,
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
                ),
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
            use_site_exchange_rate=False,
            tax_included=False
        )
    ]
)
```

