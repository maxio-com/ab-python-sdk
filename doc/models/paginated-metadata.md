
# Paginated Metadata

## Structure

`PaginatedMetadata`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `total_count` | `int` | Optional | - |
| `current_page` | `int` | Optional | - |
| `total_pages` | `int` | Optional | - |
| `per_page` | `int` | Optional | - |
| `metadata` | [`List[Metadata]`](../../doc/models/metadata.md) | Optional | - |

## Example (as JSON)

```json
{
  "total_count": 26,
  "current_page": 2,
  "total_pages": 14,
  "per_page": 20,
  "metadata": [
    {
      "id": 50,
      "value": "value8",
      "resource_id": 134,
      "name": "name6",
      "deleted_at": "2016-03-13T12:52:32.123Z"
    },
    {
      "id": 50,
      "value": "value8",
      "resource_id": 134,
      "name": "name6",
      "deleted_at": "2016-03-13T12:52:32.123Z"
    }
  ]
}
```

