
# Subscription Add Coupon Error Exception

## Structure

`SubscriptionAddCouponErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `codes` | `List[str]` | Optional | - |
| `coupon_code` | `List[str]` | Optional | - |
| `coupon_codes` | `List[str]` | Optional | - |
| `subscription` | `List[str]` | Optional | - |

## Example

```python
try:
    # make the API call
except SubscriptionAddCouponErrorException as e:
    print(e)
except APIException as e:
    print(e)
```

