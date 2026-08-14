
# Invoice Line Item Component Cost Data

## Structure

`InvoiceLineItemComponentCostData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `rates` | [`List[ComponentCostData]`](../../doc/models/component-cost-data.md) | Optional | - |

## Example

```python
from advancedbilling.models.component_cost_data import ComponentCostData
from advancedbilling.models.invoice_line_item_component_cost_data import InvoiceLineItemComponentCostData

invoice_line_item_component_cost_data = InvoiceLineItemComponentCostData(
    rates=[
        ComponentCostData(
            component_code_id=116,
            price_point_id=226,
            product_id=94,
            quantity='quantity0',
            amount='amount6'
        )
    ]
)
```

