# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateInvoiceCoupon(object):

    """Implementation of the 'Create Invoice Coupon' model.

    Attributes:
        code (str): The model property of type str.
        percentage (str | float | None): The model property of type str |
            float | None.
        amount (str | float | None): The model property of type str | float |
            None.
        description (str): The model property of type str.
        product_family_id (str | int | None): The model property of type str |
            int | None.
        compounding_strategy (CompoundingStrategy): Applicable only to
            stackable coupons. For `compound`, Percentage-based discounts will
            be calculated against the remaining price, after prior discounts
            have been calculated. For `full-price`, Percentage-based discounts
            will always be calculated against the original item price, before
            other discounts are applied.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'code',
        "percentage": 'percentage',
        "amount": 'amount',
        "description": 'description',
        "product_family_id": 'product_family_id',
        "compounding_strategy": 'compounding_strategy'
    }

    _optionals = [
        'code',
        'percentage',
        'amount',
        'description',
        'product_family_id',
        'compounding_strategy',
    ]

    def __init__(self,
                 code=APIHelper.SKIP,
                 percentage=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 product_family_id=APIHelper.SKIP,
                 compounding_strategy=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CreateInvoiceCoupon class"""

        # Initialize members of the class
        if code is not APIHelper.SKIP:
            self.code = code 
        if percentage is not APIHelper.SKIP:
            self.percentage = percentage 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if description is not APIHelper.SKIP:
            self.description = description 
        if product_family_id is not APIHelper.SKIP:
            self.product_family_id = product_family_id 
        if compounding_strategy is not APIHelper.SKIP:
            self.compounding_strategy = compounding_strategy 

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
        code = dictionary.get("code") if dictionary.get("code") else APIHelper.SKIP
        percentage = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateInvoiceCouponPercentage'), dictionary.get('percentage'), False) if dictionary.get('percentage') is not None else APIHelper.SKIP
        amount = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateInvoiceCouponAmount'), dictionary.get('amount'), False) if dictionary.get('amount') is not None else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        product_family_id = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateInvoiceCouponProductFamilyId'), dictionary.get('product_family_id'), False) if dictionary.get('product_family_id') is not None else APIHelper.SKIP
        compounding_strategy = dictionary.get("compounding_strategy") if dictionary.get("compounding_strategy") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(code,
                   percentage,
                   amount,
                   description,
                   product_family_id,
                   compounding_strategy,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'code={self.code!r}, '
                f'percentage={self.percentage!r}, '
                f'amount={self.amount!r}, '
                f'description={self.description!r}, '
                f'product_family_id={self.product_family_id!r}, '
                f'compounding_strategy={self.compounding_strategy!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'code={self.code!s}, '
                f'percentage={self.percentage!s}, '
                f'amount={self.amount!s}, '
                f'description={self.description!s}, '
                f'product_family_id={self.product_family_id!s}, '
                f'compounding_strategy={self.compounding_strategy!s}, '
                f'additional_properties={self.additional_properties!s})')
