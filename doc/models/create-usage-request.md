
# Create Usage Request

## Structure

`CreateUsageRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `usage` | [`CreateUsage`](../../doc/models/create-usage.md) | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.billing_schedule import BillingSchedule
from advancedbilling.models.component_custom_price import ComponentCustomPrice
from advancedbilling.models.create_usage import CreateUsage
from advancedbilling.models.create_usage_request import CreateUsageRequest
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.price import Price
from advancedbilling.models.pricing_scheme import PricingScheme

create_usage_request = CreateUsageRequest(
    usage=CreateUsage(
        quantity=162.34,
        price_point_id='price_point_id0',
        memo='memo2',
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
)
```

