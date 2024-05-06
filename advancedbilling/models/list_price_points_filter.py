# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from advancedbilling.api_helper import APIHelper


class ListPricePointsFilter(object):

    """Implementation of the 'List PricePoints Filter' model.

    TODO: type model description here.

    Attributes:
        date_field (BasicDateField): The type of filter you would like to
            apply to your search. Use in query:
            `filter[date_field]=created_at`.
        start_date (date): The start date (format YYYY-MM-DD) with which to
            filter the date_field. Returns price points with a timestamp at or
            after midnight (12:00:00 AM) in your site’s time zone on the date
            specified.
        end_date (date): The end date (format YYYY-MM-DD) with which to filter
            the date_field. Returns price points with a timestamp up to and
            including 11:59:59PM in your site’s time zone on the date
            specified.
        start_datetime (datetime): The start date and time (format YYYY-MM-DD
            HH:MM:SS) with which to filter the date_field. Returns price
            points with a timestamp at or after exact time provided in query.
            You can specify timezone in query - otherwise your site's time
            zone will be used. If provided, this parameter will be used
            instead of start_date.
        end_datetime (datetime): The end date and time (format YYYY-MM-DD
            HH:MM:SS) with which to filter the date_field. Returns price
            points with a timestamp at or before exact time provided in query.
            You can specify timezone in query - otherwise your site's time
            zone will be used. If provided, this parameter will be used
            instead of end_date.
        mtype (List[PricePointType]): Allows fetching price points with
            matching type. Use in query: `filter[type]=custom,catalog`.
        ids (List[int]): Allows fetching price points with matching id based
            on provided values. Use in query: `filter[ids]=1,2,3`.
        archived_at (IncludeNullOrNotNull): Allows fetching price points only
            if archived_at is present or not. Use in query:
            `filter[archived_at]=not_null`.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "date_field": 'date_field',
        "start_date": 'start_date',
        "end_date": 'end_date',
        "start_datetime": 'start_datetime',
        "end_datetime": 'end_datetime',
        "mtype": 'type',
        "ids": 'ids',
        "archived_at": 'archived_at'
    }

    _optionals = [
        'date_field',
        'start_date',
        'end_date',
        'start_datetime',
        'end_datetime',
        'mtype',
        'ids',
        'archived_at',
    ]

    def __init__(self,
                 date_field=APIHelper.SKIP,
                 start_date=APIHelper.SKIP,
                 end_date=APIHelper.SKIP,
                 start_datetime=APIHelper.SKIP,
                 end_datetime=APIHelper.SKIP,
                 mtype=APIHelper.SKIP,
                 ids=APIHelper.SKIP,
                 archived_at=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the ListPricePointsFilter class"""

        # Initialize members of the class
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
        if mtype is not APIHelper.SKIP:
            self.mtype = mtype 
        if ids is not APIHelper.SKIP:
            self.ids = ids 
        if archived_at is not APIHelper.SKIP:
            self.archived_at = archived_at 

        # Add additional model properties to the instance
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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        date_field = dictionary.get("date_field") if dictionary.get("date_field") else APIHelper.SKIP
        start_date = dateutil.parser.parse(dictionary.get('start_date')).date() if dictionary.get('start_date') else APIHelper.SKIP
        end_date = dateutil.parser.parse(dictionary.get('end_date')).date() if dictionary.get('end_date') else APIHelper.SKIP
        start_datetime = APIHelper.RFC3339DateTime.from_value(dictionary.get("start_datetime")).datetime if dictionary.get("start_datetime") else APIHelper.SKIP
        end_datetime = APIHelper.RFC3339DateTime.from_value(dictionary.get("end_datetime")).datetime if dictionary.get("end_datetime") else APIHelper.SKIP
        mtype = dictionary.get("type") if dictionary.get("type") else APIHelper.SKIP
        ids = dictionary.get("ids") if dictionary.get("ids") else APIHelper.SKIP
        archived_at = dictionary.get("archived_at") if dictionary.get("archived_at") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(date_field,
                   start_date,
                   end_date,
                   start_datetime,
                   end_datetime,
                   mtype,
                   ids,
                   archived_at,
                   dictionary)
