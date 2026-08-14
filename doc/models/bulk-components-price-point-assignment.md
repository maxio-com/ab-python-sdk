
# Bulk Components Price Point Assignment

## Structure

`BulkComponentsPricePointAssignment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `components` | [`List[ComponentPricePointAssignment]`](../../doc/models/component-price-point-assignment.md) | Optional | - |

## Example

```python
from advancedbilling.models.bulk_components_price_point_assignment import BulkComponentsPricePointAssignment
from advancedbilling.models.component_price_point_assignment import ComponentPricePointAssignment

bulk_components_price_point_assignment = BulkComponentsPricePointAssignment(
    components=[
        ComponentPricePointAssignment(
            component_id=108,
            price_point='String5'
        )
    ]
)
```

