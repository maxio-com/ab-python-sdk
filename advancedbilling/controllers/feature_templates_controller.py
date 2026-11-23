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
from advancedbilling.models.feature_template_response import (
    FeatureTemplateResponse,
)
from advancedbilling.models.feature_templates_list_response import (
    FeatureTemplatesListResponse,
)


class FeatureTemplatesController(BaseController):
    """A Controller to access Endpoints in the advancedbilling API."""

    def __init__(self, config):
        """Initialize FeatureTemplatesController object."""
        super(FeatureTemplatesController, self).__init__(config)

    def list_feature_templates(self,
                               page=1,
                               per_page=20,
                               status="active",
                               q=None,
                               kind=None,
                               updated_from=None,
                               updated_to=None,
                               sort_by="name",
                               sort_direction="asc"):
        """Perform a GET request to /features.json.

        Lists the feature templates defined for your site, active (non-archived) ones
        by default. Pass `status=archived` or `status=all` to widen the result set.
        Supply `page` or `per_page` to paginate. Without either parameter, the
        response includes the full result set.

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
            status (Status1, optional): Filters by archived state. Defaults to
                `active` (non-archived templates only).
            q (str, optional): Filters to feature templates whose name contains this
                substring (case-insensitive).
            kind (Kind, optional): Filters by feature kind.
            updated_from (date, optional): Returns feature templates updated on or
                after this date.
            updated_to (date, optional): Returns feature templates updated on or
                before this date.
            sort_by (SortBy, optional): The field to sort results by.
            sort_direction (SortDirection, optional): The sort direction of the
                returned feature templates.

        Returns:
            FeatureTemplatesListResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/features.json")
            .http_method(HttpMethodEnum.GET)
            .query_param(Parameter()
                .key("page")
                .value(page))
            .query_param(Parameter()
                .key("per_page")
                .value(per_page))
            .query_param(Parameter()
                .key("status")
                .value(status))
            .query_param(Parameter()
                .key("q")
                .value(q))
            .query_param(Parameter()
                .key("kind")
                .value(kind))
            .query_param(Parameter()
                .key("updated_from")
                .value(updated_from))
            .query_param(Parameter()
                .key("updated_to")
                .value(updated_to))
            .query_param(Parameter()
                .key("sort_by")
                .value(sort_by))
            .query_param(Parameter()
                .key("sort_direction")
                .value(sort_direction))
            .header_param(Parameter()
                .key("accept")
                .value("application/json"))
            .auth(Single("BasicAuth")),
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(FeatureTemplatesListResponse.from_dictionary)
            .local_error("403", "Forbidden", ErrorListResponseException),
        ).execute()

    def create_feature_template(self,
                                body=None):
        """Perform a POST request to /features.json.

        Defines a new feature at the site level. Feature templates aren't billable on
        their own. Attach a template to products or components to grant the feature
        to subscribers.

        Args:
            body (CreateFeatureTemplateRequest, optional): The request body parameter.

        Returns:
            FeatureTemplateResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/features.json")
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
            .deserialize_into(FeatureTemplateResponse.from_dictionary)
            .local_error("403", "Forbidden", ErrorListResponseException)
            .local_error_template("422",
                "HTTP Response Not OK. Status code: {$statusCode}. Response: '{$respo"
                "nse.body}'.",
                ErrorListResponseException),
        ).execute()

    def read_feature_template(self,
                              id):
        """Perform a GET request to /features/{id}.json.

        Returns a single feature template. Archived feature templates are not
        addressable here and return `404`. Restore a template first to read or update
        it.

        Args:
            id (int): The Advanced Billing id of the feature template.

        Returns:
            FeatureTemplateResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/features/{id}.json")
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
            .deserialize_into(FeatureTemplateResponse.from_dictionary)
            .local_error("403", "Forbidden", ErrorListResponseException)
            .local_error("404", "Not Found", APIException),
        ).execute()

    def update_feature_template(self,
                                id,
                                body=None):
        """Perform a PUT request to /features/{id}.json.

        Updates the name, description, unit, value type, default value, or default
        periodicity of a feature template. `key` is rejected on every update. `kind`
        is rejected once any feature catalog item has been created from this template.
        Archived feature templates are not addressable here and return `404`. Restore
        a template first to update it.

        Args:
            id (int): The Advanced Billing id of the feature template.
            body (UpdateFeatureTemplateRequest, optional): The request body parameter.

        Returns:
            FeatureTemplateResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/features/{id}.json")
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
            .deserialize_into(FeatureTemplateResponse.from_dictionary)
            .local_error("403", "Forbidden", ErrorListResponseException)
            .local_error("404", "Not Found", APIException)
            .local_error_template("422",
                "HTTP Response Not OK. Status code: {$statusCode}. Response: '{$respo"
                "nse.body}'.",
                ErrorListResponseException),
        ).execute()

    def archive_feature_template(self,
                                 id,
                                 remove_from_catalog=False):
        """Perform a DELETE request to /features/{id}.json.

        Archives a feature template. Archived feature templates are not addressable
        via [Read Feature Template]($e/Feature%20Templates/readFeatureTemplate) or
        [Update Feature Template]($e/Feature%20Templates/updateFeatureTemplate). Both
        endpoints return `404` until the template is restored.
        The feature template record itself is never hard-deleted, and can always be
        restored with [Restore Feature
        Template]($e/Feature%20Templates/restoreFeatureTemplate). Reversibility does
        not extend to `remove_from_catalog=true`: the feature catalog items and
        entitlements that parameter destroys are gone permanently, and restoring the
        template will not bring subscriber access back.

        Args:
            id (int): The Advanced Billing id of the feature template.
            remove_from_catalog (bool, optional): When `true`, also destroys every
                feature catalog item created from this template and cascades to their
                entitlements, revoking subscriber access immediately. When `false`
                (default), the feature template and its feature catalog items are
                archived, and existing entitlements are preserved.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/features/{id}.json")
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                .key("id")
                .value(id)
                .is_required(True)
                .should_encode(True))
            .query_param(Parameter()
                .key("remove_from_catalog")
                .value(remove_from_catalog))
            .auth(Single("BasicAuth")),
        ).execute()

    def restore_feature_template(self,
                                 id):
        """Perform a POST request to /features/{id}/restore.json.

        Clears the feature template's archived state. Feature catalog items created
        from this template are not automatically restored. Restore each one
        individually.

        Args:
            id (int): The Advanced Billing id of the feature template.

        Returns:
            FeatureTemplateResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/features/{id}/restore.json")
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
            .deserialize_into(FeatureTemplateResponse.from_dictionary)
            .local_error("403", "Forbidden", ErrorListResponseException)
            .local_error("404", "Not Found", APIException)
            .local_error_template("422",
                "HTTP Response Not OK. Status code: {$statusCode}. Response: '{$respo"
                "nse.body}'.",
                ErrorListResponseException),
        ).execute()
