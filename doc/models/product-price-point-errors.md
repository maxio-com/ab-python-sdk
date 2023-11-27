
# Product Price Point Errors

## Structure

`ProductPricePointErrors`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `price_point` | `str` | Optional | - |
| `interval` | `List[str]` | Optional | - |
| `interval_unit` | `List[str]` | Optional | - |
| `name` | `List[str]` | Optional | - |
| `price` | `List[str]` | Optional | - |
| `price_in_cents` | `List[str]` | Optional | - |

## Example (as JSON)

```json
{
  "price_point": "can't be blank",
  "interval": [
    "Recurring Interval: cannot be blank.",
    "Recurring Interval: must be greater than or equal to 1."
  ],
  "interval_unit": [
    "Interval unit: cannot be blank.",
    "Interval unit: must be 'month' or 'day'."
  ],
  "name": [
    "Name: cannot be blank."
  ],
  "price": [
    "Price: is not a number.",
    "Price: must be greater than or equal to 0."
  ],
  "price_in_cents": [
    "Price in cents: cannot be blank."
  ]
}
```

