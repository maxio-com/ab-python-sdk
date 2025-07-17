# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class AllocationPreviewLineItem(object):

    """Implementation of the 'Allocation Preview Line Item' model.

    Attributes:
        transaction_type (LineItemTransactionType): A handle for the line item
            transaction type
        kind (AllocationPreviewLineItemKind): A handle for the line item kind
            for allocation preview
        amount_in_cents (int): The model property of type int.
        memo (str): The model property of type str.
        discount_amount_in_cents (int): The model property of type int.
        taxable_amount_in_cents (int): The model property of type int.
        component_id (int): The model property of type int.
        component_handle (str): The model property of type str.
        direction (AllocationPreviewDirection): Visible when using
            Fine-grained Component Control
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
        "component_id": 'component_id',
        "component_handle": 'component_handle',
        "direction": 'direction'
    }

    _optionals = [
        'transaction_type',
        'kind',
        'amount_in_cents',
        'memo',
        'discount_amount_in_cents',
        'taxable_amount_in_cents',
        'component_id',
        'component_handle',
        'direction',
    ]

    def __init__(self,
                 transaction_type=APIHelper.SKIP,
                 kind=APIHelper.SKIP,
                 amount_in_cents=APIHelper.SKIP,
                 memo=APIHelper.SKIP,
                 discount_amount_in_cents=APIHelper.SKIP,
                 taxable_amount_in_cents=APIHelper.SKIP,
                 component_id=APIHelper.SKIP,
                 component_handle=APIHelper.SKIP,
                 direction=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the AllocationPreviewLineItem class"""

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
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if component_handle is not APIHelper.SKIP:
            self.component_handle = component_handle 
        if direction is not APIHelper.SKIP:
            self.direction = direction 

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
        component_id = dictionary.get("component_id") if dictionary.get("component_id") else APIHelper.SKIP
        component_handle = dictionary.get("component_handle") if dictionary.get("component_handle") else APIHelper.SKIP
        direction = dictionary.get("direction") if dictionary.get("direction") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(transaction_type,
                   kind,
                   amount_in_cents,
                   memo,
                   discount_amount_in_cents,
                   taxable_amount_in_cents,
                   component_id,
                   component_handle,
                   direction,
                   additional_properties)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'transaction_type={(self.transaction_type if hasattr(self, "transaction_type") else None)!r}, '
                f'kind={(self.kind if hasattr(self, "kind") else None)!r}, '
                f'amount_in_cents={(self.amount_in_cents if hasattr(self, "amount_in_cents") else None)!r}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!r}, '
                f'discount_amount_in_cents={(self.discount_amount_in_cents if hasattr(self, "discount_amount_in_cents") else None)!r}, '
                f'taxable_amount_in_cents={(self.taxable_amount_in_cents if hasattr(self, "taxable_amount_in_cents") else None)!r}, '
                f'component_id={(self.component_id if hasattr(self, "component_id") else None)!r}, '
                f'component_handle={(self.component_handle if hasattr(self, "component_handle") else None)!r}, '
                f'direction={(self.direction if hasattr(self, "direction") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'transaction_type={(self.transaction_type if hasattr(self, "transaction_type") else None)!s}, '
                f'kind={(self.kind if hasattr(self, "kind") else None)!s}, '
                f'amount_in_cents={(self.amount_in_cents if hasattr(self, "amount_in_cents") else None)!s}, '
                f'memo={(self.memo if hasattr(self, "memo") else None)!s}, '
                f'discount_amount_in_cents={(self.discount_amount_in_cents if hasattr(self, "discount_amount_in_cents") else None)!s}, '
                f'taxable_amount_in_cents={(self.taxable_amount_in_cents if hasattr(self, "taxable_amount_in_cents") else None)!s}, '
                f'component_id={(self.component_id if hasattr(self, "component_id") else None)!s}, '
                f'component_handle={(self.component_handle if hasattr(self, "component_handle") else None)!s}, '
                f'direction={(self.direction if hasattr(self, "direction") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
