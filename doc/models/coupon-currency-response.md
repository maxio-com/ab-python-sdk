
# Coupon Currency Response

## Structure

`CouponCurrencyResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_prices` | [`List[CouponCurrency]`](../../doc/models/coupon-currency.md) | Optional | - |

## Example

```python
from advancedbilling.models.coupon_currency import CouponCurrency
from advancedbilling.models.coupon_currency_response import CouponCurrencyResponse

coupon_currency_response = CouponCurrencyResponse(
    currency_prices=[
        CouponCurrency(
            id=50,
            currency='currency8',
            price=233.74,
            coupon_id=224
        ),
        CouponCurrency(
            id=50,
            currency='currency8',
            price=233.74,
            coupon_id=224
        ),
        CouponCurrency(
            id=50,
            currency='currency8',
            price=233.74,
            coupon_id=224
        )
    ]
)
```

