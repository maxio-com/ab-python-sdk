
# Invoice Line Item Event Data

## Structure

`InvoiceLineItemEventData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | - |
| `title` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `quantity` | `int` | Optional | - |
| `quantity_delta` | `int` | Optional | - |
| `unit_price` | `str` | Optional | - |
| `period_range_start` | `str` | Optional | - |
| `period_range_end` | `str` | Optional | - |
| `amount` | `str` | Optional | - |
| `line_references` | `str` | Optional | - |
| `pricing_details_index` | `int` | Optional | - |
| `pricing_details` | [`List[InvoiceLineItemPricingDetail]`](../../doc/models/invoice-line-item-pricing-detail.md) | Optional | - |
| `tax_code` | `str` | Optional | - |
| `tax_amount` | `str` | Optional | - |
| `product_id` | `int` | Optional | - |
| `product_price_point_id` | `int` | Optional | - |
| `price_point_id` | `int` | Optional | - |
| `component_id` | `int` | Optional | - |
| `billing_schedule_item_id` | `int` | Optional | - |
| `custom_item` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "uid": "uid4",
  "title": "title0",
  "description": "description6",
  "quantity": 40,
  "quantity_delta": 114
}
```

