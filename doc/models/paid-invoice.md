
# Paid Invoice

## Structure

`PaidInvoice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoice_id` | `str` | Optional | The uid of the paid invoice |
| `status` | [`InvoiceStatus`](../../doc/models/invoice-status.md) | Optional | The current status of the invoice. See [Invoice Statuses](https://chargify.zendesk.com/hc/en-us/articles/4407737494171#line-item-breakdowns) for more. |
| `due_amount` | `str` | Optional | The remaining due amount on the invoice |
| `paid_amount` | `str` | Optional | The total amount paid on this invoice (including any prior payments) |

## Example (as JSON)

```json
{
  "invoice_id": "invoice_id6",
  "status": "draft",
  "due_amount": "due_amount8",
  "paid_amount": "paid_amount8"
}
```

