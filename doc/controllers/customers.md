# Customers

```python
customers_controller = client.customers
```

## Class Name

`CustomersController`

## Methods

* [Create Customer](../../doc/controllers/customers.md#create-customer)
* [List Customers](../../doc/controllers/customers.md#list-customers)
* [Read Customer](../../doc/controllers/customers.md#read-customer)
* [Update Customer](../../doc/controllers/customers.md#update-customer)
* [Delete Customer](../../doc/controllers/customers.md#delete-customer)
* [Read Customer by Reference](../../doc/controllers/customers.md#read-customer-by-reference)
* [List Customer Subscriptions](../../doc/controllers/customers.md#list-customer-subscriptions)


# Create Customer

You may create a new Customer at any time, or you may create a Customer at the same time you create a Subscription. The only validation restriction is that you may only create one customer for a given reference value.

If provided, the `reference` value must be unique. It represents a unique identifier for the customer from your own app, i.e. the customer’s ID. This allows you to retrieve a given customer via a piece of shared information. Alternatively, you may choose to leave `reference` blank, and store Advanced Billing’s unique ID for the customer, which is in the `id` attribute.

Full documentation on how to locate, create and edit Customers in the Advanced Billing UI can be located [here](https://maxio.zendesk.com/hc/en-us/articles/24252190590093-Customer-Details).

## Required Country Format

Advanced Billing requires that you use the ISO Standard Country codes when formatting country attribute of the customer.

Countries should be formatted as 2 characters. For more information, please see the following wikipedia article on [ISO_3166-1.](http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes)

## Required State Format

Advanced Billing requires that you use the ISO Standard State codes when formatting state attribute of the customer.

+ US States (2 characters): [ISO_3166-2](https://en.wikipedia.org/wiki/ISO_3166-2:US)

+ States Outside the US (2-3 characters): To find the correct state codes outside of the US, please go to [ISO_3166-1](http://en.wikipedia.org/wiki/ISO_3166-1#Current_codes) and click on the link in the “ISO 3166-2 codes” column next to country you wish to populate.

## Locale

Advanced Billing allows you to attribute a language/region to your customer to deliver invoices in any required language.
For more: [Customer Locale](https://maxio.zendesk.com/hc/en-us/articles/24286672013709-Customer-Locale)

```python
def create_customer(self,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateCustomerRequest`](../../doc/models/create-customer-request.md) | Body, Optional | - |

## Response Type

[`CustomerResponse`](../../doc/models/customer-response.md)

## Example Usage

```python
body = CreateCustomerRequest(
    customer=CreateCustomer(
        first_name='Martha',
        last_name='Washington',
        email='martha@example.com',
        cc_emails='george@example.com',
        organization='ABC, Inc.',
        reference='1234567890',
        address='123 Main Street',
        address_2='Unit 10',
        city='Anytown',
        state='MA',
        zip='02120',
        country='US',
        phone='555-555-1212',
        locale='es-MX'
    )
)

result = customers_controller.create_customer(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "customer": {
    "first_name": "Cathryn",
    "last_name": "Parisian",
    "email": "Stella.McLaughlin6@example.net",
    "cc_emails": null,
    "organization": "Greenholt - Oberbrunner",
    "reference": null,
    "id": 76,
    "created_at": "2021-03-29T07:47:00-04:00",
    "updated_at": "2021-03-29T07:47:00-04:00",
    "address": "739 Stephon Bypass",
    "address_2": "Apt. 386",
    "city": "Sedrickchester",
    "state": "KY",
    "state_name": "Kentucky",
    "zip": "46979-7719",
    "country": "US",
    "country_name": "United States",
    "phone": "230-934-3685",
    "verified": false,
    "portal_customer_created_at": null,
    "portal_invite_last_sent_at": null,
    "portal_invite_last_accepted_at": null,
    "tax_exempt": false,
    "vat_number": null,
    "parent_id": null,
    "locale": "en-US"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 422 | Unprocessable Entity (WebDAV) | [`CustomerErrorResponseException`](../../doc/models/customer-error-response-exception.md) |


# List Customers

This request will by default list all customers associated with your Site.

## Find Customer

Use the search feature with the `q` query parameter to retrieve an array of customers that matches the search query.

Common use cases are:

+ Search by an email
+ Search by an Advanced Billing ID
+ Search by an organization
+ Search by a reference value from your application
+ Search by a first or last name

To retrieve a single, exact match by reference, please use the [lookup endpoint](https://developers.chargify.com/docs/api-docs/b710d8fbef104-read-customer-by-reference).

```python
def list_customers(self,
                  options=dict())
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `direction` | [`SortingDirection`](../../doc/models/sorting-direction.md) | Query, Optional | Direction to sort customers by time of creation |
| `page` | `int` | Query, Optional | Result records are organized in pages. By default, the first page of results is displayed. The page parameter specifies a page number of results to fetch. You can start navigating through the pages to consume the results. You do this by passing in a page parameter. Retrieve the next page by adding ?page=2 to the query string. If there are no results to return, then an empty result set will be returned.<br>Use in query `page=1`.<br><br>**Default**: `1`<br><br>**Constraints**: `>= 1` |
| `per_page` | `int` | Query, Optional | This parameter indicates how many records to fetch in each request. Default value is 50. The maximum allowed values is 200; any per_page value over 200 will be changed to 200.<br>Use in query `per_page=200`.<br><br>**Default**: `50`<br><br>**Constraints**: `<= 200` |
| `date_field` | [`BasicDateField`](../../doc/models/basic-date-field.md) | Query, Optional | The type of filter you would like to apply to your search.<br>Use in query: `date_field=created_at`. |
| `start_date` | `str` | Query, Optional | The start date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions with a timestamp at or after midnight (12:00:00 AM) in your site’s time zone on the date specified. |
| `end_date` | `str` | Query, Optional | The end date (format YYYY-MM-DD) with which to filter the date_field. Returns subscriptions with a timestamp up to and including 11:59:59PM in your site’s time zone on the date specified. |
| `start_datetime` | `str` | Query, Optional | The start date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns subscriptions with a timestamp at or after exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of start_date. |
| `end_datetime` | `str` | Query, Optional | The end date and time (format YYYY-MM-DD HH:MM:SS) with which to filter the date_field. Returns subscriptions with a timestamp at or before exact time provided in query. You can specify timezone in query - otherwise your site's time zone will be used. If provided, this parameter will be used instead of end_date. |
| `q` | `str` | Query, Optional | A search query by which to filter customers (can be an email, an ID, a reference, organization) |

## Response Type

[`List[CustomerResponse]`](../../doc/models/customer-response.md)

## Example Usage

```python
collect = {
    'page': 2,
    'per_page': 30,
    'date_field': BasicDateField.UPDATED_AT
}
result = customers_controller.list_customers(collect)
print(result)
```

## Example Response *(as JSON)*

```json
[
  {
    "customer": {
      "first_name": "Kayla",
      "last_name": "Test",
      "email": "kayla@example.com",
      "cc_emails": "john@example.com, sue@example.com",
      "organization": "",
      "reference": null,
      "id": 14126091,
      "created_at": "2016-10-04T15:22:27-04:00",
      "updated_at": "2016-10-04T15:22:30-04:00",
      "address": "",
      "address_2": "",
      "city": "",
      "state": "",
      "zip": "",
      "country": "",
      "phone": "",
      "verified": null,
      "portal_customer_created_at": "2016-10-04T15:22:29-04:00",
      "portal_invite_last_sent_at": "2016-10-04T15:22:30-04:00",
      "portal_invite_last_accepted_at": null,
      "tax_exempt": false
    }
  },
  {
    "customer": {
      "first_name": "Nick ",
      "last_name": "Test",
      "email": "nick@example.com",
      "cc_emails": "john@example.com, sue@example.com",
      "organization": "",
      "reference": null,
      "id": 14254093,
      "created_at": "2016-10-13T16:52:51-04:00",
      "updated_at": "2016-10-13T16:52:54-04:00",
      "address": "",
      "address_2": "",
      "city": "",
      "state": "",
      "zip": "",
      "country": "",
      "phone": "",
      "verified": null,
      "portal_customer_created_at": "2016-10-13T16:52:54-04:00",
      "portal_invite_last_sent_at": "2016-10-13T16:52:54-04:00",
      "portal_invite_last_accepted_at": null,
      "tax_exempt": false,
      "parent_id": 123
    }
  },
  {
    "customer": {
      "first_name": "Don",
      "last_name": "Test",
      "email": "don@example.com",
      "cc_emails": "john@example.com, sue@example.com",
      "organization": "",
      "reference": null,
      "id": 14332342,
      "created_at": "2016-10-19T10:49:13-04:00",
      "updated_at": "2016-10-19T10:49:19-04:00",
      "address": "1737 15th St",
      "address_2": "",
      "city": "Boulder",
      "state": "CO",
      "zip": "80302",
      "country": "US",
      "phone": "",
      "verified": null,
      "portal_customer_created_at": "2016-10-19T10:49:19-04:00",
      "portal_invite_last_sent_at": "2016-10-19T10:49:19-04:00",
      "portal_invite_last_accepted_at": null,
      "tax_exempt": false,
      "parent_id": null
    }
  }
]
```


# Read Customer

This method allows to retrieve the Customer properties by Advanced Billing-generated Customer ID.

```python
def read_customer(self,
                 id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | The Advanced Billing id of the customer |

## Response Type

[`CustomerResponse`](../../doc/models/customer-response.md)

## Example Usage

```python
id = 112

result = customers_controller.read_customer(id)
print(result)
```


# Update Customer

This method allows to update the Customer.

```python
def update_customer(self,
                   id,
                   body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | The Advanced Billing id of the customer |
| `body` | [`UpdateCustomerRequest`](../../doc/models/update-customer-request.md) | Body, Optional | - |

## Response Type

[`CustomerResponse`](../../doc/models/customer-response.md)

## Example Usage

```python
id = 112

body = UpdateCustomerRequest(
    customer=UpdateCustomer(
        first_name='Martha',
        last_name='Washington',
        email='martha.washington@example.com'
    )
)

result = customers_controller.update_customer(
    id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "customer": {
    "first_name": "Martha",
    "last_name": "Washington",
    "email": "martha.washington@example.com",
    "cc_emails": "george.washington@example.com",
    "organization": null,
    "reference": null,
    "id": 14967442,
    "created_at": "2016-12-05T10:33:07-05:00",
    "updated_at": "2016-12-05T10:38:00-05:00",
    "address": null,
    "address_2": null,
    "city": null,
    "state": null,
    "zip": null,
    "country": null,
    "phone": null,
    "verified": false,
    "portal_customer_created_at": null,
    "portal_invite_last_sent_at": null,
    "portal_invite_last_accepted_at": null,
    "tax_exempt": false,
    "vat_number": "012345678"
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not Found | `APIException` |
| 422 | Unprocessable Entity (WebDAV) | [`CustomerErrorResponseException`](../../doc/models/customer-error-response-exception.md) |


# Delete Customer

This method allows you to delete the Customer.

```python
def delete_customer(self,
                   id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `int` | Template, Required | The Advanced Billing id of the customer |

## Response Type

`void`

## Example Usage

```python
id = 112

customers_controller.delete_customer(id)
```


# Read Customer by Reference

Use this method to return the customer object if you have the unique **Reference ID (Your App)** value handy. It will return a single match.

```python
def read_customer_by_reference(self,
                              reference)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `reference` | `str` | Query, Required | Customer reference |

## Response Type

[`CustomerResponse`](../../doc/models/customer-response.md)

## Example Usage

```python
reference = 'reference4'

result = customers_controller.read_customer_by_reference(reference)
print(result)
```


# List Customer Subscriptions

This method lists all subscriptions that belong to a customer.

```python
def list_customer_subscriptions(self,
                               customer_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `customer_id` | `int` | Template, Required | The Chargify id of the customer |

## Response Type

[`List[SubscriptionResponse]`](../../doc/models/subscription-response.md)

## Example Usage

```python
customer_id = 150

result = customers_controller.list_customer_subscriptions(customer_id)
print(result)
```

