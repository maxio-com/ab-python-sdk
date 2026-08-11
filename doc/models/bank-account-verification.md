
# Bank Account Verification

## Structure

`BankAccountVerification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `deposit_1_in_cents` | `int` | Optional | - |
| `deposit_2_in_cents` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.bank_account_verification import BankAccountVerification

bank_account_verification = BankAccountVerification(
    deposit_1_in_cents=244,
    deposit_2_in_cents=6
)
```

