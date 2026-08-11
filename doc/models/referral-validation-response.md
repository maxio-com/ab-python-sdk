
# Referral Validation Response

## Structure

`ReferralValidationResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `referral_code` | [`ReferralCode`](../../doc/models/referral-code.md) | Optional | - |

## Example

```python
from advancedbilling.models.referral_code import ReferralCode
from advancedbilling.models.referral_validation_response import ReferralValidationResponse

referral_validation_response = ReferralValidationResponse(
    referral_code=ReferralCode(
        id=46,
        site_id=228,
        subscription_id=156,
        code='code0'
    )
)
```

