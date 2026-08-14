
# Component Response

## Structure

`ComponentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component` | [`Component`](../../doc/models/component.md) | Required | - |

## Example

```python
from advancedbilling.models.component import Component
from advancedbilling.models.component_response import ComponentResponse
from advancedbilling.models.item_category import ItemCategory
from advancedbilling.models.pricing_scheme import PricingScheme

component_response = ComponentResponse(
    component=Component(
        id=80,
        name='name8',
        handle='handle4',
        pricing_scheme=PricingScheme.PER_UNIT,
        unit_name='unit_name0',
        item_category=ItemCategory.ENUM_BUSINESS_SOFTWARE
    )
)
```

