"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: D410, E501, E101, D206
from apimatic_core.authentication.multiple.single_auth import (
    Single,
)
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter

from advancedbilling.api_helper import APIHelper
from advancedbilling.configuration import Server
from advancedbilling.controllers.base_controller import (
    BaseController,
)
from advancedbilling.exceptions.api_exception import (
    APIException,
)
from advancedbilling.exceptions.error_list_response_exception import (
    ErrorListResponseException,
)
from advancedbilling.exceptions.error_string_map_response_exception import (
    ErrorStringMapResponseException,
)
from advancedbilling.http.http_method_enum import (
    HttpMethodEnum,
)
from advancedbilling.models.bank_account_response import (
    BankAccountResponse,
)
from advancedbilling.models.get_one_time_token_request import (
    GetOneTimeTokenRequest,
)
from advancedbilling.models.payment_profile_response import (
    PaymentProfileResponse,
)


class PaymentProfilesController(BaseController):
    """A Controller to access Endpoints in the advancedbilling API."""

    def __init__(self, config):
        """Initialize PaymentProfilesController object."""
        super(PaymentProfilesController, self).__init__(config)

    def create_payment_profile(self,
                               body=None):
        """Perform a POST request to /payment_profiles.json.

        Creates a payment profile for a customer.
        When you create a new payment profile for a customer via the API, it does not
        automatically make the profile current for any of the customer’s
        subscriptions. To use the payment profile as the default, you must set it
        explicitly for the subscription or subscription group.
        Select an option from the **Request Examples** drop-down on the right side of
        the portal to see examples of common scenarios for creating payment profiles.
        Do not use real card information for testing. See the Sites articles that
        cover [testing your site
        setup](https://docs.maxio.com/hc/en-us/articles/24250712113165-Testing-Overvie
        w#testing-overview-0-0) for more details on testing in your sandbox.
        Note that collecting and sending raw card details in production requires [PCI
        compliance](https://docs.maxio.com/hc/en-us/articles/24183956938381-PCI-Compli
        ance#pci-compliance-0-0) on your end. If your business is not PCI compliant,
        use [Maxio.js (formerly
        Chargify.js)](https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify
        -js-Overview#chargify-js-overview-0-0) to collect credit card or bank account
        information.
        See the following articles to learn more about subscriptions and payments:
        + [Subscriber Payment
        Details](https://maxio.zendesk.com/hc/en-us/articles/24251599929613-Subscripti
        on-Summary-Payment-Details-Tab)
        + [Self Service
        Pages](https://maxio.zendesk.com/hc/en-us/articles/24261425318541-Self-Service
        -Pages) (Allows credit card updates by Subscriber)
        + [Public Signup Pages payment
        settings](https://maxio.zendesk.com/hc/en-us/articles/24261368332557-Individua
        l-Page-Settings)
        +
        [Taxes](https://developers.chargify.com/docs/developer-docs/d2e9e34db740e-sign
        ups#taxes)
        + [Maxio.js (formerly
        Chargify.js)](https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify
        -js-Overview)
            + [Maxio.js with GoCardless - minimal
        example](https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01
        K0PJ15QQZKCER8CFK40MR6XJ)
            + [Maxio.js with GoCardless - full
        example](https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01
        K0PJ15QR09JVHWW0MCA7HVJV)
            + [Maxio.js with Stripe Direct Debit - minimal
        example](https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01
        K0PJ15QQFKKN8Z7B7DZ9AJS5)
            + [Maxio.js with Stripe Direct Debit - full
        example](https://docs.maxio.com/hc/en-us/articles/38206331271693-Examples#h_01
        K0PJ15QRECQQ4ECS3ZA55GY7)
            + [Maxio.js with Stripe BECS Direct Debit - minimal
        example](https://developers.chargify.com/docs/developer-docs/ZG9jOjE0NjAzNDIy-
        examples#minimal-example-with-sepa-or-becs-direct-debit-stripe-gateway)
            + [Maxio.js with Stripe BECS Direct Debit - full
        example](https://developers.chargify.com/docs/developer-docs/ZG9jOjE0NjAzNDIy-
        examples#full-example-with-sepa-direct-debit-stripe-gateway)
        + [Full documentation on
        GoCardless](https://maxio.zendesk.com/hc/en-us/articles/24176159136909-GoCardl
        ess)
        + [Full documentation on Stripe SEPA Direct
        Debit](https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-
        and-BECS-Direct-Debit)
        + [Full documentation on Stripe BECS Direct
        Debit](https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-
        and-BECS-Direct-Debit)
        + [Full documentation on Stripe BACS Direct
        Debit](https://maxio.zendesk.com/hc/en-us/articles/24176170430093-Stripe-SEPA-
        and-BECS-Direct-Debit)
        ## 3D Secure (3DS) Authentication post-authentication flow
        When a payment requires 3DS Authentication to adhere to Strong Customer
        Authentication (SCA), the request enters a post-authentication flow where a
        422 Unprocessable Entity status is returned with an action_link that will
        direct the customer through 3DS Authentication.
        See the [3D Secure Post-Authentication
        Flow](https://docs.maxio.com/hc/en-us/articles/44277749524365-3D-Secure-Post-A
        uthentication-Flow) article in the product documentation to learn how to
        manage the redirect flow.

        Args:
            body (CreatePaymentProfileRequest, optional): When following the IBAN or
                the Local Bank details examples, a customer, bank account and mandate
                will be created in your current vault. If the customer, bank account,
                and mandate already exist in your vault, follow the Import example to
                link the payment profile into Advanced Billing.

        Returns:
            PaymentProfileResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/payment_profiles.json")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PaymentProfileResponse.from_dictionary)
            .local_error_template("404", "Not Found:'{$response.body}'", APIException)
            .local_error_template("422",
                "HTTP Response Not OK. Status code: {$statusCode}. Response: '{$respo"
                "nse.body}'.",
                ErrorListResponseException),
        ).execute()

    def list_payment_profiles(self,
                              options=dict()):
        """Perform a GET request to /payment_profiles.json.

        Lists all active payment profiles for a site, or for one customer within a
        site. If no payment profiles are found, this endpoint returns an empty array.

        Args:
            options (dict, optional): Key-value pairs for any of the parameters to
                this API Endpoint. All parameters to the endpoint are supplied
                through the dictionary with their names being the key and their
                desired values being the value. A list of parameters that can be used
                are::
                    page -- int -- Result records are organized in pages. By default,
                        the first page of results is displayed. The page parameter
                        specifies a page number of results to fetch. You can start
                        navigating through the pages to consume the results. You do
                        this by passing in a page parameter. Retrieve the next page
                        by adding ?page=2 to the query string. If there are no
                        results to return, then an empty result set will be returned.
                        Use in query `page=1`.
                    per_page -- int -- This parameter indicates how many records to
                        fetch in each request. Default value is 20. The maximum
                        allowed values is 200; any per_page value over 200 will be
                        changed to 200. Use in query `per_page=200`.
                    customer_id -- int -- The ID of the customer for which you wish
                        to list payment profiles

        Returns:
            List[PaymentProfileResponse]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/payment_profiles.json")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("page")
                .value(options.get("page", None)))
            .query_param(Parameter()
                .key("per_page")
                .value(options.get("per_page", None)))
            .query_param(Parameter()
                .key("customer_id")
                .value(options.get("customer_id", None)))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PaymentProfileResponse.from_dictionary),
        ).execute()

    def read_payment_profile(self,
                             payment_profile_id):
        """Perform a GET request to
        /payment_profiles/{payment_profile_id}.json.

        Returns a payment profile identified by its unique ID.
        Note that a different JSON object will be returned if the card method on file
        is a bank account.
        ### Response for Bank Account
        Example response for Bank Account:
        ```
        {
          "payment_profile": {
            "id": 10089892,
            "first_name": "Chester",
            "last_name": "Tester",
            "created_at": "2025-01-01T00:00:00-05:00",
            "updated_at": "2025-01-01T00:00:00-05:00",
            "customer_id": 14543792,
            "current_vault": "bogus",
            "vault_token": "0011223344",
            "billing_address": "456 Juniper Court",
            "billing_city": "Boulder",
            "billing_state": "CO",
            "billing_zip": "80302",
            "billing_country": "US",
            "customer_vault_token": null,
            "billing_address_2": "",
            "bank_name": "Bank of Kansas City",
            "masked_bank_routing_number": "XXXX6789",
            "masked_bank_account_number": "XXXX3344",
            "bank_account_type": "checking",
            "bank_account_holder_type": "personal",
            "payment_type": "bank_account",
            "site_gateway_setting_id": 1,
            "gateway_handle": null
          }
        }
        ```

        Args:
            payment_profile_id (int): The Chargify id of the payment profile

        Returns:
            PaymentProfileResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/payment_profiles/{payment_profile_id}.json")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("payment_profile_id")
                .value(payment_profile_id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PaymentProfileResponse.from_dictionary)
            .local_error("404", "Not Found", APIException),
        ).execute()

    def update_payment_profile(self,
                               payment_profile_id,
                               body=None):
        """Perform a PUT request to
        /payment_profiles/{payment_profile_id}.json.

        Updates a payment profile.
        ## Partial Card Updates
        In the event that you are using the Authorize.net, Stripe, Cybersource, Forte
        or Braintree Blue payment gateways, you can update just the billing and
        contact information for a payment method. Note the lack of credit-card
        related data contained in the JSON payload.
        In this case, the following JSON is acceptable:
        ```
        {
          "payment_profile": {
            "first_name": "Kelly",
            "last_name": "Test",
            "billing_address": "789 Juniper Court",
            "billing_city": "Boulder",
            "billing_state": "CO",
            "billing_zip": "80302",
            "billing_country": "US",
            "billing_address_2": null
          }
        }
        ```
        The result will be that you have updated the billing information for the
        card, yet retained the original card number data.
        ## Specific notes on updating payment profiles
        - Merchants with **Authorize.net**, **Cybersource**, **Forte**, **Braintree
        Blue** or **Stripe** as their payment gateway can update their Customer’s
        credit cards without passing in the full credit card number and CVV.
        - If you are using **Authorize.net**, **Cybersource**, **Forte**, **Braintree
        Blue** or **Stripe**, Advanced Billing will ignore the credit card number and
        CVV when processing an update via the API, and attempt a partial update
        instead. If you wish to change the card number on a payment profile, you will
        need to create a new payment profile for the given customer.
        - A Payment Profile cannot be updated with the attributes of another type of
        Payment Profile. For example, if the payment profile you are attempting to
        update is a credit card, you cannot pass in bank account attributes (like
        `bank_account_number`), and vice versa.
        - Updating a payment profile directly will not trigger an attempt to capture
        a past-due balance. If this is the intent, update the card details via the
        Subscription instead.
        - If you are using Authorize.net or Stripe, you may elect to manually trigger
        a retry for a past due subscription after a partial update.

        Args:
            payment_profile_id (int): The Chargify id of the payment profile
            body (UpdatePaymentProfileRequest, optional): The request body parameter.

        Returns:
            PaymentProfileResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/payment_profiles/{payment_profile_id}.json")
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                .key("payment_profile_id")
                .value(payment_profile_id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PaymentProfileResponse.from_dictionary)
            .local_error("404", "Not Found", APIException)
            .local_error_template("422",
                "HTTP Response Not OK. Status code: {$statusCode}. Response: '{$respo"
                "nse.body}'.",
                ErrorStringMapResponseException),
        ).execute()

    def delete_unused_payment_profile(self,
                                      payment_profile_id):
        """Perform a DELETE request to
        /payment_profiles/{payment_profile_id}.json.

        Deletes an unused payment profile.
        If the payment profile is in use by one or more subscriptions or groups, an
        error message is returned.

        Args:
            payment_profile_id (int): The Chargify id of the payment profile

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/payment_profiles/{payment_profile_id}.json")
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                .key("payment_profile_id")
                .value(payment_profile_id)
                .is_required(True)
                .should_encode(True))
            .auth(Single("BasicAuth")),
        ).execute()

    def delete_subscriptions_payment_profile(self,
                                             subscription_id,
                                             payment_profile_id):
        """Perform a DELETE request to
        /subscriptions/{subscription_id}/payment_profiles/{payment_profile_id}.json.

        Deletes a payment profile belonging to the customer on the subscription.
        If the customer has multiple subscriptions, the payment profile is removed
        from all of them.
        If you delete the default payment profile for a subscription, you need to
        specify another payment profile to be the default through the API, or either
        prompt the user to enter a card in the billing portal or on the self-service
        page, or visit the Payment Details tab on the subscription in the Admin UI
        and use the “Add New Credit Card” or “Make Active Payment Method” link,
        (depending on whether there are other cards present).

        Args:
            subscription_id (int): The Chargify id of the subscription.
            payment_profile_id (int): The Chargify id of the payment profile

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscriptions/{subscription_id}/payment_profiles/{payment_profile_id}.json")
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                .key("subscription_id")
                .value(subscription_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("payment_profile_id")
                .value(payment_profile_id)
                .is_required(True)
                .should_encode(True))
            .auth(Single("BasicAuth")),
        ).execute()

    def verify_bank_account(self,
                            bank_account_id,
                            body=None):
        """Perform a PUT request to
        /bank_accounts/{bank_account_id}/verification.json.

        Verifies a bank account. Submit the two small deposit amounts the customer
        received in their bank account to verify the bank account. (Stripe only)

        Args:
            bank_account_id (int): Identifier of the bank account in the system.
            body (BankAccountVerificationRequest, optional): The request body
                parameter.

        Returns:
            BankAccountResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/bank_accounts/{bank_account_id}/verification.json")
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                .key("bank_account_id")
                .value(bank_account_id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .body_param(Parameter()
                .value(body))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(BankAccountResponse.from_dictionary)
            .local_error_template("404", "Not Found:'{$response.body}'", APIException)
            .local_error_template("422",
                "HTTP Response Not OK. Status code: {$statusCode}. Response: '{$respo"
                "nse.body}'.",
                ErrorListResponseException),
        ).execute()

    def delete_subscription_group_payment_profile(self,
                                                  uid,
                                                  payment_profile_id):
        """Perform a DELETE request to
        /subscription_groups/{uid}/payment_profiles/{payment_profile_id}.json.

        Deletes a Payment Profile belonging to a Subscription Group.
        **Note**: If the Payment Profile belongs to multiple Subscription Groups
        and/or Subscriptions, it will be removed from all of them.

        Args:
            uid (str): The uid of the subscription group
            payment_profile_id (int): The Chargify id of the payment profile

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscription_groups/{uid}/payment_profiles/{payment_profile_id}.json")
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                .key("uid")
                .value(uid)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("payment_profile_id")
                .value(payment_profile_id)
                .is_required(True)
                .should_encode(True))
            .auth(Single("BasicAuth")),
        ).execute()

    def change_subscription_default_payment_profile(self,
                                                    subscription_id,
                                                    payment_profile_id):
        """Perform a POST request to
        /subscriptions/{subscription_id}/payment_profiles/{payment_profile_id}/change_p
        ayment_profile.json.

        Changes the default payment profile on the subscription to the existing
        payment profile with the specified ID.
        You must elect to change the existing payment profile to a new payment
        profile ID in order to receive a satisfactory response from this endpoint.

        Args:
            subscription_id (int): The Chargify id of the subscription.
            payment_profile_id (int): The Chargify id of the payment profile

        Returns:
            PaymentProfileResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscriptions/{subscription_id}/payment_profiles/{payment_profile_id}/change_payment_profile.json")
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                .key("subscription_id")
                .value(subscription_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("payment_profile_id")
                .value(payment_profile_id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PaymentProfileResponse.from_dictionary)
            .local_error("404", "Not Found", APIException)
            .local_error_template("422",
                "HTTP Response Not OK. Status code: {$statusCode}. Response: '{$respo"
                "nse.body}'.",
                ErrorListResponseException),
        ).execute()

    def change_subscription_group_default_payment_profile(self,
                                                          uid,
                                                          payment_profile_id):
        """Perform a POST request to
        /subscription_groups/{uid}/payment_profiles/{payment_profile_id}/change_payment
        _profile.json.

        Changes the default payment profile on the subscription group to the existing
        payment profile with the specified ID.
        You must elect to change the existing payment profile to a new payment
        profile ID in order to receive a satisfactory response from this endpoint.
        The new payment profile must belong to the subscription group's customer,
        otherwise you will receive an error.

        Args:
            uid (str): The uid of the subscription group
            payment_profile_id (int): The Chargify id of the payment profile

        Returns:
            PaymentProfileResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscription_groups/{uid}/payment_profiles/{payment_profile_id}/change_payment_profile.json")
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                .key("uid")
                .value(uid)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("payment_profile_id")
                .value(payment_profile_id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PaymentProfileResponse.from_dictionary)
            .local_error_template("422",
                "HTTP Response Not OK. Status code: {$statusCode}. Response: '{$respo"
                "nse.body}'.",
                ErrorListResponseException),
        ).execute()

    def read_one_time_token(self,
                            chargify_token):
        """Perform a GET request to /one_time_tokens/{chargify_token}.json.

        Returns the one-time token data, including credit card or ACH details,
        associated with the provided token ID. One Time Tokens aka Advanced Billing
        Tokens house the credit card or ACH (Authorize.Net or Stripe only) data for a
        customer.
        You can use One Time Tokens while creating a subscription or payment profile
        instead of passing all bank account or credit card data directly to a given
        API endpoint.
        To obtain a One Time Token you have to use
        [Chargify.js](https://docs.maxio.com/hc/en-us/articles/38163190843789-Chargify
        -js-Overview#chargify-js-overview-0-0).

        Args:
            chargify_token (str): Advanced Billing Token

        Returns:
            GetOneTimeTokenRequest: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/one_time_tokens/{chargify_token}.json")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("chargify_token")
                .value(chargify_token)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(GetOneTimeTokenRequest.from_dictionary)
            .local_error_template("404",
                "Not Found:'{$response.body}'",
                ErrorListResponseException),
        ).execute()

    def send_request_update_payment_email(self,
                                          subscription_id):
        """Perform a POST request to
        /subscriptions/{subscription_id}/request_payment_profiles_update.json.

        Sends a "request payment update" email to the customer associated with the
        subscription.
        If you attempt to send a "request payment update" email more than five times
        within a 30-minute period, you will receive a `422` response with an error
        message in the body. This error message will indicate that the request has
        been rejected due to excessive attempts, and will provide instructions on how
        to resubmit the request.
        Additionally, if you attempt to send a "request payment update" email for a
        subscription that does not exist, you will receive a `404` error response.
        This error message will indicate that the subscription could not be found,
        and will provide instructions on how to correct the error and resubmit the
        request.
        These error responses are designed to prevent excessive or invalid requests,
        and to provide clear and helpful information to users who encounter errors
        during the request process.

        Args:
            subscription_id (int): The Chargify id of the subscription.

        Returns:
            void: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscriptions/{subscription_id}/request_payment_profiles_update.json")
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                .key("subscription_id")
                .value(subscription_id)
                .is_required(True)
                .should_encode(True))
            .auth(Single("BasicAuth")),
        ).execute()
