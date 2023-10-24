
# Payment Method Nested Data Invoice Event

A nested data structure detailing the method of payment

## Structure

`PaymentMethodNestedDataInvoiceEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | **Default**: `'apple_pay'` |
| `masked_account_number` | `str` | Optional | - |
| `masked_routing_number` | `str` | Optional | - |
| `card_brand` | `str` | Optional | - |
| `card_expiration` | `str` | Optional | - |
| `last_four` | `str` | Optional | - |
| `masked_card_number` | `str` | Optional | - |
| `details` | `str` | Optional | - |
| `kind` | `str` | Optional | - |
| `memo` | `str` | Optional | - |
| `email` | `str` | Optional | - |

## Example (as JSON)

```json
{
  "type": "apple_pay",
  "masked_account_number": "masked_account_number6",
  "masked_routing_number": "masked_routing_number6",
  "card_brand": "card_brand6",
  "card_expiration": "card_expiration6"
}
```

