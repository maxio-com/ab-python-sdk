
# Event Based Billing Segment Write Error Response Exception

Errors returned when creating or updating a single segment. Validation problems use the per-field error map; a write to a subscription's custom price point returns a `price_point` error.

## Structure

`EventBasedBillingSegmentWriteErrorResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | `Dict[str, Any]` | Optional | - |

## Example

```python
try:
    # make the API call
except EventBasedBillingSegmentWriteErrorResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

