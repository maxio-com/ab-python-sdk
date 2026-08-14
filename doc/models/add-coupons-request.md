
# Add Coupons Request

## Structure

`AddCouponsRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `codes` | `List[str]` | Optional | - |

## Example

```python
from advancedbilling.models.add_coupons_request import AddCouponsRequest

add_coupons_request = AddCouponsRequest(
    codes=[
        'codes6',
        'codes7'
    ]
)
```

