
# Event

## Structure

`Event`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Required | - |
| `key` | [`EventKey`](../../doc/models/event-key.md) | Required | - |
| `message` | `str` | Required | **Constraints**: *Minimum Length*: `1` |
| `subscription_id` | `int` | Required | - |
| `customer_id` | `int` | Required | - |
| `created_at` | `datetime` | Required | - |
| `event_specific_data` | [Subscription Product Change](../../doc/models/subscription-product-change.md) \| [Subscription Product Change Scheduled](../../doc/models/subscription-product-change-scheduled.md) \| [Subscription State Change](../../doc/models/subscription-state-change.md) \| [Payment Related Events](../../doc/models/payment-related-events.md) \| [Refund Success](../../doc/models/refund-success.md) \| [Component Allocation Change](../../doc/models/component-allocation-change.md) \| [Metered Usage](../../doc/models/metered-usage.md) \| [Prepaid Usage](../../doc/models/prepaid-usage.md) \| [Dunning Step Reached](../../doc/models/dunning-step-reached.md) \| [Invoice Issued](../../doc/models/invoice-issued.md) \| [Pending Cancellation Change](../../doc/models/pending-cancellation-change.md) \| [Prepaid Subscription Balance Changed](../../doc/models/prepaid-subscription-balance-changed.md) \| [Proforma Invoice Issued](../../doc/models/proforma-invoice-issued.md) \| [Subscription Group Signup Event Data](../../doc/models/subscription-group-signup-event-data.md) \| [Credit Account Balance Changed](../../doc/models/credit-account-balance-changed.md) \| [Prepayment Account Balance Changed](../../doc/models/prepayment-account-balance-changed.md) \| [Payment Collection Method Changed](../../doc/models/payment-collection-method-changed.md) \| [Item Price Point Changed](../../doc/models/item-price-point-changed.md) \| [Custom Field Value Change](../../doc/models/custom-field-value-change.md) \| [Chjs Tokenization Success](../../doc/models/chjs-tokenization-success.md) \| [Chjs Tokenization Failure](../../doc/models/chjs-tokenization-failure.md) \| None | Required | This is a container for one-of cases. |

## Example

```python
import dateutil.parser

from advancedbilling.models.event import Event
from advancedbilling.models.event_key import EventKey
from advancedbilling.models.subscription_product_change import SubscriptionProductChange

event = Event(
    id=242,
    key=EventKey.SUBSCRIPTION_REMOVED_FROM_GROUP,
    message='message0',
    subscription_id=96,
    customer_id=24,
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    event_specific_data=SubscriptionProductChange(
        previous_product_id=126,
        new_product_id=12
    )
)
```

