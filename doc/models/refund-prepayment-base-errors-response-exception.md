
# Refund Prepayment Base Errors Response Exception

Errors returned on creating a refund prepayment when bad request

## Structure

`RefundPrepaymentBaseErrorsResponseException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`RefundPrepaymentBaseRefundError`](../../doc/models/refund-prepayment-base-refund-error.md) | Optional | - |

## Example

```python
try:
    # make the API call
except RefundPrepaymentBaseErrorsResponseException as e:
    print(e)
except APIException as e:
    print(e)
```

