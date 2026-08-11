
# Create Quantity Based Component

## Structure

`CreateQuantityBasedComponent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `quantity_based_component` | [`QuantityBasedComponent`](../../doc/models/quantity-based-component.md) | Required | - |

## Example

```python
from advancedbilling.models.create_quantity_based_component import CreateQuantityBasedComponent
from advancedbilling.models.credit_type import CreditType
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.quantity_based_component import QuantityBasedComponent

create_quantity_based_component = CreateQuantityBasedComponent(
    quantity_based_component=QuantityBasedComponent(
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
            )
        ],
        upgrade_charge=CreditType.PRORATED
    )
)
```

