
# Create Product Price Point

## Structure

`CreateProductPricePoint`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | The product price point name |
| `handle` | `str` | Optional | The product price point API handle |
| `price_in_cents` | `int` | Required | The product price point price, in integer cents |
| `interval` | `int` | Required | The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would mean this product price point would renew every 30 days. |
| `interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Required | A string representing the interval unit for this product price point, either month or day |
| `trial_price_in_cents` | `int` | Optional | The product price point trial price, in integer cents |
| `trial_interval` | `int` | Optional | The numerical trial interval. e.g., an interval of ‘30’ coupled with a trial_interval_unit of day would mean this product price point trial would last 30 days. |
| `trial_interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Optional | A string representing the trial interval unit for this product price point, either month or day |
| `trial_type` | [`TrialType`](../../doc/models/trial-type.md) | Optional | Indicates how a trial is handled when the trial period ends and there is no credit card on file. For `no_obligation`, the subscription transitions to a Trial Ended state. Maxio will not send any emails or statements. For `payment_expected`, the subscription transitions to a Past Due state. Maxio will send normal dunning emails and statements according to your other settings. |
| `initial_charge_in_cents` | `int` | Optional | The product price point initial charge, in integer cents |
| `initial_charge_after_trial` | `bool` | Optional | - |
| `expiration_interval` | `int` | Optional | The numerical expiration interval. e.g., an expiration_interval of ‘30’ coupled with an expiration_interval_unit of day would mean this product price point would expire after 30 days. |
| `expiration_interval_unit` | [`ExpirationIntervalUnit`](../../doc/models/expiration-interval-unit.md) | Optional | A string representing the expiration interval unit for this product price point, either month, day or never |
| `use_site_exchange_rate` | `bool` | Optional | Whether or not to use the site's exchange rate or define your own pricing when your site has multiple currencies defined.<br><br>**Default**: `True` |

## Example

```python
from advancedbilling.models.create_product_price_point import CreateProductPricePoint
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.trial_type import TrialType

create_product_price_point = CreateProductPricePoint(
    name='name4',
    price_in_cents=42,
    interval=198,
    interval_unit=IntervalUnit.DAY,
    handle='handle0',
    trial_price_in_cents=210,
    trial_interval=100,
    trial_interval_unit=IntervalUnit.DAY,
    trial_type=TrialType.NO_OBLIGATION,
    use_site_exchange_rate=True
)
```

