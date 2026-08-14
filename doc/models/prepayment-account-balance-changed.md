
# Prepayment Account Balance Changed

## Structure

`PrepaymentAccountBalanceChanged`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reason` | `str` | Required | - |
| `prepayment_account_balance_in_cents` | `int` | Required | - |
| `prepayment_balance_change_in_cents` | `int` | Required | - |
| `currency_code` | `str` | Required | - |

## Example

```python
from advancedbilling.models.prepayment_account_balance_changed import PrepaymentAccountBalanceChanged

prepayment_account_balance_changed = PrepaymentAccountBalanceChanged(
    reason='reason8',
    prepayment_account_balance_in_cents=6,
    prepayment_balance_change_in_cents=18,
    currency_code='currency_code2'
)
```

