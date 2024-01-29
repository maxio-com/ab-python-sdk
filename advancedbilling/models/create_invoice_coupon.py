# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateInvoiceCoupon(object):

    """Implementation of the 'Create Invoice Coupon' model.

    TODO: type model description here.

    Attributes:
        code (str): TODO: type description here.
        percentage (str | float | None): TODO: type description here.
        amount (str | float | None): TODO: type description here.
        description (str): TODO: type description here.
        product_family_id (str | int | None): TODO: type description here.
        compounding_strategy (CompoundingStrategy): TODO: type description
            here.

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
                 compounding_strategy=APIHelper.SKIP):
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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        code = dictionary.get("code") if dictionary.get("code") else APIHelper.SKIP
        percentage = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateInvoiceCouponPercentage'), dictionary.get('percentage'), False) if dictionary.get('percentage') is not None else APIHelper.SKIP
        amount = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateInvoiceCouponAmount'), dictionary.get('amount'), False) if dictionary.get('amount') is not None else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        product_family_id = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateInvoiceCouponProductFamilyId'), dictionary.get('product_family_id'), False) if dictionary.get('product_family_id') is not None else APIHelper.SKIP
        compounding_strategy = dictionary.get("compounding_strategy") if dictionary.get("compounding_strategy") else APIHelper.SKIP
        # Return an object of this model
        return cls(code,
                   percentage,
                   amount,
                   description,
                   product_family_id,
                   compounding_strategy)
