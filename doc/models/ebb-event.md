
# EBB Event

## Structure

`EBBEvent`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chargify` | [`ChargifyEBB`](../../doc/models/chargify-ebb.md) | Optional | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.chargify_ebb import ChargifyEBB
from advancedbilling.models.ebb_event import EBBEvent

ebb_event = EBBEvent(
    chargify=ChargifyEBB(
        timestamp=dateutil.parser.parse('2020-02-27T17:45:50-05:00'),
        subscription_id=1
    )
)
```

