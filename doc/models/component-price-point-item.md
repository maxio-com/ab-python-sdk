
# Component Price Point Item

## Structure

`ComponentPricePointItem`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | - |
| `handle` | `str` | Optional | - |
| `pricing_scheme` | `str` | Optional | - |
| `prices` | [`List[CreateComponentPrice]`](../../doc/models/create-component-price.md) | Optional | - |

## Example (as JSON)

```json
{
  "name": "name6",
  "handle": "handle2",
  "pricing_scheme": "pricing_scheme2",
  "prices": [
    {
      "starting_quantity": 64,
      "unit_price": "String3"
    },
    {
      "starting_quantity": 64,
      "unit_price": "String3"
    },
    {
      "starting_quantity": 64,
      "unit_price": "String3"
    }
  ]
}
```

