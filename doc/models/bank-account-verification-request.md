
# Bank Account Verification Request

## Structure

`BankAccountVerificationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account_verification` | [`BankAccountVerification`](../../doc/models/bank-account-verification.md) | Required | - |

## Example

```python
from advancedbilling.models.bank_account_verification import BankAccountVerification
from advancedbilling.models.bank_account_verification_request import BankAccountVerificationRequest

bank_account_verification_request = BankAccountVerificationRequest(
    bank_account_verification=BankAccountVerification(
        deposit_1_in_cents=244,
        deposit_2_in_cents=6
    )
)
```

