
# Create Invoice Payment

## Structure

`CreateInvoicePayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | str \| float \| None | Optional | This is a container for one-of cases. |
| `memo` | `str` | Optional | A description to be attached to the payment. |
| `method` | [`InvoicePaymentMethodType`](../../doc/models/invoice-payment-method-type.md) | Optional | The type of payment method used.<br>**Default**: `'other'` |
| `details` | `str` | Optional | Additional information related to the payment method (eg. Check #) |

## Example (as JSON)

```json
{
  "method": "other",
  "amount": "String9",
  "memo": "memo0",
  "details": "details6"
}
```

