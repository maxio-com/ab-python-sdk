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
from apimatic_core.types.array_serialization_format import SerializationFormats
from apimatic_core.authentication.multiple.single_auth import Single
from advancedbilling.models.metafield import Metafield
from advancedbilling.models.list_metafields_response import ListMetafieldsResponse
from advancedbilling.models.metadata import Metadata
from advancedbilling.models.paginated_metadata import PaginatedMetadata
from advancedbilling.exceptions.single_error_response_exception import SingleErrorResponseException
from advancedbilling.exceptions.api_exception import APIException


class CustomFieldsController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(CustomFieldsController, self).__init__(config)

    def create_metafields(self,
                          resource_type,
                          body=None):
        """Does a POST request to /{resource_type}/metafields.json.

        Creates metafields on a Site for either the Subscriptions or Customers
        resource. 
        Metafields and their metadata are created in the Custom Fields
        configuration page on your Site. Metafields can be populated with
        metadata when you create them or later with the [Update
        Metafield]($e/Custom%20Fields/updateMetafield), [Create
        Metadata]($e/Custom%20Fields/createMetadata), or [Update
        Metadata]($e/Custom%20Fields/updateMetadata) endpoints. The Create
        Metadata and Update Metadata endpoints allow you to add metafields and
        metadata values to a specific subscription or customer.
        Each site is limited to 100 unique metafields per resource. This means
        you can have 100 metafields for Subscriptions and another 100 for
        Customers.
        > Note: After creating a metafield, the resource type cannot be
        modified.
        In the UI and product documentation, metafields and metadata are
        called Custom Fields. 
        - Metafield is the custom field
        - Metadata is the data populating the custom field.
        See [Custom Fields
        Reference](https://docs.maxio.com/hc/en-us/articles/24266140850573-Cust
        om-Fields-Reference) and [Custom Fields
        Tab](https://maxio.zendesk.com/hc/en-us/articles/24251701302925-Subscri
        ption-Summary-Custom-Fields-Tab) for information on using Custom
        Fields in the Advanced Billing UI.

        Args:
            resource_type (ResourceType): The resource type to which the
                metafields belong.
            body (CreateMetafieldsRequest, optional): The request body
                parameter.

        Returns:
            List[Metafield]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/{resource_type}/metafields.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('resource_type')
                            .value(resource_type)
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
            .deserialize_into(Metafield.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', SingleErrorResponseException)
        ).execute()

    def list_metafields(self,
                        options=dict()):
        """Does a GET request to /{resource_type}/metafields.json.

        Lists the metafields and their associated details for a Site and
        resource type. You can filter the request to a specific metafield.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    resource_type -- ResourceType -- The resource type to
                        which the metafields belong.
                    name -- str -- Filter by the name of the metafield.
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
                    direction -- SortingDirection -- Controls the order in
                        which results are returned. Use in query
                        `direction=asc`.

        Returns:
            ListMetafieldsResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/{resource_type}/metafields.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('resource_type')
                            .value(options.get('resource_type', None))
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('name')
                         .value(options.get('name', None)))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('direction')
                         .value(options.get('direction', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListMetafieldsResponse.from_dictionary)
        ).execute()

    def update_metafield(self,
                         resource_type,
                         body=None):
        """Does a PUT request to /{resource_type}/metafields.json.

        Updates metafields on your Site for a resource type.  Depending on the
        request structure, you can update or add metafields and metadata to
        the Subscriptions or Customers resource.
        With this endpoint, you can: 
        - Add metafields. If the metafield specified in current_name does not
        exist, a new metafield is added. 
          >Note: Each site is limited to 100 unique metafields per resource.
        This means you can have 100 metafields for Subscriptions and another
        100 for Customers.
        - Change the name of a metafield. 
          >Note: To keep the metafield name the same and only update the
        metadata for the metafield, you must use the current metafield name in
        both the `current_name` and `name` parameters.
        - Change the input type for the metafield. For example, you can change
        a metafield input type from text to a dropdown. If you change the
        input type from text to a dropdown or radio, you must update the
        specific subscriptions or customers where the metafield was used to
        reflect the updated metafield and metadata. 
        - Add metadata values to the existing metadata for a dropdown or radio
        metafield. 
          >Note: Updates to metadata overwrite. To add one or more values, you
        must specify all metadata values including the new value you want to
        add.
        - Add new metadata to a dropdown or radio for a metafield that was
        created without metadata.
        - Remove  metadata for a dropdown or radio for a metafield.  
          >Note: Updates to metadata overwrite existing values. To remove one
        or more values, specify all metadata values except those you want to
        remove.
        - Add or update scope settings for a metafield.
          >Note: Scope changes overwrite existing settings. You must specify
        the complete scope, including the changes you want to make.

        Args:
            resource_type (ResourceType): The resource type to which the
                metafields belong.
            body (UpdateMetafieldsRequest, optional): The request body
                parameter.

        Returns:
            List[Metafield]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/{resource_type}/metafields.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('resource_type')
                            .value(resource_type)
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
            .deserialize_into(Metafield.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', SingleErrorResponseException)
        ).execute()

    def delete_metafield(self,
                         resource_type,
                         name=None):
        """Does a DELETE request to /{resource_type}/metafields.json.

        Deletes a metafield from your Site. Removes the metafield and
        associated metadata from all Subscriptions or Customers resources on
        the Site.

        Args:
            resource_type (ResourceType): The resource type to which the
                metafields belong.
            name (str, optional): The name of the metafield to be deleted

        Returns:
            void: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/{resource_type}/metafields.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('resource_type')
                            .value(resource_type)
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('name')
                         .value(name))
            .auth(Single('BasicAuth'))
        ).execute()

    def create_metadata(self,
                        resource_type,
                        resource_id,
                        body=None):
        """Does a POST request to /{resource_type}/{resource_id}/metadata.json.

        Creates metadata and metafields for a specific subscription or
        customer, or updates metadata values of existing metafields for a
        subscription or customer. Metadata values are limited to 2 KB in size.
        If you create metadata on a subscription or customer with a metafield
        that does not already exist, the metafield is created with the
        metadata you specify and it is always added as a text field. You can
        update the input_type for the metafield with the [Update
        Metafield]($e/Custom%20Fields/updateMetafield) endpoint. 
        >Note: Each site is limited to 100 unique metafields per resource.
        This means you can have 100 metafields for Subscriptions and another
        100 for Customers.

        Args:
            resource_type (ResourceType): The resource type to which the
                metafields belong.
            resource_id (int): The Advanced Billing id of the customer or the
                subscription for which the metadata applies
            body (CreateMetadataRequest, optional): The request body parameter.

        Returns:
            List[Metadata]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/{resource_type}/{resource_id}/metadata.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('resource_type')
                            .value(resource_type)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('resource_id')
                            .value(resource_id)
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
            .deserialize_into(Metadata.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', SingleErrorResponseException)
        ).execute()

    def list_metadata(self,
                      options=dict()):
        """Does a GET request to /{resource_type}/{resource_id}/metadata.json.

        Lists metadata and metafields for a specific customer or subscription.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    resource_type -- ResourceType -- The resource type to
                        which the metafields belong.
                    resource_id -- int -- The Advanced Billing id of the
                        customer or the subscription for which the metadata
                        applies
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
            PaginatedMetadata: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/{resource_type}/{resource_id}/metadata.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('resource_type')
                            .value(options.get('resource_type', None))
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('resource_id')
                            .value(options.get('resource_id', None))
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
            .deserialize_into(PaginatedMetadata.from_dictionary)
        ).execute()

    def update_metadata(self,
                        resource_type,
                        resource_id,
                        body=None):
        """Does a PUT request to /{resource_type}/{resource_id}/metadata.json.

        Updates metadata and metafields on the Site and the customer or
        subscription specified, and updates the metadata value on a
        subscription or customer.
        If you update metadata on a subscription or customer with a metafield
        that does not already exist, the metafield is created with the
        metadata you specify and it is always added as a text field to the
        Site and to the subscription or customer you specify. You can update
        the input_type for the metafield with the Update Metafield endpoint. 
        Each site is limited to 100 unique metafields per resource. This means
        you can have 100 metafields for Subscription and another 100 for
        Customer.

        Args:
            resource_type (ResourceType): The resource type to which the
                metafields belong.
            resource_id (int): The Advanced Billing id of the customer or the
                subscription for which the metadata applies
            body (UpdateMetadataRequest, optional): The request body parameter.

        Returns:
            List[Metadata]: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/{resource_type}/{resource_id}/metadata.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('resource_type')
                            .value(resource_type)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('resource_id')
                            .value(resource_id)
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
            .deserialize_into(Metadata.from_dictionary)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', SingleErrorResponseException)
        ).execute()

    def delete_metadata(self,
                        resource_type,
                        resource_id,
                        name=None,
                        names=None):
        """Does a DELETE request to /{resource_type}/{resource_id}/metadata.json.

        Deletes one or more metafields (and associated metadata) from the
        specified subscription or customer.

        Args:
            resource_type (ResourceType): The resource type to which the
                metafields belong.
            resource_id (int): The Advanced Billing id of the customer or the
                subscription for which the metadata applies
            name (str, optional): Name of field to be removed.
            names (List[str], optional): Names of fields to be removed. Use in
                query: `names[]=field1&names[]=my-field&names[]=another-field`.

        Returns:
            void: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/{resource_type}/{resource_id}/metadata.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('resource_type')
                            .value(resource_type)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('resource_id')
                            .value(resource_id)
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('name')
                         .value(name))
            .query_param(Parameter()
                         .key('names')
                         .value(names))
            .array_serialization_format(SerializationFormats.UN_INDEXED)
            .auth(Single('BasicAuth'))
        ).execute()

    def list_metadata_for_resource_type(self,
                                        options=dict()):
        """Does a GET request to /{resource_type}/metadata.json.

        Lists  metadata for a specified array of subscriptions or customers.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    resource_type -- ResourceType -- The resource type to
                        which the metafields belong.
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
                    date_field -- BasicDateField -- The type of filter you
                        would like to apply to your search.
                    start_date -- date -- The start date (format YYYY-MM-DD)
                        with which to filter the date_field. Returns metadata
                        with a timestamp at or after midnight (12:00:00 AM) in
                        your site’s time zone on the date specified.
                    end_date -- date -- The end date (format YYYY-MM-DD) with
                        which to filter the date_field. Returns metadata with
                        a timestamp up to and including 11:59:59PM in your
                        site’s time zone on the date specified.
                    start_datetime -- datetime -- The start date and time
                        (format YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns metadata with a timestamp at or
                        after exact time provided in query. You can specify
                        timezone in query - otherwise your site's time zone
                        will be used. If provided, this parameter will be used
                        instead of start_date.
                    end_datetime -- datetime -- The end date and time (format
                        YYYY-MM-DD HH:MM:SS) with which to filter the
                        date_field. Returns metadata with a timestamp at or
                        before exact time provided in query. You can specify
                        timezone in query - otherwise your site's time zone
                        will be used. If provided, this parameter will be used
                        instead of end_date.
                    with_deleted -- bool -- Allow to fetch deleted metadata.
                    resource_ids -- List[int] -- Allow to fetch metadata for
                        multiple records based on provided ids. Use in query:
                        `resource_ids[]=122&resource_ids[]=123&resource_ids[]=1
                        24`.
                    direction -- SortingDirection -- Controls the order in
                        which results are returned. Use in query
                        `direction=asc`.

        Returns:
            PaginatedMetadata: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/{resource_type}/metadata.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('resource_type')
                            .value(options.get('resource_type', None))
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('date_field')
                         .value(options.get('date_field', None)))
            .query_param(Parameter()
                         .key('start_date')
                         .value(options.get('start_date', None)))
            .query_param(Parameter()
                         .key('end_date')
                         .value(options.get('end_date', None)))
            .query_param(Parameter()
                         .key('start_datetime')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, options.get('start_datetime', None))))
            .query_param(Parameter()
                         .key('end_datetime')
                         .value(APIHelper.when_defined(APIHelper.RFC3339DateTime, options.get('end_datetime', None))))
            .query_param(Parameter()
                         .key('with_deleted')
                         .value(options.get('with_deleted', None)))
            .query_param(Parameter()
                         .key('resource_ids')
                         .value(options.get('resource_ids', None)))
            .query_param(Parameter()
                         .key('direction')
                         .value(options.get('direction', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.UN_INDEXED)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(PaginatedMetadata.from_dictionary)
        ).execute()
