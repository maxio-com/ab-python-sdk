
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
| `created_at` | `str` | Optional | - |
| `updated_at` | `str` | Optional | - |
| `prices` | [`List[SegmentPrice]`](../../doc/models/segment-price.md) | Optional | **Constraints**: *Minimum Items*: `1` |

## Example (as JSON)

```json
{
  "id": 6,
  "component_id": 116,
  "price_point_id": 140,
  "event_based_billing_metric_id": 200,
  "pricing_scheme": "stairstep"
}
```

