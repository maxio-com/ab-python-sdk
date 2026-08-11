
# List MRR Response Result

## Structure

`ListMRRResponseResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `page` | `int` | Optional | - |
| `per_page` | `int` | Optional | - |
| `total_pages` | `int` | Optional | - |
| `total_entries` | `int` | Optional | - |
| `currency` | `str` | Optional | - |
| `currency_symbol` | `str` | Optional | - |
| `movements` | [`List[Movement]`](../../doc/models/movement.md) | Optional | - |

## Example

```python
from advancedbilling.models.list_mrr_response_result import ListMRRResponseResult

list_mrr_response_result = ListMRRResponseResult(
    page=170,
    per_page=82,
    total_pages=208,
    total_entries=48,
    currency='currency6'
)
```

