
# Usage

## Structure

`Usage`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | **Constraints**: `>= 0` |
| `memo` | `str` | Optional | - |
| `created_at` | `datetime` | Optional | - |
| `price_point_id` | `int` | Optional | - |
| `quantity` | int \| str \| None | Optional | This is a container for one-of cases. |
| `overage_quantity` | `int` | Optional | - |
| `component_id` | `int` | Optional | - |
| `component_handle` | `str` | Optional | - |
| `subscription_id` | `int` | Optional | - |

## Example (as JSON)

```json
{
  "id": 252,
  "memo": "memo8",
  "created_at": "2016-03-13T12:52:32.123Z",
  "price_point_id": 126,
  "quantity": 130
}
```

