# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.metafield import Metafield


class ListMetafieldsResponse(object):

    """Implementation of the 'List Metafields Response' model.

    TODO: type model description here.

    Attributes:
        total_count (int): TODO: type description here.
        current_page (int): TODO: type description here.
        total_pages (int): TODO: type description here.
        per_page (int): TODO: type description here.
        metafields (List[Metafield]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "total_count": 'total_count',
        "current_page": 'current_page',
        "total_pages": 'total_pages',
        "per_page": 'per_page',
        "metafields": 'metafields'
    }

    _optionals = [
        'total_count',
        'current_page',
        'total_pages',
        'per_page',
        'metafields',
    ]

    def __init__(self,
                 total_count=APIHelper.SKIP,
                 current_page=APIHelper.SKIP,
                 total_pages=APIHelper.SKIP,
                 per_page=APIHelper.SKIP,
                 metafields=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the ListMetafieldsResponse class"""

        # Initialize members of the class
        if total_count is not APIHelper.SKIP:
            self.total_count = total_count 
        if current_page is not APIHelper.SKIP:
            self.current_page = current_page 
        if total_pages is not APIHelper.SKIP:
            self.total_pages = total_pages 
        if per_page is not APIHelper.SKIP:
            self.per_page = per_page 
        if metafields is not APIHelper.SKIP:
            self.metafields = metafields 

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
        per_page = dictionary.get("per_page") if dictionary.get("per_page") else APIHelper.SKIP
        metafields = None
        if dictionary.get('metafields') is not None:
            metafields = [Metafield.from_dictionary(x) for x in dictionary.get('metafields')]
        else:
            metafields = APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(total_count,
                   current_page,
                   total_pages,
                   per_page,
                   metafields,
                   dictionary)
