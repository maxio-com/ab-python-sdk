
# Offer Response

## Structure

`OfferResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `offer` | [`Offer`](../../doc/models/offer.md) | Optional | - |

## Example

```python
from advancedbilling.models.offer import Offer
from advancedbilling.models.offer_response import OfferResponse

offer_response = OfferResponse(
    offer=Offer(
        id=28,
        site_id=210,
        product_family_id=224,
        product_id=30,
        product_price_point_id=150
    )
)
```

