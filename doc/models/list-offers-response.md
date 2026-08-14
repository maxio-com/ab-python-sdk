
# List Offers Response

## Structure

`ListOffersResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `offers` | [`List[Offer]`](../../doc/models/offer.md) | Optional | - |

## Example

```python
from advancedbilling.models.list_offers_response import ListOffersResponse
from advancedbilling.models.offer import Offer

list_offers_response = ListOffersResponse(
    offers=[
        Offer(
            id=12,
            site_id=194,
            product_family_id=16,
            product_id=210,
            product_price_point_id=134
        ),
        Offer(
            id=12,
            site_id=194,
            product_family_id=16,
            product_id=210,
            product_price_point_id=134
        )
    ]
)
```

