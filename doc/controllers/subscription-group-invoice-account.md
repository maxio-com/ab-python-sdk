# Subscription Group Invoice Account

```python
subscription_group_invoice_account_controller = client.subscription_group_invoice_account
```

## Class Name

`SubscriptionGroupInvoiceAccountController`

## Methods

* [Create Subscription Group Prepayment](../../doc/controllers/subscription-group-invoice-account.md#create-subscription-group-prepayment)
* [List Prepayments for Subscription Group](../../doc/controllers/subscription-group-invoice-account.md#list-prepayments-for-subscription-group)
* [Issue Subscription Group Service Credit](../../doc/controllers/subscription-group-invoice-account.md#issue-subscription-group-service-credit)
* [Deduct Subscription Group Service Credit](../../doc/controllers/subscription-group-invoice-account.md#deduct-subscription-group-service-credit)


# Create Subscription Group Prepayment

A prepayment can be added for a subscription group identified by the group's `uid`. This endpoint requires a `amount`, `details`, `method`, and `memo`. On success, the prepayment will be added to the group's prepayment balance.

```python
def create_subscription_group_prepayment(self,
                                        uid,
                                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Template, Required | The uid of the subscription group |
| `body` | [`SubscriptionGroupPrepaymentRequest`](../../doc/models/subscription-group-prepayment-request.md) | Body, Optional | - |

## Response Type

[`SubscriptionGroupPrepaymentResponse`](../../doc/models/subscription-group-prepayment-response.md)

## Example Usage

```python
uid = 'uid0'

result = subscription_group_invoice_account_controller.create_subscription_group_prepayment(uid)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": 6049554,
  "amount_in_cents": 10000,
  "ending_balance_in_cents": 5000,
  "entry_type": "Debit",
  "memo": "Debit from invoice account."
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# List Prepayments for Subscription Group

This request will list a subscription group's prepayments.

```python
def list_prepayments_for_subscription_group(self,
                                           options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Template, Required | The uid of the subscription group |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br><br>**Default**: `1`<br><br>**Constraints**: `>= 1` |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br><br>**Default**: `20`<br><br>**Constraints**: `<= 200` |
| `filter` | [`ListPrepaymentsFilter`](../../doc/models/list-prepayments-filter.md) | Query, Optional | Filter to use for List Prepayments operations |

## Response Type

[`ListSubscriptionGroupPrepaymentResponse`](../../doc/models/list-subscription-group-prepayment-response.md)

## Example Usage

```python
collect = {
    'uid': 'uid0',
    'page': 2,
    'per_page': 50,
    'filter': ListPrepaymentsFilter(
        date_field=ListPrepaymentDateField.CREATED_AT,
        start_date=dateutil.parser.parse('2024-01-01').date(),
        end_date=dateutil.parser.parse('2024-01-31').date()
    )
}
result = subscription_group_invoice_account_controller.list_prepayments_for_subscription_group(collect)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "prepayments": [
    {
      "prepayment": {
        "id": 142,
        "subscription_group_uid": "grp_b4qhx3bvx72t8",
        "amount_in_cents": 10000,
        "remaining_amount_in_cents": 10000,
        "details": "test",
        "external": true,
        "memo": "test",
        "payment_type": "cash",
        "created_at": "2023-06-21T04:37:02-04:00"
      }
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |


# Issue Subscription Group Service Credit

Credit can be issued for a subscription group identified by the group's `uid`. Credit will be added to the group in the amount specified in the request body. The credit will be applied to group member invoices as they are generated.

```python
def issue_subscription_group_service_credit(self,
                                           uid,
                                           body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Template, Required | The uid of the subscription group |
| `body` | [`IssueServiceCreditRequest`](../../doc/models/issue-service-credit-request.md) | Body, Optional | - |

## Response Type

[`ServiceCreditResponse`](../../doc/models/service-credit-response.md)

## Example Usage

```python
uid = 'uid0'

body = IssueServiceCreditRequest(
    service_credit=IssueServiceCredit(
        amount=10,
        memo='Credit the group account'
    )
)

result = subscription_group_invoice_account_controller.issue_subscription_group_service_credit(
    uid,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "service_credit": {
    "id": 101,
    "amount_in_cents": 1000,
    "ending_balance_in_cents": 2000,
    "entry_type": "Credit",
    "memo": "Credit to group account"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


# Deduct Subscription Group Service Credit

Credit can be deducted for a subscription group identified by the group's `uid`. Credit will be deducted from the group in the amount specified in the request body.

```python
def deduct_subscription_group_service_credit(self,
                                            uid,
                                            body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `uid` | `str` | Template, Required | The uid of the subscription group |
| `body` | [`DeductServiceCreditRequest`](../../doc/models/deduct-service-credit-request.md) | Body, Optional | - |

## Response Type

[`ServiceCredit`](../../doc/models/service-credit.md)

## Example Usage

```python
uid = 'uid0'

body = DeductServiceCreditRequest(
    deduction=DeductServiceCredit(
        amount=10,
        memo='Deduct from group account'
    )
)

result = subscription_group_invoice_account_controller.deduct_subscription_group_service_credit(
    uid,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": 100,
  "amount_in_cents": 1000,
  "ending_balance_in_cents": 0,
  "entry_type": "Debit",
  "memo": "Debit from group account"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |

