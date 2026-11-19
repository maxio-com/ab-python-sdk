
# Subscription Component Custom Price Segment

Custom rates for one segment of an event-based component, set on the subscription through `custom_price.segments`.

Identify the segment by the property values that occur in your events, in the same positions as the segmenting properties defined on the component's meter. Each segment in a request must have a unique combination of property values.

Property values are matched against your events as text. Send values for boolean segmenting properties as the strings `"true"` and `"false"`: JSON booleans are not supported here, and a segment whose only property value is `false` is rejected with a 422.

## Structure

`SubscriptionComponentCustomPriceSegment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `segment_property_1_value` | str \| float \| int \| None | Optional | This is a container for one-of cases. |
| `segment_property_2_value` | str \| float \| int \| None | Optional | This is a container for one-of cases. |
| `segment_property_3_value` | str \| float \| int \| None | Optional | This is a container for one-of cases. |
| `segment_property_4_value` | str \| float \| int \| None | Optional | This is a container for one-of cases. |
| `segment_property_5_value` | str \| float \| int \| None | Optional | This is a container for one-of cases. |
| `segment_property_6_value` | str \| float \| int \| None | Optional | This is a container for one-of cases. |
| `segment_property_7_value` | str \| float \| int \| None | Optional | This is a container for one-of cases. |
| `segment_property_8_value` | str \| float \| int \| None | Optional | This is a container for one-of cases. |
| `segment_property_9_value` | str \| float \| int \| None | Optional | This is a container for one-of cases. |
| `segment_property_10_value` | str \| float \| int \| None | Optional | This is a container for one-of cases. |
| `pricing_scheme` | [`PricingScheme`](../../doc/models/pricing-scheme.md) | Required | The identifier for the pricing scheme. See [Product Components](https://help.chargify.com/products/product-components.html) for an overview of pricing schemes. |
| `prices` | [`List[CreateOrUpdateSegmentPrice]`](../../doc/models/create-or-update-segment-price.md) | Required | The rates for this segment. Use one price for a flat rate, or several price brackets for a tiered, volume or stairstep scheme.<br><br>**Constraints**: *Minimum Items*: `1` |

## Example

```python
from advancedbilling.models.create_or_update_segment_price import CreateOrUpdateSegmentPrice
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.subscription_component_custom_price_segment import SubscriptionComponentCustomPriceSegment

subscription_component_custom_price_segment = SubscriptionComponentCustomPriceSegment(
    pricing_scheme=PricingScheme.PER_UNIT,
    prices=[
        CreateOrUpdateSegmentPrice(
            unit_price='String3',
            starting_quantity=64,
            ending_quantity=38
        )
    ],
    segment_property_1_value='String1',
    segment_property_2_value='String3',
    segment_property_3_value='String1',
    segment_property_4_value='String5',
    segment_property_5_value='String5'
)
```

