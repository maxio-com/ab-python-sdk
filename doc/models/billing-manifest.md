
# Billing Manifest

## Structure

`BillingManifest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `line_items` | [`List[BillingManifestItem]`](../../doc/models/billing-manifest-item.md) | Optional | - |
| `total_in_cents` | `int` | Optional | - |
| `total_discount_in_cents` | `int` | Optional | - |
| `total_tax_in_cents` | `int` | Optional | - |
| `subtotal_in_cents` | `int` | Optional | - |
| `start_date` | `str` | Optional | - |
| `end_date` | `str` | Optional | - |
| `period_type` | `str` | Optional | - |
| `existing_balance_in_cents` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "line_items": [
    {
      "transaction_type": "transaction_type0",
      "kind": "kind6",
      "amount_in_cents": 24,
      "memo": "memo2",
      "discount_amount_in_cents": 172
    },
    {
      "transaction_type": "transaction_type0",
      "kind": "kind6",
      "amount_in_cents": 24,
      "memo": "memo2",
      "discount_amount_in_cents": 172
    },
    {
      "transaction_type": "transaction_type0",
      "kind": "kind6",
      "amount_in_cents": 24,
      "memo": "memo2",
      "discount_amount_in_cents": 172
    }
  ],
  "total_in_cents": 192,
  "total_discount_in_cents": 178,
  "total_tax_in_cents": 172,
  "subtotal_in_cents": 48
}
```

