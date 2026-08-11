
# Update Coupon Currency

## Structure

`UpdateCouponCurrency`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Required | ISO code for the site defined currency. |
| `price` | `int` | Required | Price for the given currency. |

## Example

```python
from advancedbilling.models.update_coupon_currency import UpdateCouponCurrency

update_coupon_currency = UpdateCouponCurrency(
    currency='currency6',
    price=14
)
```

