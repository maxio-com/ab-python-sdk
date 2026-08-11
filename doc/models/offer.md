
# Offer

## Structure

`Offer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `site_id` | `int` | Optional | - |
| `product_family_id` | `int` | Optional | - |
| `product_id` | `int` | Optional | - |
| `product_price_point_id` | `int` | Optional | - |
| `product_revisable_number` | `int` | Optional | - |
| `name` | `str` | Optional | - |
| `handle` | `str` | Optional | - |
| `description` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `archived_at` | `datetime` | Optional | - |
| `offer_items` | [`List[OfferItem]`](../../doc/models/offer-item.md) | Optional | - |
| `offer_discounts` | [`List[OfferDiscount]`](../../doc/models/offer-discount.md) | Optional | - |
| `product_family_name` | `str` | Optional | - |
| `product_name` | `str` | Optional | - |
| `product_price_point_name` | `str` | Optional | - |
| `product_price_in_cents` | `int` | Optional | - |
| `offer_signup_pages` | [`List[OfferSignupPage]`](../../doc/models/offer-signup-page.md) | Optional | - |

## Example

```python
from advancedbilling.models.offer import Offer

offer = Offer(
    id=28,
    site_id=210,
    product_family_id=224,
    product_id=30,
    product_price_point_id=150
)
```

