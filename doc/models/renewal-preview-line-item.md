
# Renewal Preview Line Item

## Structure

`RenewalPreviewLineItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_type` | [`LineItemTransactionType`](../../doc/models/line-item-transaction-type.md) | Optional | A handle for the line item transaction type |
| `kind` | [`LineItemKind`](../../doc/models/line-item-kind.md) | Optional | A handle for the line item kind |
| `amount_in_cents` | `int` | Optional | - |
| `memo` | `str` | Optional | - |
| `discount_amount_in_cents` | `int` | Optional | - |
| `taxable_amount_in_cents` | `int` | Optional | - |
| `product_id` | `int` | Optional | - |
| `product_name` | `str` | Optional | - |
| `component_id` | `int` | Optional | - |
| `component_handle` | `str` | Optional | - |
| `component_name` | `str` | Optional | - |
| `product_handle` | `str` | Optional | - |
| `period_range_start` | `str` | Optional | - |
| `period_range_end` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "transaction_type": "charge",
  "kind": "prepaid_usage_component",
  "amount_in_cents": 154,
  "memo": "memo0",
  "discount_amount_in_cents": 214
}
```

