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
from advancedbilling.models.wallet_grant_result_response import (
    WalletGrantResultResponse,
)


class WalletAdjustmentsController(BaseController):
    """A Controller to access Endpoints in the advancedbilling API."""

    def __init__(self, config):
        """Initialize WalletAdjustmentsController object."""
        super(WalletAdjustmentsController, self).__init__(config)

    def create_wallet_adjustment(self,
                                 wallet_id,
                                 idempotency_key=None,
                                 body=None):
        """Perform a POST request to /wallets/{wallet_id}/adjustments.json.

        Posts a signed correction against a specific grant (or, for an overdraft
        entry, against the overdraft): positive adds units to the grant, negative
        removes them. `reason` is required and is written to the ledger row's `memo`.
        Writes exactly one ledger row, of kind `adjustment`.
        Use `source_transaction_id` to name a specific `debit` row when you're
        correcting one recorded consumption rather than the grant's balance as a
        whole. When it names a grant-attributed debit, it's recorded for audit only:
        naming it doesn't change how `amount` is applied, and more than one
        adjustment may name the same row. When it names an overdraft entry, it
        switches the correction to the overdraft path described below.
        An overdraft entry (a `debit` row with no `grant_id`, written when an
        `allow_negative` wallet consumes past its grants) can be corrected without a
        `grant_id`. That correction is credit-only, credits no grant, and is bounded
        by the usage the entry still records and by the overdraft the wallet still
        owes. Once a later grant has repaid the overdraft, correct that grant's
        balance instead.
        An adjustment corrects the ledger, so it works on the grant's recorded
        remainder, `posted_remaining`, not on `remaining`, which on a metered wallet
        read through [Read Wallet]($e/Wallets/readWallet) also subtracts usage not
        yet posted. Send `posted_remaining` back as `expected_remaining`; sending
        `remaining` on a metered wallet with pending usage returns `409`.
        `expected_remaining` and `expected_source_corrections` are optional
        optimistic-concurrency checks; see their field descriptions. Use them when
        the correction's `amount` was derived from a value read earlier that might
        have moved since.

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
            body (CreateWalletAdjustmentRequest, optional): The request body
                parameter.

        Returns:
            WalletGrantResultResponse: Response from the API. The ledger row written,
                plus the wallet's new balance.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/wallets/{wallet_id}/adjustments.json")
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
            .deserialize_into(WalletGrantResultResponse.from_dictionary)
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
                "Returned in two cases. A request with the same `Idempotency-Key` was"
                " still being processed when this retry's wait for it timed out (`ide"
                "mpotency_request_in_progress`); retry with the same key once it fini"
                "shes. Or the state the `amount` was derived from has moved: either t"
                "he grant's `posted_remaining` no longer matches `expected_remaining`"
                ", or the corrections already posted against `source_transaction_id` "
                "no longer sum to `expected_source_corrections`. Nothing is written. "
                "Reload and re-derive the amount.",
                WalletErrorResponseException)
            .local_error("422",
                "Validation failure, or an `Idempotency-Key` reused with a different "
                "request (`idempotency_key_mismatch`). Validation failures include a "
                "missing `reason`, a `reason` over 255 characters, a missing or not-f"
                "ound `grant_id`, a zero, malformed, or out-of-range `amount`, a nega"
                "tive adjustment exceeding the grant's `posted_remaining`, a positive"
                " adjustment exceeding the grant's `original`, a malformed `expected_"
                "remaining` or `expected_source_corrections` (including an empty stri"
                "ng, which is treated as malformed rather than omitted), a `source_tr"
                "ansaction_id` not on this wallet or not a `debit` row, an overdraft "
                "correction that debits instead of credits ('Overdraft usage can only"
                " be corrected downward'), that exceeds the usage the entry still rec"
                "ords ('Adjustment exceeds the usage this entry still records'), or t"
                "hat exceeds the overdraft the wallet still owes ('Adjustment exceeds"
                " the wallet's outstanding overdraft', followed by how much can still"
                " be corrected), a `grant_id` sent with an overdraft entry, and an ar"
                "chived wallet.",
                WalletErrorResponseException),
        ).execute()
