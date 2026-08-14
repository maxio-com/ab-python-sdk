
# Coupon Currency Request

## Structure

`CouponCurrencyRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency_prices` | [`List[UpdateCouponCurrency]`](../../doc/models/update-coupon-currency.md) | Required | - |

## Example

```python
from advancedbilling.models.coupon_currency_request import CouponCurrencyRequest
from advancedbilling.models.update_coupon_currency import UpdateCouponCurrency

coupon_currency_request = CouponCurrencyRequest(
    currency_prices=[
        UpdateCouponCurrency(
            currency='currency8',
            price=78
        )
    ]
)
```

