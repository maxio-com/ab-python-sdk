
# Invoice Role

## Enumeration

`InvoiceRole`

## Fields

| Name |
|  --- |
| `UNSET` |
| `SIGNUP` |
| `RENEWAL` |
| `USAGE` |
| `REACTIVATION` |
| `PRORATION` |
| `MIGRATION` |
| `ADHOC` |
| `BACKPORT` |
| `BACKPORTBALANCERECONCILIATION` |

## Example

```python
from advancedbilling.models.invoice_role import InvoiceRole

invoice_role = InvoiceRole.RENEWAL
```

