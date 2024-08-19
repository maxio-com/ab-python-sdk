
# Invoice Refund

## Structure

`InvoiceRefund`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `int` | Optional | - |
| `payment_id` | `int` | Optional | - |
| `memo` | `str` | Optional | - |
| `original_amount` | `str` | Optional | - |
| `applied_amount` | `str` | Optional | - |
| `gateway_transaction_id` | `str` | Optional | The transaction ID for the refund as returned from the payment gateway |
| `gateway_used` | `str` | Optional | - |
| `gateway_handle` | `str` | Optional | - |
| `ach_late_reject` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "transaction_id": 172,
  "payment_id": 42,
  "memo": "memo6",
  "original_amount": "original_amount6",
  "applied_amount": "applied_amount6"
}
```

