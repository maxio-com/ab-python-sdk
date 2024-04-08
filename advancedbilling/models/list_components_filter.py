# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ListComponentsFilter(object):

    """Implementation of the 'List Components Filter' model.

    TODO: type model description here.

    Attributes:
        ids (List[int]): Allows fetching components with matching id based on
            provided value. Use in query `filter[ids]=1,2,3`.
        use_site_exchange_rate (bool): Allows fetching components with
            matching use_site_exchange_rate based on provided value (refers to
            default price point). Use in query
            `filter[use_site_exchange_rate]=true`.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "ids": 'ids',
        "use_site_exchange_rate": 'use_site_exchange_rate'
    }

    _optionals = [
        'ids',
        'use_site_exchange_rate',
    ]

    def __init__(self,
                 ids=APIHelper.SKIP,
                 use_site_exchange_rate=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the ListComponentsFilter class"""

        # Initialize members of the class
        if ids is not APIHelper.SKIP:
            self.ids = ids 
        if use_site_exchange_rate is not APIHelper.SKIP:
            self.use_site_exchange_rate = use_site_exchange_rate 

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
        ids = dictionary.get("ids") if dictionary.get("ids") else APIHelper.SKIP
        use_site_exchange_rate = dictionary.get("use_site_exchange_rate") if "use_site_exchange_rate" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(ids,
                   use_site_exchange_rate,
                   dictionary)
