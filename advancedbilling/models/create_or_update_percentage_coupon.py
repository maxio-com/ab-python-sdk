# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateOrUpdatePercentageCoupon(object):

    """Implementation of the 'Create or Update Percentage Coupon' model.

    TODO: type model description here.

    Attributes:
        name (str): the name of the coupon
        code (str): may contain uppercase alphanumeric characters and these
            special characters (which allow for email addresses to be used):
            “%”, “@”, “+”, “-”, “_”, and “.”
        description (str): TODO: type description here.
        percentage (float | str): TODO: type description here.
        allow_negative_balance (bool): TODO: type description here.
        recurring (bool): TODO: type description here.
        end_date (datetime): TODO: type description here.
        product_family_id (str): TODO: type description here.
        stackable (bool): TODO: type description here.
        compounding_strategy (CompoundingStrategy): TODO: type description
            here.
        exclude_mid_period_allocations (bool): TODO: type description here.
        apply_on_cancel_at_end_of_period (bool): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "name": 'name',
        "code": 'code',
        "percentage": 'percentage',
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
                 percentage=None,
                 description=APIHelper.SKIP,
                 allow_negative_balance=APIHelper.SKIP,
                 recurring=APIHelper.SKIP,
                 end_date=APIHelper.SKIP,
                 product_family_id=APIHelper.SKIP,
                 stackable=APIHelper.SKIP,
                 compounding_strategy=APIHelper.SKIP,
                 exclude_mid_period_allocations=APIHelper.SKIP,
                 apply_on_cancel_at_end_of_period=APIHelper.SKIP):
        """Constructor for the CreateOrUpdatePercentageCoupon class"""

        # Initialize members of the class
        self.name = name 
        self.code = code 
        if description is not APIHelper.SKIP:
            self.description = description 
        self.percentage = percentage 
        if allow_negative_balance is not APIHelper.SKIP:
            self.allow_negative_balance = allow_negative_balance 
        if recurring is not APIHelper.SKIP:
            self.recurring = recurring 
        if end_date is not APIHelper.SKIP:
            self.end_date = APIHelper.apply_datetime_converter(end_date, APIHelper.RFC3339DateTime) if end_date else None 
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
        percentage = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateOrUpdatePercentageCouponPercentage'), dictionary.get('percentage'), False) if dictionary.get('percentage') is not None else None
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        allow_negative_balance = dictionary.get("allow_negative_balance") if "allow_negative_balance" in dictionary.keys() else APIHelper.SKIP
        recurring = dictionary.get("recurring") if "recurring" in dictionary.keys() else APIHelper.SKIP
        end_date = APIHelper.RFC3339DateTime.from_value(dictionary.get("end_date")).datetime if dictionary.get("end_date") else APIHelper.SKIP
        product_family_id = dictionary.get("product_family_id") if dictionary.get("product_family_id") else APIHelper.SKIP
        stackable = dictionary.get("stackable") if "stackable" in dictionary.keys() else APIHelper.SKIP
        compounding_strategy = dictionary.get("compounding_strategy") if dictionary.get("compounding_strategy") else APIHelper.SKIP
        exclude_mid_period_allocations = dictionary.get("exclude_mid_period_allocations") if "exclude_mid_period_allocations" in dictionary.keys() else APIHelper.SKIP
        apply_on_cancel_at_end_of_period = dictionary.get("apply_on_cancel_at_end_of_period") if "apply_on_cancel_at_end_of_period" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(name,
                   code,
                   percentage,
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
        from advancedbilling.utilities.union_type_lookup import UnionTypeLookUp
        if isinstance(dictionary, cls):
            return APIHelper.is_valid_type(value=dictionary.name, type_callable=lambda value: isinstance(value, str)) \
                and APIHelper.is_valid_type(value=dictionary.code, type_callable=lambda value: isinstance(value, str)) \
                and UnionTypeLookUp.get('CreateOrUpdatePercentageCouponPercentage').validate(dictionary.percentage)

        if not isinstance(dictionary, dict):
            return False

        return APIHelper.is_valid_type(value=dictionary.get('name'), type_callable=lambda value: isinstance(value, str)) \
            and APIHelper.is_valid_type(value=dictionary.get('code'), type_callable=lambda value: isinstance(value, str)) \
            and UnionTypeLookUp.get('CreateOrUpdatePercentageCouponPercentage').validate(dictionary.get('percentage'))
