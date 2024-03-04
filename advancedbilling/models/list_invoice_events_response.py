# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_event import InvoiceEvent


class ListInvoiceEventsResponse(object):

    """Implementation of the 'List Invoice Events Response' model.

    TODO: type model description here.

    Attributes:
        events (List[InvoiceEvent]): TODO: type description here.
        page (int): TODO: type description here.
        per_page (int): TODO: type description here.
        total_pages (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "events": 'events',
        "page": 'page',
        "per_page": 'per_page',
        "total_pages": 'total_pages'
    }

    _optionals = [
        'events',
        'page',
        'per_page',
        'total_pages',
    ]

    def __init__(self,
                 events=APIHelper.SKIP,
                 page=APIHelper.SKIP,
                 per_page=APIHelper.SKIP,
                 total_pages=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the ListInvoiceEventsResponse class"""

        # Initialize members of the class
        if events is not APIHelper.SKIP:
            self.events = events 
        if page is not APIHelper.SKIP:
            self.page = page 
        if per_page is not APIHelper.SKIP:
            self.per_page = per_page 
        if total_pages is not APIHelper.SKIP:
            self.total_pages = total_pages 

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
        events = None
        if dictionary.get('events') is not None:
            events = [InvoiceEvent.from_dictionary(x) for x in dictionary.get('events')]
        else:
            events = APIHelper.SKIP
        page = dictionary.get("page") if dictionary.get("page") else APIHelper.SKIP
        per_page = dictionary.get("per_page") if dictionary.get("per_page") else APIHelper.SKIP
        total_pages = dictionary.get("total_pages") if dictionary.get("total_pages") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(events,
                   page,
                   per_page,
                   total_pages,
                   dictionary)
