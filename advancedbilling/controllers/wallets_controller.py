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
from advancedbilling.models.wallet_response import (
    WalletResponse,
)
from advancedbilling.models.wallets_list_response import (
    WalletsListResponse,
)


class WalletsController(BaseController):
    """A Controller to access Endpoints in the advancedbilling API."""

    def __init__(self, config):
        """Initialize WalletsController object."""
        super(WalletsController, self).__init__(config)

    def list_wallets(self,
                     page=1,
                     per_page=20,
                     subscription_id=None,
                     status=None):
        """Perform a GET request to /wallets.json.

        Lists the wallets on your site, in creation order, paginated. Without
        `subscription_id`, returns every wallet on the site. The API key is the
        tenancy boundary; `subscription_id` only narrows the result set further.
        Archived wallets are included unless you filter them out with `status=active`.

        Args:
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
            subscription_id (int, optional): Restricts the result to wallets owned by
                this subscription.
            status (Status2, optional): Restricts the result by wallet status. An
                unrecognized value returns `422` rather than being silently ignored.

        Returns:
            WalletsListResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/wallets.json")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("page")
                .value(page))
            .query_param(Parameter()
                .key("per_page")
                .value(per_page))
            .query_param(Parameter()
                .key("subscription_id")
                .value(subscription_id))
            .query_param(Parameter()
                .key("status")
                .value(status))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(WalletsListResponse.from_dictionary)
            .local_error("403",
                "Forbidden. The response body is plain text (`403 Forbidden`), not JS"
                "ON. Returned when the Wallets feature isn't enabled for the site.",
                APIException)
            .local_error("422",
                "Unprocessable Entity (WebDAV)",
                WalletErrorResponseException),
        ).execute()

    def create_wallet(self,
                      idempotency_key=None,
                      body=None):
        """Perform a POST request to /wallets.json.

        Creates a wallet owned by a subscription and denominated by a [Wallet
        Product]($e/Wallet%20Products/createWalletProduct): only a Wallet Product can
        denominate a wallet, not an ordinary component. The Wallet Product must be
        active; it never belongs to a product family, so there's no family check
        against the subscription. It's **immutable for the life of the wallet**;
        there's no way to repoint an existing wallet at a different one.
        This endpoint always creates a `manual` wallet. To provision a wallet
        automatically from a usage-limit entitlement instead, configure
        `wallet_behavior` on the Feature behind that entitlement (see [the Wallets
        concept
        guide](page:introduction/basic-concepts/wallets#provisioning-a-wallet-from-a-f
        eature)) rather than sending `entitlement_id` here.

        Args:
            idempotency_key (str, optional): A key you generate, such as a UUID, that
                makes retrying this request safe. 1 to 255 printable ASCII
                characters; surrounding double quotes are ignored. Keys are scoped to
                your site and kept for at least 24 hours.  The first request with a
                key runs normally. A retry with the same key, method, path and query
                string, and a byte-identical body returns the stored status and body
                of that first request without running it again. The same key with a
                different request returns `422` (`idempotency_key_mismatch`). A retry
                that arrives while the first request is still running waits for it to
                finish, and returns `409` (`idempotency_request_in_progress`) only if
                that wait times out; on Create Wallet Purchase the `409` is
                immediate. Only successful responses are stored, so a failed request
                can be retried with the same key. When this header is sent,
                `uniqueness_token` is not checked.  See [Idempotent
                retries](page:introduction/basic-concepts/wallets#idempotent-retries)
                for the details, including how wallet purchases differ.
            body (CreateWalletRequest, optional): The request body parameter.

        Returns:
            WalletResponse: Response from the API. Wallet created. The balance is
                `"0.0"` with no grants, unless a non-zero `initial_balance` was
                given. In that case, the balance and its seeded grant are already
                reflected.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/wallets.json")
            .http_method(HttpMethodEnum.POST)
            .header_param(Parameter()
                .key("Content-Type")
                .value("application/json"))
            .header_param(Parameter()
                .key("Idempotency-Key")
                .value(idempotency_key))
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
            .deserialize_into(WalletResponse.from_dictionary)
            .local_error("400",
                "The `Idempotency-Key` header is empty, longer than 255 characters, o"
                "r contains characters other than printable ASCII. Nothing is written"
                ".",
                WalletErrorResponseException)
            .local_error("403",
                "Forbidden. The response body is plain text (`403 Forbidden`), not JS"
                "ON. Returned when the Wallets feature isn't enabled for the site.",
                APIException)
            .local_error("404",
                "Unknown or cross-site subscription or meter, or a `wallet_product_id"
                "` that doesn't resolve to a Wallet Product on this site.",
                WalletErrorResponseException)
            .local_error("409",
                "A request with the same `Idempotency-Key` was still being processed "
                "when this retry's wait for it timed out (`idempotency_request_in_pro"
                "gress`). Nothing is written; retry with the same key once it finishe"
                "s.",
                WalletErrorResponseException)
            .local_error("422",
                "Validation failure, or an `Idempotency-Key` reused with a different "
                "request (`idempotency_key_mismatch`). Validation failures include a "
                "missing or archived `wallet_product_id`; a `price_point_id` that's m"
                "issing, archived, a subscription-specific custom price point, or doe"
                "sn't belong to the Wallet Product; an invalid `depletion_policy` or "
                "`hard_stop_overflow` value; a meter that isn't a `sum` or `count` me"
                "ter; an invalid `conversion_rate`; a subscription with no reference,"
                " when pairing a meter whose stream bills by subscription reference; "
                "and the `initial_balance` / `initial_balance_expires_at` error cases"
                " described on those fields. Also returned for `entitlement_id`: this"
                " endpoint never accepts it, and rejects it with the message shown be"
                "low rather than silently ignoring it. Also returned when `subscripti"
                "on_id` names a prepaid subscription: a wallet would double-meter a b"
                "alance the subscription already tracks on its own, so the two are mu"
                "tually exclusive.",
                WalletErrorResponseException),
        ).execute()

    def read_wallet(self,
                    id):
        """Perform a GET request to /wallets/{id}.json.

        Returns the wallet's balance and grant breakdown. For an active, metered
        wallet on a site with metered consumption enabled, this is the only operation
        that computes a live balance from meter usage; see the wallet resource's
        `metered_*` fields. It is also the only operation where `balance` can differ
        from `posted_balance`, and a grant's `remaining` from its `posted_remaining`:
        the pending usage is drawn from the grants in drain order, so the grants'
        `remaining` add up to `balance`. Readable regardless of status. Archiving a
        wallet doesn't affect reads.

        Args:
            id (int): The Advanced Billing id of the wallet.

        Returns:
            WalletResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/wallets/{id}.json")
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
            .deserialize_into(WalletResponse.from_dictionary)
            .local_error("403",
                "Forbidden. The response body is plain text (`403 Forbidden`), not JS"
                "ON. Returned when the Wallets feature isn't enabled for the site.",
                APIException)
            .local_error("404", "Not Found", WalletErrorResponseException),
        ).execute()

    def archive_wallet(self,
                       id):
        """Perform a DELETE request to /wallets/{id}.json.

        Archives the wallet: blocks further grants, debits, adjustments, and
        purchases (each returns `422`), stops any metered drawdown, and stops
        recurring funding (its schedule is deactivated with reason `wallet_archived`,
        not removed), while reads and the ledger stay available. Nothing already on
        the wallet is destroyed or clawed back, but nothing on it can be spent
        either, by any path, once archived. Idempotent: archiving an already-archived
        wallet returns the same `200`. There is no restore endpoint.

        Args:
            id (int): The Advanced Billing id of the wallet.

        Returns:
            WalletResponse: Response from the API. The wallet, with `"status":
                "archived"`.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/wallets/{id}.json")
            .http_method(HttpMethodEnum.DELETE)
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
            .deserialize_into(WalletResponse.from_dictionary)
            .local_error("403",
                "Forbidden. The response body is plain text (`403 Forbidden`), not JS"
                "ON. Returned when the Wallets feature isn't enabled for the site.",
                APIException)
            .local_error("404", "Not Found", WalletErrorResponseException),
        ).execute()

    def update_wallet(self,
                      id,
                      body=None):
        """Perform a PATCH request to /wallets/{id}.json.

        Updates the wallet's editable attributes. Only `name` is editable; any other
        attribute in the body is ignored. Send only the attributes to change.

        Args:
            id (int): The Advanced Billing id of the wallet.
            body (UpdateWalletRequest, optional): The request body parameter.

        Returns:
            WalletResponse: Response from the API. The updated wallet. Reports the
                stored balance, equal to `posted_balance`, with the `metered_*`
                fields `null`, as on list, create, and archive.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/wallets/{id}.json")
            .http_method(HttpMethodEnum.PATCH)
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
            .deserialize_into(WalletResponse.from_dictionary)
            .local_error("403",
                "Forbidden. The response body is plain text (`403 Forbidden`), not JS"
                "ON. Returned when the Wallets feature isn't enabled for the site.",
                APIException)
            .local_error("404", "Not Found", WalletErrorResponseException)
            .local_error("422",
                "Validation failure. Includes a body with no editable attribute (`par"
                "ameter_missing`), a `name` over 255 characters (`validation_failed`)"
                ", and an archived wallet (`wallet_archived`).",
                WalletErrorResponseException),
        ).execute()
