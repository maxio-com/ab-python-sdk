
# Remove Payment Event Data

Example schema for an `remove_payment` event

## Structure

`RemovePaymentEventData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `int` | Required | Transaction ID of the original payment that was removed |
| `memo` | `str` | Required | Memo of the original payment |
| `original_amount` | `str` | Optional | Full amount of the original payment |
| `applied_amount` | `str` | Required | Applied amount of the original payment |
| `transaction_time` | `datetime` | Required | Transaction time of the original payment, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z" |
| `payment_method` | [Payment Method Apple Pay](../../doc/models/payment-method-apple-pay.md) \| [Payment Method Bank Account](../../doc/models/payment-method-bank-account.md) \| [Payment Method Credit Card](../../doc/models/payment-method-credit-card.md) \| [Payment Method External](../../doc/models/payment-method-external.md) \| [Payment Method Paypal](../../doc/models/payment-method-paypal.md) | Required | A nested data structure detailing the method of payment |
| `prepayment` | `bool` | Required | The flag that shows whether the original payment was a prepayment or not |

## Example (as JSON)

```json
{
  "transaction_id": 180,
  "memo": "memo0",
  "applied_amount": "applied_amount2",
  "transaction_time": "2016-03-13T12:52:32.123Z",
  "payment_method": {
    "type": "apple_pay"
  },
  "prepayment": false,
  "original_amount": "original_amount0"
}
```

