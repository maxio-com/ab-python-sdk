
# Create EBB Component

## Structure

`CreateEBBComponent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `event_based_component` | [`EBBComponent`](../../doc/models/ebb-component.md) | Required | - |

## Example

```python
from advancedbilling.models.component_price_point_item import ComponentPricePointItem
from advancedbilling.models.create_ebb_component import CreateEBBComponent
from advancedbilling.models.ebb_component import EBBComponent
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme

create_ebb_component = CreateEBBComponent(
    event_based_component=EBBComponent(
        name='name8',
        unit_name='unit_name0',
        pricing_scheme=PricingScheme.STAIRSTEP,
        event_based_billing_metric_id=68,
        description='description8',
        handle='handle4',
        taxable=False,
        prices=[
            Price(
                starting_quantity=242,
                unit_price=23.26,
                ending_quantity=40
            )
        ],
        price_points=[
            ComponentPricePointItem(
                name='name2',
                handle='handle8',
                pricing_scheme=PricingScheme.PER_UNIT,
                interval=92,
                interval_unit=IntervalUnit.DAY
            )
        ]
    )
)
```

