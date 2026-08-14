
# Origin Invoice

## Structure

`OriginInvoice`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Optional | The UID of the invoice serving as an origin invoice. |
| `number` | `str` | Optional | The number of the invoice serving as an origin invoice. |

## Example

```python
from advancedbilling.models.origin_invoice import OriginInvoice

origin_invoice = OriginInvoice(
    uid='uid8',
    number='number4'
)
```

