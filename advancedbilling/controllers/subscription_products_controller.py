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
from advancedbilling.exceptions.error_list_response_exception import (
    ErrorListResponseException,
)
from advancedbilling.http.http_method_enum import (
    HttpMethodEnum,
)
from advancedbilling.models.subscription_migration_preview_response import (
    SubscriptionMigrationPreviewResponse,
)
from advancedbilling.models.subscription_response import (
    SubscriptionResponse,
)


class SubscriptionProductsController(BaseController):
    """A Controller to access Endpoints in the advancedbilling API."""

    def __init__(self, config):
        """Initialize SubscriptionProductsController object."""
        super(SubscriptionProductsController, self).__init__(config)

    def migrate_subscription_product(self,
                                     subscription_id,
                                     body=None):
        """Perform a POST request to
        /subscriptions/{subscription_id}/migrations.json.

        Migrates a subscription to a different product.
        In order to create a migration, you must pass the `product_id` or
        `product_handle` in the object when you send a POST request. You may also
        pass either a `product_price_point_id` or `product_price_point_handle` to
        choose which price point the subscription is moved to. If no price point
        identifier is passed the subscription will be moved to the products default
        price point. The response will be the updated subscription.
        ## Valid Subscriptions
        Subscriptions should be in the `active` or `trialing` state in order to be
        migrated.
        (For backwards compatibility reasons, it is possible to migrate a
        subscription that is in the `trial_ended` state via the API, however this is
        not recommended.  Since `trial_ended` is an end-of-life state, the
        subscription should be canceled, the product changed, and then the
        subscription can be reactivated.)
        ## Migrations Documentation
        Full documentation on how to record Migrations in the Advanced Billing UI can
        be located
        [here](https://maxio.zendesk.com/hc/en-us/articles/24181589372429-Data-Migrati
        on-to-Advanced-Billing).
        ## Failed Migrations
        Important note: One of the most common ways that a migration can fail is when
        the attempt is made to migrate a subscription to its current product.
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
            subscription_id (int): The Chargify id of the subscription.
            body (SubscriptionProductMigrationRequest, optional): The request body
                parameter.

        Returns:
            SubscriptionResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscriptions/{subscription_id}/migrations.json")
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                .key("subscription_id")
                .value(subscription_id)
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
            .deserialize_into(SubscriptionResponse.from_dictionary)
            .local_error_template("422",
                "HTTP Response Not OK. Status code: {$statusCode}. Response: '{$respo"
                "nse.body}'.",
                ErrorListResponseException),
        ).execute()

    def preview_subscription_product_migration(self,
                                               subscription_id,
                                               body=None):
        """Perform a POST request to
        /subscriptions/{subscription_id}/migrations/preview.json.

        Previews the charges resulting from migrating a subscription to a different
        product.
        ## Previewing a future date
        It is also possible to preview the migration for a date in the future, as
        long as it's still within the subscription's current billing period, by
        passing a `proration_date` along with the request (e.g., `"proration_date":
        "2020-12-18T18:25:43.511Z"`).
        This will calculate the prorated adjustment, charge, payment and credit
        applied values assuming the migration is done at that date in the future as
        opposed to right now.

        Args:
            subscription_id (int): The Chargify id of the subscription.
            body (SubscriptionMigrationPreviewRequest, optional): The request body
                parameter.

        Returns:
            SubscriptionMigrationPreviewResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscriptions/{subscription_id}/migrations/preview.json")
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                .key("subscription_id")
                .value(subscription_id)
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
            .deserialize_into(SubscriptionMigrationPreviewResponse.from_dictionary)
            .local_error_template("422",
                "HTTP Response Not OK. Status code: {$statusCode}. Response: '{$respo"
                "nse.body}'.",
                ErrorListResponseException),
        ).execute()
