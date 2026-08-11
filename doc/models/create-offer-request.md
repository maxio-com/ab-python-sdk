
# Create Offer Request

## Structure

`CreateOfferRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `offer` | [`CreateOffer`](../../doc/models/create-offer.md) | Required | - |

## Example

```python
from advancedbilling.models.create_offer import CreateOffer
from advancedbilling.models.create_offer_component import CreateOfferComponent
from advancedbilling.models.create_offer_request import CreateOfferRequest

create_offer_request = CreateOfferRequest(
    offer=CreateOffer(
        name='name4',
        handle='handle0',
        product_id=30,
        description='description6',
        product_price_point_id=150,
        components=[
            CreateOfferComponent(
                component_id=108,
                price_point_id=124,
                starting_quantity=84
            ),
            CreateOfferComponent(
                component_id=108,
                price_point_id=124,
                starting_quantity=84
            )
        ],
        coupons=[
            'coupons6'
        ]
    )
)
```

