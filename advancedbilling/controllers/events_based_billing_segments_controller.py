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
from advancedbilling.models.segment_response import SegmentResponse
from advancedbilling.models.list_segments_response import ListSegmentsResponse
from advancedbilling.exceptions.api_exception import APIException
from advancedbilling.exceptions.event_based_billing_segment_errors_exception import EventBasedBillingSegmentErrorsException
from advancedbilling.exceptions.event_based_billing_list_segments_errors_exception import EventBasedBillingListSegmentsErrorsException
from advancedbilling.exceptions.event_based_billing_segment_exception import EventBasedBillingSegmentException


class EventsBasedBillingSegmentsController(BaseController):

    """A Controller to access Endpoints in the advancedbilling API."""
    def __init__(self, config):
        super(EventsBasedBillingSegmentsController, self).__init__(config)

    def create_segment(self,
                       component_id,
                       price_point_id,
                       body=None):
        """Does a POST request to /components/{component_id}/price_points/{price_point_id}/segments.json.

        This endpoint creates a new Segment for a Component with segmented
        Metric. It allows you to specify properties to bill upon and prices
        for each Segment. You can only pass as many "property_values" as the
        related Metric has segmenting properties defined.
        You may specify component and/or price point by using either the
        numeric ID or the `handle:gold` syntax.

        Args:
            component_id (str): ID or Handle for the Component
            price_point_id (str): ID or Handle for the Price Point belonging
                to the Component
            body (CreateSegmentRequest, optional): TODO: type description here.

        Returns:
            SegmentResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/components/{component_id}/price_points/{price_point_id}/segments.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('price_point_id')
                            .value(price_point_id)
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
            .deserialize_into(SegmentResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', EventBasedBillingSegmentErrorsException)
        ).execute()

    def list_segments_for_price_point(self,
                                      options=dict()):
        """Does a GET request to /components/{component_id}/price_points/{price_point_id}/segments.json.

        This endpoint allows you to fetch Segments created for a given Price
        Point. They will be returned in the order of creation.
        You can pass `page` and `per_page` parameters in order to access all
        of the segments. By default it will return `30` records. You can set
        `per_page` to `200` at most.
        You may specify component and/or price point by using either the
        numeric ID or the `handle:gold` syntax.

        Args:
            options (dict, optional): Key-value pairs for any of the
                parameters to this API Endpoint. All parameters to the
                endpoint are supplied through the dictionary with their names
                being the key and their desired values being the value. A list
                of parameters that can be used are::

                    component_id -- str -- ID or Handle for the Component
                    price_point_id -- str -- ID or Handle for the Price Point
                        belonging to the Component
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
                        records to fetch in each request. Default value is 30.
                        The maximum allowed values is 200; any per_page value
                        over 200 will be changed to 200. Use in query
                        `per_page=200`.
                    filter -- ListSegmentsFilter -- Filter to use for List
                        Segments for a Price Point operation

        Returns:
            ListSegmentsResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/components/{component_id}/price_points/{price_point_id}/segments.json')
            .http_method(HttpMethodEnum.GET)
            .template_param(Parameter()
                            .key('component_id')
                            .value(options.get('component_id', None))
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('price_point_id')
                            .value(options.get('price_point_id', None))
                            .is_required(True)
                            .should_encode(True))
            .query_param(Parameter()
                         .key('page')
                         .value(options.get('page', None)))
            .query_param(Parameter()
                         .key('per_page')
                         .value(options.get('per_page', None)))
            .query_param(Parameter()
                         .key('filter')
                         .value(options.get('filter', None)))
            .header_param(Parameter()
                          .key('accept')
                          .value('application/json'))
            .array_serialization_format(SerializationFormats.CSV)
            .auth(Single('BasicAuth'))
        ).response(
            ResponseHandler()
            .deserializer(APIHelper.json_deserialize)
            .deserialize_into(ListSegmentsResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', EventBasedBillingListSegmentsErrorsException)
        ).execute()

    def update_segment(self,
                       component_id,
                       price_point_id,
                       id,
                       body=None):
        """Does a PUT request to /components/{component_id}/price_points/{price_point_id}/segments/{id}.json.

        This endpoint updates a single Segment for a Component with a
        segmented Metric. It allows you to update the pricing for the segment.
        You may specify component and/or price point by using either the
        numeric ID or the `handle:gold` syntax.

        Args:
            component_id (str): ID or Handle of the Component
            price_point_id (str): ID or Handle of the Price Point belonging to
                the Component
            id (float): The ID of the Segment
            body (UpdateSegmentRequest, optional): TODO: type description here.

        Returns:
            SegmentResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/components/{component_id}/price_points/{price_point_id}/segments/{id}.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('price_point_id')
                            .value(price_point_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('id')
                            .value(id)
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
            .deserialize_into(SegmentResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', EventBasedBillingSegmentErrorsException)
        ).execute()

    def delete_segment(self,
                       component_id,
                       price_point_id,
                       id):
        """Does a DELETE request to /components/{component_id}/price_points/{price_point_id}/segments/{id}.json.

        This endpoint allows you to delete a Segment with specified ID.
        You may specify component and/or price point by using either the
        numeric ID or the `handle:gold` syntax.

        Args:
            component_id (str): ID or Handle of the Component
            price_point_id (str): ID or Handle of the Price Point belonging to
                the Component
            id (float): The ID of the Segment

        Returns:
            void: Response from the API. No Content

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/components/{component_id}/price_points/{price_point_id}/segments/{id}.json')
            .http_method(HttpMethodEnum.DELETE)
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('price_point_id')
                            .value(price_point_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('id')
                            .value(id)
                            .is_required(True)
                            .should_encode(True))
            .auth(Single('BasicAuth'))
        ).execute()

    def bulk_create_segments(self,
                             component_id,
                             price_point_id,
                             body=None):
        """Does a POST request to /components/{component_id}/price_points/{price_point_id}/segments/bulk.json.

        This endpoint allows you to create multiple segments in one request.
        The array of segments can contain up to `2000` records.
        If any of the records contain an error the whole request would fail
        and none of the requested segments get created. The error response
        contains a message for only the one segment that failed validation,
        with the corresponding index in the array.
        You may specify component and/or price point by using either the
        numeric ID or the `handle:gold` syntax.

        Args:
            component_id (str): ID or Handle for the Component
            price_point_id (str): ID or Handle for the Price Point belonging
                to the Component
            body (BulkCreateSegments, optional): TODO: type description here.

        Returns:
            ListSegmentsResponse: Response from the API. Created

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/components/{component_id}/price_points/{price_point_id}/segments/bulk.json')
            .http_method(HttpMethodEnum.POST)
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('price_point_id')
                            .value(price_point_id)
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
            .deserialize_into(ListSegmentsResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', EventBasedBillingSegmentException)
        ).execute()

    def bulk_update_segments(self,
                             component_id,
                             price_point_id,
                             body=None):
        """Does a PUT request to /components/{component_id}/price_points/{price_point_id}/segments/bulk.json.

        This endpoint allows you to update multiple segments in one request.
        The array of segments can contain up to `1000` records.
        If any of the records contain an error the whole request would fail
        and none of the requested segments get updated. The error response
        contains a message for only the one segment that failed validation,
        with the corresponding index in the array.
        You may specify component and/or price point by using either the
        numeric ID or the `handle:gold` syntax.

        Args:
            component_id (str): ID or Handle for the Component
            price_point_id (str): ID or Handle for the Price Point belonging
                to the Component
            body (BulkUpdateSegments, optional): TODO: type description here.

        Returns:
            ListSegmentsResponse: Response from the API. OK

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        return super().new_api_call_builder.request(
            RequestBuilder().server(Server.PRODUCTION)
            .path('/components/{component_id}/price_points/{price_point_id}/segments/bulk.json')
            .http_method(HttpMethodEnum.PUT)
            .template_param(Parameter()
                            .key('component_id')
                            .value(component_id)
                            .is_required(True)
                            .should_encode(True))
            .template_param(Parameter()
                            .key('price_point_id')
                            .value(price_point_id)
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
            .deserialize_into(ListSegmentsResponse.from_dictionary)
            .local_error_template('404', 'Not Found:\'{$response.body}\'', APIException)
            .local_error_template('422', 'HTTP Response Not OK. Status code: {$statusCode}. Response: \'{$response.body}\'.', EventBasedBillingSegmentException)
        ).execute()
