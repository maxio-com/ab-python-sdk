
# Getting Started with Maxio Advanced Billing

## Introduction

Maxio Advanced Billing (formerly Chargify) provides an HTTP-based API that conforms to the principles of REST.
One of the many reasons to use Advanced Billing is the immense feature set and surrounding community [client libraries](page:development-tools/client-libraries).
The Maxio API returns JSON responses as the primary and recommended format, but XML is also provided as a backwards compatible option for Merchants who require it.

### Steps to make your first Maxio Advanced Billing API call

1. [Sign-up](https://app.chargify.com/signup/maxio-billing-sandbox) or [log-in](https://app.chargify.com/login.html) to your [test site](https://maxio-chargify.zendesk.com/hc/en-us/articles/5405553861773-Testing-Intro) account.
2. [Setup and configure authentication](https://maxio-chargify.zendesk.com/hc/en-us/articles/5405281550477-API-Keys#api) credentials.
3. Submit your API request and try it out.
4. Verify results through response.
5. Test our integrations.

We strongly suggest exploring the developer portal, our [integrations](https://www.maxio.com/integrations) and the API guide, as well as the entire set of application-based documentation to aid in your discovery of the product.

#### Example

The following example uses the curl command-line tool to execute API requests.

**Request**

curl -u <api_key>:x -H Accept:application/json -H Content-Type:application/json https://acme.chargify.com/subscriptions.json

## Install the Package

The package is compatible with Python versions `3 >=3.7, <= 3.11`.
Install the package from PyPi using the following pip command:

```python
pip install maxio-advanced-billing-sdk==1.0.1
```

You can also view the package at:
https://pypi.python.org/pypi/maxio-advanced-billing-sdk/1.0.1

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `subdomain` | `str` | The subdomain for your Chargify site.<br>*Default*: `'subdomain'` |
| `domain` | `str` | The Chargify server domain.<br>*Default*: `'chargify.com'` |
| `environment` | `Environment` | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 30** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `basic_auth_credentials` | [`BasicAuthCredentials`](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/$a/https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/basic-authentication.md) | The credential object for Basic Authentication |

The API client can be initialized as follows:

```python
client = AdvancedBillingClient(
    basic_auth_credentials=BasicAuthCredentials(
        username='BasicAuthUserName',
        password='BasicAuthPassword'
    )
)
```

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| production | **Default** Production server |
| environment2 | Production server |

## Authorization

This API uses the following authentication schemes.

* [`BasicAuth (Basic Authentication)`](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/$a/https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/basic-authentication.md)

## List of APIs

* [API Exports](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/api-exports.md)
* [Advance Invoice](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/advance-invoice.md)
* [Billing Portal](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/billing-portal.md)
* [Custom Fields](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/custom-fields.md)
* [Events-Based Billing Segments](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/events-based-billing-segments.md)
* [Payment Profiles](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/payment-profiles.md)
* [Product Families](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/product-families.md)
* [Product Price Points](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/product-price-points.md)
* [Proforma Invoices](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/proforma-invoices.md)
* [Reason Codes](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/reason-codes.md)
* [Referral Codes](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/referral-codes.md)
* [Sales Commissions](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/sales-commissions.md)
* [Subscription Components](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/subscription-components.md)
* [Subscription Groups](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/subscription-groups.md)
* [Subscription Group Invoice Account](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/subscription-group-invoice-account.md)
* [Subscription Group Status](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/subscription-group-status.md)
* [Subscription Invoice Account](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/subscription-invoice-account.md)
* [Subscription Notes](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/subscription-notes.md)
* [Subscription Products](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/subscription-products.md)
* [Subscription Status](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/subscription-status.md)
* [Coupons](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/coupons.md)
* [Components](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/components.md)
* [Customers](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/customers.md)
* [Events](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/events.md)
* [Insights](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/insights.md)
* [Invoices](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/invoices.md)
* [Offers](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/offers.md)
* [Products](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/products.md)
* [Sites](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/sites.md)
* [Subscriptions](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/subscriptions.md)
* [Webhooks](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/controllers/webhooks.md)

## Classes Documentation

* [Utility Classes](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/utility-classes.md)
* [HttpResponse](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/http-response.md)
* [HttpRequest](https://www.github.com/maxio-com/ab-python-sdk/tree/1.0.1/doc/http-request.md)

