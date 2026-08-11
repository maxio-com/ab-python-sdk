
# Too Many Management Link Requests Error Exception

## Structure

`TooManyManagementLinkRequestsErrorException`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `errors` | [`TooManyManagementLinkRequests`](../../doc/models/too-many-management-link-requests.md) | Required | - |

## Example

```python
try:
    # make the API call
except TooManyManagementLinkRequestsErrorException as e:
    print(e)
except APIException as e:
    print(e)
```

