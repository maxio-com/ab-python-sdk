
# Scheduled Renewal Configuration Item Request

## Structure

`ScheduledRenewalConfigurationItemRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `renewal_configuration_item` | [Scheduled Renewal Item Request Body Component](../../doc/models/scheduled-renewal-item-request-body-component.md) \| [Scheduled Renewal Item Request Body Product](../../doc/models/scheduled-renewal-item-request-body-product.md) | Required | This is a container for one-of cases. |

## Example

```python
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.scheduled_renewal_component_custom_price import ScheduledRenewalComponentCustomPrice
from advancedbilling.models.scheduled_renewal_configuration_item_request import ScheduledRenewalConfigurationItemRequest
from advancedbilling.models.scheduled_renewal_item_request_body_component import ScheduledRenewalItemRequestBodyComponent

scheduled_renewal_configuration_item_request = ScheduledRenewalConfigurationItemRequest(
    renewal_configuration_item=ScheduledRenewalItemRequestBodyComponent(
        item_id=108,
        price_point_id=122,
        quantity=212,
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
)
```

