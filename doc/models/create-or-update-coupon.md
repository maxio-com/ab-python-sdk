
# Create or Update Coupon

## Structure

`CreateOrUpdateCoupon`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `coupon` | [Create or Update Percentage Coupon](../../doc/models/create-or-update-percentage-coupon.md) \| [Create or Update Flat Amount Coupon](../../doc/models/create-or-update-flat-amount-coupon.md) \| None | Optional | This is a container for one-of cases. |
| `restricted_products` | Dict[str, Dict[str, bool]] \| None | Optional | This is Dictionary of a container for one-of cases. |
| `restricted_components` | Dict[str, Dict[str, bool]] \| None | Optional | This is Dictionary of a container for one-of cases. |

## Example (as JSON)

```json
{
  "coupon": {
    "name": "name0",
    "code": "code8",
    "description": "description0",
    "percentage": 11.02,
    "allow_negative_balance": "allow_negative_balance8",
    "recurring": "recurring4",
    "end_date": "end_date0",
    "product_family_id": "product_family_id6"
  },
  "restricted_products": {
    "key0": {
      "key0": true,
      "key1": false
    }
  },
  "restricted_components": {
    "key0": {
      "key0": true,
      "key1": false
    }
  }
}
```

