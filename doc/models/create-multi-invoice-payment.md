
# Create Multi Invoice Payment

## Structure

`CreateMultiInvoicePayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `memo` | `str` | Optional | A description to be attached to the payment. |
| `details` | `str` | Optional | Additional information related to the payment method (eg. Check #). |
| `method` | [`InvoicePaymentMethodTypeEnum`](../../doc/models/invoice-payment-method-type-enum.md) | Optional | The type of payment method used.<br>**Default**: `'other'` |
| `amount` | str \| float | Required | This is a container for one-of cases. |
| `received_on` | `str` | Optional | Date reflecting when the payment was received from a customer. Must be in the past. |
| `applications` | [`List[CreateInvoicePaymentApplication]`](../../doc/models/create-invoice-payment-application.md) | Required | - |

## Example (as JSON)

```json
{
  "method": "other",
  "amount": "String7",
  "applications": [
    {
      "invoice_uid": "invoice_uid8",
      "amount": "amount0"
    }
  ],
  "memo": "memo8",
  "details": "details4",
  "received_on": "received_on6"
}
```

