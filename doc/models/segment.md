
# Segment

## Structure

`Segment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `component_id` | `int` | Optional | - |
| `price_point_id` | `int` | Optional | - |
| `event_based_billing_metric_id` | `int` | Optional | - |
| `pricing_scheme` | [`PricingScheme`](../../doc/models/pricing-scheme.md) | Optional | The identifier for the pricing scheme. See [Product Components](https://help.chargify.com/products/product-components.html) for an overview of pricing schemes. |
| `segment_property_1_value` | str \| float \| int \| bool \| None | Optional | This is a container for one-of cases. |
| `segment_property_2_value` | str \| float \| int \| bool \| None | Optional | This is a container for one-of cases. |
| `segment_property_3_value` | str \| float \| int \| bool \| None | Optional | This is a container for one-of cases. |
| `segment_property_4_value` | str \| float \| int \| bool \| None | Optional | This is a container for one-of cases. |
| `created_at` | `datetime` | Optional | - |
| `updated_at` | `datetime` | Optional | - |
| `prices` | [`List[SegmentPrice]`](../../doc/models/segment-price.md) | Optional | **Constraints**: *Minimum Items*: `1` |
| `currency_prices` | [`List[ComponentCurrencyPrice]`](../../doc/models/component-currency-price.md) | Optional | Prices of the segment in the site's non-primary currencies, one entry for each price and currency. This field is present only when the request includes `currency_prices=true`. If the price point uses the site exchange rate, the prices are calculated from the current rate and each `id` is `null`. |

## Example

```python
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.segment import Segment

segment = Segment(
    id=118,
    component_id=228,
    price_point_id=4,
    event_based_billing_metric_id=56,
    pricing_scheme=PricingScheme.STAIRSTEP
)
```

