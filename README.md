
# Getting Started with Maxio Advanced Billing

## Introduction

Maxio Advanced Billing (formerly Chargify) provides an HTTP-based API that conforms to the principles of REST.
One of the many reasons to use Advanced Billing is the immense feature set and [client libraries](page:development-tools/client-libraries).
The Maxio API returns JSON responses as the primary and recommended format, but XML is also provided as a backwards compatible option for merchants who require it.

### Steps to make your first Maxio Advanced Billing API call

1. [Sign-up](https://app.chargify.com/signup/maxio-billing-sandbox) or [log-in](https://app.chargify.com/login.html) to your [test site](https://maxio.zendesk.com/hc/en-us/articles/24250712113165-Testing-Overview) account.
2. [Setup authentication](https://maxio.zendesk.com/hc/en-us/articles/24294819360525-API-Keys) credentials.
3. [Submit an API request and verify the response](page:development-tools/client-libraries#make-your-first-maxio-advanced-billing-api-request).
4. Test the Advanced Billing [integrations](https://www.maxio.com/integrations).

Next, you can explore [authentication methods](page:introduction/authentication), [basic concepts](page:introduction/basic-concepts/connected-sites) for interacting with Advanced Billing via the API, and the entire set of [application-based documentation](https://docs.maxio.com/hc/en-us) to aid in your discovery of the product.

#### Request Example

The following example uses the curl command-line tool to make an API request.

**Request**

curl -u <api_key>:x -H Accept:application/json -H Content-Type:application/json https://acme.chargify.com/subscriptions.json

## Install the Package

The package is compatible with Python versions `3.7+`.
Install the package from PyPi using the following pip command:

```bash
pip install maxio-advanced-billing-sdk==7.0.0
```

You can also view the package at:
https://pypi.python.org/pypi/maxio-advanced-billing-sdk/7.0.0

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| site | `str` | The subdomain for your Advanced Billing site.<br>*Default*: `'subdomain'` |
| environment | `Environment` | The API environment. <br> **Default: `Environment.US`** |
| http_client_instance | `HttpClient` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 120** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| basic_auth_credentials | [`BasicAuthCredentials`](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/auth/basic-authentication.md) | The credential object for Basic Authentication |

The API client can be initialized as follows:

```python
from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment
from advancedbilling.http.auth.basic_auth import BasicAuthCredentials

client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    ),
    environment=Environment.US,
    site='subdomain'
)
```

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| US | **Default** Default Advanced Billing environment hosted in US. Valid for the majority of our customers. |
| EU | Advanced Billing environment hosted in EU. Use only when you requested EU hosting for your AB account. |

## Authorization

This API uses the following authentication schemes.

* [`BasicAuth (Basic Authentication)`](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/auth/basic-authentication.md)

## List of APIs

* [API Exports](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/api-exports.md)
* [Advance Invoice](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/advance-invoice.md)
* [Billing Portal](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/billing-portal.md)
* [Component Price Points](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/component-price-points.md)
* [Custom Fields](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/custom-fields.md)
* [Events-Based Billing Segments](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/events-based-billing-segments.md)
* [Payment Profiles](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/payment-profiles.md)
* [Product Families](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/product-families.md)
* [Product Price Points](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/product-price-points.md)
* [Proforma Invoices](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/proforma-invoices.md)
* [Reason Codes](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/reason-codes.md)
* [Referral Codes](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/referral-codes.md)
* [Sales Commissions](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/sales-commissions.md)
* [Subscription Components](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/subscription-components.md)
* [Subscription Groups](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/subscription-groups.md)
* [Subscription Group Invoice Account](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/subscription-group-invoice-account.md)
* [Subscription Group Status](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/subscription-group-status.md)
* [Subscription Invoice Account](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/subscription-invoice-account.md)
* [Subscription Notes](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/subscription-notes.md)
* [Subscription Products](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/subscription-products.md)
* [Subscription Status](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/subscription-status.md)
* [Coupons](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/coupons.md)
* [Components](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/components.md)
* [Customers](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/customers.md)
* [Events](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/events.md)
* [Insights](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/insights.md)
* [Invoices](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/invoices.md)
* [Offers](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/offers.md)
* [Products](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/products.md)
* [Sites](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/sites.md)
* [Subscriptions](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/subscriptions.md)
* [Webhooks](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/controllers/webhooks.md)

## SDK Infrastructure

### HTTP

* [HttpResponse](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/http-response.md)
* [HttpRequest](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/http-request.md)

### Utilities

* [ApiHelper](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/api-helper.md)
* [HttpDateTime](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/http-date-time.md)
* [RFC3339DateTime](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/rfc3339-date-time.md)
* [UnixDateTime](https://www.github.com/maxio-com/ab-python-sdk/tree/7.0.0/doc/unix-date-time.md)

