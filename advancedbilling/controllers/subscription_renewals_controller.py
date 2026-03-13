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
from advancedbilling.models.scheduled_renewal_configuration_item_response import (
    ScheduledRenewalConfigurationItemResponse,
)
from advancedbilling.models.scheduled_renewal_configuration_response import (
    ScheduledRenewalConfigurationResponse,
)
from advancedbilling.models.scheduled_renewal_configurations_response import (
    ScheduledRenewalConfigurationsResponse,
)


class SubscriptionRenewalsController(BaseController):
    """A Controller to access Endpoints in the advancedbilling API."""

    def __init__(self, config):
        """Initialize SubscriptionRenewalsController object."""
        super(SubscriptionRenewalsController, self).__init__(config)

    def create_scheduled_renewal_configuration(self,
                                               subscription_id,
                                               body=None):
        """Perform a POST request to
        /subscriptions/{subscription_id}/scheduled_renewals.json.

        Creates a scheduled renewal configuration for a subscription. The scheduled
        renewal is based on the subscription’s current product and component setup.

        Args:
            subscription_id (int): The Chargify id of the subscription.
            body (ScheduledRenewalConfigurationRequest, optional): The request body
                parameter.

        Returns:
            ScheduledRenewalConfigurationResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscriptions/{subscription_id}/scheduled_renewals.json")
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
            .deserialize_into(ScheduledRenewalConfigurationResponse.from_dictionary)
            .local_error("422",
                "Unprocessable Entity (WebDAV)",
                ErrorListResponseException),
        ).execute()

    def list_scheduled_renewal_configurations(self,
                                              subscription_id,
                                              status=None):
        """Perform a GET request to
        /subscriptions/{subscription_id}/scheduled_renewals.json.

        Lists scheduled renewal configurations for the subscription and permits an
        optional status query filter.

        Args:
            subscription_id (int): The Chargify id of the subscription.
            status (Status, optional): (Optional) Status filter for scheduled renewal
                configurations.

        Returns:
            ScheduledRenewalConfigurationsResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscriptions/{subscription_id}/scheduled_renewals.json")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("subscription_id")
                .value(subscription_id)
                .is_required(True)
                .should_encode(True))
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
            .deserialize_into(ScheduledRenewalConfigurationsResponse.from_dictionary),
        ).execute()

    def read_scheduled_renewal_configuration(self,
                                             subscription_id,
                                             id):
        """Perform a GET request to
        /subscriptions/{subscription_id}/scheduled_renewals/{id}.json.

        Retrieves the configuration settings for the scheduled renewal.

        Args:
            subscription_id (int): The Chargify id of the subscription.
            id (int): The renewal id.

        Returns:
            ScheduledRenewalConfigurationResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscriptions/{subscription_id}/scheduled_renewals/{id}.json")
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                .key("subscription_id")
                .value(subscription_id)
                .is_required(True)
                .should_encode(True))
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
            .deserialize_into(ScheduledRenewalConfigurationResponse.from_dictionary),
        ).execute()

    def update_scheduled_renewal_configuration(self,
                                               subscription_id,
                                               id,
                                               body=None):
        """Perform a PUT request to
        /subscriptions/{subscription_id}/scheduled_renewals/{id}.json.

        Updates an existing configuration.

        Args:
            subscription_id (int): The Chargify id of the subscription.
            id (int): The renewal id.
            body (ScheduledRenewalConfigurationRequest, optional): The request body
                parameter.

        Returns:
            ScheduledRenewalConfigurationResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscriptions/{subscription_id}/scheduled_renewals/{id}.json")
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                .key("subscription_id")
                .value(subscription_id)
                .is_required(True)
                .should_encode(True))
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
            .deserialize_into(ScheduledRenewalConfigurationResponse.from_dictionary)
            .local_error("422",
                "Unprocessable Entity (WebDAV)",
                ErrorListResponseException),
        ).execute()

    def schedule_scheduled_renewal_lock_in(self,
                                           subscription_id,
                                           id,
                                           body=None):
        """Perform a PUT request to
        /subscriptions/{subscription_id}/scheduled_renewals/{id}/schedule_lock_in.json.

        Schedules a future lock-in date for the renewal.

        Args:
            subscription_id (int): The Chargify id of the subscription.
            id (int): The renewal id.
            body (ScheduledRenewalLockInRequest, optional): The request body
                parameter.

        Returns:
            ScheduledRenewalConfigurationResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscriptions/{subscription_id}/scheduled_renewals/{id}/schedule_lock_in.json")
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                .key("subscription_id")
                .value(subscription_id)
                .is_required(True)
                .should_encode(True))
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
            .deserialize_into(ScheduledRenewalConfigurationResponse.from_dictionary)
            .local_error("422",
                "Unprocessable Entity (WebDAV)",
                ErrorListResponseException),
        ).execute()

    def lock_in_scheduled_renewal_immediately(self,
                                              subscription_id,
                                              id):
        """Perform a PUT request to
        /subscriptions/{subscription_id}/scheduled_renewals/{id}/immediate_lock_in.json
        .

        Locks in the renewal immediately.

        Args:
            subscription_id (int): The Chargify id of the subscription.
            id (int): The renewal id.

        Returns:
            ScheduledRenewalConfigurationResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscriptions/{subscription_id}/scheduled_renewals/{id}/immediate_lock_in.json")
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                .key("subscription_id")
                .value(subscription_id)
                .is_required(True)
                .should_encode(True))
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
            .deserialize_into(ScheduledRenewalConfigurationResponse.from_dictionary)
            .local_error("422",
                "Unprocessable Entity (WebDAV)",
                ErrorListResponseException),
        ).execute()

    def unpublish_scheduled_renewal_configuration(self,
                                                  subscription_id,
                                                  id):
        """Perform a PUT request to
        /subscriptions/{subscription_id}/scheduled_renewals/{id}/unpublish.json.

        Returns a scheduled renewal configuration to an editable state.

        Args:
            subscription_id (int): The Chargify id of the subscription.
            id (int): The renewal id.

        Returns:
            ScheduledRenewalConfigurationResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscriptions/{subscription_id}/scheduled_renewals/{id}/unpublish.json")
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                .key("subscription_id")
                .value(subscription_id)
                .is_required(True)
                .should_encode(True))
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
            .deserialize_into(ScheduledRenewalConfigurationResponse.from_dictionary)
            .local_error("422",
                "Unprocessable Entity (WebDAV)",
                ErrorListResponseException),
        ).execute()

    def cancel_scheduled_renewal_configuration(self,
                                               subscription_id,
                                               id):
        """Perform a PUT request to
        /subscriptions/{subscription_id}/scheduled_renewals/{id}/cancel.json.

        Cancels a scheduled renewal configuration.

        Args:
            subscription_id (int): The Chargify id of the subscription.
            id (int): The renewal id.

        Returns:
            ScheduledRenewalConfigurationResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscriptions/{subscription_id}/scheduled_renewals/{id}/cancel.json")
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                .key("subscription_id")
                .value(subscription_id)
                .is_required(True)
                .should_encode(True))
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
            .deserialize_into(ScheduledRenewalConfigurationResponse.from_dictionary)
            .local_error("422",
                "Unprocessable Entity (WebDAV)",
                ErrorListResponseException),
        ).execute()

    def create_scheduled_renewal_configuration_item(self,
                                                    subscription_id,
                                                    scheduled_renewals_configuration_id,
                                                    body=None):
        """Perform a POST request to
        /subscriptions/{subscription_id}/scheduled_renewals/{scheduled_renewals_configu
        ration_id}/configuration_items.json.

        Adds product and component line items to the scheduled renewal.

        Args:
            subscription_id (int): The Chargify id of the subscription.
            scheduled_renewals_configuration_id (int): The scheduled renewal
                configuration id.
            body (ScheduledRenewalConfigurationItemRequest, optional): The request
                body parameter.

        Returns:
            ScheduledRenewalConfigurationItemResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscriptions/{subscription_id}/scheduled_renewals/{scheduled_renewals_configuration_id}/configuration_items.json")
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                .key("subscription_id")
                .value(subscription_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("scheduled_renewals_configuration_id")
                .value(scheduled_renewals_configuration_id)
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
            .deserialize_into(ScheduledRenewalConfigurationItemResponse.from_dictionary)
            .local_error("422",
                "Unprocessable Entity (WebDAV)",
                ErrorListResponseException),
        ).execute()

    def update_scheduled_renewal_configuration_item(self,
                                                    subscription_id,
                                                    scheduled_renewals_configuration_id,
                                                    id,
                                                    body=None):
        """Perform a PUT request to
        /subscriptions/{subscription_id}/scheduled_renewals/{scheduled_renewals_configu
        ration_id}/configuration_items/{id}.json.

        Updates an existing configuration item’s pricing and quantity.

        Args:
            subscription_id (int): The Chargify id of the subscription.
            scheduled_renewals_configuration_id (int): The scheduled renewal
                configuration id.
            id (int): The scheduled renewal configuration item id.
            body (ScheduledRenewalUpdateRequest, optional): The request body
                parameter.

        Returns:
            ScheduledRenewalConfigurationItemResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscriptions/{subscription_id}/scheduled_renewals/{scheduled_renewals_configuration_id}/configuration_items/{id}.json")
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                .key("subscription_id")
                .value(subscription_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("scheduled_renewals_configuration_id")
                .value(scheduled_renewals_configuration_id)
                .is_required(True)
                .should_encode(True))
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
            .deserialize_into(ScheduledRenewalConfigurationItemResponse.from_dictionary)
            .local_error("422",
                "Unprocessable Entity (WebDAV)",
                ErrorListResponseException),
        ).execute()

    def delete_scheduled_renewal_configuration_item(self,
                                                    subscription_id,
                                                    scheduled_renewals_configuration_id,
                                                    id):
        """Perform a DELETE request to
        /subscriptions/{subscription_id}/scheduled_renewals/{scheduled_renewals_configu
        ration_id}/configuration_items/{id}.json.

        Removes an item from the pending renewal configuration.

        Args:
            subscription_id (int): The Chargify id of the subscription.
            scheduled_renewals_configuration_id (int): The scheduled renewal
                configuration id.
            id (int): The scheduled renewal configuration item id.

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from the
                remote API. This exception includes the HTTP Response code, an error
                message, and the HTTP body that was received in the request.

        """
        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path("/subscriptions/{subscription_id}/scheduled_renewals/{scheduled_renewals_configuration_id}/configuration_items/{id}.json")
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                .key("subscription_id")
                .value(subscription_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("scheduled_renewals_configuration_id")
                .value(scheduled_renewals_configuration_id)
                .is_required(True)
                .should_encode(True))
            .template_param(Parameter()
                .key("id")
                .value(id)
                .is_required(True)
                .should_encode(True))
            .auth(Single("BasicAuth")),
        ).execute()
