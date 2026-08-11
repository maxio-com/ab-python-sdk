
# List Price Points Filter

## Structure

`ListPricePointsFilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_field` | [`BasicDateField`](../../doc/models/basic-date-field.md) | Optional | The type of filter you would like to apply to your search. Use in query: `filter[date_field]=created_at`. |
| `start_date` | `date` | Optional | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns price points with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. |
| `end_date` | `date` | Optional | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns price points with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. |
| `start_datetime` | `datetime` | Optional | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns price points with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of start_date. |
| `end_datetime` | `datetime` | Optional | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns price points with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of end_date. |
| `mtype` | [`List[PricePointType]`](../../doc/models/price-point-type.md) | Optional | Allows fetching price points with matching type. Use in query: `filter[type]=custom,catalog`. |
| `ids` | `List[int]` | Optional | Allows fetching price points with matching id based on provided values. Use in query: `filter[ids]=1,2,3`. |
| `archived_at` | [`IncludeNullOrNotNull`](../../doc/models/include-null-or-not-null.md) | Optional | Allows fetching price points only if archived_at is present or not. Use in query: `filter[archived_at]=not_null`. |

## Example

```python
import dateutil.parser

from advancedbilling.models.basic_date_field import BasicDateField
from advancedbilling.models.list_price_points_filter import ListPricePointsFilter
from advancedbilling.models.price_point_type import PricePointType

list_price_points_filter = ListPricePointsFilter(
    date_field=BasicDateField.UPDATED_AT,
    start_date=dateutil.parser.parse('2011-12-17').date(),
    end_date=dateutil.parser.parse('2011-12-15').date(),
    start_datetime=dateutil.parser.parse('2011-12-19T09:15:30+00:00'),
    end_datetime=dateutil.parser.parse('2019-06-07T17:20:06Z'),
    mtype=[
        PricePointType.CATALOG,
        PricePointType.DEFAULT,
        PricePointType.CUSTOM
    ],
    ids=[
        1,
        2,
        3
    ]
)
```

