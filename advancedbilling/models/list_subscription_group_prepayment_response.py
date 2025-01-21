# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.models.list_subscription_group_prepayment import ListSubscriptionGroupPrepayment


class ListSubscriptionGroupPrepaymentResponse(object):

    """Implementation of the 'List Subscription Group Prepayment Response' model.

    Attributes:
        prepayments (List[ListSubscriptionGroupPrepayment]): The model
            property of type List[ListSubscriptionGroupPrepayment].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "prepayments": 'prepayments'
    }

    def __init__(self,
                 prepayments=None,
                 additional_properties=None):
        """Constructor for the ListSubscriptionGroupPrepaymentResponse class"""

        # Initialize members of the class
        self.prepayments = prepayments 

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
        prepayments = None
        if dictionary.get('prepayments') is not None:
            prepayments = [ListSubscriptionGroupPrepayment.from_dictionary(x) for x in dictionary.get('prepayments')]
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(prepayments,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'prepayments={self.prepayments!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'prepayments={self.prepayments!s}, '
                f'additional_properties={self.additional_properties!s})')
