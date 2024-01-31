
# Payment Method Credit Card

## Structure

`PaymentMethodCreditCard`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_brand` | `str` | Required | - |
| `card_expiration` | `str` | Optional | - |
| `last_four` | `str` | Optional | - |
| `masked_card_number` | `str` | Required | - |
| `mtype` | [`InvoiceEventPaymentMethod`](../../doc/models/invoice-event-payment-method.md) | Required | - |

## Example (as JSON)

```json
{
  "card_brand": "card_brand4",
  "card_expiration": "card_expiration2",
  "last_four": "last_four4",
  "masked_card_number": "masked_card_number0",
  "type": "external"
}
```

