"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
from advancedbilling.api_helper import APIHelper


class SubscriptionProductChangeScheduled(object):
    """Implementation of the 'Subscription Product Change Scheduled' model.

    Attributes:
        previous_product_id (int): The model property of type int.
        new_product_id (int): The model property of type int.
        previous_product_price_point_id (int): The model property of type int.
        new_product_price_point_id (int): The model property of type int.
        effective_at (datetime): When the scheduled product change takes effect (the
            subscription's next renewal).
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "previous_product_id": "previous_product_id",
        "new_product_id": "new_product_id",
        "previous_product_price_point_id": "previous_product_price_point_id",
        "new_product_price_point_id": "new_product_price_point_id",
        "effective_at": "effective_at",
    }

    _optionals = [
        "previous_product_price_point_id",
        "new_product_price_point_id",
        "effective_at",
    ]

    _nullables = [
        "previous_product_price_point_id",
        "new_product_price_point_id",
        "effective_at",
    ]

    def __init__(
        self,
        previous_product_id=None,
        new_product_id=None,
        previous_product_price_point_id=APIHelper.SKIP,
        new_product_price_point_id=APIHelper.SKIP,
        effective_at=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a SubscriptionProductChangeScheduled instance."""
        # Initialize members of the class
        self.previous_product_id = previous_product_id
        self.new_product_id = new_product_id
        if previous_product_price_point_id is not APIHelper.SKIP:
            self.previous_product_price_point_id = previous_product_price_point_id
        if new_product_price_point_id is not APIHelper.SKIP:
            self.new_product_price_point_id = new_product_price_point_id
        if effective_at is not APIHelper.SKIP:
            self.effective_at =\
                 APIHelper.apply_datetime_converter(
                effective_at, APIHelper.RFC3339DateTime)\
                 if effective_at else None

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
        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        previous_product_id =\
            dictionary.get("previous_product_id")\
            if dictionary.get("previous_product_id")\
                else None
        new_product_id =\
            dictionary.get("new_product_id")\
            if dictionary.get("new_product_id")\
                else None
        previous_product_price_point_id =\
            dictionary.get("previous_product_price_point_id")\
            if "previous_product_price_point_id" in dictionary.keys()\
                else APIHelper.SKIP
        new_product_price_point_id =\
            dictionary.get("new_product_price_point_id")\
            if "new_product_price_point_id" in dictionary.keys()\
                else APIHelper.SKIP
        if "effective_at" in dictionary.keys():
            effective_at = APIHelper.RFC3339DateTime.from_value(
                dictionary.get("effective_at")).datetime\
                if dictionary.get("effective_at") else None

        else:
            effective_at = APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(previous_product_id,
                   new_product_id,
                   previous_product_price_point_id,
                   new_product_price_point_id,
                   effective_at,
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
                    value=dictionary.previous_product_id,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        int,
                )) \
                and APIHelper.is_valid_type(
                    value=dictionary.new_product_id,
                    type_callable=lambda value:
                        isinstance(
                        value,
                        int,
                ))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(
                value=dictionary.get("previous_product_id"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    int,
            )) \
            and APIHelper.is_valid_type(
                value=dictionary.get("new_product_id"),
                type_callable=lambda value:
                    isinstance(
                    value,
                    int,
            ))

    def __repr__(self):
        """Return a unambiguous string representation."""
        _previous_product_id=self.previous_product_id
        _new_product_id=self.new_product_id
        _previous_product_price_point_id=(
            self.previous_product_price_point_id
            if hasattr(self, "previous_product_price_point_id")
            else None
        )
        _new_product_price_point_id=(
            self.new_product_price_point_id
            if hasattr(self, "new_product_price_point_id")
            else None
        )
        _effective_at=(
            self.effective_at
            if hasattr(self, "effective_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"previous_product_id={_previous_product_id!r}, "
            f"new_product_id={_new_product_id!r}, "
            f"previous_product_price_point_id={_previous_product_price_point_id!r}, "
            f"new_product_price_point_id={_new_product_price_point_id!r}, "
            f"effective_at={_effective_at!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _previous_product_id=self.previous_product_id
        _new_product_id=self.new_product_id
        _previous_product_price_point_id=(
            self.previous_product_price_point_id
            if hasattr(self, "previous_product_price_point_id")
            else None
        )
        _new_product_price_point_id=(
            self.new_product_price_point_id
            if hasattr(self, "new_product_price_point_id")
            else None
        )
        _effective_at=(
            self.effective_at
            if hasattr(self, "effective_at")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"previous_product_id={_previous_product_id!s}, "
            f"new_product_id={_new_product_id!s}, "
            f"previous_product_price_point_id={_previous_product_price_point_id!s}, "
            f"new_product_price_point_id={_new_product_price_point_id!s}, "
            f"effective_at={_effective_at!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
