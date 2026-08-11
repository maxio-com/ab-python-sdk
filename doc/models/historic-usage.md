
# Historic Usage

(Optional) For Event Based Components. If the `include=historic_usages` query param is provided, the last ten billing periods will be returned.

## Structure

`HistoricUsage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_usage_quantity` | `float` | Optional | Total usage of a component for billing period |
| `billing_period_starts_at` | `datetime` | Optional | Start date of billing period |
| `billing_period_ends_at` | `datetime` | Optional | End date of billing period |

## Example

```python
import dateutil.parser

from advancedbilling.models.historic_usage import HistoricUsage

historic_usage = HistoricUsage(
    total_usage_quantity=247.74,
    billing_period_starts_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    billing_period_ends_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
)
```

