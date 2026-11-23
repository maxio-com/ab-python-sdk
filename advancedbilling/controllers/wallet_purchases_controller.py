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
from advancedbilling.models.wallet_purchase_preview_response import (
    WalletPurchasePreviewResponse,
)
from advancedbilling.models.wallet_purchase_result_response import (
    WalletPurchaseResultResponse,
)


class WalletPurchasesController(BaseController):
    """A Controller to access Endpoints in the advancedbilling API."""

    def __init__(self, config):
        """Initialize WalletPurchasesController object."""
        super(WalletPurchasesController, self).__init__(config)

    def create_wallet_purchase(self,
                               wallet_id,
                               idempotency_key=None,
                               body=None):
        """Perform a POST request to /wallets/{wallet_id}/purchases.json.

        Purchases prepaid units for the wallet and charges the subscription's payment
        method for them, using the wallet's `price_point_id` unless a different price
        point is named. A successful purchase writes a grant of origin `purchase`,
        with its expiration following the funding entitlement's grant expiration
        policy.
        How "charged" works depends on the subscription's collection method. For
        card/automatic collection, the payment is attempted immediately; a decline
        writes nothing to the wallet, and the call fails with a `422` naming the
        gateway's decline reason. For invoice-billed (remittance) subscriptions,
        there's no immediate charge to decline: an invoice is drafted, the wallet is
        credited right away, and the invoice is issued afterward. If issuing the
        invoice fails at that point, the invoice is left in draft state and reported
        for follow-up, but the call still returns `201` and the units already
        credited are **not** rolled back. See [Preview Wallet
        Purchase]($e/Wallet%20Purchases/previewWalletPurchase) to quote a price
        before charging anything.

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
            body (CreateWalletPurchaseRequest, optional): The request body parameter.

        Returns:
            WalletPurchaseResultResponse: Response from the API. Purchase completed.
                Charges the subscription's payment method and, once payment succeeds,
                credits the wallet.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/wallets/{wallet_id}/purchases.json")
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
            .deserialize_into(WalletPurchaseResultResponse.from_dictionary)
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
                "Returned in two cases, both with nothing new charged or written. `id"
                "empotency_request_in_progress`: a purchase with the same `Idempotenc"
                "y-Key` is still running; retry with the same key once it finishes. `"
                "idempotency_key_outcome_unknown`: an earlier purchase with this key "
                "ended with a server error or an unexpected failure before its result"
                " was recorded, so it may or may not have charged the customer. Check"
                " the subscription's invoices before buying again under a new key.",
                WalletErrorResponseException)
            .local_error("422",
                "Validation or payment failure, or an `Idempotency-Key` reused with a"
                " different request (`idempotency_key_mismatch`). Validation failures"
                " include a missing `purchase` root, a missing, malformed, non-positi"
                "ve, or out-of-range `quantity`, a `price_point_id` that doesn't belo"
                "ng to the wallet's billing product, an archived, custom, or otherwis"
                "e unusable price point, no price point to purchase at (neither sent "
                "nor set on the wallet), a memo over 255 characters, an archived wall"
                "et, a price point with no price in the subscription's currency, a de"
                "clined payment (message includes the gateway's own detail), an invoi"
                "ce that couldn't be created at all, a payment that settled but whose"
                " units could not be credited (`purchase_paid_but_uncredited`, whose "
                "message ends with the paid invoice's uid so it can be reconciled), a"
                " declined payment whose invoice could not be voided and is still ope"
                "n (`purchase_declined_invoice_open`), a purchase that failed before "
                "payment and left its invoice open (`purchase_invoice_left_open`), an"
                "d a wallet whose billing product isn't a Wallet Product (only possib"
                "le for a wallet created before Wallet Products became required).\n\n"
                "`purchase_paid_but_uncredited`, `purchase_declined_invoice_open` and"
                " `purchase_invoice_left_open` bodies also carry `invoice_uid` and `i"
                "nvoice_number`. With an `Idempotency-Key`, these three responses are"
                " stored and replayed like a success.",
                WalletErrorResponseException)
            .local_error("500",
                "`purchase_payment_outcome_unknown`: the payment was attempted but th"
                "e gateway did not confirm whether the card was charged. Nothing is c"
                "redited by this call; if the invoice turns out to be paid, the units"
                " are credited automatically (see [Purchasing Units](page:introductio"
                "n/basic-concepts/wallets#purchasing-units)). The body includes `invo"
                "ice_uid` and `invoice_number` when an invoice was created; check tha"
                "t invoice before buying again. Retrying with the same `Idempotency-K"
                "ey` returns `409` (`idempotency_key_outcome_unknown`) rather than ch"
                "arging again.",
                WalletErrorResponseException),
        ).execute()

    def preview_wallet_purchase(self,
                                wallet_id,
                                body=None):
        """Perform a POST request to
        /wallets/{wallet_id}/purchases/preview.json.

        Quotes the price for a purchase at the given quantity and price point,
        without charging the payment method or writing to the wallet. Takes the same
        parameters as [Create Wallet
        Purchase]($e/Wallet%20Purchases/createWalletPurchase).

        Args:
            wallet_id (int): The Advanced Billing id of the wallet.
            body (CreateWalletPurchaseRequest, optional): The request body parameter.

        Returns:
            WalletPurchasePreviewResponse: Response from the API. A price quote.
                Charges nothing and writes nothing to the wallet.

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/wallets/{wallet_id}/purchases/preview.json")
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                .key("wallet_id")
                .value(wallet_id)
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
            .deserialize_into(WalletPurchasePreviewResponse.from_dictionary)
            .local_error("403",
                "Forbidden. The response body is plain text (`403 Forbidden`), not JS"
                "ON. Returned when the Wallets feature isn't enabled for the site.",
                APIException)
            .local_error("404", "Not Found", WalletErrorResponseException)
            .local_error("422",
                "Validation failure. Same cases as Create Wallet Purchase, minus the "
                "payment-outcome cases, since nothing is charged.",
                WalletErrorResponseException),
        ).execute()
