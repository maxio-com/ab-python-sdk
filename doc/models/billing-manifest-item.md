
# Billing Manifest Item

## Structure

`BillingManifestItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_type` | `str` | Optional | - |
| `kind` | `str` | Optional | - |
| `amount_in_cents` | `int` | Optional | - |
| `memo` | `str` | Optional | - |
| `discount_amount_in_cents` | `int` | Optional | - |
| `taxable_amount_in_cents` | `int` | Optional | - |
| `component_id` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "transaction_type": "transaction_type2",
  "kind": "kind8",
  "amount_in_cents": 216,
  "memo": "memo4",
  "discount_amount_in_cents": 236
}
```

