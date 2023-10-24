
# Apply Payment Event Data

Example schema for an `apply_payment` event

## Structure

`ApplyPaymentEventData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `memo` | `str` | Optional | The payment memo |
| `original_amount` | `str` | Optional | The full, original amount of the payment transaction as a string in full units. Incoming payments can be split amongst several invoices, which will result in a `applied_amount` less than the `original_amount`. Example: A $100.99 payment, of which $40.11 is applied to this invoice, will have an `original_amount` of `"100.99"`. |
| `applied_amount` | `str` | Optional | The amount of the payment applied to this invoice. Incoming payments can be split amongst several invoices, which will result in a `applied_amount` less than the `original_amount`. Example: A $100.99 payment, of which $40.11 is applied to this invoice, will have an `applied_amount` of `"40.11"`. |
| `transaction_time` | `datetime` | Optional | The time the payment was applied, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z" |
| `payment_method` | [Payment Method Apple Pay Type](../../doc/models/payment-method-apple-pay-type.md) \| [Payment Method Bank Account Type](../../doc/models/payment-method-bank-account-type.md) \| [Payment Method Credit Card Type](../../doc/models/payment-method-credit-card-type.md) \| [Payment Method External Type](../../doc/models/payment-method-external-type.md) \| [Payment Method Paypal Type](../../doc/models/payment-method-paypal-type.md) \| None | Optional | This is a container for one-of cases. |
| `transaction_id` | `int` | Optional | The Chargify id of the original payment |

## Example (as JSON)

```json
{
  "memo": "memo8",
  "original_amount": "original_amount8",
  "applied_amount": "applied_amount4",
  "transaction_time": "2016-03-13T12:52:32.123Z",
  "payment_method": {
    "type": "type4"
  }
}
```

