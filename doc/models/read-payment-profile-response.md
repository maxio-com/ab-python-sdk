
# Read Payment Profile Response

## Structure

`ReadPaymentProfileResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_profile` | [Bank Account Payment Profile](../../doc/models/bank-account-payment-profile.md) \| [Credit Card Payment Profile](../../doc/models/credit-card-payment-profile.md) | Required | This is a container for one-of cases. |

## Example (as JSON)

```json
{
  "payment_profile": {
    "verified": false,
    "id": 188,
    "first_name": "first_name6",
    "last_name": "last_name4",
    "customer_id": 226,
    "current_vault": "current_vault6"
  }
}
```

