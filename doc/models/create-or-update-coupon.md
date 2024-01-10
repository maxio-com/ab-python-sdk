
# Create or Update Coupon

## Structure

`CreateOrUpdateCoupon`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `coupon` | [Create or Update Percentage Coupon](../../doc/models/create-or-update-percentage-coupon.md) \| [Create or Update Flat Amount Coupon](../../doc/models/create-or-update-flat-amount-coupon.md) \| None | Optional | This is a container for one-of cases. |
| `restricted_products` | `Dict[str, bool]` | Optional | An object where the keys are product_ids and the values are booleans indicating if the coupon should be applicable to the product |
| `restricted_components` | `Dict[str, bool]` | Optional | An object where the keys are component_ids and the values are booleans indicating if the coupon should be applicable to the component |

## Example (as JSON)

```json
{
  "coupon": {
    "name": "name0",
    "code": "code8",
    "description": "description0",
    "percentage": 11.02,
    "allow_negative_balance": false,
    "recurring": false,
    "end_date": "2016-03-13T12:52:32.123Z",
    "product_family_id": "product_family_id6"
  },
  "restricted_products": {
    "key0": true
  },
  "restricted_components": {
    "key0": true
  }
}
```

