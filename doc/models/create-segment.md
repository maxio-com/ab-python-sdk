
# Create Segment

## Structure

`CreateSegment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `segment_property_1_value` | str \| float \| int \| bool \| None | Optional | This is a container for one-of cases. |
| `segment_property_2_value` | str \| float \| int \| bool \| None | Optional | This is a container for one-of cases. |
| `segment_property_3_value` | str \| float \| int \| bool \| None | Optional | This is a container for one-of cases. |
| `segment_property_4_value` | str \| float \| int \| bool \| None | Optional | This is a container for one-of cases. |
| `pricing_scheme` | `str` | Required | The handle for the pricing scheme. Available options: per_unit, volume, tiered, stairstep. See [Price Bracket Rules](https://help.chargify.com/products/product-components.html#price-bracket-rules) for an overview of pricing schemes. |
| `prices` | [`List[CreateOrUpdateSegmentPrice]`](../../doc/models/create-or-update-segment-price.md) | Optional | - |

## Example (as JSON)

```json
{
  "segment_property_1_value": "String9",
  "segment_property_2_value": "String1",
  "segment_property_3_value": "String3",
  "segment_property_4_value": "String3",
  "pricing_scheme": "pricing_scheme6",
  "prices": [
    {
      "starting_quantity": 64,
      "ending_quantity": 38,
      "unit_price": "String3"
    },
    {
      "starting_quantity": 64,
      "ending_quantity": 38,
      "unit_price": "String3"
    },
    {
      "starting_quantity": 64,
      "ending_quantity": 38,
      "unit_price": "String3"
    }
  ]
}
```

