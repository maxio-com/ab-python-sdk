
# Chjs Tokenization Success

## Structure

`ChjsTokenizationSuccess`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_profile` | [`TokenizedPaymentProfile`](../../doc/models/tokenized-payment-profile.md) | Required | - |
| `gateway_customer_id` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.chjs_tokenization_success import ChjsTokenizationSuccess
from advancedbilling.models.tokenized_payment_profile import TokenizedPaymentProfile

chjs_tokenization_success = ChjsTokenizationSuccess(
    payment_profile=TokenizedPaymentProfile(
        id=44,
        vault_token='vault_token6',
        gateway_handle='gateway_handle4',
        customer_vault_token='customer_vault_token2'
    ),
    gateway_customer_id=106
)
```

