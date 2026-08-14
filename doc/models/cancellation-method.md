
# Cancellation Method

The process used to cancel the subscription, if the subscription has been canceled. It is nil if the subscription's state is not canceled.

## Enumeration

`CancellationMethod`

## Fields

| Name |
|  --- |
| `MERCHANT_UI` |
| `MERCHANT_API` |
| `DUNNING` |
| `BILLING_PORTAL` |
| `UNKNOWN` |
| `IMPORTED` |

## Example

```python
from advancedbilling.models.cancellation_method import CancellationMethod

cancellation_method = CancellationMethod.UNKNOWN
```

