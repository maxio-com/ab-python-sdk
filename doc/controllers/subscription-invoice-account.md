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
| `subscription_id` | `str` | Template, Required | The Chargify id of the subscription |

## Response Type

[`AccountBalances`](../../doc/models/account-balances.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

result = subscription_invoice_account_controller.read_account_balances(subscription_id)
print(result)
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
| `subscription_id` | `str` | Template, Required | The Chargify id of the subscription |
| `body` | [`CreatePrepaymentRequest`](../../doc/models/create-prepayment-request.md) | Body, Optional | - |

## Response Type

[`CreatePrepaymentResponse`](../../doc/models/create-prepayment-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

body = CreatePrepaymentRequest(
    prepayment=CreatePrepayment(
        amount=100,
        details='John Doe signup for $100',
        memo='Signup for $100',
        method=PrepaymentMethodEnum.CHECK
    )
)

result = subscription_invoice_account_controller.create_prepayment(
    subscription_id,
    body=body
)
print(result)
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


# List Prepayments

This request will list a subscription's prepayments.

```python
def list_prepayments(self,
                    subscription_id,
                    page=1,
                    per_page=20,
                    filter_date_field=None,
                    filter_start_date=None,
                    filter_end_date=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `subscription_id` | `str` | Template, Required | The Chargify id of the subscription |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br>**Default**: `1`<br>**Constraints**: `>= 1` |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 20. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br>**Default**: `20`<br>**Constraints**: `<= 200` |
| `filter_date_field` | [`BasicDateFieldEnum`](../../doc/models/basic-date-field-enum.md) | Query, Optional | The type of filter you would like to apply to your search. created_at - Time when prepayment was created. application_at - Time when prepayment was applied to invoice. Use in query `filter[date_field]=created_at`. |
| `filter_start_date` | `str` | Query, Optional | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns prepayments with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. Use in query `filter[start_date]=2011-12-15`. |
| `filter_end_date` | `str` | Query, Optional | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns prepayments with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. Use in query `filter[end_date]=2011-12-15`. |

## Response Type

[`SubscriptionsPrepaymentsJsonResponse`](../../doc/models/subscriptions-prepayments-json-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

page = 2

per_page = 50

Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')result = subscription_invoice_account_controller.list_prepayments(Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')Liquid error: Value cannot be null. (Parameter 'key')
    subscription_id,
    page=page,
    per_page=per_page
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "prepayments": [
    {
      "prepayment": {
        "id": 17,
        "subscription_id": 3558750,
        "amount_in_cents": 2000,
        "remaining_amount_in_cents": 1100,
        "external": true,
        "memo": "test",
        "details": "test details",
        "payment_type": "cash",
        "created_at": "2022-01-18T22:45:41+11:00"
      }
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | `APIException` |
| 403 | Forbidden | `APIException` |
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
| `subscription_id` | `str` | Template, Required | The Chargify id of the subscription |
| `body` | [`IssueServiceCreditRequest`](../../doc/models/issue-service-credit-request.md) | Body, Optional | - |

## Response Type

[`ServiceCredit`](../../doc/models/service-credit.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

body = IssueServiceCreditRequest(
    service_credit=IssueServiceCredit(
        amount='1',
        memo='Courtesy credit'
    )
)

result = subscription_invoice_account_controller.issue_service_credit(
    subscription_id,
    body=body
)
print(result)
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
| `subscription_id` | `str` | Template, Required | The Chargify id of the subscription |
| `body` | [`DeductServiceCreditRequest`](../../doc/models/deduct-service-credit-request.md) | Body, Optional | - |

## Response Type

`void`

## Example Usage

```python
subscription_id = 'subscription_id0'

body = DeductServiceCreditRequest(
    deduction=DeductServiceCredit(
        amount='1',
        memo='Deduction'
    )
)

result = subscription_invoice_account_controller.deduct_service_credit(
    subscription_id,
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`ErrorListResponseException`](../../doc/models/error-list-response-exception.md) |


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
| `subscription_id` | `str` | Template, Required | The Chargify id of the subscription |
| `prepayment_id` | `str` | Template, Required | id of prepayment |
| `body` | [`RefundPrepaymentRequest`](../../doc/models/refund-prepayment-request.md) | Body, Optional | - |

## Response Type

[`PrepaymentResponse`](../../doc/models/prepayment-response.md)

## Example Usage

```python
subscription_id = 'subscription_id0'

prepayment_id = 'prepayment_id8'

result = subscription_invoice_account_controller.refund_prepayment(
    subscription_id,
    prepayment_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request | [`SubscriptionsPrepaymentsRefundsJson400ErrorException`](../../doc/models/subscriptions-prepayments-refunds-json-400-error-exception.md) |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`SubscriptionsPrepaymentsRefundsJson422ErrorException`](../../doc/models/subscriptions-prepayments-refunds-json-422-error-exception.md) |

