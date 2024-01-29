# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class RenewalPreviewLineItem(object):

    """Implementation of the 'Renewal Preview Line Item' model.

    TODO: type model description here.

    Attributes:
        transaction_type (LineItemTransactionType): A handle for the line item
            transaction type
        kind (LineItemKind): A handle for the line item kind
        amount_in_cents (long|int): TODO: type description here.
        memo (str): TODO: type description here.
        discount_amount_in_cents (long|int): TODO: type description here.
        taxable_amount_in_cents (long|int): TODO: type description here.
        product_id (int): TODO: type description here.
        product_name (str): TODO: type description here.
        component_id (int): TODO: type description here.
        component_handle (str): TODO: type description here.
        component_name (str): TODO: type description here.
        product_handle (str): TODO: type description here.
        period_range_start (str): TODO: type description here.
        period_range_end (str): TODO: type description here.

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
                 period_range_end=APIHelper.SKIP):
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

        if dictionary is None:
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
                   period_range_end)
