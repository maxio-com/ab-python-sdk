# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from advancedbilling.api_helper import APIHelper
from advancedbilling.configuration import Server
from advancedbilling.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from advancedbilling.http.http_method_enum import HttpMethodEnum
from apimatic_core.types.array_serialization_format import SerializationFormats
from apimatic_core.authentication.multiple.single_auth import Single
from advancedbilling.models.subscription_response import SubscriptionResponse
from advancedbilling.models.prepaid_configuration_response import PrepaidConfigurationResponse
from advancedbilling.models.subscription_preview_response import SubscriptionPreviewResponse
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException
from advancedbilling.exceptions.single_error_response_exception import SingleErrorResponseException
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.subscription_response_error_exception import SubscriptionResponseErrorException
from advancedbilling.exceptions.subscription_add_coupon_error_exception import SubscriptionAddCouponErrorException
from advancedbilling.exceptions.subscription_remove_coupon_errors_exception import SubscriptionRemoveCouponErrorsException
from advancedbilling.exceptions.error_array_map_response_exception import ErrorArrayMapResponseException


class SubscriptionsController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(SubscriptionsController, self).__init__(config)

    def create_subscription(self,
                            body=None):
        """Does a POST request to /subscriptions.json.

        Full documentation on how subscriptions operate within Advanced
        Billing can be located under the following topics:
        + [Subscriptions
        Reference](https://maxio.zendesk.com/hc/en-us/articles/24251526991757-S
        ubscription-Overview)
        + [Subscriptions
        Actions](https://maxio.zendesk.com/hc/en-us/articles/24251983024653-Sub
        scription-Actions-Overview)
        + [Subscription
        Cancellation](https://maxio.zendesk.com/hc/en-us/articles/2425195777882
        9-Cancel-Subscriptions)
        + [Subscription
        Reactivation](https://maxio.zendesk.com/hc/en-us/articles/2425210950362
        9-Reactivating-and-Resuming)
        + [Subscription
        Import](https://maxio.zendesk.com/hc/en-us/articles/24251489107213-Impo
        rts)
        When creating a subscription, you must specify a product and a
        customer. Credit card details may be required, depending on the
        options for the Product being subscribed ([see Product
        Options](https://maxio.zendesk.com/hc/en-us/articles/24261076617869-Pro
        duct-Editing)).
        The product may be specified by `product_id` or by `product_handle`
        (API Handle). In similar fashion, to pass a particular product price
        point, you may either use `product_price_point_handle` or
        `product_price_point_id`.
        An existing customer may be specified by a `customer_id` (ID within
        Advanced Billing) or a `customer_reference` (unique value within your
        app that you have shared with Advanced Billing via the reference
        attribute on a customer). You may also pass in an existing payment
        profile for that customer with `payment_profile_id`. A new customer
        may be created by providing `customer_attributes`.
        Credit card details may be required, depending on the options for the
        product being subscribed. The product can be specified by `product_id`
        or by `product_handle` (API Handle).
        If you are creating a subscription with a payment profile, the
        attribute to send will be `credit_card_attributes` or
        `bank_account_attributes` for ACH and Direct Debit. That said, when
        you read the subscription after creation, we return the profile
        details under `credit_card` or `bank_account`.
        ## Bulk creation of subscriptions
        Bulk creation of subscriptions is currently not supported. For
        scenarios where multiple subscriptions must be added, particularly
        when assigning to the same subscription group, it is essential to
        switch to a single-threaded approach. 
        To avoid data conflicts or inaccuracies, incorporate a sleep interval
        between requests.
        While this single-threaded approach may impact performance, it ensures
        data consistency and accuracy in cases where concurrent creation
        attempts could otherwise lead to issues with subscription alignment
        and integrity.        
        ## Taxable Subscriptions
        If your intent is to charge your subscribers tax via [Avalara
        Taxes](https://maxio.zendesk.com/hc/en-us/articles/24287043035661-Avala
        ra-VAT-Tax) or [Custom
        Taxes](https://maxio.zendesk.com/hc/en-us/articles/24287044212749-Custo
        m-Taxes), there are a few considerations to be made regarding
        collecting subscription data.
        For subscribers to be eligible to be taxed, the following information
        for the `customer` object or `payment_profile` object must by supplied:
        + A subscription to a [taxable
        product](https://maxio.zendesk.com/hc/en-us/articles/24261076617869-Pro
        duct-Editing#tax-settings)
        + [Full valid billing or shipping
        address](https://maxio.zendesk.com/hc/en-us/articles/24287008131853-Adv
        anced-Billing-Managed-Sales-Tax#full-address-required-for-taxable-subsc
        riptions) to identify the tax locale
        + The portion of the address that houses the [state
        information](https://maxio.zendesk.com/hc/en-us/articles/24287008131853
        -Advanced-Billing-Managed-Sales-Tax#required-state-format-for-taxable-s
        ubscriptions) of either adddress must adhere to the ISO standard of a
        2-3 character limit/format.
        + The portion of the address that houses the [country
        information](https://maxio.zendesk.com/hc/en-us/articles/24287008131853
        -Advanced-Billing-Managed-Sales-Tax#required-country-format-for-taxable
        -subscriptions) must adhere to the ISO standard of a 2 character
        limit/format.
        ## Subscription Request Examples
        The subscription examples below will be split into two sections.
        The first section, "Subscription Customization", will focus on passing
        different information with a subscription, such as components,
        calendar billing, and custom fields. These examples will presume you
        are using a secure `chargify_token` generated by Chargify.js.
        The second section, "Passing Payment Information", will focus on
        passing payment information into Advanced Billing. Please be aware
        that <b>collecting and sending Advanced Billing raw card details
        requires PCI compliance on your end</b>; these examples are provided
        as guidance. If your business is not PCI compliant, we recommend using
        Chargify.js to collect credit cards or bank accounts.
        # Subscription Customization
        ## With Components
        Different components require slightly different data. For example,
        quantity-based and on/off components accept `allocated_quantity`,
        while metered components accept `unit_balance`.
        When creating a subscription with a component, a `price_point_id` can
        be passed in along with the `component_id` to specify which price
        point to use. If not passed in, the default price point will be used.
        Note: if an invalid `price_point_id` is used, the subscription will
        still proceed but will use the component's default price point.
        Components and their price points may be added by ID or by handle. See
        the example request body labeled "Components By Handle
        (Quantity-Based)"; the format will be the same for other component
        types.
        ## With Coupon(s)
        Pass an array of `coupon_codes`. See the example request body "With
        Coupon".
        ## With Manual Invoice Collection
        The `invoice` collection method works only on legacy Statement
        Architecture.
        On Relationship Invoicing Architecture use the `remittance` collection
        method.
        ## Prepaid Subscription
        A prepaid subscription can be created with the usual subscription
        creation parameters, specifying `prepaid` as the
        `payment_collection_method` and including a nested
        `prepaid_configuration`.
        After a prepaid subscription has been created, additional funds can be
        manually added to the prepayment account through the [Create
        Prepayment
        Endpoint](https://developers.chargify.com/docs/api-docs/7ec482de77ba7-c
        reate-prepayment).
        Prepaid subscriptions do not work on legacy Statement Architecture.
        ## With Metafields
        Metafields can either attach to subscriptions or customers. Metafields
        are popuplated with the supplied metadata to the resource specified.
        If the metafield doesn't exist yet, it will be created on-the-fly.
        ## With Custom Pricing
        Custom pricing is pricing specific to the subscription in question.
        Create a subscription with custom pricing by passing pricing
        information instead of a price point.
        For a custom priced product, pass the custom_price object in place of
        `product_price_point_id`. For a custom priced component, pass the
        `custom_price` object within the component object.
        Custom prices and price points can exist in harmony on a subscription.
        # Passing Payment Information
        ## Subscription with Chargify.js token
        The `chargify_token` can be obtained using
        [Chargify.js](https://developers.chargify.com/docs/developer-docs/ZG9jO
        jE0NjAzNDI0-overview). The token represents payment profile attributes
        that were provided by the customer in their browser and stored at the
        payment gateway.
        The `payment_type` attribute may either be `credit_card` or
        `bank_account`, depending on the type of payment method being added.
        If a bank account is being passed, the payment attributes should be
        changed to `bank_account_attributes`.
        ```json
        {
          "subscription": {
            "product_handle": "pro-plan",
            "customer_attributes": {
              "first_name": "Joe",
              "last_name": "Smith",
              "email": "j.smith@example.com"
            },
            "credit_card_attributes": {
              "chargify_token": "tok_cwhvpfcnbtgkd8nfkzf9dnjn",
              "payment_type": "credit_card"
            }
          }
        }
        ```
        ## Subscription with vault token
        If you already have a customer and card stored in your payment
        gateway, you may create a subscription with a `vault_token`. 
        Providing the last_four, card type and expiration date will allow the
        card to be displayed properly in the Advanced Billing UI.
        ```json
        {
          "subscription": {
            "product_handle": "pro-plan",
            "customer_attributes": {
              "first_name": "Joe",
              "last_name": "Smith",
              "email": "j.smith@example.com"
            },
            "credit_card_attributes": {
              first_name: "Joe,
              last_name: "Smith",
              card_type: "visa",
              expiration_month: "05",
              expiration_year: "2025",
              last_four: "1234",
              vault_token: "12345abc",
              current_vault: "braintree_blue"
          }
        }
        ```
        ## Subscription with ACH as Payment Profile
        ```json
        {
          "subscription": {
            "product_handle": "gold-product",
            "customer_attributes": {
              "first_name": "Joe",
              "last_name": "Blow",
              "email": "joe@example.com",
              "zip": "02120",
              "state": "MA",
              "reference": "XYZ",
              "phone": "(617) 111 - 0000",
              "organization": "Acme",
              "country": "US",
              "city": "Boston",
              "address_2": null,
              "address": "123 Mass Ave."
            },
            "bank_account_attributes": {
              "bank_name": "Best Bank",
              "bank_routing_number": "021000089",
              "bank_account_number": "111111111111",
              "bank_account_type": "checking",
              "bank_account_holder_type": "business",
              "payment_type": "bank_account"
            }
          }
        }
        ```
        ## Subscription with PayPal payment profile
        ### With the nonce from Braintree JS
        ```json
        { "subscription": {
            "product_handle":"test-product-b",
            "customer_attributes": {
              "first_name":"Amelia",
              "last_name":"Johnson",
              "email":"amelia@example.com",
              "organization":"My Awesome Company"
            },
            "payment_profile_attributes":{
              "paypal_email": "amelia@example.com",
              "current_vault": "braintree_blue",
              "payment_method_nonce":"abc123",
              "payment_type":"paypal_account"
            }
          }
        ```
        ### With the Braintree Customer ID as the vault token:
        ```json
        { "subscription": {
            "product_handle":"test-product-b",
            "customer_attributes": {
              "first_name":"Amelia",
              "last_name":"Johnson",
              "email":"amelia@example.com",
              "organization":"My Awesome Company"
            },
            "payment_profile_attributes":{
              "paypal_email": "amelia@example.com",
              "current_vault": "braintree_blue",
              "vault_token":"58271347",
              "payment_type":"paypal_account"
            }
          }
        ```
        ## Subscription using GoCardless Bank Number
        These examples creates a customer, bank account and mandate in
        GoCardless.
        For more information on GoCardless, please view the following two
        resources:
        + [Payment Profiles via API for
        GoCardless](https://developers.chargify.com/docs/api-docs/1f10a4f170405
        -create-payment-profile#gocardless)
        + [Full documentation on
        GoCardless](https://maxio.zendesk.com/hc/en-us/articles/24176159136909-
        GoCardless)
        + [Using Chargify.js with GoCardless - minimal
        example](https://developers.chargify.com/docs/developer-docs/ZG9jOjE0Nj
        AzNDIy-examples#minimal-example-with-direct-debit-gocardless-gateway)
        + [Using Chargify.js with GoCardless - full
        example](https://developers.chargify.com/docs/developer-docs/ZG9jOjE0Nj
        AzNDIy-examples#full-example-with-direct-debit-gocardless-gateway)
        ```json
        {
          "subscription": {
            "product_handle": "gold-product",
            "customer_attributes": {
              "first_name": "Jane",
              "last_name": "Doe",
              "email": "jd@chargify.test"
            },
            "bank_account_attributes": {
              "bank_name": "Royal Bank of France",
              "bank_account_number": "0000000",
              "bank_routing_number": "0003",
              "bank_branch_code": "00006",
              "payment_type": "bank_account",
              "billing_address": "20 Place de la Gare",
              "billing_city": "Colombes",
              "billing_state": "Île-de-France",
              "billing_zip": "92700",
              "billing_country": "FR"
            }
          }
        }
        ```
        ## Subscription using GoCardless IBAN Number
        ```json
        {
          "subscription": {
            "product_handle": "gold-product",
            "customer_attributes": {
              "first_name": "Jane",
              "last_name": "Doe",
              "email": "jd@chargify.test"
            },
            "bank_account_attributes": {
              "bank_name": "French Bank",
              "bank_iban": "FR1420041010050500013M02606",
              "payment_type": "bank_account",
              "billing_address": "20 Place de la Gare",
              "billing_city": "Colombes",
              "billing_state": "Île-de-France",
              "billing_zip": "92700",
              "billing_country": "FR"
            }
          }
        }
        ```
        ## Subscription using Stripe SEPA Direct Debit
        For more information on Stripe Direct Debit, please view the following
        two resources:
        + [Payment Profiles via API for Stripe SEPA Direct
        Debit](https://developers.chargify.com/docs/api-docs/1f10a4f170405-crea
        te-payment-profile#sepa-direct-debit)
        + [Full documentation on Stripe Direct
        Debit](https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Strip
        e-SEPA-and-BECS-Direct-Debit)
        + [Using Chargify.js with Stripe SEPA or BECS Direct Debit - minimal
        example](https://developers.chargify.com/docs/developer-docs/ZG9jOjE0Nj
        AzNDIy-examples#minimal-example-with-sepa-or-becs-direct-debit-stripe-g
        ateway)
        + [Using Chargify.js with Stripe SEPA Direct Debit - full
        example](https://developers.chargify.com/docs/developer-docs/ZG9jOjE0Nj
        AzNDIy-examples#full-example-with-sepa-direct-debit-stripe-gateway)
        ```json
        {
          "subscription": {
            "product_handle": "gold-product",
            "customer_attributes": {
              "first_name": "Jane",
              "last_name": "Doe",
              "email": "jd@chargify.test"
            },
            "bank_account_attributes": {
              "bank_name": "Test Bank",
              "bank_iban": "DE89370400440532013000",
              "payment_type": "bank_account"
            }
          }
        }
        ```
        ## Subscription using Stripe BECS Direct Debit
        For more information on Stripe Direct Debit, please view the following
        two resources:
        + [Payment Profiles via API for Stripe BECS Direct
        Debit]($e/Payment%20Profiles/createPaymentProfile)
        + [Full documentation on Stripe Direct
        Debit](https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Strip
        e-SEPA-and-BECS-Direct-Debit)
        + [Using Chargify.js with Stripe SEPA, BECS or BACS Direct Debit -
        minimal
        example](page:development-tools/chargify-js/examples#minimal-example-wi
        th-sepa-becs-or-bacs-direct-debit-stripe-gateway)
        + [Using Chargify.js with Stripe BECS Direct Debit - full
        example](page:development-tools/chargify-js/examples#full-example-with-
        becs-direct-debit-stripe-gateway)
        ```json
        {
          "subscription": {
            "product_handle": "gold-product",
            "customer_attributes": {
              "first_name": "Jane",
              "last_name": "Doe",
              "email": "jd@chargify.test"
            },
            "bank_account_attributes": {
              "bank_name": "Test Bank",
              "bank_branch_code": "000000",
              "bank_account_number": "000123456",
              "payment_type": "bank_account"
            }
          }
        }
        ```
        ## Subscription using Stripe BACS Direct Debit
        For more information on Stripe Direct Debit, please view the following
        two resources:
        + [Payment Profiles via API for Stripe BACS Direct
        Debit]($e/Payment%20Profiles/createPaymentProfile)
        + [Full documentation on Stripe Direct
        Debit](https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Strip
        e-SEPA-and-BECS-Direct-Debit)
        + [Using Chargify.js with Stripe SEPA, BECS or BACS Direct Debit -
        minimal
        example](page:development-tools/chargify-js/examples#minimal-example-wi
        th-sepa-becs-or-bacs-direct-debit-stripe-gateway)
        + [Using Chargify.js with Stripe BACS Direct Debit - full
        example](page:development-tools/chargify-js/examples#full-example-with-
        bacs-direct-debit-stripe-gateway)
        ```json
        {
          "subscription": {
            "product_handle": "gold-product",
            "customer_attributes": {
              "first_name": "Jane",
              "last_name": "Doe",
              "email": "jd@chargify.test"
            },
            "bank_account_attributes": {
              "bank_name": "Test Bank",
              "bank_branch_code": "108800",
              "bank_account_number": "00012345",
              "payment_type": "bank_account",
              "billing_address": "123 Main St.",
              "billing_city": "London",
              "billing_state": "LND",
              "billing_zip": "W1A 1AA",
              "billing_country": "GB"
            }
          }
        }
        ```
        ## 3D Secure - Stripe
        It may happen that a payment needs 3D Secure Authentication when the
        subscription is created; this is referred to in our help docs as a
        [post-authentication
        flow](https://maxio.zendesk.com/hc/en-us/articles/24176278996493-Testin
        g-Implementing-3D-Secure#psd2-flows-pre-authentication-and-post-authent
        ication). The server returns `422 Unprocessable Entity` in this case
        with the following response:
        ```json
        {
          "errors": [
            "Your card was declined. This transaction requires 3D secure
        authentication."
          ],
          "gateway_payment_id": "pi_1F0aGoJ2UDb3Q4av7zU3sHPh",
          "description": "This card requires 3D secure authentication.
        Redirect the customer to the URL from the action_link attribute to
        authenticate. Attach callback_url param to this URL if you want to be
        notified about the result of 3D Secure authentication. Attach
        redirect_url param to this URL if you want to redirect a customer back
        to your page after 3D Secure authentication. Example:
        https://mysite.chargify.com/3d-secure/pi_1FCm4RKDeye4C0XfbqquXRYm?one_t
        ime_token_id=128&callback_url=https://localhost:4000&redirect_url=https
        ://yourpage.com will do a POST request to https://localhost:4000 after
        payment is authenticated and will redirect a customer to
        https://yourpage.com after 3DS authentication.",
          "action_link":
        "http://acme.chargify.com/3d-secure/pi_1F0aGoJ2UDb3Q4av7zU3sHPh?one_tim
        e_token_id=242"
        }
        ```
        To let the customer go through 3D Secure Authentication, they need to
        be redirected to the URL specified in `action_link`.
        Optionally, you can specify `callback_url` parameter in the
        `action_link` URL if you’d like to be notified about the result of 3D
        Secure Authentication. The `callback_url` will return the following
        information:
        - whether the authentication was successful (`success`)
        - the gateway ID for the payment (`gateway_payment_id`)
        - the subscription ID (`subscription_id`)
        Lastly, you can also specify a `redirect_url` within the `action_link`
        URL if you’d like to redirect a customer back to your site.
        It is not possible to use `action_link` in an iframe inside a custom
        application. You have to redirect the customer directly to the
        `action_link`, then, to be notified about the result, use
        `redirect_url` or `callback_url`.
        The final URL that you send a customer to to complete 3D Secure may
        resemble the following, where the first half is the `action_link` and
        the second half contains a `redirect_url` and `callback_url`:
        `https://mysite.chargify.com/3d-secure/pi_1FCm4RKDeye4C0XfbqquXRYm?one_
        time_token_id=128&callback_url=https://localhost:4000&redirect_url=http
        s://yourpage.com`
        ## 3D Secure - Checkout
        It may happen that a payment needs 3D Secure Authentication when the
        subscription is created; this is referred to in our help docs as a
        [post-authentication
        flow](https://maxio.zendesk.com/hc/en-us/articles/24176278996493-Testin
        g-Implementing-3D-Secure#psd2-flows-pre-authentication-and-post-authent
        ication). The server returns `422 Unprocessable Entity` in this case
        with the following response:
        ```json
        {
          "errors": [
            "Your card was declined. This transaction requires 3D secure
        authentication."
          ],
          "gateway_payment_id": "pay_6gjofv7dlyrkpizlolsuspvtiu",
          "description": "This card requires 3D secure authentication.
        Redirect the customer to the URL from the action_link attribute to
        authenticate. Attach callback_url param to this URL if you want to be
        notified about the result of 3D Secure authentication. Attach
        redirect_url param to this URL if you want to redirect a customer back
        to your page after 3D Secure authentication. Example:
        https://mysite.chargify.com/3d-secure/pay_6gjofv7dlyrkpizlolsuspvtiu?on
        e_time_token_id=123&callback_url=https://localhost:4000&redirect_url=ht
        tps://yourpage.com will do a POST request to https://localhost:4000
        after payment is authenticated and will redirect a customer to
        https://yourpage.com after 3DS authentication.",
          "action_link":
        "http://mysite.chargify.com/3d-secure/pay_6gjofv7dlyrkpizlolsuspvtiu?on
        e_time_token_id=123"
        }
        ```
        To let the customer go through 3D Secure Authentication, they need to
        be redirected to the URL specified in `action_link`.
        Optionally, you can specify `callback_url` parameter in the
        `action_link` URL if you’d like to be notified about the result of 3D
        Secure Authentication. The `callback_url` will return the following
        information:
        - whether the authentication was successful (`success`)
        - the gateway ID for the payment (`gateway_payment_id`)
        - the subscription ID (`subscription_id`)
        Lastly, you can also specify a `redirect_url` parameter within the
        `action_link` URL if you’d like to redirect a customer back to your
        site.
        It is not possible to use `action_link` in an iframe inside a custom
        application. You have to redirect the customer directly to the
        `action_link`, then, to be notified about the result, use
        `redirect_url` or `callback_url`.
        The final URL that you send a customer to complete 3D Secure may
        resemble the following, where the first half is the `action_link` and
        the second half contains a `redirect_url` and `callback_url`:
        `https://mysite.chargify.com/3d-secure/pay_6gjofv7dlyrkpizlolsuspvtiu?o
        ne_time_token_id=123&callback_url=https://localhost:4000&redirect_url=h
        ttps://yourpage.com`
        ### Example Redirect Flow
        You may wish to redirect customers to different pages depending on
        whether their SCA was performed successfully. Here's an example flow
        to use as a reference:
        1. Create a subscription via API; it requires 3DS
        2. You receive a `gateway_payment_id` in the `action_link` along other
        params in the response.
        3. Use this `gateway_payment_id` to, for example, connect with your
        internal resources or generate a session_id
        4. Include 1 of those attributes inside the `callback_url` and
        `redirect_url` to be aware which “session” this applies to
        5. Redirect the customer to the `action_link` with `callback_url` and
        `redirect_url` applied
        6. After the customer finishes 3DS authentication, we let you know the
        result by making a request to applied `callback_url`.
        7. After that, we redirect the customer to the `redirect_url`; at this
        point the result of authentication is known
        8. Optionally, you can use the applied "msg" param in the
        `redirect_url` to determine whether it was successful or not
        ## Subscriptions Import
        Subscriptions can be “imported” via the API to handle the following
        scenarios:
        + You already have existing subscriptions with specific start and
        renewal dates that you would like to import to Advanced Billing
        + You already have credit cards stored in your provider’s vault and
        you would like to create subscriptions using those tokens
        Before importing, you should have already set up your products to
        match your offerings. Then, you can create Subscriptions via the API
        just like you normally would, but using a few special attributes.
        Full documentation on how import Subscriptions using the **import
        tool** in the Advanced Billing UI can be located
        [here](https://maxio.zendesk.com/hc/en-us/articles/24251489107213-Impor
        ts).
        ### Important Notices and Disclaimers regarding Imports
        Before performing a bulk import of subscriptions via the API, we
        suggest reading the [Subscriptions
        Import](https://maxio.zendesk.com/hc/en-us/articles/24251489107213-Impo
        rts) instructions to understand the repurcussions of a large import.
        ### Subscription Input Attributes
        The following _additional_ attributes to the subscription input
        attributes make imports possible: `next_billing_at`,
        `previous_billing_at`, and `import_mrr`.
        ### Current Vault
        If you are using a Legacy gateway such as "eWAY Rapid (Legacy)" or
        "Stripe (Legacy)" then please contact Support for further instructions
        on subscription imports.
        ### Braintree Blue (Braintree v2) Imports
        Braintree Blue is Braintree’s newer (version 2) API. For this gateway,
        please provide the `vault_token` parameter with the value from
        Braintree’s “Customer ID” rather than the “Payment Profile Token”. At
        this time we do not use `current_vault_token` with the Braintree Blue
        gateway, and we only support a single payment profile per Braintree
        Customer.
        When importing PayPal type payment profiles, please set `payment_type`
        to `paypal_account`.
        ### Stripe ACH Imports
        If the bank account has already been verified, currently you will need
        to create the customer, create the payment profile in Advanced Billing
        - setting verified=true, then create a subscription using the
        customer_id and payment_profile_id.
        ### Webhooks During Import
        If no `next_billing_at` is provided, webhooks will be fired as normal.
        If you do set a future `next_billing_at`, only a subset of the
        webhooks are fired when the subscription is created. Keep reading for
        more information as to what webhooks will be fired under which
        scenarios.
        #### Successful creation with Billing Date
        Scenario: If `next_billing_at` provided
        + `signup_success`
        + `billing_date_change`
        #### Successful creation without Billing Date
        Scenario: If no `next_billing_at` provided
        + `signup_success`
        + `payment_success`
        #### Unsuccessful creation
        Scenario: If card can’t be charged, and no `next_billing_at` provided
        + signup_failure
        #### Webhooks fired when next_billing_at is reached:
        + `renewal_success or renewal_failure`
        + `payment_success or payment_failure`
        ### Date and Time Formats
        We will attempt to parse any string you send as the value of
        next_billing_at in to a date or time. For best results, use a known
        format like described in “Date and Time Specification” of RFC 2822 or
        ISO 8601 .
        The following are all equivalent and will work as input to
        `next_billing_at`:
        ```
        Aug 06 2030 11:34:00 -0400
        Aug 06 2030 11:34 -0400
        2030-08-06T11:34:00-04:00
        8/6/2030 11:34:00 EDT
        8/6/2030 8:34:00 PDT
        2030-08-06T15:34:00Z
        ```
        You may also pass just a date, in which case we will assume the time
        to be noon
        ```
        2010-08-06
        ```
        ## Subscription Hierarchies & WhoPays
        When subscription groups were first added to our Relationship
        Invoicing architecture, to group together invoices for related
        subscriptions and allow for complex customer hierarchies and WhoPays
        scenarios, they were designed to consist of a primary and a collection
        of group members. The primary would control many aspects of the group,
        such as when the consolidated invoice is generated. As of today,
        groups still function this way.
        In the future, the concept of a "primary" will be removed in order to
        offer more flexibility into group management and reduce confusion
        concerning what actions must be done on a primary level, rather than a
        member level.
        We have introduced a two scheme system as a bridge between these two
        group organizations. Scheme 1, which is relevant to all subscription
        groups today, marks the group as being "ruled" by a primary.
        When reading a subscription via API, they will return a top-level
        attribute called `group`, which will denote which scheme is being
        used. At this time, the `scheme` attribute will always be 1.
        ### Subscription in a Customer Hierarchy
        For sites making use of the [Relationship
        Billing](https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Adv
        anced-Billing-Invoices-Overview) and [Customer
        Hierarchy](https://maxio.zendesk.com/hc/en-us/articles/24252185211533-C
        ustomer-Hierarchies-WhoPays) features, it is possible to create
        subscriptions within a customer hierarchy.  This can be achieved
        through the API by passing group parameters in the **Create
        Subscription** request.
        + The `group` parameters are optional and consist of the required
        `target` and optional `billing` parameters.
        When the `target` parameter specifies a customer that is already part
        of a hierarchy, the new subscription will become a member of the
        customer hierarchy as well.  If the target customer is not part of a
        hierarchy, a new customer hierarchy will be created and both the
        target customer and the new subscription will become part of the
        hierarchy with the specified target customer set as the responsible
        payer for the hierarchy's subscriptions.
        Rather than specifying a customer, the `target` parameter could
        instead simply have a value of `self` which indicates the subscription
        will be paid for not by some other customer, but by the subscribing
        customer.  This will be true whether the customer is being created
        new, is already part of a hierarchy, or already exists outside a
        hierarchy.  A valid payment method must also be specified in the
        subscription parameters.
        Note that when creating subscriptions in a customer hierarchy, if the
        customer hierarchy does not already have a payment method, passing
        valid credit card attributes in the subscription parameters will also
        result in the payment method being established as the default payment
        method for the customer hierarchy irrespective of the responsible
        payer.
        The optional `billing` parameters specify how some aspects of the
        billing for the new subscription should be handled.  Rather than
        capturing payment immediately, the `accrue` parameter can be included
        so that the new subscription charges accrue until the next assessment
        date.  Regarding the date, the `align_date` parameter can be included
        so that the billing date of the new subscription matches up with the
        default subscription group in the customer hierarchy.  When choosing
        to align the dates, the `prorate` parameter can also be specified so
        that the new subscription charges are prorated based on the billing
        period of the default subscription group in the customer hierarchy
        also.
        ### Subscription in a Subscription Group
        For sites making use of [Relationship
        Billing](https://maxio.zendesk.com/hc/en-us/articles/24252287829645-Adv
        anced-Billing-Invoices-Overview) it may be desireable to create a
        subscription as part of a [subscription
        group](https://maxio.zendesk.com/hc/en-us/articles/24252172565005-Subsc
        ription-Groups-Overview) in order to rely on [invoice
        consolidation](https://maxio.zendesk.com/hc/en-us/articles/242522699093
        89-Invoice-Consolidation). This can be achieved through the API by
        passing group parameters in the Create Subscription request.  The
        `group` parameters are optional and consist of the required `target`
        and optional `billing` parameters.
        The `target` parameters specify an existing subscription with which
        the newly created subscription should be grouped.  If the target
        subscription is already part of a group, the new subscription will
        become a member of the group as well.  If the target subscription is
        not part of a group, a new group will be created and both the target
        and the new subscription will become part of the group with the target
        as the group's primary subscription.
        The optional `billing` parameters specify how some aspects of the
        billing for the new subscription should be handled.  Rather than
        capturing payment immediately, the `accrue` parameter can be included
        so that the new subscription charges accrue until the next assessment
        date.  Regarding the date, the `align_date` parameter can be included
        so that the billing date of the new subscription matches up with the
        target subscription.  When choosing to align the dates, the `prorate`
        parameter can also be specified so that the new subscription charges
        are prorated based on the billing period of the target subscription
        also.
        ## Providing Agreement Acceptance Params
        It is possible to provide a proof of customer's acceptance of terms
        and policies.
        We will be storing this proof in case it might be required (i.e.
        chargeback).
        Currently, we already keep it for subscriptions created via Public
        Signup Pages.
        In order to create a subscription with the proof of agreement
        acceptance, you must provide additional parameters `agreement
        acceptance` with `ip_address` and at least one url to the policy that
        was accepted: `terms_url` or `privacy_policy_url`. Additional urls
        that can be provided: `return_refund_policy_url`,
        `delivery_policy_url` and
        `secure_checkout_policy_url`.
        ```json
          "subscription": {
            "product_handle": "gold-product",
            "customer_attributes": {
              "first_name": "Jane",
              "last_name": "Doe",
              "email": "jd@chargify.test"
            },
            "agreement_acceptance": {
              "ip_address": "1.2.3.4",
              "terms_url": "https://terms.url",
              "privacy_policy_url": "https://privacy_policy.url",
              "return_refund_policy_url": "https://return_refund_policy.url",
              "delivery_policy_url": "https://delivery_policy.url",
              "secure_checkout_policy_url":
        "https://secure_checkout_policy.url"
            }
          }
        }
        ```
        **For Maxio Payments subscriptions, the agreement acceptance params
        are required, with at least terms_url provided.**
        ## Providing ACH Agreement params
        It is also possible to provide a proof that a customer authorized ACH
        agreement terms.
        The proof will be stored and the email will be sent to the customer
        with a copy of the terms (if enabled).
        In order to create a subscription with the proof of authorized ACH
        agreement terms, you must provide the additional parameter
        `ach_agreement` with the following nested parameters:
        `agreement_terms`, `authorizer_first_name`, `authorizer_last_name` and
        `ip_address`.
        Each of them is required.
        ```json
          "subscription": {
            "product_handle": "gold-product",
            "customer_attributes": {
              "first_name": "Jane",
              "last_name": "Doe",
              "email": "jd@chargify.test"
            },
            "bank_account_attributes": {
              "bank_name": "Test Bank",
              "bank_routing_number": "021000089",
              "bank_account_number": "111111111111",
              "bank_account_type": "checking",
              "bank_account_holder_type": "business",
              "payment_type": "bank_account"
            },
            "ach_agreement": {
              "agreement_terms": "ACH agreement terms",
              "authorizer_first_name": "Jane",
              "authorizer_last_name": "Doe",
              "ip_address": "1.2.3.4"
            }
          }
        ```

        Args:
            body (CreateSubscriptionRequest, optional): The request body
                parameter.

        Returns:
            SubscriptionResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions.json')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def list_subscriptions(self,
                           options=dict()):
        """Does a GET request to /subscriptions.json.

        This method will return an array of subscriptions from a Site. Pay
        close attention to query string filters and pagination in order to
        control responses from the server.
        ## Search for a subscription
        Use the query strings below to search for a subscription using the
        criteria available. The return value will be an array.
        ## Self-Service Page token
        Self-Service Page token for the subscriptions is not returned by
        default. If this information is desired, the
        include[]=self_service_page_token parameter must be provided with the
        request.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    page -- int -- Result records are organized in pages. By
                        default, the first page of results is displayed. The
                        page parameter specifies a page number of results to
                        fetch. You can start navigating through the pages to
                        consume the results. You do this by passing in a page
                        parameter. Retrieve the next page by adding ?page=2 to
                        the query string. If there are no results to return,
                        then an empty result set will be returned. Use in
                        query `page=1`.
                    per_page -- int -- This parameter indicates how many
                        records to fetch in each request. Default value is 20.
                        The maximum allowed values is 200; any per_page value
                        over 200 will be changed to 200. Use in query
                        `per_page=200`.
                    state -- SubscriptionStateFilter -- The current state of
                        the subscription
                    product -- int -- The product id of the subscription.
                        (Note that the product handle cannot be used.)
                    product_price_point_id -- int -- The ID of the product
                        price point. If supplied, product is required
                    coupon -- int -- The numeric id of the coupon currently
                        applied to the subscription. (This can be found in the
                        URL when editing a coupon. Note that the coupon code
                        cannot be used.)
                    coupon_code -- str -- The coupon code currently applied to
                        the subscription
                    date_field -- SubscriptionDateField -- The type of filter
                        you'd like to apply to your search.  Allowed Values: ,
                        current_period_ends_at, current_period_starts_at,
                        created_at, activated_at, canceled_at, expires_at,
                        trial_started_at, trial_ended_at, updated_at
                    start_date -- date -- The start date (format YYYY-MM-DD)
                        with which to filter the date_field. Returns
                        subscriptions with a timestamp at or after midnight
                        (12:00:00 AM) in your site’s time zone on the date
                        specified. Use in query `start_date=2022-07-01`.
                    end_date -- date -- The end date (format YYYY-MM-DD) with
                        which to filter the date_field. Returns subscriptions
                        with a timestamp up to and including 11:59:59PM in
                        your site’s time zone on the date specified. Use in
                        query `end_date=2022-08-01`.
                    start_datetime -- datetime -- The start date and time
                        (format YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns subscriptions with a timestamp at
                        or after exact time provided in query. You can specify
                        timezone in query - otherwise your site's time zone
                        will be used. If provided, this parameter will be used
                        instead of start_date. Use in query
                        `start_datetime=2022-07-01 09:00:05`.
                    end_datetime -- datetime -- The end date and time (format
                        YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns subscriptions with a timestamp at
                        or before exact time provided in query. You can
                        specify timezone in query - otherwise your site's time
                        zone will be used. If provided, this parameter will be
                        used instead of end_date. Use in query
                        `end_datetime=2022-08-01 10:00:05`.
                    metadata -- Dict[str, str] -- The value of the metadata
                        field specified in the parameter. Use in query
                        `metadata[my-field]=value&metadata[other-field]=another
                        _value`.
                    direction -- SortingDirection -- Controls the order in
                        which results are returned. Use in query
                        `direction=asc`.
                    sort -- SubscriptionSort -- The attribute by which to sort
                    include -- List[SubscriptionListInclude] -- Allows
                        including additional data in the response. Use in
                        query: `include[]=self_service_page_token`.

        Returns:
            List[SubscriptionResponse]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('state')
                         .value(options.get('state', None)))
            .query_param(Parameter()
                         .key('product')
                         .value(options.get('product', None)))
            .query_param(Parameter()
                         .key('product_price_point_id')
                         .value(options.get('product_price_point_id', None)))
            .query_param(Parameter()
                         .key('coupon')
                         .value(options.get('coupon', None)))
            .query_param(Parameter()
                         .key('coupon_code')
                         .value(options.get('coupon_code', None)))
            .query_param(Parameter()
                         .key('date_field')
                         .value(options.get('date_field', None)))
            .query_param(Parameter()
                         .key('start_date')
                         .value(options.get('start_date', None)))
            .query_param(Parameter()
                         .key('end_date')
                         .value(options.get('end_date', None)))
            .query_param(Parameter()
                         .key('start_datetime')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, options.get('start_datetime', None))))
            .query_param(Parameter()
                         .key('end_datetime')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, options.get('end_datetime', None))))
            .query_param(Parameter()
                         .key('metadata')
                         .value(options.get('metadata', None)))
            .query_param(Parameter()
                         .key('direction')
                         .value(options.get('direction', None)))
            .query_param(Parameter()
                         .key('sort')
                         .value(options.get('sort', None)))
            .query_param(Parameter()
                         .key('include')
                         .value(options.get('include', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.UN_INDEXED)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionResponse.from_dictionary)
        ).execute()

    def update_subscription(self,
                            subscription_id,
                            body=None):
        """Does a PUT request to /subscriptions/{subscription_id}.json.

        The subscription endpoint allows you to instantly update one or many
        attributes about a subscription in a single call.
        ## Update Subscription Payment Method
        Change the card that your Subscriber uses for their subscription. You
        can also use this method to simply change the expiration date of the
        card **if your gateway allows**.
        Note that partial card updates for **Authorize.Net** are not allowed
        via this endpoint. The existing Payment Profile must be directly
        updated instead.
        You also use this method to change the subscription to a different
        product by setting a new value for product_handle. A product change
        can be done in two different ways, **product change** or **delayed
        product change**.
        ## Product Change
        This endpoint may be used to change a subscription's product. The new
        payment amount is calculated and charged at the normal start of the
        next period. If you desire complex product changes or prorated
        upgrades and downgrades instead, please see the documentation on
        Migrating Subscription Products.
        To perform a product change, simply set either the `product_handle` or
        `product_id` attribute to that of a different product from the same
        site as the subscription. You can also change the price point by
        passing in either `product_price_point_id` or
        `product_price_point_handle` - otherwise the new product's default
        price point will be used.
        ### Delayed Product Change
        This method also changes the product and/or price point, and the new
        payment amount is calculated and charged at the normal start of the
        next period.
        This method schedules the product change to happen automatically at
        the subscription’s next renewal date. To perform a Delayed Product
        Change, set the `product_handle` attribute as you would in a regular
        product change, but also set the `product_change_delayed` attribute to
        `true`. No proration applies in this case.
        You can also perform a delayed change to the price point by passing in
        either `product_price_point_id` or `product_price_point_handle`
        **Note: To cancel a delayed product change, set `next_product_id` to
        an empty string.**
        ## Billing Date Changes
        ### Regular Billing Date Changes
        Send the `next_billing_at` to set the next billing date for the
        subscription. After that date passes and the subscription is
        processed, the following billing date will be set according to the
        subscription's product period.
        Note that if you pass an invalid date, we will automatically interpret
        and set the correct date. For example, when February 30 is entered,
        the next billing will be set to March 2nd in a non-leap year.
        The server response will not return data under the key/value pair of
        `next_billing`. Please view the key/value pair of
        `current_period_ends_at` to verify that the `next_billing` date has
        been changed successfully.
        ### Snap Day Changes
        For a subscription using Calendar Billing, setting the next billing
        date is a bit different. Send the `snap_day` attribute to change the
        calendar billing date for **a subscription using a product eligible
        for calendar billing**.
        Note: If you change the product associated with a subscription that
        contains a `snap_date` and immediately `READ/GET` the subscription
        data, it will still contain evidence of the existing `snap_date`. This
        is due to the fact that a product change is instantanous and only
        affects the product associated with a subscription. After the
        `next_billing` date arrives, the `snap_day` associated with the
        subscription will return to `null.` Another way of looking at this is
        that you willl have to wait for the next billing cycle to arrive
        before the `snap_date` will reset to `null`.

        Args:
            subscription_id (int): The Chargify id of the subscription
            body (UpdateSubscriptionRequest, optional): The request body
                parameter.

        Returns:
            SubscriptionResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/{subscription_id}.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorListResponseException)
        ).execute()

    def read_subscription(self,
                          subscription_id,
                          include=None):
        """Does a GET request to /subscriptions/{subscription_id}.json.

        Use this endpoint to find subscription details.
        ## Self-Service Page token
        Self-Service Page token for the subscription is not returned by
        default. If this information is desired, the
        include[]=self_service_page_token parameter must be provided with the
        request.

        Args:
            subscription_id (int): The Chargify id of the subscription
            include (List[SubscriptionInclude], optional): Allows including
                additional data in the response. Use in query:
                `include[]=coupons&include[]=self_service_page_token`.

        Returns:
            SubscriptionResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/{subscription_id}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('include')
                         .value(include))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.UN_INDEXED)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionResponse.from_dictionary)
        ).execute()

    def override_subscription(self,
                              subscription_id,
                              body=None):
        """Does a PUT request to /subscriptions/{subscription_id}/override.json.

        This API endpoint allows you to set certain subscription fields that
        are usually managed for you automatically. Some of the fields can be
        set via the normal Subscriptions Update API, but others can only be
        set using this endpoint.
        This endpoint is provided for cases where you need to “align” Advanced
        Billing data with data that happened in your system, perhaps before
        you started using Advanced Billing. For example, you may choose to
        import your historical subscription data, and would like the
        activation and cancellation dates in Advanced Billing to match your
        existing historical dates. Advanced Billing does not backfill
        historical events (i.e. from the Events API), but some static data can
        be changed via this API.
        Why are some fields only settable from this endpoint, and not the
        normal subscription create and update endpoints? Because we want users
        of this endpoint to be aware that these fields are usually managed by
        Advanced Billing, and using this API means **you are stepping out on
        your own.**
        Changing these fields will not affect any other attributes. For
        example, adding an expiration date will not affect the next assessment
        date on the subscription.
        If you regularly need to override the current_period_starts_at for new
        subscriptions, this can also be accomplished by setting both
        `previous_billing_at` and `next_billing_at` at subscription creation.
        See the documentation on [Importing
        Subscriptions](./b3A6MTQxMDgzODg-create-subscription#subscriptions-impo
        rt) for more information.
        ## Limitations
        When passing `current_period_starts_at` some validations are made:
        1. The subscription needs to be unbilled (no statements or invoices).
        2. The value passed must be a valid date/time. We recommend using the
        iso 8601 format.
        3. The value passed must be before the current date/time.
        If unpermitted parameters are sent, a 400 HTTP response is sent along
        with a string giving the reason for the problem.

        Args:
            subscription_id (int): The Chargify id of the subscription
            body (OverrideSubscriptionRequest, optional): Only these fields
                are available to be set.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/{subscription_id}/override.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).execute()

    def find_subscription(self,
                          reference=None):
        """Does a GET request to /subscriptions/lookup.json.

        Use this endpoint to find a subscription by its reference.

        Args:
            reference (str, optional): Subscription reference

        Returns:
            SubscriptionResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/lookup.json')
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                         .key('reference')
                         .value(reference))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
        ).execute()

    def purge_subscription(self,
                           subscription_id,
                           ack,
                           cascade=None):
        """Does a POST request to /subscriptions/{subscription_id}/purge.json.

        For sites in test mode, you may purge individual subscriptions.
        Provide the subscription ID in the url.  To confirm, supply the
        customer ID in the query string `ack` parameter. You may also delete
        the customer record and/or payment profiles by passing `cascade`
        parameters. For example, to delete just the customer record, the query
        params would be: `?ack={customer_id}&cascade[]=customer`
        If you need to remove subscriptions from a live site, please contact
        support to discuss your use case.
        ### Delete customer and payment profile
        The query params will be:
        `?ack={customer_id}&cascade[]=customer&cascade[]=payment_profile`

        Args:
            subscription_id (int): The Chargify id of the subscription
            ack (int): id of the customer.
            cascade (List[SubscriptionPurgeType], optional): Options are
                "customer" or "payment_profile". Use in query:
                `cascade[]=customer&cascade[]=payment_profile`.

        Returns:
            SubscriptionResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/{subscription_id}/purge.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('ack')
                         .value(ack)
                         .is_required(True))
            .query_param(Parameter()
                         .key('cascade')
                         .value(cascade))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.UN_INDEXED)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionResponse.from_dictionary)
            .local_error_template('400', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', SubscriptionResponseErrorException)
        ).execute()

    def update_prepaid_subscription_configuration(self,
                                                  subscription_id,
                                                  body=None):
        """Does a POST request to /subscriptions/{subscription_id}/prepaid_configurations.json.

        Use this endpoint to update a subscription's prepaid configuration.

        Args:
            subscription_id (int): The Chargify id of the subscription
            body (UpsertPrepaidConfigurationRequest, optional): The request
                body parameter.

        Returns:
            PrepaidConfigurationResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/{subscription_id}/prepaid_configurations.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PrepaidConfigurationResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', APIException)
        ).execute()

    def preview_subscription(self,
                             body=None):
        """Does a POST request to /subscriptions/preview.json.

        The Chargify API allows you to preview a subscription by POSTing the
        same JSON or XML as for a subscription creation.
        The "Next Billing" amount and "Next Billing" date are represented in
        each Subscriber's Summary.
        A subscription will not be created by utilizing this endpoint; it is
        meant to serve as a prediction.
        For more information, please see our documentation
        [here](https://maxio.zendesk.com/hc/en-us/articles/24252493695757-Subsc
        riber-Interface-Overview).
        ## Taxable Subscriptions
        This endpoint will preview taxes applicable to a purchase. In order
        for taxes to be previewed, the following conditions must be met:
        + Taxes must be configured on the subscription
        + The preview must be for the purchase of a taxable product or
        component, or combination of the two.
        + The subscription payload must contain a full billing or shipping
        address in order to calculate tax
        For more information about creating taxable previews, please see our
        documentation guide on how to create [taxable
        subscriptions.](https://maxio.zendesk.com/hc/en-us/sections/24287012349
        325-Taxes)
        You do **not** need to include a card number to generate tax
        information when you are previewing a subscription. However, please
        note that when you actually want to create the subscription, you must
        include the credit card information if you want the billing address to
        be stored in Advanced Billing. The billing address and the credit card
        information are stored together within the payment profile object.
        Also, you may not send a billing address to Advanced Billing without
        payment profile information, as the address is stored on the card.
        You can pass shipping and billing addresses and still decide not to
        calculate taxes. To do that, pass `skip_billing_manifest_taxes: true`
        attribute.
        ## Non-taxable Subscriptions
        If you'd like to calculate subscriptions that do not include tax,
        please feel free to leave off the billing information.

        Args:
            body (CreateSubscriptionRequest, optional): The request body
                parameter.

        Returns:
            SubscriptionPreviewResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/preview.json')
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionPreviewResponse.from_dictionary)
        ).execute()

    def apply_coupons_to_subscription(self,
                                      subscription_id,
                                      code=None,
                                      body=None):
        """Does a POST request to /subscriptions/{subscription_id}/add_coupon.json.

        An existing subscription can accommodate multiple discounts/coupon
        codes. This is only applicable if each coupon is stackable. For more
        information on stackable coupons, we recommend reviewing our [coupon
        documentation.](https://maxio.zendesk.com/hc/en-us/articles/24261259337
        101-Coupons-and-Subscriptions#stackability-rules)
        ## Query Parameters vs Request Body Parameters
        Passing in a coupon code as a query parameter will add the code to the
        subscription, completely replacing all existing coupon codes on the
        subscription.
        For this reason, using this query parameter on this endpoint has been
        deprecated in favor of using the request body parameters as described
        below. When passing in request body parameters, the list of coupon
        codes will simply be added to any existing list of codes on the
        subscription.

        Args:
            subscription_id (int): The Chargify id of the subscription
            code (str, optional): A code for the coupon that would be applied
                to a subscription
            body (AddCouponsRequest, optional): The request body parameter.

        Returns:
            SubscriptionResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/{subscription_id}/add_coupon.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .query_param(Parameter()
                         .key('code')
                         .value(code))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionResponse.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', SubscriptionAddCouponErrorException)
        ).execute()

    def remove_coupon_from_subscription(self,
                                        subscription_id,
                                        coupon_code=None):
        """Does a DELETE request to /subscriptions/{subscription_id}/remove_coupon.json.

        Use this endpoint to remove a coupon from an existing subscription.
        For more information on the expected behaviour of removing a coupon
        from a subscription, please see our documentation
        [here.](https://maxio.zendesk.com/hc/en-us/articles/24261259337101-Coup
        ons-and-Subscriptions#removing-a-coupon)

        Args:
            subscription_id (int): The Chargify id of the subscription
            coupon_code (str, optional): The coupon code

        Returns:
            str: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/{subscription_id}/remove_coupon.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('coupon_code')
                         .value(coupon_code))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', SubscriptionRemoveCouponErrorsException)
        ).execute()

    def activate_subscription(self,
                              subscription_id,
                              body=None):
        """Does a PUT request to /subscriptions/{subscription_id}/activate.json.

        Advanced Billing offers the ability to activate awaiting signup and
        trialing subscriptions. This feature is only available on the
        Relationship Invoicing architecture. Subscriptions in a group may not
        be activated immediately.
        For details on how the activation works, and how to activate
        subscriptions through the application, see [activation](#).
        The `revert_on_failure` parameter controls the behavior upon
        activation failure.
        - If set to `true` and something goes wrong i.e. payment fails, then
        Advanced Billing will not change the subscription's state. The
        subscription’s billing period will also remain the same.
        - If set to `false` and something goes wrong i.e. payment fails, then
        Advanced Billing will continue through with the activation and enter
        an end of life state. For trialing subscriptions, that will either be
        trial ended (if the trial is no obligation), past due (if the trial
        has an obligation), or canceled (if the site has no dunning strategy,
        or has a strategy that says to cancel immediately). For awaiting
        signup subscriptions, that will always be canceled.
        The default activation failure behavior can be configured per
        activation attempt, or you may set a default value under Config >
        Settings > Subscription Activation Settings.
        ## Activation Scenarios
        ### Activate Awaiting Signup subscription
        - Given you have a product without trial
        - Given you have a site without dunning strategy
        ```mermaid
          flowchart LR
            AS[Awaiting Signup] --> A{Activate}
            A -->|Success| Active
            A -->|Failure| ROF{revert_on_failure}
            ROF -->|true| AS
            ROF -->|false| Canceled
        ```
        - Given you have a product with trial
        - Given you have a site with dunning strategy
        ```mermaid
          flowchart LR
            AS[Awaiting Signup] --> A{Activate}
            A -->|Success| Trialing
            A -->|Failure| ROF{revert_on_failure}
            ROF -->|true| AS
            ROF -->|false| PD[Past Due]
        ```
        ### Activate Trialing subscription
        You can read more about the behavior of trialing subscriptions
        [here](https://maxio.zendesk.com/hc/en-us/articles/24252155721869-Trial
        ing-Subscriptions).
        When the `revert_on_failure` parameter is set to `true`, the
        subscription's state will remain as Trialing, we will void the invoice
        from activation and return any prepayments and credits applied to the
        invoice back to the subscription.

        Args:
            subscription_id (int): The Chargify id of the subscription
            body (ActivateSubscriptionRequest, optional): The request body
                parameter.

        Returns:
            SubscriptionResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/subscriptions/{subscription_id}/activate.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionResponse.from_dictionary)
            .local_error_template('400', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', ErrorArrayMapResponseException)
        ).execute()
