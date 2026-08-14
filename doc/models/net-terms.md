
# Net Terms

## Structure

`NetTerms`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `default_net_terms` | `int` | Optional | **Default**: `0` |
| `automatic_net_terms` | `int` | Optional | **Default**: `0` |
| `remittance_net_terms` | `int` | Optional | **Default**: `0` |
| `net_terms_on_remittance_signups_enabled` | `bool` | Optional | **Default**: `False` |
| `custom_net_terms_enabled` | `bool` | Optional | **Default**: `False` |

## Example

```python
from advancedbilling.models.net_terms import NetTerms

net_terms = NetTerms(
    default_net_terms=0,
    automatic_net_terms=0,
    remittance_net_terms=0,
    net_terms_on_remittance_signups_enabled=False,
    custom_net_terms_enabled=False
)
```

