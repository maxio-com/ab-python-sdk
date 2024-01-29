# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.site import Site


class SiteResponse(object):

    """Implementation of the 'Site Response' model.

    TODO: type model description here.

    Attributes:
        site (Site): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "site": 'site'
    }

    def __init__(self,
                 site=None):
        """Constructor for the SiteResponse class"""

        # Initialize members of the class
        self.site = site 

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
        site = Site.from_dictionary(dictionary.get('site')) if dictionary.get('site') else None
        # Return an object of this model
        return cls(site)
