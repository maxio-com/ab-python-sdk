# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateOrUpdateFlatAmountCoupon(object):

    """Implementation of the 'Create or Update Flat Amount Coupon' model.

    TODO: type model description here.

    Attributes:
        name (str): the name of the coupon
        code (str): may contain uppercase alphanumeric characters and these
            special characters (which allow for email addresses to be used):
            “%”, “@”, “+”, “-”, “_”, and “.”
        description (str): TODO: type description here.
        amount_in_cents (long|int): TODO: type description here.
        allow_negative_balance (str): TODO: type description here.
        recurring (str): TODO: type description here.
        end_date (str): TODO: type description here.
        product_family_id (str): TODO: type description here.
        stackable (str): TODO: type description here.
        compounding_strategy (CompoundingStrategy | None): TODO: type
            description here.
        exclude_mid_period_allocations (bool): TODO: type description here.
        apply_on_cancel_at_end_of_period (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "code": 'code',
        "amount_in_cents": 'amount_in_cents',
        "description": 'description',
        "allow_negative_balance": 'allow_negative_balance',
        "recurring": 'recurring',
        "end_date": 'end_date',
        "product_family_id": 'product_family_id',
        "stackable": 'stackable',
        "compounding_strategy": 'compounding_strategy',
        "exclude_mid_period_allocations": 'exclude_mid_period_allocations',
        "apply_on_cancel_at_end_of_period": 'apply_on_cancel_at_end_of_period'
    }

    _optionals = [
        'description',
        'allow_negative_balance',
        'recurring',
        'end_date',
        'product_family_id',
        'stackable',
        'compounding_strategy',
        'exclude_mid_period_allocations',
        'apply_on_cancel_at_end_of_period',
    ]

    def __init__(self,
                 name=None,
                 code=None,
                 amount_in_cents=None,
                 description=APIHelper.SKIP,
                 allow_negative_balance=APIHelper.SKIP,
                 recurring=APIHelper.SKIP,
                 end_date=APIHelper.SKIP,
                 product_family_id=APIHelper.SKIP,
                 stackable=APIHelper.SKIP,
                 compounding_strategy=APIHelper.SKIP,
                 exclude_mid_period_allocations=APIHelper.SKIP,
                 apply_on_cancel_at_end_of_period=APIHelper.SKIP):
        """Constructor for the CreateOrUpdateFlatAmountCoupon class"""

        # Initialize members of the class
        self.name = name 
        self.code = code 
        if description is not APIHelper.SKIP:
            self.description = description 
        self.amount_in_cents = amount_in_cents 
        if allow_negative_balance is not APIHelper.SKIP:
            self.allow_negative_balance = allow_negative_balance 
        if recurring is not APIHelper.SKIP:
            self.recurring = recurring 
        if end_date is not APIHelper.SKIP:
            self.end_date = end_date 
        if product_family_id is not APIHelper.SKIP:
            self.product_family_id = product_family_id 
        if stackable is not APIHelper.SKIP:
            self.stackable = stackable 
        if compounding_strategy is not APIHelper.SKIP:
            self.compounding_strategy = compounding_strategy 
        if exclude_mid_period_allocations is not APIHelper.SKIP:
            self.exclude_mid_period_allocations = exclude_mid_period_allocations 
        if apply_on_cancel_at_end_of_period is not APIHelper.SKIP:
            self.apply_on_cancel_at_end_of_period = apply_on_cancel_at_end_of_period 

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
        name = dictionary.get("name") if dictionary.get("name") else None
        code = dictionary.get("code") if dictionary.get("code") else None
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else None
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        allow_negative_balance = dictionary.get("allow_negative_balance") if dictionary.get("allow_negative_balance") else APIHelper.SKIP
        recurring = dictionary.get("recurring") if dictionary.get("recurring") else APIHelper.SKIP
        end_date = dictionary.get("end_date") if dictionary.get("end_date") else APIHelper.SKIP
        product_family_id = dictionary.get("product_family_id") if dictionary.get("product_family_id") else APIHelper.SKIP
        stackable = dictionary.get("stackable") if dictionary.get("stackable") else APIHelper.SKIP
        compounding_strategy = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateOrUpdateFlatAmountCouponCompoundingStrategy'), dictionary.get('compounding_strategy'), False) if dictionary.get('compounding_strategy') is not None else APIHelper.SKIP
        exclude_mid_period_allocations = dictionary.get("exclude_mid_period_allocations") if "exclude_mid_period_allocations" in dictionary.keys() else APIHelper.SKIP
        apply_on_cancel_at_end_of_period = dictionary.get("apply_on_cancel_at_end_of_period") if "apply_on_cancel_at_end_of_period" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   code,
                   amount_in_cents,
                   description,
                   allow_negative_balance,
                   recurring,
                   end_date,
                   product_family_id,
                   stackable,
                   compounding_strategy,
                   exclude_mid_period_allocations,
                   apply_on_cancel_at_end_of_period)

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
            return APIHelper.is_valid_type(value=dictionary.name, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.code, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.amount_in_cents, type_callable=lambda value: isinstance(value, int))

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('name'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('code'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('amount_in_cents'), type_callable=lambda value: isinstance(value, int))
