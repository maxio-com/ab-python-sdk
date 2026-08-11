
# Coupon Response

## Structure

`CouponResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `coupon` | [`Coupon`](../../doc/models/coupon.md) | Optional | - |

## Example

```python
from advancedbilling.models.coupon import Coupon
from advancedbilling.models.coupon_response import CouponResponse

coupon_response = CouponResponse(
    coupon=Coupon(
        id=196,
        name='name4',
        code='code2',
        description='description6',
        amount=97.66
    )
)
```

