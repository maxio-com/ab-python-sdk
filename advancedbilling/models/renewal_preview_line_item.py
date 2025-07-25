# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class RenewalPreviewLineItem(object):

    """Implementation of the 'Renewal Preview Line Item' model.

    Attributes:
        transaction_type (LineItemTransactionType): A handle for the line item
            transaction type
        kind (LineItemKind): A handle for the line item kind
        amount_in_cents (int): The model property of type int.
        memo (str): The model property of type str.
        discount_amount_in_cents (int): The model property of type int.
        taxable_amount_in_cents (int): The model property of type int.
        product_id (int): The model property of type int.
        product_name (str): The model property of type str.
        component_id (int): The model property of type int.
        component_handle (str): The model property of type str.
        component_name (str): The model property of type str.
        product_handle (str): The model property of type str.
        period_range_start (str): The model property of type str.
        period_range_end (str): The model property of type str.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "transaction_type": 'transaction_type',
        "kind": 'kind',
        "amount_in_cents": 'amount_in_cents',
        "memo": 'memo',
        "discount_amount_in_cents": 'discount_amount_in_cents',
        "taxable_amount_in_cents": 'taxable_amount_in_cents',
        "product_id": 'product_id',
        "product_name": 'product_name',
        "component_id": 'component_id',
        "component_handle": 'component_handle',
        "component_name": 'component_name',
        "product_handle": 'product_handle',
        "period_range_start": 'period_range_start',
        "period_range_end": 'period_range_end'
    }

    _optionals = [
        'transaction_type',
        'kind',
        'amount_in_cents',
        'memo',
        'discount_amount_in_cents',
        'taxable_amount_in_cents',
        'product_id',
        'product_name',
        'component_id',
        'component_handle',
        'component_name',
        'product_handle',
        'period_range_start',
        'period_range_end',
    ]

    def __init__(self,
                 transaction_type=APIHelper.SKIP,
                 kind=APIHelper.SKIP,
                 amount_in_cents=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 discount_amount_in_cents=APIHelper.SKIP,
                 taxable_amount_in_cents=APIHelper.SKIP,
                 product_id=APIHelper.SKIP,
                 product_name=APIHelper.SKIP,
                 component_id=APIHelper.SKIP,
                 component_handle=APIHelper.SKIP,
                 component_name=APIHelper.SKIP,
                 product_handle=APIHelper.SKIP,
                 period_range_start=APIHelper.SKIP,
                 period_range_end=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the RenewalPreviewLineItem class"""

        # Initialize members of the class
        if transaction_type is not APIHelper.SKIP:
            self.transaction_type = transaction_type 
        if kind is not APIHelper.SKIP:
            self.kind = kind 
        if amount_in_cents is not APIHelper.SKIP:
            self.amount_in_cents = amount_in_cents 
        if memo is not APIHelper.SKIP:
            self.memo = memo 
        if discount_amount_in_cents is not APIHelper.SKIP:
            self.discount_amount_in_cents = discount_amount_in_cents 
        if taxable_amount_in_cents is not APIHelper.SKIP:
            self.taxable_amount_in_cents = taxable_amount_in_cents 
        if product_id is not APIHelper.SKIP:
            self.product_id = product_id 
        if product_name is not APIHelper.SKIP:
            self.product_name = product_name 
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if component_handle is not APIHelper.SKIP:
            self.component_handle = component_handle 
        if component_name is not APIHelper.SKIP:
            self.component_name = component_name 
        if product_handle is not APIHelper.SKIP:
            self.product_handle = product_handle 
        if period_range_start is not APIHelper.SKIP:
            self.period_range_start = period_range_start 
        if period_range_end is not APIHelper.SKIP:
            self.period_range_end = period_range_end 

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
        transaction_type = dictionary.get("transaction_type") if dictionary.get("transaction_type") else APIHelper.SKIP
        kind = dictionary.get("kind") if dictionary.get("kind") else APIHelper.SKIP
        amount_in_cents = dictionary.get("amount_in_cents") if dictionary.get("amount_in_cents") else APIHelper.SKIP
        memo = dictionary.get("memo") if dictionary.get("memo") else APIHelper.SKIP
        discount_amount_in_cents = dictionary.get("discount_amount_in_cents") if dictionary.get("discount_amount_in_cents") else APIHelper.SKIP
        taxable_amount_in_cents = dictionary.get("taxable_amount_in_cents") if dictionary.get("taxable_amount_in_cents") else APIHelper.SKIP
        product_id = dictionary.get("product_id") if dictionary.get("product_id") else APIHelper.SKIP
        product_name = dictionary.get("product_name") if dictionary.get("product_name") else APIHelper.SKIP
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        component_handle = dictionary.get("component_handle") if dictionary.get("component_handle") else APIHelper.SKIP
        component_name = dictionary.get("component_name") if dictionary.get("component_name") else APIHelper.SKIP
        product_handle = dictionary.get("product_handle") if dictionary.get("product_handle") else APIHelper.SKIP
        period_range_start = dictionary.get("period_range_start") if dictionary.get("period_range_start") else APIHelper.SKIP
        period_range_end = dictionary.get("period_range_end") if dictionary.get("period_range_end") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(transaction_type,
                   kind,
                   amount_in_cents,
                   memo,
                   discount_amount_in_cents,
                   taxable_amount_in_cents,
                   product_id,
                   product_name,
                   component_id,
                   component_handle,
                   component_name,
                   product_handle,
                   period_range_start,
                   period_range_end,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'transaction_type={(self.transaction_type if hasattr(self, "transaction_type") else None)!r}, '
                f'kind={(self.kind if hasattr(self, "kind") else None)!r}, '
                f'amount_in_cents={(self.amount_in_cents if hasattr(self, "amount_in_cents") else None)!r}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!r}, '
                f'discount_amount_in_cents={(self.discount_amount_in_cents if hasattr(self, "discount_amount_in_cents") else None)!r}, '
                f'taxable_amount_in_cents={(self.taxable_amount_in_cents if hasattr(self, "taxable_amount_in_cents") else None)!r}, '
                f'product_id={(self.product_id if hasattr(self, "product_id") else None)!r}, '
                f'product_name={(self.product_name if hasattr(self, "product_name") else None)!r}, '
                f'component_id={(self.component_id if hasattr(self, "component_id") else None)!r}, '
                f'component_handle={(self.component_handle if hasattr(self, "component_handle") else None)!r}, '
                f'component_name={(self.component_name if hasattr(self, "component_name") else None)!r}, '
                f'product_handle={(self.product_handle if hasattr(self, "product_handle") else None)!r}, '
                f'period_range_start={(self.period_range_start if hasattr(self, "period_range_start") else None)!r}, '
                f'period_range_end={(self.period_range_end if hasattr(self, "period_range_end") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'transaction_type={(self.transaction_type if hasattr(self, "transaction_type") else None)!s}, '
                f'kind={(self.kind if hasattr(self, "kind") else None)!s}, '
                f'amount_in_cents={(self.amount_in_cents if hasattr(self, "amount_in_cents") else None)!s}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!s}, '
                f'discount_amount_in_cents={(self.discount_amount_in_cents if hasattr(self, "discount_amount_in_cents") else None)!s}, '
                f'taxable_amount_in_cents={(self.taxable_amount_in_cents if hasattr(self, "taxable_amount_in_cents") else None)!s}, '
                f'product_id={(self.product_id if hasattr(self, "product_id") else None)!s}, '
                f'product_name={(self.product_name if hasattr(self, "product_name") else None)!s}, '
                f'component_id={(self.component_id if hasattr(self, "component_id") else None)!s}, '
                f'component_handle={(self.component_handle if hasattr(self, "component_handle") else None)!s}, '
                f'component_name={(self.component_name if hasattr(self, "component_name") else None)!s}, '
                f'product_handle={(self.product_handle if hasattr(self, "product_handle") else None)!s}, '
                f'period_range_start={(self.period_range_start if hasattr(self, "period_range_start") else None)!s}, '
                f'period_range_end={(self.period_range_end if hasattr(self, "period_range_end") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
