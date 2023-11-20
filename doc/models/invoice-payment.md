
# Invoice Payment

## Structure

`InvoicePayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_time` | `str` | Optional | - |
| `memo` | `str` | Optional | - |
| `original_amount` | `str` | Optional | - |
| `applied_amount` | `str` | Optional | - |
| `payment_method` | [`InvoicePaymentMethod`](../../doc/models/invoice-payment-method.md) | Optional | - |
| `transaction_id` | `int` | Optional | - |
| `prepayment` | `bool` | Optional | - |
| `gateway_handle` | `str` | Optional | - |
| `gateway_used` | `str` | Optional | - |
| `gateway_transaction_id` | `str` | Optional | The transaction ID for the payment as returned from the payment gateway |

## Example (as JSON)

```json
{
  "transaction_time": "transaction_time4",
  "memo": "memo6",
  "original_amount": "original_amount6",
  "applied_amount": "applied_amount6",
  "payment_method": {
    "details": "details0",
    "kind": "kind8",
    "memo": "memo4",
    "type": "type0",
    "card_brand": "card_brand6"
  }
}
```

