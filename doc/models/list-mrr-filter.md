
# List Mrr Filter

## Structure

`ListMrrFilter`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_ids` | `List[int]` | Optional | Submit ids in order to limit results. Use in query: `filter[subscription_ids]=1,2,3`.<br><br>**Constraints**: *Minimum Items*: `1` |

## Example

```python
from advancedbilling.models.list_mrr_filter import ListMrrFilter

list_mrr_filter = ListMrrFilter(
    subscription_ids=[
        1,
        2,
        3
    ]
)
```

