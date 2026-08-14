
# Create Usage

## Structure

`CreateUsage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `quantity` | `float` | Optional | integer by default or decimal number if fractional quantities are enabled for the component |
| `price_point_id` | `str` | Optional | - |
| `memo` | `str` | Optional | - |
| `billing_schedule` | [`BillingSchedule`](../../doc/models/billing-schedule.md) | Optional | Billing schedule settings for component allocations or usages on multi-frequency subscriptions. Use this to start a component's billing period on a custom date instead of aligning with the product charge schedule. |
| `custom_price` | [`ComponentCustomPrice`](../../doc/models/component-custom-price.md) | Optional | Create or update custom pricing unique to the subscription. Used in place of `price_point_id`. |

## Example

```python
import dateutil.parser

from advancedbilling.models.billing_schedule import BillingSchedule
from advancedbilling.models.component_custom_price import ComponentCustomPrice
from advancedbilling.models.create_usage import CreateUsage
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme

create_usage = CreateUsage(
    quantity=244.02,
    price_point_id='price_point_id8',
    memo='memo0',
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

