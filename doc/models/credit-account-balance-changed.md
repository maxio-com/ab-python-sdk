
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

## Example

```python
import dateutil.parser

from advancedbilling.models.credit_account_balance_changed import CreditAccountBalanceChanged

credit_account_balance_changed = CreditAccountBalanceChanged(
    reason='reason8',
    service_credit_account_balance_in_cents=64,
    service_credit_balance_change_in_cents=190,
    currency_code='currency_code8',
    at_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

