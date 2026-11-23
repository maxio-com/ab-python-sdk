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
from advancedbilling.exceptions.wallet_error_response_exception import (
    WalletErrorResponseException,
)
from advancedbilling.http.http_method_enum import (
    HttpMethodEnum,
)
from advancedbilling.models.wallet_product_response import (
    WalletProductResponse,
)
from advancedbilling.models.wallet_product_usage_response import (
    WalletProductUsageResponse,
)
from advancedbilling.models.wallet_products_list_response import (
    WalletProductsListResponse,
)


class WalletProductsController(BaseController):
    """A Controller to access Endpoints in the advancedbilling API."""

    def __init__(self, config):
        """Initialize WalletProductsController object."""
        super(WalletProductsController, self).__init__(config)

    def list_wallet_products(self,
                             include_archived=None,
                             status=None,
                             q=None,
                             sort_by="name",
                             sort_direction="asc",
                             page=1,
                             per_page=20):
        """Perform a GET request to /wallet_products.json.

        Lists the Wallet Products on your site.

        Args:
            include_archived (bool, optional): Includes archived Wallet Products in
                the result. Defaults to `false`. Ignored when `status` is also sent.
            status (Status1, optional): Restricts the result by status, and overrides
                `include_archived` when sent. An unrecognized value falls back to
                `active` rather than returning `422`.
            q (str, optional): Restricts the result to Wallet Products whose name,
                handle, or unit name contains this substring (case-insensitive).
            sort_by (SortBy1, optional): The field to sort results by. An
                unrecognized value falls back to `name`.
            sort_direction (SortDirection, optional): The sort direction. Anything
                other than `desc` is treated as `asc`.
            page (int, optional): Result records are organized in pages. By default,
                the first page of results is displayed. The page parameter specifies
                a page number of results to fetch. You can start navigating through
                the pages to consume the results. You do this by passing in a page
                parameter. Retrieve the next page by adding ?page=2 to the query
                string. If there are no results to return, then an empty result set
                will be returned. Use in query `page=1`.
            per_page (int, optional): This parameter indicates how many records to
                fetch in each request. Default value is 20. The maximum allowed
                values is 200; any per_page value over 200 will be changed to 200.
                Use in query `per_page=200`.

        Returns:
            WalletProductsListResponse: Response from the API. OK. Unlike most list
                endpoints, this one is unpaginated (returns the full matching set in
                one response) unless `page` or `per_page` is sent; sending either
                turns on pagination, defaulting to 20 per page with a maximum of 200.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/wallet_products.json")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("include_archived")
                .value(include_archived))
            .query_param(Parameter()
                .key("status")
                .value(status))
            .query_param(Parameter()
                .key("q")
                .value(q))
            .query_param(Parameter()
                .key("sort_by")
                .value(sort_by))
            .query_param(Parameter()
                .key("sort_direction")
                .value(sort_direction))
            .query_param(Parameter()
                .key("page")
                .value(page))
            .query_param(Parameter()
                .key("per_page")
                .value(per_page))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(WalletProductsListResponse.from_dictionary)
            .local_error("403",
                "Forbidden. The response body is plain text (`403 Forbidden`), not JS"
                "ON. Returned when the Wallets feature isn't enabled for the site.",
                APIException),
        ).execute()

    def create_wallet_product(self,
                              body=None):
        """Perform a POST request to /wallet_products.json.

        Creates a Wallet Product: a billing product with no product family, meant to
        denominate wallets and to be purchased through [Create Wallet
        Purchase]($e/Wallet%20Purchases/createWalletPurchase). It's a Component under
        the hood, so it returns the full Component field set, and can optionally be
        priced with one or more price points in the same call.

        Args:
            body (CreateWalletProductRequest, optional): The request body parameter.

        Returns:
            WalletProductResponse: Response from the API. Wallet Product created.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/wallet_products.json")
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
            .deserialize_into(WalletProductResponse.from_dictionary)
            .local_error("403",
                "Forbidden. The response body is plain text (`403 Forbidden`), not JS"
                "ON. Returned when the Wallets feature isn't enabled for the site.",
                APIException)
            .local_error("422",
                "Validation failure. Includes a `product_family_id` (rejected rather "
                "than ignored), and any failure validating a price point in `price_po"
                "int`/`price_points`, which rolls back the whole call, including the "
                "Wallet Product itself.",
                WalletErrorResponseException),
        ).execute()

    def read_wallet_product(self,
                            id):
        """Perform a GET request to /wallet_products/{id}.json.

        Returns the Wallet Product.

        Args:
            id (str): The Advanced Billing id of the Wallet Product, or its handle
                prefixed with `handle:` (for example `handle:token-pack`). A bare
                handle returns `404`.

        Returns:
            WalletProductResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/wallet_products/{id}.json")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("id")
                .value(id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(WalletProductResponse.from_dictionary)
            .local_error("403",
                "Forbidden. The response body is plain text (`403 Forbidden`), not JS"
                "ON. Returned when the Wallets feature isn't enabled for the site.",
                APIException)
            .local_error("404", "Not Found", WalletErrorResponseException),
        ).execute()

    def update_wallet_product(self,
                              id,
                              body=None):
        """Perform a PUT request to /wallet_products/{id}.json.

        Updates the Wallet Product's catalog-facing fields. Omitted fields are left
        unchanged. Unlike [Create Wallet
        Product]($e/Wallet%20Products/createWalletProduct), this does not accept
        `unit_name`, `handle`, `price_point`, or `price_points`; see the request
        schema for which fields are actually mutable.

        Args:
            id (str): The Advanced Billing id of the Wallet Product, or its handle
                prefixed with `handle:` (for example `handle:token-pack`). A bare
                handle returns `404`.
            body (UpdateWalletProductRequest, optional): The request body parameter.

        Returns:
            WalletProductResponse: Response from the API. Wallet Product updated.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/wallet_products/{id}.json")
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                .key("id")
                .value(id)
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
            .deserialize_into(WalletProductResponse.from_dictionary)
            .local_error("403",
                "Forbidden. The response body is plain text (`403 Forbidden`), not JS"
                "ON. Returned when the Wallets feature isn't enabled for the site.",
                APIException)
            .local_error("404", "Not Found", WalletErrorResponseException)
            .local_error("422", "Validation failure.", WalletErrorResponseException),
        ).execute()

    def read_wallet_product_usage(self,
                                  id):
        """Perform a GET request to /wallet_products/{id}/usage.json.

        Returns everything drawing on this Wallet Product: the wallet templates
        billing through it, split into ones using its default price point and ones
        overriding it, plus a sample of up to 50 of the active wallets actually
        created from them. A wallet template can appear more than once in
        `wallet_templates`/`price_point_overrides`, once per Feature and owning
        plan/component sharing it, so these arrays aren't one row per template.

        Args:
            id (str): The Advanced Billing id of the Wallet Product, or its handle
                prefixed with `handle:` (for example `handle:token-pack`). A bare
                handle returns `404`.

        Returns:
            WalletProductUsageResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/wallet_products/{id}/usage.json")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("id")
                .value(id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(WalletProductUsageResponse.from_dictionary)
            .local_error("403",
                "Forbidden. The response body is plain text (`403 Forbidden`), not JS"
                "ON. Returned when the Wallets feature isn't enabled for the site.",
                APIException)
            .local_error("404", "Not Found", WalletErrorResponseException),
        ).execute()

    def archive_wallet_product(self,
                               id):
        """Perform a POST request to /wallet_products/{id}/archive.json.

        Archives the Wallet Product. Refuses when an active Feature's
        `wallet_behavior` still points at it, or when it's used in a scheduled
        renewal. This protects Feature-provisioned wallets, but not a wallet created
        manually against this product: a manual wallet can be left denominated by an
        archived Wallet Product, and [Create Wallet
        Purchase]($e/Wallet%20Purchases/createWalletPurchase) doesn't check whether
        the billing product is archived before pricing and charging a purchase
        against it.

        Args:
            id (str): The Advanced Billing id of the Wallet Product, or its handle
                prefixed with `handle:` (for example `handle:token-pack`). A bare
                handle returns `404`.

        Returns:
            WalletProductResponse: Response from the API. Wallet Product archived.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/wallet_products/{id}/archive.json")
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                .key("id")
                .value(id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(WalletProductResponse.from_dictionary)
            .local_error("403",
                "Forbidden. The response body is plain text (`403 Forbidden`), not JS"
                "ON. Returned when the Wallets feature isn't enabled for the site.",
                APIException)
            .local_error("404", "Not Found", WalletErrorResponseException)
            .local_error("422",
                "The Wallet Product is already archived, is in use by one or more Fea"
                "tures, or is in use by a scheduled renewal.",
                WalletErrorResponseException),
        ).execute()

    def unarchive_wallet_product(self,
                                 id):
        """Perform a POST request to /wallet_products/{id}/unarchive.json.

        Restores an archived Wallet Product.

        Args:
            id (str): The Advanced Billing id of the Wallet Product, or its handle
                prefixed with `handle:` (for example `handle:token-pack`). A bare
                handle returns `404`.

        Returns:
            WalletProductResponse: Response from the API. Wallet Product unarchived.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/wallet_products/{id}/unarchive.json")
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                .key("id")
                .value(id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(WalletProductResponse.from_dictionary)
            .local_error("403",
                "Forbidden. The response body is plain text (`403 Forbidden`), not JS"
                "ON. Returned when the Wallets feature isn't enabled for the site.",
                APIException)
            .local_error("404", "Not Found", WalletErrorResponseException)
            .local_error("422",
                "The Wallet Product is not archived.",
                WalletErrorResponseException),
        ).execute()
