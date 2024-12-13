# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from advancedbilling.api_helper import APIHelper


class SubscriptionFilter(object):

    """Implementation of the 'Subscription Filter' model.

    Nested filter used for List Subscription Components For Site Filter

    Attributes:
        states (List[SubscriptionStateFilter]): Allows fetching components
            allocations that belong to the subscription with matching states
            based on provided values. To use this filter you also have to
            include the following param in the request `include=subscription`.
            Use in query
            `filter[subscription][states]=active,canceled&include=subscription`
            .
        date_field (SubscriptionListDateField): The type of filter you'd like
            to apply to your search. To use this filter you also have to
            include the following param in the request `include=subscription`.
        start_date (date): The start date (format YYYY-MM-DD) with which to
            filter the date_field. Returns components that belong to the
            subscription with a timestamp at or after midnight (12:00:00 AM)
            in your site’s time zone on the date specified. To use this filter
            you also have to include the following param in the request
            `include=subscription`.
        end_date (date): The end date (format YYYY-MM-DD) with which to filter
            the date_field. Returns components that belong to the subscription
            with a timestamp up to and including 11:59:59PM in your site’s
            time zone on the date specified. To use this filter you also have
            to include the following param in the request
            `include=subscription`.
        start_datetime (datetime): The start date and time (format YYYY-MM-DD
            HH:MM:SS) with which to filter the date_field. Returns components
            that belong to the subscription with a timestamp at or after exact
            time provided in query. You can specify timezone in query -
            otherwise your site''s time zone will be used. If provided, this
            parameter will be used instead of start_date. To use this filter
            you also have to include the following param in the request
            `include=subscription`.
        end_datetime (datetime): The end date and time (format YYYY-MM-DD
            HH:MM:SS) with which to filter the date_field. Returns components
            that belong to the subscription with a timestamp at or before
            exact time provided in query. You can specify timezone in query -
            otherwise your site''s time zone will be used. If provided, this
            parameter will be used instead of end_date. To use this filter you
            also have to include the following param in the request
            `include=subscription`.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "states": 'states',
        "date_field": 'date_field',
        "start_date": 'start_date',
        "end_date": 'end_date',
        "start_datetime": 'start_datetime',
        "end_datetime": 'end_datetime'
    }

    _optionals = [
        'states',
        'date_field',
        'start_date',
        'end_date',
        'start_datetime',
        'end_datetime',
    ]

    def __init__(self,
                 states=APIHelper.SKIP,
                 date_field=APIHelper.SKIP,
                 start_date=APIHelper.SKIP,
                 end_date=APIHelper.SKIP,
                 start_datetime=APIHelper.SKIP,
                 end_datetime=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SubscriptionFilter class"""

        # Initialize members of the class
        if states is not APIHelper.SKIP:
            self.states = states 
        if date_field is not APIHelper.SKIP:
            self.date_field = date_field 
        if start_date is not APIHelper.SKIP:
            self.start_date = start_date 
        if end_date is not APIHelper.SKIP:
            self.end_date = end_date 
        if start_datetime is not APIHelper.SKIP:
            self.start_datetime = APIHelper.apply_datetime_converter(start_datetime, APIHelper.RFC3339DateTime) if start_datetime else None 
        if end_datetime is not APIHelper.SKIP:
            self.end_datetime = APIHelper.apply_datetime_converter(end_datetime, APIHelper.RFC3339DateTime) if end_datetime else None 

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        states = dictionary.get("states") if dictionary.get("states") else APIHelper.SKIP
        date_field = dictionary.get("date_field") if dictionary.get("date_field") else APIHelper.SKIP
        start_date = dateutil.parser.parse(dictionary.get('start_date')).date() if dictionary.get('start_date') else APIHelper.SKIP
        end_date = dateutil.parser.parse(dictionary.get('end_date')).date() if dictionary.get('end_date') else APIHelper.SKIP
        start_datetime = APIHelper.RFC3339DateTime.from_value(dictionary.get("start_datetime")).datetime if dictionary.get("start_datetime") else APIHelper.SKIP
        end_datetime = APIHelper.RFC3339DateTime.from_value(dictionary.get("end_datetime")).datetime if dictionary.get("end_datetime") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(states,
                   date_field,
                   start_date,
                   end_date,
                   start_datetime,
                   end_datetime,
                   additional_properties)
