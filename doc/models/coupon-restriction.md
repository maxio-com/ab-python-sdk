
# Coupon Restriction

## Structure

`CouponRestriction`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `item_type` | [`RestrictionType`](../../doc/models/restriction-type.md) | Optional | - |
| `item_id` | `int` | Optional | - |
| `name` | `str` | Optional | - |
| `handle` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.coupon_restriction import CouponRestriction
from advancedbilling.models.restriction_type import RestrictionType

coupon_restriction = CouponRestriction(
    id=190,
    item_type=RestrictionType.COMPONENT,
    item_id=82,
    name='name2',
    handle='handle8'
)
```

