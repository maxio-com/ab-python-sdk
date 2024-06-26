# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ListSegmentsFilter(object):

    """Implementation of the 'List Segments Filter' model.

    TODO: type model description here.

    Attributes:
        segment_property_1_value (str): The value passed here would be used to
            filter segments. Pass a value related to `segment_property_1` on
            attached Metric. If empty string is passed, this filter would be
            rejected. Use in query `filter[segment_property_1_value]=EU`.
        segment_property_2_value (str): The value passed here would be used to
            filter segments. Pass a value related to `segment_property_2` on
            attached Metric. If empty string is passed, this filter would be
            rejected.
        segment_property_3_value (str): The value passed here would be used to
            filter segments. Pass a value related to `segment_property_3` on
            attached Metric. If empty string is passed, this filter would be
            rejected.
        segment_property_4_value (str): The value passed here would be used to
            filter segments. Pass a value related to `segment_property_4` on
            attached Metric. If empty string is passed, this filter would be
            rejected.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "segment_property_1_value": 'segment_property_1_value',
        "segment_property_2_value": 'segment_property_2_value',
        "segment_property_3_value": 'segment_property_3_value',
        "segment_property_4_value": 'segment_property_4_value'
    }

    _optionals = [
        'segment_property_1_value',
        'segment_property_2_value',
        'segment_property_3_value',
        'segment_property_4_value',
    ]

    def __init__(self,
                 segment_property_1_value=APIHelper.SKIP,
                 segment_property_2_value=APIHelper.SKIP,
                 segment_property_3_value=APIHelper.SKIP,
                 segment_property_4_value=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the ListSegmentsFilter class"""

        # Initialize members of the class
        if segment_property_1_value is not APIHelper.SKIP:
            self.segment_property_1_value = segment_property_1_value 
        if segment_property_2_value is not APIHelper.SKIP:
            self.segment_property_2_value = segment_property_2_value 
        if segment_property_3_value is not APIHelper.SKIP:
            self.segment_property_3_value = segment_property_3_value 
        if segment_property_4_value is not APIHelper.SKIP:
            self.segment_property_4_value = segment_property_4_value 

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
        segment_property_1_value = dictionary.get("segment_property_1_value") if dictionary.get("segment_property_1_value") else APIHelper.SKIP
        segment_property_2_value = dictionary.get("segment_property_2_value") if dictionary.get("segment_property_2_value") else APIHelper.SKIP
        segment_property_3_value = dictionary.get("segment_property_3_value") if dictionary.get("segment_property_3_value") else APIHelper.SKIP
        segment_property_4_value = dictionary.get("segment_property_4_value") if dictionary.get("segment_property_4_value") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(segment_property_1_value,
                   segment_property_2_value,
                   segment_property_3_value,
                   segment_property_4_value,
                   dictionary)
