
# Proforma Invoice Issued

## Structure

`ProformaInvoiceIssued`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Required | - |
| `number` | `str` | Required | - |
| `role` | `str` | Required | - |
| `delivery_date` | `date` | Required | - |
| `created_at` | `datetime` | Required | - |
| `due_amount` | `str` | Required | - |
| `paid_amount` | `str` | Required | - |
| `tax_amount` | `str` | Required | - |
| `total_amount` | `str` | Required | - |
| `product_name` | `str` | Required | - |
| `line_items` | [`List[InvoiceLineItemEventData]`](../../doc/models/invoice-line-item-event-data.md) | Required | - |

## Example (as JSON)

```json
{
  "uid": "uid0",
  "number": "number2",
  "role": "role6",
  "delivery_date": "2016-03-13",
  "created_at": "2016-03-13T12:52:32.123Z",
  "due_amount": "due_amount2",
  "paid_amount": "paid_amount8",
  "tax_amount": "tax_amount6",
  "total_amount": "total_amount6",
  "product_name": "product_name6",
  "line_items": [
    {
      "uid": "uid8",
      "title": "title4",
      "description": "description8",
      "quantity": 102,
      "quantity_delta": 204
    }
  ]
}
```

