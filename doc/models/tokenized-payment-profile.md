
# Tokenized Payment Profile

## Structure

`TokenizedPaymentProfile`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `vault_token` | `str` | Optional | - |
| `gateway_handle` | `str` | Optional | - |
| `customer_vault_token` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.tokenized_payment_profile import TokenizedPaymentProfile

tokenized_payment_profile = TokenizedPaymentProfile(
    id=216,
    vault_token='vault_token4',
    gateway_handle='gateway_handle6',
    customer_vault_token='customer_vault_token0'
)
```

