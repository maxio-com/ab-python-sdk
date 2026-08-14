
# Referral Code

## Structure

`ReferralCode`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `site_id` | `int` | Optional | - |
| `subscription_id` | `int` | Optional | - |
| `code` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.referral_code import ReferralCode

referral_code = ReferralCode(
    id=46,
    site_id=228,
    subscription_id=156,
    code='code0'
)
```

