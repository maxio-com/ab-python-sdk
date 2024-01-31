
# Invoice Event Payment 1

A nested data structure detailing the method of payment

## Structure

`InvoiceEventPayment1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | - |
| `masked_account_number` | `str` | Required | - |
| `masked_routing_number` | `str` | Required | - |
| `card_brand` | `str` | Required | - |
| `card_expiration` | `str` | Optional | - |
| `last_four` | `str` | Optional | - |
| `masked_card_number` | `str` | Required | - |
| `details` | `str` | Required | - |
| `kind` | `str` | Required | - |
| `memo` | `str` | Required | - |
| `email` | `str` | Required | - |

## Example (as JSON)

```json
{
  "type": "Invoice Event Payment1",
  "masked_account_number": "masked_account_number4",
  "masked_routing_number": "masked_routing_number4",
  "card_brand": "card_brand8",
  "card_expiration": "card_expiration4",
  "last_four": "last_four2",
  "masked_card_number": "masked_card_number6",
  "details": "details8",
  "kind": "kind6",
  "memo": "memo2",
  "email": "email8"
}
```

