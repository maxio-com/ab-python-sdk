"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
class SendEmail(object):
    """Implementation of the 'SendEmail' model.

    Attributes:
        can_execute (bool): The model property of type bool.
        url (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "can_execute": "can_execute",
        "url": "url",
    }

    def __init__(
        self,
        can_execute=None,
        url=None,
        additional_properties=None):
        """Initialize a SendEmail instance."""
        # Initialize members of the class
        self.can_execute = can_execute
        self.url = url

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
        can_execute =\
            dictionary.get("can_execute")\
            if "can_execute" in dictionary.keys()\
                else None
        url =\
            dictionary.get("url")\
            if dictionary.get("url")\
                else None

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(can_execute,
                   url,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _can_execute=self.can_execute
        _url=self.url
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"can_execute={_can_execute!r}, "
            f"url={_url!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _can_execute=self.can_execute
        _url=self.url
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"can_execute={_can_execute!s}, "
            f"url={_url!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
