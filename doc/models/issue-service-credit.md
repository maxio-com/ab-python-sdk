
# Issue Service Credit

## Structure

`IssueServiceCredit`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | float \| str | Required | This is a container for one-of cases. |
| `memo` | `str` | Optional | - |

## Example

```python
from advancedbilling.models.issue_service_credit import IssueServiceCredit

issue_service_credit = IssueServiceCredit(
    amount=216.68,
    memo='memo6'
)
```

