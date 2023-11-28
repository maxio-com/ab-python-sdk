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
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from advancedbilling.models.subscription_response import SubscriptionResponse
from advancedbilling.models.subscription_migration_preview_response import SubscriptionMigrationPreviewResponse
from advancedbilling.exceptions.error_list_response_exception import ErrorListResponseException


class SubscriptionProductsController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(SubscriptionProductsController, self).__init__(config)

    def migrate_subscription_product(self,
                                     subscription_id,
                                     body=None):
        """Does a POST request to /subscriptions/{subscription_id}/migrations.json.

        In order to create a migration, you must pass the `product_id` or
        `product_handle` in the object when you send a POST request. You may
        also pass either a `product_price_point_id` or
        `product_price_point_handle` to choose which price point the
        subscription is moved to. If no price point identifier is passed the
        subscription will be moved to the products default price point. The
        response will be the updated subscription.
        ## Valid Subscriptions
        Subscriptions should be in the `active` or `trialing` state in order
        to be migrated.
        (For backwards compatibility reasons, it is possible to migrate a
        subscription that is in the `trial_ended` state via the API, however
        this is not recommended.  Since `trial_ended` is an end-of-life state,
        the subscription should be canceled, the product changed, and then the
        subscription can be reactivated.)
        ## Migrations Documentation
        Full documentation on how to record Migrations in the Chargify UI can
        be located
        [here](https://chargify.zendesk.com/hc/en-us/articles/4407898373531).
        ## Failed Migrations
        One of the most common ways that a migration can fail is when the
        attempt is made to migrate a subscription to it's current product.
        Please be aware of this issue!
        ## Migration 3D Secure - Stripe
        It may happen that a payment needs 3D Secure Authentication when the
        subscription is migrated to a new product; this is referred to in our
        help docs as a [post-authentication
        flow](https://maxio-chargify.zendesk.com/hc/en-us/articles/540517743207
        7#psd2-flows-pre-authentication-and-post-authentication). The server
        returns `422 Unprocessable Entity` in this case with the following
        response:
        ```json
        {
          "errors": [
            "Your card was declined. This transaction requires 3D secure
            authentication."
          ],
          "gateway_payment_id": "pi_1F0aGoJ2UDb3Q4av7zU3sHPh",
          "description": "This card requires 3D secure authentication.
          Redirect the customer to the URL from the action_link attribute to
          authenticate. Attach callback_url param to this URL if you want to
          be notified about the result of 3D Secure authentication. Attach
          redirect_url param to this URL if you want to redirect a customer
          back to your page after 3D Secure authentication. Example:
          https://mysite.chargify.com/3d-secure/pi_1FCm4RKDeye4C0XfbqquXRYm?one
          _time_token_id=128&callback_url=https://localhost:4000&redirect_url=h
          ttps://yourpage.com will do a POST request to https://localhost:4000
          after payment is authenticated and will redirect a customer to
          https://yourpage.com after 3DS authentication.",
          "action_link":
          "http://acme.chargify.com/3d-secure/pi_1F0aGoJ2UDb3Q4av7zU3sHPh?one_t
          ime_token_id=242"
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
        ### Example Redirect Flow
        You may wish to redirect customers to different pages depending on
        whether their SCA was performed successfully. Here's an example flow
        to use as a reference:
        1. Create a migration via API; it requires 3DS
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
        `redirect_url` to determine whether it was successful or not.

        Args:
            subscription_id (str): The Chargify id of the subscription
            body (SubscriptionProductMigrationRequest, optional): TODO: type
                description here.

        Returns:
            SubscriptionResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/migrations.json')
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
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionResponse.from_dictionary)
            .local_error('422', 'Unprocessable Entity (WebDAV)', ErrorListResponseException)
        ).execute()

    def preview_subscription_product_migration(self,
                                               subscription_id,
                                               body=None):
        """Does a POST request to /subscriptions/{subscription_id}/migrations/preview.json.

        ## Previewing a future date
        It is also possible to preview the migration for a date in the future,
        as long as it's still within the subscription's current billing
        period, by passing a `proration_date` along with the request (eg:
        `"proration_date": "2020-12-18T18:25:43.511Z"`).
        This will calculate the prorated adjustment, charge, payment and
        credit applied values assuming the migration is done at that date in
        the future as opposed to right now.

        Args:
            subscription_id (str): The Chargify id of the subscription
            body (SubscriptionMigrationPreviewRequest, optional): TODO: type
                description here.

        Returns:
            SubscriptionMigrationPreviewResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/migrations/preview.json')
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
            .auth(Single('global'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionMigrationPreviewResponse.from_dictionary)
            .local_error('422', 'Unprocessable Entity (WebDAV)', ErrorListResponseException)
        ).execute()
