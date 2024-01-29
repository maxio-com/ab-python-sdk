
# Payment Method Nested Data

A nested data structure detailing the method of payment

## Structure

`PaymentMethodNestedData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | - |
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
  "type": "Payment Method Nested Data",
  "masked_account_number": "masked_account_number8",
  "masked_routing_number": "masked_routing_number8",
  "card_brand": "card_brand4",
  "card_expiration": "card_expiration2"
}
```

