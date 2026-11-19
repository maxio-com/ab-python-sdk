"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.create_or_update_segment_price import (
    CreateOrUpdateSegmentPrice,
)
from advancedbilling.models.pricing_scheme import (
    PricingScheme,
)


class SubscriptionComponentCustomPriceSegment(object):
    """Implementation of the 'Subscription Component Custom Price Segment' model.

    Custom rates for one segment of an event-based component, set on the subscription
    through `custom_price.segments`.
    Identify the segment by the property values that occur in your events, in the
    same positions as the segmenting properties defined on the component's meter.
    Each segment in a request must have a unique combination of property values.
    Property values are matched against your events as text. Send values for boolean
    segmenting properties as the strings `"true"` and `"false"`: JSON booleans are
    not supported here, and a segment whose only property value is `false` is
    rejected with a 422.

    Attributes:
        segment_property_1_value (str | float | int | None): A value that will occur
            in your events that you want to bill upon. For a boolean segmenting
            property, send the value as a string, `"true"` or `"false"`.
        segment_property_2_value (str | float | int | None): A value that will occur
            in your events that you want to bill upon. For a boolean segmenting
            property, send the value as a string, `"true"` or `"false"`.
        segment_property_3_value (str | float | int | None): A value that will occur
            in your events that you want to bill upon. For a boolean segmenting
            property, send the value as a string, `"true"` or `"false"`.
        segment_property_4_value (str | float | int | None): A value that will occur
            in your events that you want to bill upon. For a boolean segmenting
            property, send the value as a string, `"true"` or `"false"`.
        segment_property_5_value (str | float | int | None): A value that will occur
            in your events that you want to bill upon. For a boolean segmenting
            property, send the value as a string, `"true"` or `"false"`.
        segment_property_6_value (str | float | int | None): A value that will occur
            in your events that you want to bill upon. For a boolean segmenting
            property, send the value as a string, `"true"` or `"false"`.
        segment_property_7_value (str | float | int | None): A value that will occur
            in your events that you want to bill upon. For a boolean segmenting
            property, send the value as a string, `"true"` or `"false"`.
        segment_property_8_value (str | float | int | None): A value that will occur
            in your events that you want to bill upon. For a boolean segmenting
            property, send the value as a string, `"true"` or `"false"`.
        segment_property_9_value (str | float | int | None): A value that will occur
            in your events that you want to bill upon. For a boolean segmenting
            property, send the value as a string, `"true"` or `"false"`.
        segment_property_10_value (str | float | int | None): A value that will occur
            in your events that you want to bill upon. For a boolean segmenting
            property, send the value as a string, `"true"` or `"false"`.
        pricing_scheme (PricingScheme): The identifier for the pricing scheme. See
            [Product
            Components](https://help.chargify.com/products/product-components.html)
            for an overview of pricing schemes.
        prices (List[CreateOrUpdateSegmentPrice]): The rates for this segment. Use
            one price for a flat rate, or several price brackets for a tiered, volume
            or stairstep scheme.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pricing_scheme": "pricing_scheme",
        "prices": "prices",
        "segment_property_1_value": "segment_property_1_value",
        "segment_property_2_value": "segment_property_2_value",
        "segment_property_3_value": "segment_property_3_value",
        "segment_property_4_value": "segment_property_4_value",
        "segment_property_5_value": "segment_property_5_value",
        "segment_property_6_value": "segment_property_6_value",
        "segment_property_7_value": "segment_property_7_value",
        "segment_property_8_value": "segment_property_8_value",
        "segment_property_9_value": "segment_property_9_value",
        "segment_property_10_value": "segment_property_10_value",
    }

    _optionals = [
        "segment_property_1_value",
        "segment_property_2_value",
        "segment_property_3_value",
        "segment_property_4_value",
        "segment_property_5_value",
        "segment_property_6_value",
        "segment_property_7_value",
        "segment_property_8_value",
        "segment_property_9_value",
        "segment_property_10_value",
    ]

    def __init__(
        self,
        pricing_scheme=None,
        prices=None,
        segment_property_1_value=APIHelper.SKIP,
        segment_property_2_value=APIHelper.SKIP,
        segment_property_3_value=APIHelper.SKIP,
        segment_property_4_value=APIHelper.SKIP,
        segment_property_5_value=APIHelper.SKIP,
        segment_property_6_value=APIHelper.SKIP,
        segment_property_7_value=APIHelper.SKIP,
        segment_property_8_value=APIHelper.SKIP,
        segment_property_9_value=APIHelper.SKIP,
        segment_property_10_value=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a SubscriptionComponentCustomPriceSegment instance."""
        # Initialize members of the class
        if segment_property_1_value is not APIHelper.SKIP:
            self.segment_property_1_value = segment_property_1_value
        if segment_property_2_value is not APIHelper.SKIP:
            self.segment_property_2_value = segment_property_2_value
        if segment_property_3_value is not APIHelper.SKIP:
            self.segment_property_3_value = segment_property_3_value
        if segment_property_4_value is not APIHelper.SKIP:
            self.segment_property_4_value = segment_property_4_value
        if segment_property_5_value is not APIHelper.SKIP:
            self.segment_property_5_value = segment_property_5_value
        if segment_property_6_value is not APIHelper.SKIP:
            self.segment_property_6_value = segment_property_6_value
        if segment_property_7_value is not APIHelper.SKIP:
            self.segment_property_7_value = segment_property_7_value
        if segment_property_8_value is not APIHelper.SKIP:
            self.segment_property_8_value = segment_property_8_value
        if segment_property_9_value is not APIHelper.SKIP:
            self.segment_property_9_value = segment_property_9_value
        if segment_property_10_value is not APIHelper.SKIP:
            self.segment_property_10_value = segment_property_10_value
        self.pricing_scheme = pricing_scheme
        self.prices = prices

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Create an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        from advancedbilling.utilities.union_type_lookup import (
            UnionTypeLookUp,
        )

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        pricing_scheme =\
            dictionary.get("pricing_scheme")\
            if dictionary.get("pricing_scheme")\
                else None
        prices = None
        if dictionary.get("prices") is not None:
            prices = [
                CreateOrUpdateSegmentPrice.from_dictionary(x)
                    for x in dictionary.get("prices")
            ]
        segment_property_1_value = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("SubscriptionComponentCustomPriceSegmentSegmentProperty1Value"),
            dictionary.get("segment_property_1_value"),
            False)\
            if dictionary.get("segment_property_1_value") is not None\
            else APIHelper.SKIP
        segment_property_2_value = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("SubscriptionComponentCustomPriceSegmentSegmentProperty2Value"),
            dictionary.get("segment_property_2_value"),
            False)\
            if dictionary.get("segment_property_2_value") is not None\
            else APIHelper.SKIP
        segment_property_3_value = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("SubscriptionComponentCustomPriceSegmentSegmentProperty3Value"),
            dictionary.get("segment_property_3_value"),
            False)\
            if dictionary.get("segment_property_3_value") is not None\
            else APIHelper.SKIP
        segment_property_4_value = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("SubscriptionComponentCustomPriceSegmentSegmentProperty4Value"),
            dictionary.get("segment_property_4_value"),
            False)\
            if dictionary.get("segment_property_4_value") is not None\
            else APIHelper.SKIP
        segment_property_5_value = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("SubscriptionComponentCustomPriceSegmentSegmentProperty5Value"),
            dictionary.get("segment_property_5_value"),
            False)\
            if dictionary.get("segment_property_5_value") is not None\
            else APIHelper.SKIP
        segment_property_6_value = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("SubscriptionComponentCustomPriceSegmentSegmentProperty6Value"),
            dictionary.get("segment_property_6_value"),
            False)\
            if dictionary.get("segment_property_6_value") is not None\
            else APIHelper.SKIP
        segment_property_7_value = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("SubscriptionComponentCustomPriceSegmentSegmentProperty7Value"),
            dictionary.get("segment_property_7_value"),
            False)\
            if dictionary.get("segment_property_7_value") is not None\
            else APIHelper.SKIP
        segment_property_8_value = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("SubscriptionComponentCustomPriceSegmentSegmentProperty8Value"),
            dictionary.get("segment_property_8_value"),
            False)\
            if dictionary.get("segment_property_8_value") is not None\
            else APIHelper.SKIP
        segment_property_9_value = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("SubscriptionComponentCustomPriceSegmentSegmentProperty9Value"),
            dictionary.get("segment_property_9_value"),
            False)\
            if dictionary.get("segment_property_9_value") is not None\
            else APIHelper.SKIP
        segment_property_10_value = APIHelper.deserialize_union_type(
            UnionTypeLookUp.get("SubscriptionComponentCustomPriceSegmentSegmentProperty10Value"),
            dictionary.get("segment_property_10_value"),
            False)\
            if dictionary.get("segment_property_10_value") is not None\
            else APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(pricing_scheme,
                   prices,
                   segment_property_1_value,
                   segment_property_2_value,
                   segment_property_3_value,
                   segment_property_4_value,
                   segment_property_5_value,
                   segment_property_6_value,
                   segment_property_7_value,
                   segment_property_8_value,
                   segment_property_9_value,
                   segment_property_10_value,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validate dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """
        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(
                    value=dictionary.pricing_scheme,
                    type_callable=lambda value:
                        PricingScheme.validate(value)) \
                and APIHelper.is_valid_type(
                    value=dictionary.prices,
                    type_callable=lambda value:
                        CreateOrUpdateSegmentPrice.validate(value),
                    is_model_dict=True,
                    is_inner_model_dict=True)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("pricing_scheme"),
                type_callable=lambda value:
                    PricingScheme.validate(value)) \
            and APIHelper.is_valid_type(
                value=dictionary.get("prices"),
                type_callable=lambda value:
                    CreateOrUpdateSegmentPrice.validate(value),
                is_model_dict=True,
                is_inner_model_dict=True)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _segment_property_1_value=(
            self.segment_property_1_value
            if hasattr(self, "segment_property_1_value")
            else None
        )
        _segment_property_2_value=(
            self.segment_property_2_value
            if hasattr(self, "segment_property_2_value")
            else None
        )
        _segment_property_3_value=(
            self.segment_property_3_value
            if hasattr(self, "segment_property_3_value")
            else None
        )
        _segment_property_4_value=(
            self.segment_property_4_value
            if hasattr(self, "segment_property_4_value")
            else None
        )
        _segment_property_5_value=(
            self.segment_property_5_value
            if hasattr(self, "segment_property_5_value")
            else None
        )
        _segment_property_6_value=(
            self.segment_property_6_value
            if hasattr(self, "segment_property_6_value")
            else None
        )
        _segment_property_7_value=(
            self.segment_property_7_value
            if hasattr(self, "segment_property_7_value")
            else None
        )
        _segment_property_8_value=(
            self.segment_property_8_value
            if hasattr(self, "segment_property_8_value")
            else None
        )
        _segment_property_9_value=(
            self.segment_property_9_value
            if hasattr(self, "segment_property_9_value")
            else None
        )
        _segment_property_10_value=(
            self.segment_property_10_value
            if hasattr(self, "segment_property_10_value")
            else None
        )
        _pricing_scheme=self.pricing_scheme
        _prices=self.prices
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"segment_property_1_value={_segment_property_1_value!r}, "
            f"segment_property_2_value={_segment_property_2_value!r}, "
            f"segment_property_3_value={_segment_property_3_value!r}, "
            f"segment_property_4_value={_segment_property_4_value!r}, "
            f"segment_property_5_value={_segment_property_5_value!r}, "
            f"segment_property_6_value={_segment_property_6_value!r}, "
            f"segment_property_7_value={_segment_property_7_value!r}, "
            f"segment_property_8_value={_segment_property_8_value!r}, "
            f"segment_property_9_value={_segment_property_9_value!r}, "
            f"segment_property_10_value={_segment_property_10_value!r}, "
            f"pricing_scheme={_pricing_scheme!r}, "
            f"prices={_prices!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _segment_property_1_value=(
            self.segment_property_1_value
            if hasattr(self, "segment_property_1_value")
            else None
        )
        _segment_property_2_value=(
            self.segment_property_2_value
            if hasattr(self, "segment_property_2_value")
            else None
        )
        _segment_property_3_value=(
            self.segment_property_3_value
            if hasattr(self, "segment_property_3_value")
            else None
        )
        _segment_property_4_value=(
            self.segment_property_4_value
            if hasattr(self, "segment_property_4_value")
            else None
        )
        _segment_property_5_value=(
            self.segment_property_5_value
            if hasattr(self, "segment_property_5_value")
            else None
        )
        _segment_property_6_value=(
            self.segment_property_6_value
            if hasattr(self, "segment_property_6_value")
            else None
        )
        _segment_property_7_value=(
            self.segment_property_7_value
            if hasattr(self, "segment_property_7_value")
            else None
        )
        _segment_property_8_value=(
            self.segment_property_8_value
            if hasattr(self, "segment_property_8_value")
            else None
        )
        _segment_property_9_value=(
            self.segment_property_9_value
            if hasattr(self, "segment_property_9_value")
            else None
        )
        _segment_property_10_value=(
            self.segment_property_10_value
            if hasattr(self, "segment_property_10_value")
            else None
        )
        _pricing_scheme=self.pricing_scheme
        _prices=self.prices
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"segment_property_1_value={_segment_property_1_value!s}, "
            f"segment_property_2_value={_segment_property_2_value!s}, "
            f"segment_property_3_value={_segment_property_3_value!s}, "
            f"segment_property_4_value={_segment_property_4_value!s}, "
            f"segment_property_5_value={_segment_property_5_value!s}, "
            f"segment_property_6_value={_segment_property_6_value!s}, "
            f"segment_property_7_value={_segment_property_7_value!s}, "
            f"segment_property_8_value={_segment_property_8_value!s}, "
            f"segment_property_9_value={_segment_property_9_value!s}, "
            f"segment_property_10_value={_segment_property_10_value!s}, "
            f"pricing_scheme={_pricing_scheme!s}, "
            f"prices={_prices!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
