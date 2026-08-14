
# Cancellation Request

## Structure

`CancellationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription` | [`CancellationOptions`](../../doc/models/cancellation-options.md) | Required | - |

## Example

```python
import dateutil.parser

from advancedbilling.models.cancellation_options import CancellationOptions
from advancedbilling.models.cancellation_request import CancellationRequest

cancellation_request = CancellationRequest(
    subscription=CancellationOptions(
        cancellation_message='cancellation_message2',
        reason_code='reason_code8',
        cancel_at_end_of_period=False,
        scheduled_cancellation_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
        refund_prepayment_account_balance=False
    )
)
```

