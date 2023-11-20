
# Payment Method Credit Card Type

## Structure

`PaymentMethodCreditCardType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `card_brand` | `str` | Optional | - |
| `card_expiration` | `str` | Optional | - |
| `last_four` | `str` | Optional | - |
| `masked_card_number` | `str` | Optional | - |
| `mtype` | `str` | Optional | **Default**: `'credit_card'` |

## Example (as JSON)

```json
{
  "type": "credit_card",
  "card_brand": "card_brand0",
  "card_expiration": "card_expiration8",
  "last_four": "last_four0",
  "masked_card_number": "masked_card_number4"
}
```

