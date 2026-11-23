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
from advancedbilling.models.wallet_transaction_result_response import (
    WalletTransactionResultResponse,
)
from advancedbilling.models.wallet_transactions_list_response import (
    WalletTransactionsListResponse,
)


class WalletTransactionsController(BaseController):
    """A Controller to access Endpoints in the advancedbilling API."""

    def __init__(self, config):
        """Initialize WalletTransactionsController object."""
        super(WalletTransactionsController, self).__init__(config)

    def list_wallet_transactions(self,
                                 wallet_id,
                                 page=1,
                                 per_page=20):
        """Perform a GET request to /wallets/{wallet_id}/transactions.json.

        Lists the wallet's append-only ledger, newest first, paginated.

        Args:
            wallet_id (int): The Advanced Billing id of the wallet.
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
            WalletTransactionsListResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/wallets/{wallet_id}/transactions.json")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("wallet_id")
                .value(wallet_id)
                .is_required(True)
                .should_encode(True))
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
            .deserialize_into(WalletTransactionsListResponse.from_dictionary)
            .local_error("403",
                "Forbidden. The response body is plain text (`403 Forbidden`), not JS"
                "ON. Returned when the Wallets feature isn't enabled for the site.",
                APIException)
            .local_error("404", "Not Found", WalletErrorResponseException),
        ).execute()

    def create_wallet_transaction(self,
                                  wallet_id,
                                  idempotency_key=None,
                                  body=None):
        """Perform a POST request to /wallets/{wallet_id}/transactions.json.

        Grants units to the wallet, or debits units from it, depending on `kind`.
        `amount` is always sent positive, and `kind` determines the direction written
        to the ledger.
        **`kind: grant`**: a one-time manual top-up. On a non-negative balance, this
        creates a grant and writes one ledger row. On a negative balance, it repays
        the overdraft first (a `kind: grant` row with `grant_id: null`, for the
        repaid amount), then creates the grant: its `original` is always the full
        `amount` sent, and its `remaining` is what's left after the overdraft was
        repaid, which is `0` if the overdraft absorbed the whole top-up. The grant
        row is still written, and its `amount` is that `remaining`, not `original`,
        so the ledger rows sum to the balance change. A grant may carry `expires_at`;
        a debit may not.
        **`kind: debit`**: direct consumption. Drains grants
        earliest-expiration-first, one `kind: debit` row per grant touched, plus any
        overdue expiration rows this same call triggers first (see below):
        - Under the wallet's default `hard_stop_overflow: discard`, the drain is
        capped at the available balance. For a metered wallet, that cap is the live
        metered balance, not the stored one, so a debit can drain less than its
        stored balance would suggest, or even drain nothing at all (`201` with
        `drained_amount: "0.0"`) if live usage has already consumed what the ledger
        hadn't caught up to yet. A debit against a wallet whose *stored* balance is
        already zero or negative (`discard` only ever reaches zero) returns `422
        "Wallet is depleted"`. Before that failure is returned, this call still
        expires any grants that were already overdue, so a `422` response can still
        leave new `kind: expiration` rows written.
        - Under `hard_stop_overflow: allow_negative`, the full amount is deducted.
        The excess past the wallet's grants is booked as one overdraft row with
        `grant_id: null`, `rejected_amount` is always `"0.0"`, and the balance goes
        negative.

        Args:
            wallet_id (int): The Advanced Billing id of the wallet.
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
            body (CreateWalletTransactionRequest, optional): The request body
                parameter.

        Returns:
            WalletTransactionResultResponse: Response from the API. Transaction
                applied. For `kind: grant`, the ledger row(s) written plus the new
                balance. For `kind: debit`, one row per grant touched plus the
                requested/drained/rejected accounting and the new balance.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/wallets/{wallet_id}/transactions.json")
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                .key("wallet_id")
                .value(wallet_id)
                .is_required(True)
                .should_encode(True))
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
            .deserialize_into(WalletTransactionResultResponse.from_dictionary)
            .local_error("400",
                "The `Idempotency-Key` header is empty, longer than 255 characters, o"
                "r contains characters other than printable ASCII. Nothing is written"
                ".",
                WalletErrorResponseException)
            .local_error("403",
                "Forbidden. The response body is plain text (`403 Forbidden`), not JS"
                "ON. Returned when the Wallets feature isn't enabled for the site.",
                APIException)
            .local_error("404", "Not Found", WalletErrorResponseException)
            .local_error("409",
                "A request with the same `Idempotency-Key` was still being processed "
                "when this retry's wait for it timed out (`idempotency_request_in_pro"
                "gress`). Nothing is written; retry with the same key once it finishe"
                "s.",
                WalletErrorResponseException)
            .local_error("422",
                "Validation failure, or an `Idempotency-Key` reused with a different "
                "request (`idempotency_key_mismatch`). Validation failures include an"
                " unrecognized `kind`, a missing `wallet_transaction` root, a malform"
                "ed, non-positive, or out-of-range `amount`, a memo over 255 characte"
                "rs, `expires_at` sent with `kind: debit`, a malformed or past-dated "
                "`expires_at`, an archived wallet, and, for `kind: debit` only, a dep"
                "leted wallet.",
                WalletErrorResponseException)
            .local_error("500",
                "For a metered wallet, usage could be read but settling it against th"
                "e ledger failed.",
                WalletErrorResponseException)
            .local_error("503",
                "For a metered wallet, live usage could not be read in time to comput"
                "e the debit. Not returned for `kind: grant`.",
                WalletErrorResponseException),
        ).execute()
