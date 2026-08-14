
# Movement Line Item

## Structure

`MovementLineItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `int` | Optional | - |
| `component_id` | `int` | Optional | For Product (or "baseline") line items, this field will have a value of `0`. |
| `price_point_id` | `int` | Optional | - |
| `name` | `str` | Optional | - |
| `mrr` | `int` | Optional | - |
| `mrr_movements` | [`List[MRRMovement]`](../../doc/models/mrr-movement.md) | Optional | - |
| `quantity` | `int` | Optional | - |
| `prev_quantity` | `int` | Optional | - |
| `recurring` | `bool` | Optional | When `true`, the line item's MRR value will contribute to the `plan` breakout. When `false`, the line item contributes to the `usage` breakout. |

## Example

```python
from advancedbilling.models.movement_line_item import MovementLineItem

movement_line_item = MovementLineItem(
    product_id=60,
    component_id=228,
    price_point_id=4,
    name='name0',
    mrr=250
)
```

