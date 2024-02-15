
# Allocation Preview

## Structure

`AllocationPreview`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `start_date` | `datetime` | Optional | - |
| `end_date` | `datetime` | Optional | - |
| `subtotal_in_cents` | `long\|int` | Optional | - |
| `total_tax_in_cents` | `long\|int` | Optional | - |
| `total_discount_in_cents` | `long\|int` | Optional | - |
| `total_in_cents` | `long\|int` | Optional | - |
| `direction` | [`AllocationPreviewDirection`](../../doc/models/allocation-preview-direction.md) | Optional | - |
| `proration_scheme` | `str` | Optional | - |
| `line_items` | [`List[AllocationPreviewLineItem]`](../../doc/models/allocation-preview-line-item.md) | Optional | - |
| `accrue_charge` | `bool` | Optional | - |
| `allocations` | [`List[AllocationPreviewItem]`](../../doc/models/allocation-preview-item.md) | Optional | - |
| `period_type` | `str` | Optional | - |
| `existing_balance_in_cents` | `long\|int` | Optional | An integer representing the amount of the subscription's current balance |

## Example (as JSON)

```json
{
  "start_date": "2016-03-13T12:52:32.123Z",
  "end_date": "2016-03-13T12:52:32.123Z",
  "subtotal_in_cents": 4,
  "total_tax_in_cents": 128,
  "total_discount_in_cents": 122
}
```

