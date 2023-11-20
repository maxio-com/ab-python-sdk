
# Prepayment Account Balance Changed

## Structure

`PrepaymentAccountBalanceChanged`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | `str` | Required | - |
| `prepayment_account_balance_in_cents` | `long\|int` | Required | - |
| `prepayment_balance_change_in_cents` | `long\|int` | Required | - |
| `currency_code` | `str` | Required | - |

## Example (as JSON)

```json
{
  "reason": "reason4",
  "prepayment_account_balance_in_cents": 182,
  "prepayment_balance_change_in_cents": 206,
  "currency_code": "currency_code4"
}
```

