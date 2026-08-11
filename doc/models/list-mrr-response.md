
# List MRR Response

## Structure

`ListMRRResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mrr` | [`ListMRRResponseResult`](../../doc/models/list-mrr-response-result.md) | Required | - |

## Example

```python
from advancedbilling.models.list_mrr_response import ListMRRResponse
from advancedbilling.models.list_mrr_response_result import ListMRRResponseResult

list_mrr_response = ListMRRResponse(
    mrr=ListMRRResponseResult(
        page=30,
        per_page=198,
        total_pages=92,
        total_entries=188,
        currency='currency4'
    )
)
```

