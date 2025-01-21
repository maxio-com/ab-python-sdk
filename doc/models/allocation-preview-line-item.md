
# Allocation Preview Line Item

## Structure

`AllocationPreviewLineItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_type` | [`LineItemTransactionType`](../../doc/models/line-item-transaction-type.md) | Optional | A handle for the line item transaction type |
| `kind` | [`AllocationPreviewLineItemKind`](../../doc/models/allocation-preview-line-item-kind.md) | Optional | A handle for the line item kind for allocation preview |
| `amount_in_cents` | `int` | Optional | - |
| `memo` | `str` | Optional | - |
| `discount_amount_in_cents` | `int` | Optional | - |
| `taxable_amount_in_cents` | `int` | Optional | - |
| `component_id` | `int` | Optional | - |
| `component_handle` | `str` | Optional | - |
| `direction` | [`AllocationPreviewDirection`](../../doc/models/allocation-preview-direction.md) | Optional | Visible when using Fine-grained Component Control |

## Example (as JSON)

```json
{
  "transaction_type": "credit",
  "kind": "quantity_based_component",
  "amount_in_cents": 24,
  "memo": "memo6",
  "discount_amount_in_cents": 172
}
```

