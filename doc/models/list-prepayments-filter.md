
# List Prepayments Filter

## Structure

`ListPrepaymentsFilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_field` | [`ListPrepaymentDateField`](../../doc/models/list-prepayment-date-field.md) | Optional | The type of filter you would like to apply to your search. `created_at` - Time when prepayment was created. `application_at` - Time when prepayment was applied to invoice. Use in query `filter[date_field]=created_at`. |
| `start_date` | `date` | Optional | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns prepayments with a timestamp at or after midnight (12:00:00 AM) in your site's time zone on the date specified. Use in query: `filter[start_date]=2011-12-15`. |
| `end_date` | `date` | Optional | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns prepayments with a timestamp up to and including 11:59:59PM in your site's time zone on the date specified. Use in query: `filter[end_date]=2011-12-15`. |

## Example

```python
import dateutil.parser

from advancedbilling.models.list_prepayment_date_field import ListPrepaymentDateField
from advancedbilling.models.list_prepayments_filter import ListPrepaymentsFilter

list_prepayments_filter = ListPrepaymentsFilter(
    date_field=ListPrepaymentDateField.CREATED_AT,
    start_date=dateutil.parser.parse('2024-01-01').date(),
    end_date=dateutil.parser.parse('2024-01-31').date()
)
```

