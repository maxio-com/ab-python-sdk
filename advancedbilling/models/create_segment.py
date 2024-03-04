# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.create_or_update_segment_price import CreateOrUpdateSegmentPrice


class CreateSegment(object):

    """Implementation of the 'Create Segment' model.

    TODO: type model description here.

    Attributes:
        segment_property_1_value (str | float | int | bool | None): A value
            that will occur in your events that you want to bill upon. The
            type of the value depends on the property type in the related
            event based billing metric.
        segment_property_2_value (str | float | int | bool | None): A value
            that will occur in your events that you want to bill upon. The
            type of the value depends on the property type in the related
            event based billing metric.
        segment_property_3_value (str | float | int | bool | None): A value
            that will occur in your events that you want to bill upon. The
            type of the value depends on the property type in the related
            event based billing metric.
        segment_property_4_value (str | float | int | bool | None): A value
            that will occur in your events that you want to bill upon. The
            type of the value depends on the property type in the related
            event based billing metric.
        pricing_scheme (PricingScheme): The identifier for the pricing scheme.
            See [Product
            Components](https://help.chargify.com/products/product-components.h
            tml) for an overview of pricing schemes.
        prices (List[CreateOrUpdateSegmentPrice]): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pricing_scheme": 'pricing_scheme',
        "segment_property_1_value": 'segment_property_1_value',
        "segment_property_2_value": 'segment_property_2_value',
        "segment_property_3_value": 'segment_property_3_value',
        "segment_property_4_value": 'segment_property_4_value',
        "prices": 'prices'
    }

    _optionals = [
        'segment_property_1_value',
        'segment_property_2_value',
        'segment_property_3_value',
        'segment_property_4_value',
        'prices',
    ]

    def __init__(self,
                 pricing_scheme=None,
                 segment_property_1_value=APIHelper.SKIP,
                 segment_property_2_value=APIHelper.SKIP,
                 segment_property_3_value=APIHelper.SKIP,
                 segment_property_4_value=APIHelper.SKIP,
                 prices=APIHelper.SKIP,
                 additional_properties={}):
        """Constructor for the CreateSegment class"""

        # Initialize members of the class
        if segment_property_1_value is not APIHelper.SKIP:
            self.segment_property_1_value = segment_property_1_value 
        if segment_property_2_value is not APIHelper.SKIP:
            self.segment_property_2_value = segment_property_2_value 
        if segment_property_3_value is not APIHelper.SKIP:
            self.segment_property_3_value = segment_property_3_value 
        if segment_property_4_value is not APIHelper.SKIP:
            self.segment_property_4_value = segment_property_4_value 
        self.pricing_scheme = pricing_scheme 
        if prices is not APIHelper.SKIP:
            self.prices = prices 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        pricing_scheme = dictionary.get("pricing_scheme") if dictionary.get("pricing_scheme") else None
        segment_property_1_value = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateSegmentSegmentProperty1Value'), dictionary.get('segment_property_1_value'), False) if dictionary.get('segment_property_1_value') is not None else APIHelper.SKIP
        segment_property_2_value = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateSegmentSegmentProperty2Value'), dictionary.get('segment_property_2_value'), False) if dictionary.get('segment_property_2_value') is not None else APIHelper.SKIP
        segment_property_3_value = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateSegmentSegmentProperty3Value'), dictionary.get('segment_property_3_value'), False) if dictionary.get('segment_property_3_value') is not None else APIHelper.SKIP
        segment_property_4_value = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateSegmentSegmentProperty4Value'), dictionary.get('segment_property_4_value'), False) if dictionary.get('segment_property_4_value') is not None else APIHelper.SKIP
        prices = None
        if dictionary.get('prices') is not None:
            prices = [CreateOrUpdateSegmentPrice.from_dictionary(x) for x in dictionary.get('prices')]
        else:
            prices = APIHelper.SKIP
        # Clean out expected properties from dictionary
        for key in cls._names.values():
            if key in dictionary:
                del dictionary[key]
        # Return an object of this model
        return cls(pricing_scheme,
                   segment_property_1_value,
                   segment_property_2_value,
                   segment_property_3_value,
                   segment_property_4_value,
                   prices,
                   dictionary)
