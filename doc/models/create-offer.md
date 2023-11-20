
# Create Offer

## Structure

`CreateOffer`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Required | - |
| `handle` | `str` | Required | - |
| `description` | `str` | Optional | - |
| `product_id` | `int` | Required | - |
| `product_price_point_id` | `int` | Optional | - |
| `components` | [`List[CreateOfferComponent]`](../../doc/models/create-offer-component.md) | Optional | - |
| `coupons` | `List[str]` | Optional | - |

## Example (as JSON)

```json
{
  "name": "name4",
  "handle": "handle0",
  "description": "description4",
  "product_id": 208,
  "product_price_point_id": 132,
  "components": [
    {
      "component_id": 108,
      "starting_quantity": 84
    },
    {
      "component_id": 108,
      "starting_quantity": 84
    }
  ],
  "coupons": [
    "coupons4"
  ]
}
```

