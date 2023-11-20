
# Remove Payment Event Data

Example schema for an `remove_payment` event

## Structure

`RemovePaymentEventData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transaction_id` | `int` | Optional | Transaction ID of the original payment that was removed |
| `memo` | `str` | Optional | Memo of the original payment |
| `original_amount` | `str` | Optional | Full amount of the original payment |
| `applied_amount` | `str` | Optional | Applied amount of the original payment |
| `transaction_time` | `datetime` | Optional | Transaction time of the original payment, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z" |
| `payment_method` | [Payment Method Apple Pay Type](../../doc/models/payment-method-apple-pay-type.md) \| [Payment Method Bank Account Type](../../doc/models/payment-method-bank-account-type.md) \| [Payment Method Credit Card Type](../../doc/models/payment-method-credit-card-type.md) \| [Payment Method External Type](../../doc/models/payment-method-external-type.md) \| [Payment Method Paypal Type](../../doc/models/payment-method-paypal-type.md) \| None | Optional | This is a container for one-of cases. |
| `prepayment` | `bool` | Optional | The flag that shows whether the original payment was a prepayment or not |

## Example (as JSON)

```json
{
  "transaction_id": 180,
  "memo": "memo0",
  "original_amount": "original_amount0",
  "applied_amount": "applied_amount2",
  "transaction_time": "2016-03-13T12:52:32.123Z"
}
```

