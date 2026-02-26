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
from advancedbilling.models.enable_webhooks_response import (
    EnableWebhooksResponse,
)
from advancedbilling.models.endpoint import (
    Endpoint,
)
from advancedbilling.models.endpoint_response import (
    EndpointResponse,
)
from advancedbilling.models.replay_webhooks_response import (
    ReplayWebhooksResponse,
)
from advancedbilling.models.webhook_response import (
    WebhookResponse,
)


class WebhooksController(BaseController):
    """A Controller to access Endpoints in the advancedbilling API."""

    def __init__(self, config):
        """Initialize WebhooksController object."""
        super(WebhooksController, self).__init__(config)

    def list_webhooks(self,
                      options=dict()):
        """Perform a GET request to /webhooks.json.

        Allows you to view a list of webhooks.  You can pass query parameters if you
        want to filter webhooks. See the
        [Webhooks](page:introduction/webhooks/webhooks) documentation for more
        information.

        Args:
            options (dict, optional): Key-value pairs for any of the parameters to
                this API Endpoint. All parameters to the endpoint are supplied
                through the dictionary with their names being the key and their
                desired values being the value. A list of parameters that can be used
                are::
                    status -- WebhookStatus -- Webhooks with matching status would be
                        returned.
                    since_date -- str -- Format YYYY-MM-DD. Returns Webhooks with the
                        created_at date greater than or equal to the one specified.
                    until_date -- str -- Format YYYY-MM-DD. Returns Webhooks with the
                        created_at date less than or equal to the one specified.
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
                    order -- WebhookOrder -- The order in which the Webhooks are
                        returned.
                    subscription -- int -- The Advanced Billing id of a subscription
                        you'd like to filter for

        Returns:
            List[WebhookResponse]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/webhooks.json")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("status")
                .value(options.get("status", None)))
            .query_param(Parameter()
                .key("since_date")
                .value(options.get("since_date", None)))
            .query_param(Parameter()
                .key("until_date")
                .value(options.get("until_date", None)))
            .query_param(Parameter()
                .key("page")
                .value(options.get("page", None)))
            .query_param(Parameter()
                .key("per_page")
                .value(options.get("per_page", None)))
            .query_param(Parameter()
                .key("order")
                .value(options.get("order", None)))
            .query_param(Parameter()
                .key("subscription")
                .value(options.get("subscription", None)))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(WebhookResponse.from_dictionary),
        ).execute()

    def enable_webhooks(self,
                        body=None):
        """Perform a PUT request to /webhooks/settings.json.

        Allows you to enable webhooks for your site

        Args:
            body (EnableWebhooksRequest, optional): The request body parameter.

        Returns:
            EnableWebhooksResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/webhooks/settings.json")
            .http_method(HttpMethodEnum.PUT)
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
            .deserialize_into(EnableWebhooksResponse.from_dictionary),
        ).execute()

    def replay_webhooks(self,
                        body=None):
        """Perform a POST request to /webhooks/replay.json.

        Replays webhooks. Posting to this endpoint does not immediately resend the
        webhooks. They are added to a queue and sent as soon as possible, depending
        on available system resources. You can submit an array of up to 1000 webhook
        IDs in the replay request.

        Args:
            body (ReplayWebhooksRequest, optional): The request body parameter.

        Returns:
            ReplayWebhooksResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/webhooks/replay.json")
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
            .deserialize_into(ReplayWebhooksResponse.from_dictionary),
        ).execute()

    def create_endpoint(self,
                        body=None):
        """Perform a POST request to /endpoints.json.

        Creates an endpoint and assigns a list of webhooks subscriptions (events) to
        it.
        See the [Webhooks
        Reference](page:introduction/webhooks/webhooks-reference#events) page for
        available events.

        Args:
            body (CreateOrUpdateEndpointRequest, optional): The request body
                parameter.

        Returns:
            EndpointResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/endpoints.json")
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
            .deserialize_into(EndpointResponse.from_dictionary)
            .local_error_template("422",
                "HTTP Response Not OK. Status code: {$statusCode}. Response: '{$respo"
                "nse.body}'.",
                ErrorListResponseException),
        ).execute()

    def list_endpoints(self):
        """Perform a GET request to /endpoints.json.

        Returns created endpoints for a site.

        Returns:
            List[Endpoint]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/endpoints.json")
            .http_method(HttpMethodEnum.GET)
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(Endpoint.from_dictionary),
        ).execute()

    def update_endpoint(self,
                        endpoint_id,
                        body=None):
        """Perform a PUT request to /endpoints/{endpoint_id}.json.

        Updates an Endpoint. You can change the `url` of your endpoint or the list of
        `webhook_subscriptions` to which you are subscribed. See the [Webhooks
        Reference](page:introduction/webhooks/webhooks-reference#events) page for
        available events.
        Always send a complete list of events to which you want to subscribe. Sending
        a PUT request for an existing endpoint with an empty list of
        `webhook_subscriptions` will unsubscribe all events.
        If you want unsubscribe from a specific event, send a list of
        `webhook_subscriptions` without the specific event key.

        Args:
            endpoint_id (int): The Advanced Billing id for the endpoint that should
                be updated
            body (CreateOrUpdateEndpointRequest, optional): The request body
                parameter.

        Returns:
            EndpointResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/endpoints/{endpoint_id}.json")
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                .key("endpoint_id")
                .value(endpoint_id)
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
            .deserialize_into(EndpointResponse.from_dictionary)
            .local_error_template("404", "Not Found:'{$response.body}'", APIException)
            .local_error_template("422",
                "HTTP Response Not OK. Status code: {$statusCode}. Response: '{$respo"
                "nse.body}'.",
                ErrorListResponseException),
        ).execute()
