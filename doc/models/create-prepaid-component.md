
# Create Prepaid Component

## Structure

`CreatePrepaidComponent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `prepaid_usage_component` | [`PrepaidUsageComponent`](../../doc/models/prepaid-usage-component.md) | Required | - |

## Example

```python
from advancedbilling.models.create_prepaid_component import CreatePrepaidComponent
from advancedbilling.models.credit_type import CreditType
from advancedbilling.models.overage_pricing import OveragePricing
from advancedbilling.models.prepaid_usage_component import PrepaidUsageComponent
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme

create_prepaid_component = CreatePrepaidComponent(
    prepaid_usage_component=PrepaidUsageComponent(
        name='name2',
        unit_name='unit_name4',
        pricing_scheme=PricingScheme.PER_UNIT,
        overage_pricing=OveragePricing(
            pricing_scheme=PricingScheme.STAIRSTEP,
            prices=[
                Price(
                    starting_quantity=242,
                    unit_price=23.26,
                    ending_quantity=40
                )
            ]
        ),
        description='description2',
        handle='handle8',
        taxable=False,
        prices=[
            Price(
                starting_quantity=242,
                unit_price=23.26,
                ending_quantity=40
            )
        ],
        upgrade_charge=CreditType.FULL
    )
)
```

