
# Bank Account Response

## Structure

`BankAccountResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_profile` | [`BankAccountPaymentProfile`](../../doc/models/bank-account-payment-profile.md) | Required | - |

## Example

```python
from advancedbilling.models.bank_account_payment_profile import BankAccountPaymentProfile
from advancedbilling.models.bank_account_response import BankAccountResponse
from advancedbilling.models.bank_account_vault import BankAccountVault
from advancedbilling.models.payment_type import PaymentType

bank_account_response = BankAccountResponse(
    payment_profile=BankAccountPaymentProfile(
        payment_type=PaymentType.BANK_ACCOUNT,
        id=44,
        first_name='first_name4',
        last_name='last_name2',
        customer_id=82,
        current_vault=BankAccountVault.AUTHORIZENET,
        verified=False
    )
)
```

