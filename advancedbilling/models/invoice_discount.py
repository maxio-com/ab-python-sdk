# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_discount_breakout import InvoiceDiscountBreakout


class InvoiceDiscount(object):

    """Implementation of the 'Invoice Discount' model.

    TODO: type model description here.

    Attributes:
        uid (str): TODO: type description here.
        title (str): TODO: type description here.
        description (str): TODO: type description here.
        code (str): TODO: type description here.
        source_type (InvoiceDiscountSourceType): TODO: type description here.
        source_id (int): TODO: type description here.
        discount_type (InvoiceDiscountType): TODO: type description here.
        percentage (str): TODO: type description here.
        eligible_amount (str): TODO: type description here.
        discount_amount (str): TODO: type description here.
        transaction_id (int): TODO: type description here.
        line_item_breakouts (List[InvoiceDiscountBreakout]): TODO: type
            description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "title": 'title',
        "description": 'description',
        "code": 'code',
        "source_type": 'source_type',
        "source_id": 'source_id',
        "discount_type": 'discount_type',
        "percentage": 'percentage',
        "eligible_amount": 'eligible_amount',
        "discount_amount": 'discount_amount',
        "transaction_id": 'transaction_id',
        "line_item_breakouts": 'line_item_breakouts'
    }

    _optionals = [
        'uid',
        'title',
        'description',
        'code',
        'source_type',
        'source_id',
        'discount_type',
        'percentage',
        'eligible_amount',
        'discount_amount',
        'transaction_id',
        'line_item_breakouts',
    ]

    _nullables = [
        'description',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 title=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 code=APIHelper.SKIP,
                 source_type=APIHelper.SKIP,
                 source_id=APIHelper.SKIP,
                 discount_type=APIHelper.SKIP,
                 percentage=APIHelper.SKIP,
                 eligible_amount=APIHelper.SKIP,
                 discount_amount=APIHelper.SKIP,
                 transaction_id=APIHelper.SKIP,
                 line_item_breakouts=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the InvoiceDiscount class"""

        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid 
        if title is not APIHelper.SKIP:
            self.title = title 
        if description is not APIHelper.SKIP:
            self.description = description 
        if code is not APIHelper.SKIP:
            self.code = code 
        if source_type is not APIHelper.SKIP:
            self.source_type = source_type 
        if source_id is not APIHelper.SKIP:
            self.source_id = source_id 
        if discount_type is not APIHelper.SKIP:
            self.discount_type = discount_type 
        if percentage is not APIHelper.SKIP:
            self.percentage = percentage 
        if eligible_amount is not APIHelper.SKIP:
            self.eligible_amount = eligible_amount 
        if discount_amount is not APIHelper.SKIP:
            self.discount_amount = discount_amount 
        if transaction_id is not APIHelper.SKIP:
            self.transaction_id = transaction_id 
        if line_item_breakouts is not APIHelper.SKIP:
            self.line_item_breakouts = line_item_breakouts 

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
        uid = dictionary.get("uid") if dictionary.get("uid") else APIHelper.SKIP
        title = dictionary.get("title") if dictionary.get("title") else APIHelper.SKIP
        description = dictionary.get("description") if "description" in dictionary.keys() else APIHelper.SKIP
        code = dictionary.get("code") if dictionary.get("code") else APIHelper.SKIP
        source_type = dictionary.get("source_type") if dictionary.get("source_type") else APIHelper.SKIP
        source_id = dictionary.get("source_id") if dictionary.get("source_id") else APIHelper.SKIP
        discount_type = dictionary.get("discount_type") if dictionary.get("discount_type") else APIHelper.SKIP
        percentage = dictionary.get("percentage") if dictionary.get("percentage") else APIHelper.SKIP
        eligible_amount = dictionary.get("eligible_amount") if dictionary.get("eligible_amount") else APIHelper.SKIP
        discount_amount = dictionary.get("discount_amount") if dictionary.get("discount_amount") else APIHelper.SKIP
        transaction_id = dictionary.get("transaction_id") if dictionary.get("transaction_id") else APIHelper.SKIP
        line_item_breakouts = None
        if dictionary.get('line_item_breakouts') is not None:
            line_item_breakouts = [InvoiceDiscountBreakout.from_dictionary(x) for x in dictionary.get('line_item_breakouts')]
        else:
            line_item_breakouts = APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(uid,
                   title,
                   description,
                   code,
                   source_type,
                   source_id,
                   discount_type,
                   percentage,
                   eligible_amount,
                   discount_amount,
                   transaction_id,
                   line_item_breakouts,
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
            return True

        if not isinstance(dictionary, dict):
            return False

        return True
