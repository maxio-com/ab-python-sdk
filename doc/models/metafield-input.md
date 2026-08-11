
# Metafield Input

Indicates the type of metafield. A text metafield allows any string value. Dropdown and radio metafields have a set of values that can be selected. Defaults to 'text'.

## Enumeration

`MetafieldInput`

## Fields

| Name |
|  --- |
| `BALANCE_TRACKER` |
| `TEXT` |
| `RADIO` |
| `DROPDOWN` |

## Example

```python
from advancedbilling.models.metafield_input import MetafieldInput

metafield_input = MetafieldInput.RADIO
```

