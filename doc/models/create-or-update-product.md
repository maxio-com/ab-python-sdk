
# Create or Update Product

## Structure

`CreateOrUpdateProduct`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | The product name |
| `handle` | `str` | Optional | The product API handle |
| `description` | `str` | Required | The product description |
| `accounting_code` | `str` | Optional | E.g. Internal ID or SKU Number |
| `require_credit_card` | `bool` | Optional | Deprecated value that can be ignored unless you have legacy hosted pages. For Public Signup Page users, read this attribute from under the signup page. |
| `price_in_cents` | `int` | Required | The product price, in integer cents |
| `interval` | `int` | Required | The numerical interval. e.g., an interval of ‘30’ coupled with an interval_unit of day would mean this product would renew every 30 days. |
| `interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Required | A string representing the interval unit for this product, either month or day |
| `trial_price_in_cents` | `int` | Optional | The product trial price, in integer cents |
| `trial_interval` | `int` | Optional | The numerical trial interval. e.g., an interval of ‘30’ coupled with a trial_interval_unit of day would mean this product trial would last 30 days. |
| `trial_interval_unit` | [`IntervalUnit`](../../doc/models/interval-unit.md) | Optional | A string representing the trial interval unit for this product, either month or day |
| `trial_type` | [`TrialType`](../../doc/models/trial-type.md) | Optional | Indicates how a trial is handled when the trial period ends and there is no credit card on file. For `no_obligation`, the subscription transitions to a Trial Ended state. Maxio will not send any emails or statements. For `payment_expected`, the subscription transitions to a Past Due state. Maxio will send normal dunning emails and statements according to your other settings. |
| `expiration_interval` | `int` | Optional | The numerical expiration interval. e.g., an expiration_interval of ‘30’ coupled with an expiration_interval_unit of day would mean this product would expire after 30 days. |
| `expiration_interval_unit` | [`ExpirationIntervalUnit`](../../doc/models/expiration-interval-unit.md) | Optional | A string representing the expiration interval unit for this product, either month, day or never |
| `auto_create_signup_page` | `bool` | Optional | - |
| `tax_code` | `str` | Optional | A string representing the tax code related to the product type. This is especially important when using AvaTax to tax based on locale. This attribute has a max length of 25 characters. |
| `unspsc_code` | `str` | Optional | (Optional) Custom UNSPSC commodity code for Level 3/CEDP payment data. When set, this value is sent as the commodity code on invoice line items for this product instead of the default derived from item_category. |

## Example

```python
from advancedbilling.models.create_or_update_product import CreateOrUpdateProduct
from advancedbilling.models.interval_unit import IntervalUnit

create_or_update_product = CreateOrUpdateProduct(
    name='name0',
    description='description0',
    price_in_cents=48,
    interval=64,
    interval_unit=IntervalUnit.DAY,
    handle='handle6',
    accounting_code='accounting_code6',
    require_credit_card=False,
    trial_price_in_cents=216,
    trial_interval=162
)
```

