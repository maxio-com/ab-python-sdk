
# Create Metered Component

## Structure

`CreateMeteredComponent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `metered_component` | [`MeteredComponent`](../../doc/models/metered-component.md) | Required | - |

## Example

```python
from advancedbilling.models.create_metered_component import CreateMeteredComponent
from advancedbilling.models.metered_component import MeteredComponent
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.secondary_pricing import SecondaryPricing

create_metered_component = CreateMeteredComponent(
    metered_component=MeteredComponent(
        name='name0',
        unit_name='unit_name2',
        pricing_scheme=PricingScheme.STAIRSTEP,
        description='description0',
        handle='handle6',
        taxable=False,
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
        )
    )
)
```

