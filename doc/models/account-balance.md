
# Account Balance

## Structure

`AccountBalance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_in_cents` | `int` | Optional | The balance in cents. |
| `automatic_balance_in_cents` | `int` | Optional | The automatic balance in cents. |
| `remittance_balance_in_cents` | `int` | Optional | The remittance balance in cents. |

## Example

```python
from advancedbilling.models.account_balance import AccountBalance

account_balance = AccountBalance(
    balance_in_cents=166,
    automatic_balance_in_cents=76,
    remittance_balance_in_cents=212
)
```

