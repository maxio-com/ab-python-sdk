# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class ChangeInvoiceCollectionMethodEventData(object):

    """Implementation of the 'Change Invoice Collection Method Event Data' model.

    Example schema for an `change_invoice_collection_method` event

    Attributes:
        from_collection_method (str): The previous collection method of the
            invoice.
        to_collection_method (str): The new collection method of the invoice.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "from_collection_method": 'from_collection_method',
        "to_collection_method": 'to_collection_method'
    }

    def __init__(self,
                 from_collection_method=None,
                 to_collection_method=None,
                 additional_properties=None):
        """Constructor for the ChangeInvoiceCollectionMethodEventData class"""

        # Initialize members of the class
        self.from_collection_method = from_collection_method 
        self.to_collection_method = to_collection_method 

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        from_collection_method = dictionary.get("from_collection_method") if dictionary.get("from_collection_method") else None
        to_collection_method = dictionary.get("to_collection_method") if dictionary.get("to_collection_method") else None
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(from_collection_method,
                   to_collection_method,
                   additional_properties)

    @classmethod
    def validate(cls, dictionary):
        """Validates dictionary against class required properties

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            boolean : if dictionary is valid contains required properties.

        """

        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(value=dictionary.from_collection_method,
                                           type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.to_collection_method,
                                            type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('from_collection_method'),
                                       type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('to_collection_method'),
                                        type_callable=lambda value: isinstance(value, str))
