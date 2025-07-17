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

    Attributes:
        uid (str): The model property of type str.
        title (str): The model property of type str.
        description (str): The model property of type str.
        code (str): The model property of type str.
        source_type (InvoiceDiscountSourceType): The model property of type
            InvoiceDiscountSourceType.
        source_id (int): The model property of type int.
        discount_type (InvoiceDiscountType): The model property of type
            InvoiceDiscountType.
        percentage (str): The model property of type str.
        eligible_amount (str): The model property of type str.
        discount_amount (str): The model property of type str.
        transaction_id (int): The model property of type int.
        line_item_breakouts (List[InvoiceDiscountBreakout]): The model
            property of type List[InvoiceDiscountBreakout].
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

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'uid={(self.uid if hasattr(self, "uid") else None)!r}, '
                f'title={(self.title if hasattr(self, "title") else None)!r}, '
                f'description={(self.description if hasattr(self, "description") else None)!r}, '
                f'code={(self.code if hasattr(self, "code") else None)!r}, '
                f'source_type={(self.source_type if hasattr(self, "source_type") else None)!r}, '
                f'source_id={(self.source_id if hasattr(self, "source_id") else None)!r}, '
                f'discount_type={(self.discount_type if hasattr(self, "discount_type") else None)!r}, '
                f'percentage={(self.percentage if hasattr(self, "percentage") else None)!r}, '
                f'eligible_amount={(self.eligible_amount if hasattr(self, "eligible_amount") else None)!r}, '
                f'discount_amount={(self.discount_amount if hasattr(self, "discount_amount") else None)!r}, '
                f'transaction_id={(self.transaction_id if hasattr(self, "transaction_id") else None)!r}, '
                f'line_item_breakouts={(self.line_item_breakouts if hasattr(self, "line_item_breakouts") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'uid={(self.uid if hasattr(self, "uid") else None)!s}, '
                f'title={(self.title if hasattr(self, "title") else None)!s}, '
                f'description={(self.description if hasattr(self, "description") else None)!s}, '
                f'code={(self.code if hasattr(self, "code") else None)!s}, '
                f'source_type={(self.source_type if hasattr(self, "source_type") else None)!s}, '
                f'source_id={(self.source_id if hasattr(self, "source_id") else None)!s}, '
                f'discount_type={(self.discount_type if hasattr(self, "discount_type") else None)!s}, '
                f'percentage={(self.percentage if hasattr(self, "percentage") else None)!s}, '
                f'eligible_amount={(self.eligible_amount if hasattr(self, "eligible_amount") else None)!s}, '
                f'discount_amount={(self.discount_amount if hasattr(self, "discount_amount") else None)!s}, '
                f'transaction_id={(self.transaction_id if hasattr(self, "transaction_id") else None)!s}, '
                f'line_item_breakouts={(self.line_item_breakouts if hasattr(self, "line_item_breakouts") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
