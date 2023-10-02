
# Movement Line Item

## Structure

`MovementLineItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `product_id` | `int` | Optional | - |
| `component_id` | `int` | Optional | For Product (or "baseline") line items, this field will have a value of `0`. |
| `name` | `str` | Optional | - |
| `mrr` | `int` | Optional | - |
| `mrr_movements` | [`List[MRRMovement]`](../../doc/models/mrr-movement.md) | Optional | - |
| `quantity` | `int` | Optional | - |
| `prev_quantity` | `int` | Optional | - |
| `recurring` | `bool` | Optional | When `true`, the line item's MRR value will contribute to the `plan` breakout. When `false`, the line item contributes to the `usage` breakout. |

## Example (as JSON)

```json
{
  "product_id": 156,
  "component_id": 68,
  "name": "name6",
  "mrr": 154,
  "mrr_movements": [
    {
      "amount": 90,
      "category": "category4"
    },
    {
      "amount": 90,
      "category": "category4"
    },
    {
      "amount": 90,
      "category": "category4"
    }
  ]
}
```

