
# Collection Method

The type of payment collection to be used in the subscription. For legacy Statements Architecture valid options are - `invoice`, `automatic`. For current Relationship Invoicing Architecture valid options are - `remittance`, `automatic`, `prepaid`.

## Enumeration

`CollectionMethod`

## Fields

| Name |
|  --- |
| `AUTOMATIC` |
| `REMITTANCE` |
| `PREPAID` |
| `INVOICE` |

## Example

```python
from advancedbilling.models.collection_method import CollectionMethod

collection_method = CollectionMethod.PREPAID
```

