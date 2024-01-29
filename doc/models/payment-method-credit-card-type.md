
# Payment Method Credit Card Type

## Structure

`PaymentMethodCreditCardType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_brand` | `str` | Required | - |
| `card_expiration` | `str` | Optional | - |
| `last_four` | `str` | Optional | - |
| `masked_card_number` | `str` | Required | - |
| `mtype` | `str` | Required | **Default**: `'credit_card'` |

## Example (as JSON)

```json
{
  "card_brand": "card_brand0",
  "masked_card_number": "masked_card_number4",
  "type": "credit_card",
  "card_expiration": "card_expiration8",
  "last_four": "last_four0"
}
```

