
# Client Class Documentation

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| `subdomain` | `str` | The subdomain for your Chargify site.<br>*Default*: `'subdomain'` |
| `domain` | `str` | The Chargify server domain.<br>*Default*: `'chargify.com'` |
| `environment` | Environment | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| `http_client_instance` | `HttpClient` | The Http Client passed from the sdk user for making requests |
| `override_http_client_configuration` | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| `http_call_back` | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| `timeout` | `float` | The value to use for connection timeout. <br> **Default: 30** |
| `max_retries` | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| `backoff_factor` | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| `retry_statuses` | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| `retry_methods` | `Array of string` | The http methods on which retry is to be done. <br> **Default: ['GET', 'PUT']** |
| `basic_auth_user_name` | `str` | The username to use with basic authentication |
| `basic_auth_password` | `str` | The password to use with basic authentication |

The API client can be initialized as follows:

```python
from advancedbilling.advanced_billing_client import AdvancedBillingClient
from advancedbilling.configuration import Environment

client = AdvancedBillingClient(
    basic_auth_user_name='BasicAuthUserName',
    basic_auth_password='BasicAuthPassword'
)
```

## Maxio Advanced Billing Client

The gateway for the SDK. This class acts as a factory for the Controllers and also holds the configuration of the SDK.

## Controllers

| Name | Description |
|  --- | --- |
| api_exports | Gets APIExportsController |
| advance_invoice | Gets AdvanceInvoiceController |
| billing_portal | Gets BillingPortalController |
| coupons | Gets CouponsController |
| components | Gets ComponentsController |
| customers | Gets CustomersController |
| custom_fields | Gets CustomFieldsController |
| events | Gets EventsController |
| events_based_billing_segments | Gets EventsBasedBillingSegmentsController |
| insights | Gets InsightsController |
| invoices | Gets InvoicesController |
| offers | Gets OffersController |
| payment_profiles | Gets PaymentProfilesController |
| product_families | Gets ProductFamiliesController |
| products | Gets ProductsController |
| product_price_points | Gets ProductPricePointsController |
| proforma_invoices | Gets ProformaInvoicesController |
| reason_codes | Gets ReasonCodesController |
| referral_codes | Gets ReferralCodesController |
| sales_commissions | Gets SalesCommissionsController |
| sites | Gets SitesController |
| subscriptions | Gets SubscriptionsController |
| subscription_components | Gets SubscriptionComponentsController |
| subscription_groups | Gets SubscriptionGroupsController |
| subscription_group_invoice_account | Gets SubscriptionGroupInvoiceAccountController |
| subscription_group_status | Gets SubscriptionGroupStatusController |
| subscription_invoice_account | Gets SubscriptionInvoiceAccountController |
| subscription_notes | Gets SubscriptionNotesController |
| subscription_products | Gets SubscriptionProductsController |
| subscription_status | Gets SubscriptionStatusController |
| webhooks | Gets WebhooksController |

