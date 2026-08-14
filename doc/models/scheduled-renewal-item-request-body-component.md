
# Scheduled Renewal Item Request Body Component

## Structure

`ScheduledRenewalItemRequestBodyComponent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `item_type` | `str` | Required, Constant | Item type to add. Either Product or Component.<br><br>**Value**: `"Component"` |
| `item_id` | `int` | Required | Product or component identifier. |
| `price_point_id` | `int` | Optional | Price point identifier. |
| `quantity` | `int` | Optional | (Optional) Quantity for the item. |
| `custom_price` | [`ScheduledRenewalComponentCustomPrice`](../../doc/models/scheduled-renewal-component-custom-price.md) | Optional | Custom pricing for a component within a scheduled renewal. |

## Example

```python
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.scheduled_renewal_component_custom_price import ScheduledRenewalComponentCustomPrice
from advancedbilling.models.scheduled_renewal_item_request_body_component import ScheduledRenewalItemRequestBodyComponent

scheduled_renewal_item_request_body_component = ScheduledRenewalItemRequestBodyComponent(
    item_id=228,
    price_point_id=214,
    quantity=36,
    custom_price=ScheduledRenewalComponentCustomPrice(
        pricing_scheme=PricingScheme.STAIRSTEP,
        prices=[
            Price(
                starting_quantity=242,
                unit_price=23.26,
                ending_quantity=40
            ),
            Price(
                starting_quantity=242,
                unit_price=23.26,
                ending_quantity=40
            )
        ],
        tax_included=False
    )
)
```

