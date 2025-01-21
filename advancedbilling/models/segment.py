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

    Attributes:
        id (int): The model property of type int.
        component_id (int): The model property of type int.
        price_point_id (int): The model property of type int.
        event_based_billing_metric_id (int): The model property of type int.
        pricing_scheme (PricingScheme): The identifier for the pricing scheme.
            See [Product
            Components](https://help.chargify.com/products/product-components.h
            tml) for an overview of pricing schemes.
        segment_property_1_value (str | float | int | bool | None): The model
            property of type str | float | int | bool | None.
        segment_property_2_value (str | float | int | bool | None): The model
            property of type str | float | int | bool | None.
        segment_property_3_value (str | float | int | bool | None): The model
            property of type str | float | int | bool | None.
        segment_property_4_value (str | float | int | bool | None): The model
            property of type str | float | int | bool | None.
        created_at (datetime): The model property of type datetime.
        updated_at (datetime): The model property of type datetime.
        prices (List[SegmentPrice]): The model property of type
            List[SegmentPrice].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
                 prices=APIHelper.SKIP,
                 additional_properties=None):
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
            self.created_at = APIHelper.apply_datetime_converter(created_at, APIHelper.RFC3339DateTime) if created_at else None 
        if updated_at is not APIHelper.SKIP:
            self.updated_at = APIHelper.apply_datetime_converter(updated_at, APIHelper.RFC3339DateTime) if updated_at else None 
        if prices is not APIHelper.SKIP:
            self.prices = prices 

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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if not isinstance(dictionary, dict) or dictionary is None:
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
        created_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("created_at")).datetime if dictionary.get("created_at") else APIHelper.SKIP
        updated_at = APIHelper.RFC3339DateTime.from_value(dictionary.get("updated_at")).datetime if dictionary.get("updated_at") else APIHelper.SKIP
        prices = None
        if dictionary.get('prices') is not None:
            prices = [SegmentPrice.from_dictionary(x) for x in dictionary.get('prices')]
        else:
            prices = APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
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
                   prices,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!r}, '
                f'component_id={self.component_id!r}, '
                f'price_point_id={self.price_point_id!r}, '
                f'event_based_billing_metric_id={self.event_based_billing_metric_id!r}, '
                f'pricing_scheme={self.pricing_scheme!r}, '
                f'segment_property_1_value={self.segment_property_1_value!r}, '
                f'segment_property_2_value={self.segment_property_2_value!r}, '
                f'segment_property_3_value={self.segment_property_3_value!r}, '
                f'segment_property_4_value={self.segment_property_4_value!r}, '
                f'created_at={self.created_at!r}, '
                f'updated_at={self.updated_at!r}, '
                f'prices={self.prices!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!s}, '
                f'component_id={self.component_id!s}, '
                f'price_point_id={self.price_point_id!s}, '
                f'event_based_billing_metric_id={self.event_based_billing_metric_id!s}, '
                f'pricing_scheme={self.pricing_scheme!s}, '
                f'segment_property_1_value={self.segment_property_1_value!s}, '
                f'segment_property_2_value={self.segment_property_2_value!s}, '
                f'segment_property_3_value={self.segment_property_3_value!s}, '
                f'segment_property_4_value={self.segment_property_4_value!s}, '
                f'created_at={self.created_at!s}, '
                f'updated_at={self.updated_at!s}, '
                f'prices={self.prices!s}, '
                f'additional_properties={self.additional_properties!s})')
