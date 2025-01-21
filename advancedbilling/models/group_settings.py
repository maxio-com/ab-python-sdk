# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.group_billing import GroupBilling
from advancedbilling.models.group_target import GroupTarget


class GroupSettings(object):

    """Implementation of the 'Group Settings' model.

    Attributes:
        target (GroupTarget): Attributes of the target customer who will be
            the responsible payer of the created subscription. Required.
        billing (GroupBilling): Optional attributes related to billing date
            and accrual. Note: Only applicable for new subscriptions.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "target": 'target',
        "billing": 'billing'
    }

    _optionals = [
        'billing',
    ]

    def __init__(self,
                 target=None,
                 billing=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the GroupSettings class"""

        # Initialize members of the class
        self.target = target 
        if billing is not APIHelper.SKIP:
            self.billing = billing 

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
        target = GroupTarget.from_dictionary(dictionary.get('target')) if dictionary.get('target') else None
        billing = GroupBilling.from_dictionary(dictionary.get('billing')) if 'billing' in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(target,
                   billing,
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
            return APIHelper.is_valid_type(value=dictionary.target,
                                           type_callable=lambda value: GroupTarget.validate(value),
                                           is_model_dict=True)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('target'),
                                       type_callable=lambda value: GroupTarget.validate(value),
                                       is_model_dict=True)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'target={self.target!r}, '
                f'billing={self.billing!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'target={self.target!s}, '
                f'billing={self.billing!s}, '
                f'additional_properties={self.additional_properties!s})')
