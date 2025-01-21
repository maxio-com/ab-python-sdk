
# Credit Account Balance Changed

## Structure

`CreditAccountBalanceChanged`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | `str` | Required | - |
| `service_credit_account_balance_in_cents` | `int` | Required | - |
| `service_credit_balance_change_in_cents` | `int` | Required | - |
| `currency_code` | `str` | Required | - |
| `at_time` | `datetime` | Required | - |

## Example (as JSON)

```json
{
  "reason": "reason8",
  "service_credit_account_balance_in_cents": 10,
  "service_credit_balance_change_in_cents": 116,
  "currency_code": "currency_code8",
  "at_time": "2016-03-13T12:52:32.123Z"
}
```

