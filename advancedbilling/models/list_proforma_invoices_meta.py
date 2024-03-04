# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ListProformaInvoicesMeta(object):

    """Implementation of the 'List Proforma Invoices Meta' model.

    TODO: type model description here.

    Attributes:
        total_count (int): TODO: type description here.
        current_page (int): TODO: type description here.
        total_pages (int): TODO: type description here.
        status_code (int): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "total_count": 'total_count',
        "current_page": 'current_page',
        "total_pages": 'total_pages',
        "status_code": 'status_code'
    }

    _optionals = [
        'total_count',
        'current_page',
        'total_pages',
        'status_code',
    ]

    def __init__(self,
                 total_count=APIHelper.SKIP,
                 current_page=APIHelper.SKIP,
                 total_pages=APIHelper.SKIP,
                 status_code=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the ListProformaInvoicesMeta class"""

        # Initialize members of the class
        if total_count is not APIHelper.SKIP:
            self.total_count = total_count 
        if current_page is not APIHelper.SKIP:
            self.current_page = current_page 
        if total_pages is not APIHelper.SKIP:
            self.total_pages = total_pages 
        if status_code is not APIHelper.SKIP:
            self.status_code = status_code 

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
        total_count = dictionary.get("total_count") if dictionary.get("total_count") else APIHelper.SKIP
        current_page = dictionary.get("current_page") if dictionary.get("current_page") else APIHelper.SKIP
        total_pages = dictionary.get("total_pages") if dictionary.get("total_pages") else APIHelper.SKIP
        status_code = dictionary.get("status_code") if dictionary.get("status_code") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(total_count,
                   current_page,
                   total_pages,
                   status_code,
                   dictionary)
