
# Billing Manifest Item

## Structure

`BillingManifestItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_type` | [`LineItemTransactionType`](../../doc/models/line-item-transaction-type.md) | Optional | A handle for the line item transaction type |
| `kind` | [`BillingManifestLineItemKind`](../../doc/models/billing-manifest-line-item-kind.md) | Optional | A handle for the billing manifest line item kind |
| `amount_in_cents` | `long\|int` | Optional | - |
| `memo` | `str` | Optional | - |
| `discount_amount_in_cents` | `long\|int` | Optional | - |
| `taxable_amount_in_cents` | `long\|int` | Optional | - |
| `component_id` | `int` | Optional | - |
| `component_handle` | `str` | Optional | - |
| `component_name` | `str` | Optional | - |
| `product_id` | `int` | Optional | - |
| `product_handle` | `str` | Optional | - |
| `product_name` | `str` | Optional | - |
| `period_range_start` | `str` | Optional | - |
| `period_range_end` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "transaction_type": "info_transaction",
  "kind": "baseline",
  "amount_in_cents": 216,
  "memo": "memo4",
  "discount_amount_in_cents": 236
}
```

