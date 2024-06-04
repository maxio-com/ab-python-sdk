
# Payment Method Bank Account

## Structure

`PaymentMethodBankAccount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `masked_account_number` | `str` | Required | - |
| `masked_routing_number` | `str` | Required | - |
| `mtype` | [`InvoiceEventPaymentMethod`](../../doc/models/invoice-event-payment-method.md) | Required | - |

## Example (as JSON)

```json
{
  "masked_account_number": "masked_account_number2",
  "masked_routing_number": "masked_routing_number2",
  "type": "bank_account"
}
```

