
# Create Prepayment

## Structure

`CreatePrepayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | `float` | Required | - |
| `details` | `str` | Required | - |
| `memo` | `str` | Required | - |
| `method` | [`PrepaymentMethodEnum`](../../doc/models/prepayment-method-enum.md) | Required | :- When the `method` specified is `"credit_card_on_file"`, the prepayment amount will be collected using the default credit card payment profile and applied to the prepayment account balance. This is especially useful for manual replenishment of prepaid subscriptions. |
| `payment_profile_id` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "amount": 23.92,
  "details": "details6",
  "memo": "memo0",
  "method": "paypal_account",
  "payment_profile_id": 240
}
```

