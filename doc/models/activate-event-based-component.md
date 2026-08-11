
# Activate Event Based Component

## Structure

`ActivateEventBasedComponent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_point_id` | `int` | Optional | The Chargify id of the price point |
| `billing_schedule` | [`BillingSchedule`](../../doc/models/billing-schedule.md) | Optional | Billing schedule settings for component allocations or usages on multi-frequency subscriptions. Use this to start a component's billing period on a custom date instead of aligning with the product charge schedule. |
| `custom_price` | [`ComponentCustomPrice`](../../doc/models/component-custom-price.md) | Optional | Create or update custom pricing unique to the subscription. Used in place of `price_point_id`. |

## Example

```python
import dateutil.parser

from advancedbilling.models.activate_event_based_component import ActivateEventBasedComponent
from advancedbilling.models.billing_schedule import BillingSchedule
from advancedbilling.models.component_custom_price import ComponentCustomPrice
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme

activate_event_based_component = ActivateEventBasedComponent(
    price_point_id=166,
    billing_schedule=BillingSchedule(
        initial_billing_at=dateutil.parser.parse('2016-03-13').date()
    ),
    custom_price=ComponentCustomPrice(
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
        tax_included=False,
        pricing_scheme=PricingScheme.STAIRSTEP,
        interval=66,
        interval_unit=IntervalUnit.DAY,
        list_price_point_id=174
    )
)
```

