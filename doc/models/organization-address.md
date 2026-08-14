
# Organization Address

## Structure

`OrganizationAddress`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `street` | `str` | Optional | - |
| `line_2` | `str` | Optional | - |
| `city` | `str` | Optional | - |
| `state` | `str` | Optional | - |
| `zip` | `str` | Optional | - |
| `country` | `str` | Optional | - |
| `name` | `str` | Optional | - |
| `phone` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.organization_address import OrganizationAddress

organization_address = OrganizationAddress(
    street='street6',
    line_2='line20',
    city='city6',
    state='state2',
    zip='zip0'
)
```

