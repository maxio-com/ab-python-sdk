# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from advancedbilling.api_helper import APIHelper


class ListPrepaymentsFilter(object):

    """Implementation of the 'List Prepayments Filter' model.

    TODO: type model description here.

    Attributes:
        date_field (ListPrepaymentDateField): The type of filter you would
            like to apply to your search. `created_at` - Time when prepayment
            was created. `application_at` - Time when prepayment was applied
            to invoice. Use in query `filter[date_field]=created_at`.
        start_date (date): The start date (format YYYY-MM-DD) with which to
            filter the date_field. Returns prepayments with a timestamp at or
            after midnight (12:00:00 AM) in your site's time zone on the date
            specified. Use in query: `filter[start_date]=2011-12-15`.
        end_date (date): The end date (format YYYY-MM-DD) with which to filter
            the date_field. Returns prepayments with a timestamp up to and
            including 11:59:59PM in your site's time zone on the date
            specified. Use in query: `filter[end_date]=2011-12-15`.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "date_field": 'date_field',
        "start_date": 'start_date',
        "end_date": 'end_date'
    }

    _optionals = [
        'date_field',
        'start_date',
        'end_date',
    ]

    def __init__(self,
                 date_field=APIHelper.SKIP,
                 start_date=APIHelper.SKIP,
                 end_date=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the ListPrepaymentsFilter class"""

        # Initialize members of the class
        if date_field is not APIHelper.SKIP:
            self.date_field = date_field 
        if start_date is not APIHelper.SKIP:
            self.start_date = start_date 
        if end_date is not APIHelper.SKIP:
            self.end_date = end_date 

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
        date_field = dictionary.get("date_field") if dictionary.get("date_field") else APIHelper.SKIP
        start_date = dateutil.parser.parse(dictionary.get('start_date')).date() if dictionary.get('start_date') else APIHelper.SKIP
        end_date = dateutil.parser.parse(dictionary.get('end_date')).date() if dictionary.get('end_date') else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(date_field,
                   start_date,
                   end_date,
                   additional_properties)
