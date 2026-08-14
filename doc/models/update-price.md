
# Update Price

## Structure

`UpdatePrice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Optional | - |
| `ending_quantity` | int \| str \| None | Optional | This is a container for one-of cases. |
| `unit_price` | float \| str \| None | Optional | This is a container for one-of cases. |
| `destroy` | `bool` | Optional | - |
| `starting_quantity` | int \| str \| None | Optional | This is a container for one-of cases. |

## Example

```python
from advancedbilling.models.update_price import UpdatePrice

update_price = UpdatePrice(
    id=94,
    ending_quantity=216,
    unit_price=118.74,
    destroy=False,
    starting_quantity=90
)
```

