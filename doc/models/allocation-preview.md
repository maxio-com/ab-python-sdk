
# Allocation Preview

## Structure

`AllocationPreview`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_date` | `str` | Optional | - |
| `end_date` | `str` | Optional | - |
| `subtotal_in_cents` | `int` | Optional | - |
| `total_tax_in_cents` | `int` | Optional | - |
| `total_discount_in_cents` | `int` | Optional | - |
| `total_in_cents` | `int` | Optional | - |
| `direction` | `str` | Optional | - |
| `proration_scheme` | `str` | Optional | - |
| `line_items` | [`List[AllocationPreviewLineItem]`](../../doc/models/allocation-preview-line-item.md) | Optional | - |
| `accrue_charge` | `bool` | Optional | - |
| `allocations` | [`List[AllocationPreviewItem]`](../../doc/models/allocation-preview-item.md) | Optional | - |

## Example (as JSON)

```json
{
  "start_date": "start_date2",
  "end_date": "end_date8",
  "subtotal_in_cents": 4,
  "total_tax_in_cents": 128,
  "total_discount_in_cents": 122
}
```

