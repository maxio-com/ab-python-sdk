# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

from advancedbilling.api_helper import APIHelper
from advancedbilling.configuration import Server
from advancedbilling.controllers.base_controller import BaseController
from apimatic_core.request_builder import RequestBuilder
from apimatic_core.response_handler import ResponseHandler
from apimatic_core.types.parameter import Parameter
from advancedbilling.http.http_method_enum import HttpMethodEnum
from apimatic_core.authentication.multiple.single_auth import Single
from apimatic_core.authentication.multiple.and_auth_group import And
from apimatic_core.authentication.multiple.or_auth_group import Or
from advancedbilling.models.subscription_note_response import SubscriptionNoteResponse
from advancedbilling.exceptions.api_exception import APIException


class SubscriptionNotesController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(SubscriptionNotesController, self).__init__(config)

    def create_subscription_note(self,
                                 subscription_id,
                                 body=None):
        """Does a POST request to /subscriptions/{subscription_id}/notes.json.

        Use the following method to create a note for a subscription.
        ## How to Use Subscription Notes
        Notes allow you to record information about a particular Subscription
        in a free text format.
        If you have structured data such as birth date, color, etc., consider
        using Metadata instead.
        Full documentation on how to use Notes in the Chargify UI can be
        located
        [here](https://maxio-chargify.zendesk.com/hc/en-us/articles/54044349031
        81-Subscription-Summary#notes).

        Args:
            subscription_id (int): The Chargify id of the subscription
            body (UpdateSubscriptionNoteRequest, optional): TODO: type
                description here.

        Returns:
            SubscriptionNoteResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/notes.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionNoteResponse.from_dictionary)
        ).execute()

    def list_subscription_notes(self,
                                options=dict()):
        """Does a GET request to /subscriptions/{subscription_id}/notes.json.

        Use this method to retrieve a list of Notes associated with a
        Subscription. The response will be an array of Notes.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    subscription_id -- int -- The Chargify id of the
                        subscription
                    page -- int -- Result records are organized in pages. By
                        default, the first page of results is displayed. The
                        page parameter specifies a page number of results to
                        fetch. You can start navigating through the pages to
                        consume the results. You do this by passing in a page
                        parameter. Retrieve the next page by adding ?page=2 to
                        the query string. If there are no results to return,
                        then an empty result set will be returned. Use in
                        query `page=1`.
                    per_page -- int -- This parameter indicates how many
                        records to fetch in each request. Default value is 20.
                        The maximum allowed values is 200; any per_page value
                        over 200 will be changed to 200. Use in query
                        `per_page=200`.

        Returns:
            List[SubscriptionNoteResponse]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/notes.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(options.get('subscription_id', None))
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionNoteResponse.from_dictionary)
        ).execute()

    def read_subscription_note(self,
                               subscription_id,
                               note_id):
        """Does a GET request to /subscriptions/{subscription_id}/notes/{note_id}.json.

        Once you have obtained the ID of the note you wish to read, use this
        method to show a particular note attached to a subscription.

        Args:
            subscription_id (int): The Chargify id of the subscription
            note_id (int): The Chargify id of the note

        Returns:
            SubscriptionNoteResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/notes/{note_id}.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('note_id')
                            .value(note_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionNoteResponse.from_dictionary)
        ).execute()

    def update_subscription_note(self,
                                 subscription_id,
                                 note_id,
                                 body=None):
        """Does a PUT request to /subscriptions/{subscription_id}/notes/{note_id}.json.

        Use the following method to update a note for a Subscription.

        Args:
            subscription_id (int): The Chargify id of the subscription
            note_id (int): The Chargify id of the note
            body (UpdateSubscriptionNoteRequest, optional): TODO: type
                description here.

        Returns:
            SubscriptionNoteResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/notes/{note_id}.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('note_id')
                            .value(note_id)
                            .is_required(True)
                            .should_encode(True))
            .header_param(Parameter()
                          .key('Content-Type')
                          .value('application/json'))
            .body_param(Parameter()
                        .value(body))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .body_serializer(APIHelper.json_serialize)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(SubscriptionNoteResponse.from_dictionary)
        ).execute()

    def delete_subscription_note(self,
                                 subscription_id,
                                 note_id):
        """Does a DELETE request to /subscriptions/{subscription_id}/notes/{note_id}.json.

        Use the following method to delete a note for a Subscription.

        Args:
            subscription_id (int): The Chargify id of the subscription
            note_id (int): The Chargify id of the note

        Returns:
            void: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.DEFAULT)
            .path('/subscriptions/{subscription_id}/notes/{note_id}.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('subscription_id')
                            .value(subscription_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('note_id')
                            .value(note_id)
                            .is_required(True)
                            .should_encode(True))
            .auth(Single('BasicAuth'))
        ).execute()
