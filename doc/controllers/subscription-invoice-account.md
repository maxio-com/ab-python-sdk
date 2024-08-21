# Subscription Invoice Account

```python
subscription_invoice_account_controller = client.subscription_invoice_account
```

## Class Name

`SubscriptionInvoiceAccountController`

## Methods

* [Read Account Balances](../../doc/controllers/subscription-invoice-account.md#read-account-balances)
* [Create Prepayment](../../doc/controllers/subscription-invoice-account.md#create-prepayment)
* [List Prepayments](../../doc/controllers/subscription-invoice-account.md#list-prepayments)
* [Issue Service Credit](../../doc/controllers/subscription-invoice-account.md#issue-service-credit)
* [Deduct Service Credit](../../doc/controllers/subscription-invoice-account.md#deduct-service-credit)
* [Refund Prepayment](../../doc/controllers/subscription-invoice-account.md#refund-prepayment)


# Read Account Balances

Returns the `balance_in_cents` of the Subscription's Pending Discount, Service Credit, and Prepayment accounts, as well as the sum of the Subscription's open, payable invoices.

```python
def read_account_balances(self,
                         subscription_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription |

## Response Type

[`AccountBalances`](../../doc/models/account-balances.md)

## Example Usage

```python
subscription_id = 222

result = subscription_invoice_account_controller.read_account_balances(subscription_id)
```


# Create Prepayment

## Create Prepayment

In order to specify a prepayment made against a subscription, specify the `amount, memo, details, method`.

When the `method` specified is `"credit_card_on_file"`, the prepayment amount will be collected using the default credit card payment profile and applied to the prepayment account balance.  This is especially useful for manual replenishment of prepaid subscriptions.

Please note that you **can't** pass `amount_in_cents`.

```python
def create_prepayment(self,
                     subscription_id,
                     body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription |
| `body` | [`CreatePrepaymentRequest`](../../doc/models/create-prepayment-request.md) | Body, Optional | - |

## Response Type

[`CreatePrepaymentResponse`](../../doc/models/create-prepayment-response.md)

## Example Usage

```python
subscription_id = 222

body = CreatePrepaymentRequest(
    prepayment=CreatePrepayment(
        amount=100,
        details='John Doe signup for $100',
        memo='Signup for $100',
        method=CreatePrepaymentMethod.CHECK
    )
)

result = subscription_invoice_account_controller.create_prepayment(
    subscription_id,
    body=body
)
```

## Example Response *(as JSON)*

```json
{
  "prepayment": {
    "id": 1,
    "subscription_id": 1,
    "amount_in_cents": 10000,
    "memo": "John Doe - Prepayment",
    "created_at": "2020-07-31T05:52:32-04:00",
    "starting_balance_in_cents": 0,
    "ending_balance_in_cents": -10000
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | `APIException` |


# List Prepayments

This request will list a subscription's prepayments.

```python
def list_prepayments(self,
                    options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`. |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`. |
| `filter` | [`ListPrepaymentsFilter`](../../doc/models/list-prepayments-filter.md) | Query, Optional | Filter to use for List Prepayments operations |

## Response Type

[`PrepaymentsResponse`](../../doc/models/prepayments-response.md)

## Example Usage

```python
collect = {
    'subscription_id': 222,
    'page': 2,
    'per_page': 50,
    'filter': ListPrepaymentsFilter(
        date_field=ListPrepaymentDateField.CREATED_AT,
        start_date=dateutil.parser.parse('2024-01-01').date(),
        end_date=dateutil.parser.parse('2024-01-31').date()
    )
}
result = subscription_invoice_account_controller.list_prepayments(collect)
```

## Example Response *(as JSON)*

```json
{
  "prepayments": [
    {
      "id": 17,
      "subscription_id": 3558750,
      "amount_in_cents": 2000,
      "remaining_amount_in_cents": 1100,
      "refunded_amount_in_cents": 0,
      "external": true,
      "memo": "test",
      "details": "test details",
      "payment_type": "cash",
      "created_at": "2022-01-18T22:45:41+11:00"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |


# Issue Service Credit

Credit will be added to the subscription in the amount specified in the request body. The credit is subsequently applied to the next generated invoice.

```python
def issue_service_credit(self,
                        subscription_id,
                        body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription |
| `body` | [`IssueServiceCreditRequest`](../../doc/models/issue-service-credit-request.md) | Body, Optional | - |

## Response Type

[`ServiceCredit`](../../doc/models/service-credit.md)

## Example Usage

```python
subscription_id = 222

body = IssueServiceCreditRequest(
    service_credit=IssueServiceCredit(
        amount='1'
    )
)

result = subscription_invoice_account_controller.issue_service_credit(
    subscription_id,
    body=body
)
```

## Example Response *(as JSON)*

```json
{
  "id": 101,
  "amount_in_cents": 1000,
  "ending_balance_in_cents": 2000,
  "entry_type": "Credit",
  "memo": "Credit to group account"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | `APIException` |


# Deduct Service Credit

Credit will be removed from the subscription in the amount specified in the request body. The credit amount being deducted must be equal to or less than the current credit balance.

```python
def deduct_service_credit(self,
                         subscription_id,
                         body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription |
| `body` | [`DeductServiceCreditRequest`](../../doc/models/deduct-service-credit-request.md) | Body, Optional | - |

## Response Type

`void`

## Example Usage

```python
subscription_id = 222

body = DeductServiceCreditRequest(
    deduction=DeductServiceCredit(
        amount='1',
        memo='Deduction'
    )
)

subscription_invoice_account_controller.deduct_service_credit(
    subscription_id,
    body=body
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | `APIException` |


# Refund Prepayment

This endpoint will refund, completely or partially, a particular prepayment applied to a subscription. The `prepayment_id` will be the account transaction ID of the original payment. The prepayment must have some amount remaining in order to be refunded.

The amount may be passed either as a decimal, with `amount`, or an integer in cents, with `amount_in_cents`.

```python
def refund_prepayment(self,
                     subscription_id,
                     prepayment_id,
                     body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `int` | Template, Required | The Chargify id of the subscription |
| `prepayment_id` | `long\|int` | Template, Required | id of prepayment |
| `body` | [`RefundPrepaymentRequest`](../../doc/models/refund-prepayment-request.md) | Body, Optional | - |

## Response Type

[`PrepaymentResponse`](../../doc/models/prepayment-response.md)

## Example Usage

```python
subscription_id = 222

prepayment_id = 228

result = subscription_invoice_account_controller.refund_prepayment(
    subscription_id,
    prepayment_id
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`RefundPrepaymentBaseErrorsResponseException`](../../doc/models/refund-prepayment-base-errors-response-exception.md) |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity | `APIException` |

