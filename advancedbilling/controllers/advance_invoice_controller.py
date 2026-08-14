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
from advancedbilling.http.http_method_enum import (
    HttpMethodEnum,
)
from advancedbilling.models.invoice import Invoice


class AdvanceInvoiceController(BaseController):
    """A Controller to access Endpoints in the advancedbilling API."""

    def __init__(self, config):
        """Initialize AdvanceInvoiceController object."""
        super(AdvanceInvoiceController, self).__init__(config)

    def issue_advance_invoice(self,
                              subscription_id,
                              body=None):
        """Perform a POST request to
        /subscriptions/{subscription_id}/advance_invoice/issue.json.

        Issues an invoice in advance for a subscription's next renewal date. For the
        most part, advance invoices function like any other invoice, except they are
        issued early and have special behavior upon being voided. For more
        information on advance invoices, including eligibility for generating one,
        see [Issue Invoice In
        Advance](https://maxio.zendesk.com/hc/en-us/articles/24252026404749-Issue-Invo
        ice-In-Advance).
        A subscription can only have one advance invoice per billing period.
        Attempting to issue an advance invoice when one already exists returns an
        error.
        Regeneration of the invoice can be forced with the params `force: true`,
        which voids an advance invoice if one exists and generates a new one. If no
        advance invoice exists, a new one is generated.
        Consider using either the create or preview endpoints for proforma invoices
        to preview this advance invoice before using this endpoint to generate it.

        Args:
            subscription_id (int): The Chargify id of the subscription.
            body (IssueAdvanceInvoiceRequest, optional): The request body parameter.

        Returns:
            Invoice: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscriptions/{subscription_id}/advance_invoice/issue.json")
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
            .deserialize_into(Invoice.from_dictionary)
            .local_error_template("404", "Not Found:'{$response.body}'", APIException)
            .local_error_template("422",
                "HTTP Response Not OK. Status code: {$statusCode}. Response: '{$respo"
                "nse.body}'.",
                ErrorListResponseException),
        ).execute()

    def read_advance_invoice(self,
                             subscription_id):
        """Perform a GET request to
        /subscriptions/{subscription_id}/advance_invoice.json.

        Returns the advance invoice generated for a subscription's upcoming renewal.
        There can only be one advance invoice per subscription per billing cycle.

        Args:
            subscription_id (int): The Chargify id of the subscription.

        Returns:
            Invoice: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscriptions/{subscription_id}/advance_invoice.json")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("subscription_id")
                .value(subscription_id)
                .is_required(True)
                .should_encode(True))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Invoice.from_dictionary)
            .local_error_template("404", "Not Found:'{$response.body}'", APIException),
        ).execute()

    def void_advance_invoice(self,
                             subscription_id,
                             body=None):
        """Perform a POST request to
        /subscriptions/{subscription_id}/advance_invoice/void.json.

        Voids a subscription's existing advance invoice. Once voided, it can later be
        regenerated if desired.
        A `reason` is required to void, and the invoice must have an open status.
        Voiding causes any prepayments and credits that were applied to the invoice
        to be returned to the subscription.
        For a full overview of the impact of voiding, see [Invoice]($m/Invoice).

        Args:
            subscription_id (int): The Chargify id of the subscription.
            body (VoidInvoiceRequest, optional): The request body parameter.

        Returns:
            Invoice: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscriptions/{subscription_id}/advance_invoice/void.json")
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
            .deserialize_into(Invoice.from_dictionary)
            .local_error_template("404", "Not Found:'{$response.body}'", APIException),
        ).execute()
