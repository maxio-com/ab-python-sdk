
# Agreement Acceptance

Required when creating a subscription with Maxio Payments.

## Structure

`AgreementAcceptance`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ip_address` | `str` | Optional | Required when providing agreement acceptance params. |
| `terms_url` | `str` | Optional | Required when creating a subscription with Maxio Payments. Either terms_url or privacy_policy_url is required when providing agreement_acceptance params. |
| `privacy_policy_url` | `str` | Optional | - |
| `return_refund_policy_url` | `str` | Optional | - |
| `delivery_policy_url` | `str` | Optional | - |
| `secure_checkout_policy_url` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.agreement_acceptance import AgreementAcceptance

agreement_acceptance = AgreementAcceptance(
    ip_address='ip_address8',
    terms_url='terms_url6',
    privacy_policy_url='privacy_policy_url4',
    return_refund_policy_url='return_refund_policy_url0',
    delivery_policy_url='delivery_policy_url4'
)
```

