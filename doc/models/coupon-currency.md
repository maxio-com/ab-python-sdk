
# Coupon Currency

## Structure

`CouponCurrency`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `currency` | `str` | Optional | - |
| `price` | `float` | Optional | - |
| `coupon_id` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.coupon_currency import CouponCurrency

coupon_currency = CouponCurrency(
    id=52,
    currency='currency8',
    price=136.44,
    coupon_id=222
)
```

