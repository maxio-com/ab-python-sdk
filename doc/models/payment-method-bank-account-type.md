
# Payment Method Bank Account Type

## Structure

`PaymentMethodBankAccountType`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `masked_account_number` | `str` | Optional | - |
| `masked_routing_number` | `str` | Optional | - |
| `mtype` | `str` | Optional | **Default**: `'bank_account'` |

## Example (as JSON)

```json
{
  "type": "bank_account",
  "masked_account_number": "masked_account_number2",
  "masked_routing_number": "masked_routing_number2"
}
```

