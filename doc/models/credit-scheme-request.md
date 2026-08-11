
# Credit Scheme Request

## Structure

`CreditSchemeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `credit_scheme` | [`CreditScheme`](../../doc/models/credit-scheme.md) | Required | - |

## Example

```python
from advancedbilling.models.credit_scheme import CreditScheme
from advancedbilling.models.credit_scheme_request import CreditSchemeRequest

credit_scheme_request = CreditSchemeRequest(
    credit_scheme=CreditScheme.REFUND
)
```

