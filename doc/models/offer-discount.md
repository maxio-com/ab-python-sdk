
# Offer Discount

## Structure

`OfferDiscount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `coupon_code` | `str` | Optional | - |
| `coupon_id` | `int` | Optional | - |
| `coupon_name` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.offer_discount import OfferDiscount

offer_discount = OfferDiscount(
    coupon_code='coupon_code4',
    coupon_id=106,
    coupon_name='coupon_name6'
)
```

