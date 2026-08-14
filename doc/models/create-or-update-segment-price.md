
# Create or Update Segment Price

## Structure

`CreateOrUpdateSegmentPrice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `starting_quantity` | `int` | Optional | - |
| `ending_quantity` | `int` | Optional | - |
| `unit_price` | str \| float | Required | This is a container for one-of cases. |

## Example

```python
from advancedbilling.models.create_or_update_segment_price import CreateOrUpdateSegmentPrice

create_or_update_segment_price = CreateOrUpdateSegmentPrice(
    unit_price='String7',
    starting_quantity=94,
    ending_quantity=188
)
```

