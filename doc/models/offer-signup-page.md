
# Offer Signup Page

## Structure

`OfferSignupPage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `nickname` | `str` | Optional | - |
| `enabled` | `bool` | Optional | - |
| `return_url` | `str` | Optional | - |
| `return_params` | `str` | Optional | - |
| `url` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.offer_signup_page import OfferSignupPage

offer_signup_page = OfferSignupPage(
    id=78,
    nickname='nickname0',
    enabled=False,
    return_url='return_url0',
    return_params='return_params2'
)
```

