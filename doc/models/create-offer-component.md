
# Create Offer Component

## Structure

`CreateOfferComponent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `component_id` | `int` | Optional | - |
| `price_point_id` | `int` | Optional | - |
| `starting_quantity` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.create_offer_component import CreateOfferComponent

create_offer_component = CreateOfferComponent(
    component_id=206,
    price_point_id=230,
    starting_quantity=242
)
```

