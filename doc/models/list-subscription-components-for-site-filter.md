
# List Subscription Components for Site Filter

## Structure

`ListSubscriptionComponentsForSiteFilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currencies` | `List[str]` | Optional | Allows fetching components allocation with matching currency based on provided values. Use in query `filter[currencies]=USD,EUR`.<br><br>**Constraints**: *Minimum Items*: `1` |
| `use_site_exchange_rate` | `bool` | Optional | Allows fetching components allocation with matching use_site_exchange_rate based on provided value. Use in query `filter[use_site_exchange_rate]=true`. |
| `subscription` | [`SubscriptionFilter`](../../doc/models/subscription-filter.md) | Optional | Nested filter used for List Subscription Components For Site Filter |

## Example (as JSON)

```json
{
  "currencies": [
    "EUR",
    "USD"
  ],
  "use_site_exchange_rate": false,
  "subscription": {
    "states": [
      "active",
      "canceled",
      "expired"
    ],
    "date_field": "updated_at",
    "start_date": "2016-03-13",
    "end_date": "2016-03-13",
    "start_datetime": "2016-03-13T12:52:32.123Z"
  }
}
```

