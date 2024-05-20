
# Apply Payment Event Data

Example schema for an `apply_payment` event

## Structure

`ApplyPaymentEventData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `consolidation_level` | [`InvoiceConsolidationLevel`](../../doc/models/invoice-consolidation-level.md) | Required | - |
| `memo` | `str` | Required | The payment memo |
| `original_amount` | `str` | Required | The full, original amount of the payment transaction as a string in full units. Incoming payments can be split amongst several invoices, which will result in a `applied_amount` less than the `original_amount`. Example: A $100.99 payment, of which $40.11 is applied to this invoice, will have an `original_amount` of `"100.99"`. |
| `applied_amount` | `str` | Required | The amount of the payment applied to this invoice. Incoming payments can be split amongst several invoices, which will result in a `applied_amount` less than the `original_amount`. Example: A $100.99 payment, of which $40.11 is applied to this invoice, will have an `applied_amount` of `"40.11"`. |
| `transaction_time` | `datetime` | Required | The time the payment was applied, in ISO 8601 format, i.e. "2019-06-07T17:20:06Z" |
| `payment_method` | [Payment Method Apple Pay](../../doc/models/payment-method-apple-pay.md) \| [Payment Method Bank Account](../../doc/models/payment-method-bank-account.md) \| [Payment Method Credit Card](../../doc/models/payment-method-credit-card.md) \| [Payment Method External](../../doc/models/payment-method-external.md) \| [Payment Method Paypal](../../doc/models/payment-method-paypal.md) | Required | A nested data structure detailing the method of payment |
| `transaction_id` | `int` | Optional | The Chargify id of the original payment |
| `parent_invoice_number` | `int` | Optional | - |
| `remaining_prepayment_amount` | `str` | Optional | - |
| `prepayment` | `bool` | Optional | - |
| `external` | `bool` | Optional | - |

## Example (as JSON)

```json
{
  "consolidation_level": "child",
  "memo": "memo8",
  "original_amount": "original_amount8",
  "applied_amount": "applied_amount4",
  "transaction_time": "2016-03-13T12:52:32.123Z",
  "payment_method": {
    "type": "apple_pay"
  },
  "transaction_id": 196,
  "parent_invoice_number": 174,
  "remaining_prepayment_amount": "remaining_prepayment_amount6",
  "prepayment": false,
  "external": false
}
```

