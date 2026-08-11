
# Create Offer

## Structure

`CreateOffer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `handle` | `str` | Required | - |
| `description` | `str` | Optional | - |
| `product_id` | `int` | Required | - |
| `product_price_point_id` | `int` | Optional | - |
| `components` | [`List[CreateOfferComponent]`](../../doc/models/create-offer-component.md) | Optional | - |
| `coupons` | `List[str]` | Optional | - |

## Example

```python
from advancedbilling.models.create_offer import CreateOffer
from advancedbilling.models.create_offer_component import CreateOfferComponent

create_offer = CreateOffer(
    name='name2',
    handle='handle8',
    product_id=8,
    description='description2',
    product_price_point_id=188,
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
        'coupons8'
    ]
)
```

