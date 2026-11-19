
# Segment Price Point Errors Error Exception

Returned when a segment write targets a subscription's custom price point. Segments on a custom price point can only be set through `custom_price` on the subscription or component endpoints.

## Structure

`SegmentPricePointErrorsErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`Errors`](../../doc/models/errors.md) | Required | - |

## Example

```python
try:
    # make the API call
except SegmentPricePointErrorsErrorException as e:
    print(e)
except APIException as e:
    print(e)
```

