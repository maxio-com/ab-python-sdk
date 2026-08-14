
# Coupon Subcodes Response

## Structure

`CouponSubcodesResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_codes` | `List[str]` | Optional | - |
| `duplicate_codes` | `List[str]` | Optional | - |
| `invalid_codes` | `List[str]` | Optional | - |

## Example

```python
from advancedbilling.models.coupon_subcodes_response import CouponSubcodesResponse

coupon_subcodes_response = CouponSubcodesResponse(
    created_codes=[
        'created_codes7',
        'created_codes8'
    ],
    duplicate_codes=[
        'duplicate_codes0',
        'duplicate_codes1'
    ],
    invalid_codes=[
        'invalid_codes4'
    ]
)
```

