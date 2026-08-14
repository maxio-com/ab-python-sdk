
# Subscription Remove Coupon Errors Exception

## Structure

`SubscriptionRemoveCouponErrorsException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription` | `List[str]` | Required | - |

## Example

```python
try:
    # make the API call
except SubscriptionRemoveCouponErrorsException as e:
    print(e)
except APIException as e:
    print(e)
```

