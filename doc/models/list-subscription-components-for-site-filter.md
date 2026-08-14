
# List Subscription Components for Site Filter

## Structure

`ListSubscriptionComponentsForSiteFilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currencies` | `List[str]` | Optional | Allows fetching components allocation with matching currency based on provided values. Use in query `filter[currencies]=USD,EUR`.<br><br>**Constraints**: *Minimum Items*: `1` |
| `use_site_exchange_rate` | `bool` | Optional | Allows fetching components allocation with matching use_site_exchange_rate based on provided value. Use in query `filter[use_site_exchange_rate]=true`. |
| `subscription` | [`SubscriptionFilter`](../../doc/models/subscription-filter.md) | Optional | Nested filter used for List Subscription Components For Site Filter |

## Example

```python
import dateutil.parser

from advancedbilling.models.list_subscription_components_for_site_filter import ListSubscriptionComponentsForSiteFilter
from advancedbilling.models.subscription_filter import SubscriptionFilter
from advancedbilling.models.subscription_list_date_field import SubscriptionListDateField
from advancedbilling.models.subscription_state_filter import SubscriptionStateFilter

list_subscription_components_for_site_filter = ListSubscriptionComponentsForSiteFilter(
    currencies=[
        'EUR',
        'USD'
    ],
    use_site_exchange_rate=False,
    subscription=SubscriptionFilter(
        states=[
            SubscriptionStateFilter.TRIALING,
            SubscriptionStateFilter.UNPAID,
            SubscriptionStateFilter.ACTIVE
        ],
        date_field=SubscriptionListDateField.UPDATED_AT,
        start_date=dateutil.parser.parse('2016-03-13').date(),
        end_date=dateutil.parser.parse('2016-03-13').date(),
        start_datetime=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
    )
)
```

