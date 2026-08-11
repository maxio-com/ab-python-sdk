
# Subscription Custom Price

(Optional) Used in place of `product_price_point_id` to define a custom price point unique to the subscription. A subscription can have up to 30 custom price points. Exceeding this limit will result in an API error.

## Structure

`SubscriptionCustomPrice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | (Optional) |
| `handle` | `str` | Optional | (Optional) |
| `price_in_cents` | str \| int | Required | This is a container for one-of cases. |
| `interval` | str \| int | Required | This is a container for one-of cases. |
| `interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Required | Required if using `custom_price` attribute. |
| `trial_price_in_cents` | str \| int \| None | Optional | This is a container for one-of cases. |
| `trial_interval` | str \| int \| None | Optional | This is a container for one-of cases. |
| `trial_interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Optional | (Optional) |
| `trial_type` | [`TrialType`](../../doc/models/trial-type.md) | Optional | Indicates how a trial is handled when the trial period ends and there is no credit card on file. For `no_obligation`, the subscription transitions to a Trial Ended state. Maxio will not send any emails or statements. For `payment_expected`, the subscription transitions to a Past Due state. Maxio will send normal dunning emails and statements according to your other settings. |
| `initial_charge_in_cents` | str \| int \| None | Optional | This is a container for one-of cases. |
| `initial_charge_after_trial` | `bool` | Optional | (Optional) |
| `expiration_interval` | str \| int \| None | Optional | This is a container for one-of cases. |
| `expiration_interval_unit` | [`ExpirationIntervalUnit`](../../doc/models/expiration-interval-unit.md) | Optional | (Optional) |
| `tax_included` | `bool` | Optional | (Optional) |

## Example

```python
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.subscription_custom_price import SubscriptionCustomPrice

subscription_custom_price = SubscriptionCustomPrice(
    price_in_cents='String7',
    interval='String1',
    interval_unit=IntervalUnit.DAY,
    name='name2',
    handle='handle8',
    trial_price_in_cents='String7',
    trial_interval='String3',
    trial_interval_unit=IntervalUnit.DAY
)
```

