
# Site Statistics

## Structure

`SiteStatistics`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_subscriptions` | `int` | Optional | - |
| `subscriptions_today` | `int` | Optional | - |
| `total_revenue` | `str` | Optional | - |
| `revenue_today` | `str` | Optional | - |
| `revenue_this_month` | `str` | Optional | - |
| `revenue_this_year` | `str` | Optional | - |
| `total_canceled_subscriptions` | `int` | Optional | - |
| `total_active_subscriptions` | `int` | Optional | - |
| `total_past_due_subscriptions` | `int` | Optional | - |
| `total_unpaid_subscriptions` | `int` | Optional | - |
| `total_dunning_subscriptions` | `int` | Optional | - |

## Example

```python
from advancedbilling.models.site_statistics import SiteStatistics

site_statistics = SiteStatistics(
    total_subscriptions=186,
    subscriptions_today=152,
    total_revenue='total_revenue6',
    revenue_today='revenue_today4',
    revenue_this_month='revenue_this_month4'
)
```

