
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
| `product_price_in_cents` | `long\|int` | Optional | - |
| `offer_signup_pages` | [`List[OfferSignupPage]`](../../doc/models/offer-signup-page.md) | Optional | - |

## Example (as JSON)

```json
{
  "id": 154,
  "site_id": 80,
  "product_family_id": 158,
  "product_id": 96,
  "product_price_point_id": 20
}
```

