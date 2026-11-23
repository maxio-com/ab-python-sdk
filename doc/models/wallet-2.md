
# Wallet 2

## Structure

`Wallet2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | `str` | Optional | A merchant-facing label for the wallet. Surrounding spaces are stripped; a blank or `null` value clears it.<br><br>**Constraints**: *Maximum Length*: `255` |

## Example

```python
from advancedbilling.models.wallet_2 import Wallet2

wallet_2 = Wallet2(
    name='name6'
)
```

