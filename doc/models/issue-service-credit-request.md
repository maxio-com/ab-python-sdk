
# Issue Service Credit Request

## Structure

`IssueServiceCreditRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `service_credit` | [`IssueServiceCredit`](../../doc/models/issue-service-credit.md) | Required | - |

## Example

```python
from advancedbilling.models.issue_service_credit import IssueServiceCredit
from advancedbilling.models.issue_service_credit_request import IssueServiceCreditRequest

issue_service_credit_request = IssueServiceCreditRequest(
    service_credit=IssueServiceCredit(
        amount=31.42,
        memo='memo0'
    )
)
```

