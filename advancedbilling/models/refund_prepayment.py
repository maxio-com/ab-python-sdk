# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class RefundPrepayment(object):

    """Implementation of the 'Refund Prepayment' model.

    Attributes:
        amount_in_cents (int): `amount` is not required if you pass
            `amount_in_cents`.
        amount (str | float): `amount_in_cents` is not required if you pass
            `amount`.
        memo (str): The model property of type str.
        external (bool): Specify the type of refund you wish to initiate. When
            the prepayment is external, the `external` flag is optional. But
            if the prepayment was made through a payment profile, the
            `external` flag is required.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount_in_cents": 'amount_in_cents',
        "amount": 'amount',
        "memo": 'memo',
        "external": 'external'
    }

    _optionals = [
        'external',
    ]

    _nullables = [
        'amount_in_cents',
    ]

    def __init__(self,
                 amount_in_cents=None,
                 amount=None,
                 memo=None,
                 external=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the RefundPrepayment class"""

        # Initialize members of the class
        self.amount_in_cents = amount_in_cents 
        self.amount = amount 
        self.memo = memo 
        if external is not APIHelper.SKIP:
            self.external = external 

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
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else None
        amount = APIHelper.deserialize_union_type(UnionTypeLookUp.get('RefundPrepaymentAmount'), dictionary.get('amount'), False) if dictionary.get('amount') is not None else None
        memo = dictionary.get("memo") if dictionary.get("memo") else None
        external = dictionary.get("external") if "external" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(amount_in_cents,
                   amount,
                   memo,
                   external,
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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp

        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(value=dictionary.amount_in_cents,
                                           type_callable=lambda value: isinstance(value, int),
                                           is_value_nullable=True) \
                and UnionTypeLookUp.get('RefundPrepaymentAmount').validate(dictionary.amount).is_valid \
                and APIHelper.is_valid_type(value=dictionary.memo,
                                            type_callable=lambda value: isinstance(value, str))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('amount_in_cents'),
                                       type_callable=lambda value: isinstance(value, int),
                                       is_value_nullable=True) \
            and UnionTypeLookUp.get('RefundPrepaymentAmount').validate(dictionary.get('amount')).is_valid \
            and APIHelper.is_valid_type(value=dictionary.get('memo'),
                                        type_callable=lambda value: isinstance(value, str))

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'amount_in_cents={self.amount_in_cents!r}, '
                f'amount={self.amount!r}, '
                f'memo={self.memo!r}, '
                f'external={(self.external if hasattr(self, "external") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'amount_in_cents={self.amount_in_cents!s}, '
                f'amount={self.amount!s}, '
                f'memo={self.memo!s}, '
                f'external={(self.external if hasattr(self, "external") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
