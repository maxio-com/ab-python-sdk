
# Clone Component Price Point Request

## Structure

`CloneComponentPricePointRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_point` | [`CloneComponentPricePoint`](../../doc/models/clone-component-price-point.md) | Required | - |

## Example

```python
from advancedbilling.models.clone_component_price_point import CloneComponentPricePoint
from advancedbilling.models.clone_component_price_point_request import CloneComponentPricePointRequest

clone_component_price_point_request = CloneComponentPricePointRequest(
    price_point=CloneComponentPricePoint(
        name='name0',
        handle='handle6'
    )
)
```

