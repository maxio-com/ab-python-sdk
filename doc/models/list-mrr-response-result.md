
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

## Example (as JSON)

```json
{
  "page": 150,
  "per_page": 238,
  "total_pages": 16,
  "total_entries": 112,
  "currency": "currency8"
}
```

