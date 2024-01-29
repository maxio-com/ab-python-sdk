# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.segment_price import SegmentPrice


class Segment(object):

    """Implementation of the 'Segment' model.

    TODO: type model description here.

    Attributes:
        id (int): TODO: type description here.
        component_id (int): TODO: type description here.
        price_point_id (int): TODO: type description here.
        event_based_billing_metric_id (int): TODO: type description here.
        pricing_scheme (PricingScheme): The identifier for the pricing scheme.
            See [Product
            Components](https://help.chargify.com/products/product-components.h
            tml) for an overview of pricing schemes.
        segment_property_1_value (str | float | int | bool | None): TODO: type
            description here.
        segment_property_2_value (str | float | int | bool | None): TODO: type
            description here.
        segment_property_3_value (str | float | int | bool | None): TODO: type
            description here.
        segment_property_4_value (str | float | int | bool | None): TODO: type
            description here.
        created_at (str): TODO: type description here.
        updated_at (str): TODO: type description here.
        prices (List[SegmentPrice]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "component_id": 'component_id',
        "price_point_id": 'price_point_id',
        "event_based_billing_metric_id": 'event_based_billing_metric_id',
        "pricing_scheme": 'pricing_scheme',
        "segment_property_1_value": 'segment_property_1_value',
        "segment_property_2_value": 'segment_property_2_value',
        "segment_property_3_value": 'segment_property_3_value',
        "segment_property_4_value": 'segment_property_4_value',
        "created_at": 'created_at',
        "updated_at": 'updated_at',
        "prices": 'prices'
    }

    _optionals = [
        'id',
        'component_id',
        'price_point_id',
        'event_based_billing_metric_id',
        'pricing_scheme',
        'segment_property_1_value',
        'segment_property_2_value',
        'segment_property_3_value',
        'segment_property_4_value',
        'created_at',
        'updated_at',
        'prices',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 component_id=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 event_based_billing_metric_id=APIHelper.SKIP,
                 pricing_scheme=APIHelper.SKIP,
                 segment_property_1_value=APIHelper.SKIP,
                 segment_property_2_value=APIHelper.SKIP,
                 segment_property_3_value=APIHelper.SKIP,
                 segment_property_4_value=APIHelper.SKIP,
                 created_at=APIHelper.SKIP,
                 updated_at=APIHelper.SKIP,
                 prices=APIHelper.SKIP):
        """Constructor for the Segment class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 
        if event_based_billing_metric_id is not APIHelper.SKIP:
            self.event_based_billing_metric_id = event_based_billing_metric_id 
        if pricing_scheme is not APIHelper.SKIP:
            self.pricing_scheme = pricing_scheme 
        if segment_property_1_value is not APIHelper.SKIP:
            self.segment_property_1_value = segment_property_1_value 
        if segment_property_2_value is not APIHelper.SKIP:
            self.segment_property_2_value = segment_property_2_value 
        if segment_property_3_value is not APIHelper.SKIP:
            self.segment_property_3_value = segment_property_3_value 
        if segment_property_4_value is not APIHelper.SKIP:
            self.segment_property_4_value = segment_property_4_value 
        if created_at is not APIHelper.SKIP:
            self.created_at = created_at 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = updated_at 
        if prices is not APIHelper.SKIP:
            self.prices = prices 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if dictionary.get("price_point_id") else APIHelper.SKIP
        event_based_billing_metric_id = dictionary.get("event_based_billing_metric_id") if dictionary.get("event_based_billing_metric_id") else APIHelper.SKIP
        pricing_scheme = dictionary.get("pricing_scheme") if dictionary.get("pricing_scheme") else APIHelper.SKIP
        segment_property_1_value = APIHelper.deserialize_union_type(UnionTypeLookUp.get('SegmentSegmentProperty1Value'), dictionary.get('segment_property_1_value'), False) if dictionary.get('segment_property_1_value') is not None else APIHelper.SKIP
        segment_property_2_value = APIHelper.deserialize_union_type(UnionTypeLookUp.get('SegmentSegmentProperty2Value'), dictionary.get('segment_property_2_value'), False) if dictionary.get('segment_property_2_value') is not None else APIHelper.SKIP
        segment_property_3_value = APIHelper.deserialize_union_type(UnionTypeLookUp.get('SegmentSegmentProperty3Value'), dictionary.get('segment_property_3_value'), False) if dictionary.get('segment_property_3_value') is not None else APIHelper.SKIP
        segment_property_4_value = APIHelper.deserialize_union_type(UnionTypeLookUp.get('SegmentSegmentProperty4Value'), dictionary.get('segment_property_4_value'), False) if dictionary.get('segment_property_4_value') is not None else APIHelper.SKIP
        created_at = dictionary.get("created_at") if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = dictionary.get("updated_at") if dictionary.get("updated_at") else APIHelper.SKIP
        prices = None
        if dictionary.get('prices') is not None:
            prices = [SegmentPrice.from_dictionary(x) for x in dictionary.get('prices')]
        else:
            prices = APIHelper.SKIP
        # Return an object of this model
        return cls(id,
                   component_id,
                   price_point_id,
                   event_based_billing_metric_id,
                   pricing_scheme,
                   segment_property_1_value,
                   segment_property_2_value,
                   segment_property_3_value,
                   segment_property_4_value,
                   created_at,
                   updated_at,
                   prices)
