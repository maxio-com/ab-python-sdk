
# Coupon Request

## Structure

`CouponRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `coupon` | [`CouponPayload`](../../doc/models/coupon-payload.md) | Optional | - |
| `restricted_products` | `Dict[str, bool]` | Optional | An object where the keys are product IDs or handles (prefixed with 'handle:'), and the values are booleans indicating if the coupon should be applicable to the product |
| `restricted_components` | `Dict[str, bool]` | Optional | An object where the keys are component IDs or handles (prefixed with 'handle:'), and the values are booleans indicating if the coupon should be applicable to the component |

## Example (as JSON)

```json
{
  "coupon": {
    "name": "name4",
    "code": "code2",
    "description": "description6",
    "percentage": "String3",
    "amount_in_cents": 230
  },
  "restricted_products": {
    "key0": true
  },
  "restricted_components": {
    "key0": true
  }
}
```

