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
from advancedbilling.models.aggregated_entitlements_response import (
    AggregatedEntitlementsResponse,
)


class EntitlementsController(BaseController):
    """A Controller to access Endpoints in the advancedbilling API."""

    def __init__(self, config):
        """Initialize EntitlementsController object."""
        super(EntitlementsController, self).__init__(config)

    def read_subscription_entitlements(self,
                                       subscription_id):
        """Perform a GET request to
        /subscriptions/{subscription_id}/entitlements.json.

        Returns every feature a subscription is entitled to, collapsed into one entry
        per feature key and periodicity window across all products and components on
        the subscription. A `usage_limit` feature granted with two different
        periodicities comes back as two entries sharing one `feature_key`, each
        identified by its own `periodicity_key`.
        When more than one product or component grants the same feature key and
        periodicity, the values are combined:
        - **`access_right`** features are combined with a boolean OR. If any
        contributor grants access, the aggregate is `true`. `source_products` only
        lists the contributors that granted `true`.
        - **`usage_limit`** features are summed across every contributor sharing the
        same periodicity window. `source_products` lists every contributor. Grants
        with different periodicities are not summed together. Each periodicity is
        returned as a separate entry.
        - **`service_right`** features are not combined: one contributor's value
        wins. Do not rely on which one when several grant the same feature key.
        `enabled` reflects both the aggregated value and the subscription's state.
        The field is `false` whenever the subscription is not in a live state
        (`active`, `trialing`, `assessing`, `past_due`, `soft_failure`), regardless
        of the aggregated value. Entitlements deliberately stay enabled through
        dunning.

        Args:
            subscription_id (int): The Chargify id of the subscription.

        Returns:
            AggregatedEntitlementsResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscriptions/{subscription_id}/entitlements.json")
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
            .deserialize_into(AggregatedEntitlementsResponse.from_dictionary)
            .local_error("403", "Forbidden", ErrorListResponseException)
            .local_error("404", "Not Found", APIException),
        ).execute()
