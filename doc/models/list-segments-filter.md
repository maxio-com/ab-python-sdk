
# List Segments Filter

## Structure

`ListSegmentsFilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `segment_property_1_value` | `str` | Optional | The value passed here would be used to filter segments. Pass a value related to `segment_property_1` on attached Metric. If empty string is passed, this filter would be rejected. Use in query `filter[segment_property_1_value]=EU`. |
| `segment_property_2_value` | `str` | Optional | The value passed here would be used to filter segments. Pass a value related to `segment_property_2` on attached Metric. If empty string is passed, this filter would be rejected. |
| `segment_property_3_value` | `str` | Optional | The value passed here would be used to filter segments. Pass a value related to `segment_property_3` on attached Metric. If empty string is passed, this filter would be rejected. |
| `segment_property_4_value` | `str` | Optional | The value passed here would be used to filter segments. Pass a value related to `segment_property_4` on attached Metric. If empty string is passed, this filter would be rejected. |

## Example

```python
from advancedbilling.models.list_segments_filter import ListSegmentsFilter

list_segments_filter = ListSegmentsFilter(
    segment_property_1_value='EU',
    segment_property_2_value='segment_property_2_value4',
    segment_property_3_value='segment_property_3_value8',
    segment_property_4_value='segment_property_4_value6'
)
```

