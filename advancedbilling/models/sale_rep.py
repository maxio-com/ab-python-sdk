# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.sale_rep_subscription import SaleRepSubscription


class SaleRep(object):

    """Implementation of the 'Sale Rep' model.

    Attributes:
        id (int): The model property of type int.
        full_name (str): The model property of type str.
        subscriptions_count (int): The model property of type int.
        test_mode (bool): The model property of type bool.
        subscriptions (List[SaleRepSubscription]): The model property of type
            List[SaleRepSubscription].
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "id": 'id',
        "full_name": 'full_name',
        "subscriptions_count": 'subscriptions_count',
        "test_mode": 'test_mode',
        "subscriptions": 'subscriptions'
    }

    _optionals = [
        'id',
        'full_name',
        'subscriptions_count',
        'test_mode',
        'subscriptions',
    ]

    def __init__(self,
                 id=APIHelper.SKIP,
                 full_name=APIHelper.SKIP,
                 subscriptions_count=APIHelper.SKIP,
                 test_mode=APIHelper.SKIP,
                 subscriptions=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the SaleRep class"""

        # Initialize members of the class
        if id is not APIHelper.SKIP:
            self.id = id 
        if full_name is not APIHelper.SKIP:
            self.full_name = full_name 
        if subscriptions_count is not APIHelper.SKIP:
            self.subscriptions_count = subscriptions_count 
        if test_mode is not APIHelper.SKIP:
            self.test_mode = test_mode 
        if subscriptions is not APIHelper.SKIP:
            self.subscriptions = subscriptions 

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
        id = dictionary.get("id") if dictionary.get("id") else APIHelper.SKIP
        full_name = dictionary.get("full_name") if dictionary.get("full_name") else APIHelper.SKIP
        subscriptions_count = dictionary.get("subscriptions_count") if dictionary.get("subscriptions_count") else APIHelper.SKIP
        test_mode = dictionary.get("test_mode") if "test_mode" in dictionary.keys() else APIHelper.SKIP
        subscriptions = None
        if dictionary.get('subscriptions') is not None:
            subscriptions = [SaleRepSubscription.from_dictionary(x) for x in dictionary.get('subscriptions')]
        else:
            subscriptions = APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(id,
                   full_name,
                   subscriptions_count,
                   test_mode,
                   subscriptions,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!r}, '
                f'full_name={self.full_name!r}, '
                f'subscriptions_count={self.subscriptions_count!r}, '
                f'test_mode={self.test_mode!r}, '
                f'subscriptions={self.subscriptions!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'id={self.id!s}, '
                f'full_name={self.full_name!s}, '
                f'subscriptions_count={self.subscriptions_count!s}, '
                f'test_mode={self.test_mode!s}, '
                f'subscriptions={self.subscriptions!s}, '
                f'additional_properties={self.additional_properties!s})')
