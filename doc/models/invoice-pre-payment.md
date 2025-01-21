
# Invoice Pre Payment

## Structure

`InvoicePrePayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Optional | The subscription id for the prepayment account |
| `amount_in_cents` | `int` | Optional | The amount in cents of the prepayment that was created as a result of this payment. |
| `ending_balance_in_cents` | `int` | Optional | The total balance of the prepayment account for this subscription including any prior prepayments |

## Example (as JSON)

```json
{
  "subscription_id": 180,
  "amount_in_cents": 100,
  "ending_balance_in_cents": 60
}
```

