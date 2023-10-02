# -*- coding: utf-8 -*-

"""
maxioadvancedbillingformerlychargifyapi

This file was automatically generated by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from maxioadvancedbillingformerlychargifyapi.api_helper import APIHelper


class ProformaInvoiceLineItem(object):

    """Implementation of the 'Proforma Invoice Line Item' model.

    TODO: type model description here.

    Attributes:
        uid (str): TODO: type description here.
        title (str): TODO: type description here.
        description (str): TODO: type description here.
        quantity (str): TODO: type description here.
        unit_price (str): TODO: type description here.
        subtotal_amount (str): TODO: type description here.
        discount_amount (str): TODO: type description here.
        tax_amount (str): TODO: type description here.
        total_amount (str): TODO: type description here.
        tiered_unit_price (bool): TODO: type description here.
        period_range_start (str): TODO: type description here.
        period_range_end (str): TODO: type description here.
        product_id (int): TODO: type description here.
        product_version (int): TODO: type description here.
        product_price_point_id (int): TODO: type description here.
        component_id (str): TODO: type description here.
        price_point_id (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "title": 'title',
        "description": 'description',
        "quantity": 'quantity',
        "unit_price": 'unit_price',
        "subtotal_amount": 'subtotal_amount',
        "discount_amount": 'discount_amount',
        "tax_amount": 'tax_amount',
        "total_amount": 'total_amount',
        "tiered_unit_price": 'tiered_unit_price',
        "period_range_start": 'period_range_start',
        "period_range_end": 'period_range_end',
        "product_id": 'product_id',
        "product_version": 'product_version',
        "product_price_point_id": 'product_price_point_id',
        "component_id": 'component_id',
        "price_point_id": 'price_point_id'
    }

    _optionals = [
        'uid',
        'title',
        'description',
        'quantity',
        'unit_price',
        'subtotal_amount',
        'discount_amount',
        'tax_amount',
        'total_amount',
        'tiered_unit_price',
        'period_range_start',
        'period_range_end',
        'product_id',
        'product_version',
        'product_price_point_id',
        'component_id',
        'price_point_id',
    ]

    _nullables = [
        'component_id',
        'price_point_id',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 title=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 quantity=APIHelper.SKIP,
                 unit_price=APIHelper.SKIP,
                 subtotal_amount=APIHelper.SKIP,
                 discount_amount=APIHelper.SKIP,
                 tax_amount=APIHelper.SKIP,
                 total_amount=APIHelper.SKIP,
                 tiered_unit_price=APIHelper.SKIP,
                 period_range_start=APIHelper.SKIP,
                 period_range_end=APIHelper.SKIP,
                 product_id=APIHelper.SKIP,
                 product_version=APIHelper.SKIP,
                 product_price_point_id=APIHelper.SKIP,
                 component_id=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP):
        """Constructor for the ProformaInvoiceLineItem class"""

        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid 
        if title is not APIHelper.SKIP:
            self.title = title 
        if description is not APIHelper.SKIP:
            self.description = description 
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if unit_price is not APIHelper.SKIP:
            self.unit_price = unit_price 
        if subtotal_amount is not APIHelper.SKIP:
            self.subtotal_amount = subtotal_amount 
        if discount_amount is not APIHelper.SKIP:
            self.discount_amount = discount_amount 
        if tax_amount is not APIHelper.SKIP:
            self.tax_amount = tax_amount 
        if total_amount is not APIHelper.SKIP:
            self.total_amount = total_amount 
        if tiered_unit_price is not APIHelper.SKIP:
            self.tiered_unit_price = tiered_unit_price 
        if period_range_start is not APIHelper.SKIP:
            self.period_range_start = period_range_start 
        if period_range_end is not APIHelper.SKIP:
            self.period_range_end = period_range_end 
        if product_id is not APIHelper.SKIP:
            self.product_id = product_id 
        if product_version is not APIHelper.SKIP:
            self.product_version = product_version 
        if product_price_point_id is not APIHelper.SKIP:
            self.product_price_point_id = product_price_point_id 
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 

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
        uid = dictionary.get("uid") if dictionary.get("uid") else APIHelper.SKIP
        title = dictionary.get("title") if dictionary.get("title") else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else APIHelper.SKIP
        unit_price = dictionary.get("unit_price") if dictionary.get("unit_price") else APIHelper.SKIP
        subtotal_amount = dictionary.get("subtotal_amount") if dictionary.get("subtotal_amount") else APIHelper.SKIP
        discount_amount = dictionary.get("discount_amount") if dictionary.get("discount_amount") else APIHelper.SKIP
        tax_amount = dictionary.get("tax_amount") if dictionary.get("tax_amount") else APIHelper.SKIP
        total_amount = dictionary.get("total_amount") if dictionary.get("total_amount") else APIHelper.SKIP
        tiered_unit_price = dictionary.get("tiered_unit_price") if "tiered_unit_price" in dictionary.keys() else APIHelper.SKIP
        period_range_start = dictionary.get("period_range_start") if dictionary.get("period_range_start") else APIHelper.SKIP
        period_range_end = dictionary.get("period_range_end") if dictionary.get("period_range_end") else APIHelper.SKIP
        product_id = dictionary.get("product_id") if dictionary.get("product_id") else APIHelper.SKIP
        product_version = dictionary.get("product_version") if dictionary.get("product_version") else APIHelper.SKIP
        product_price_point_id = dictionary.get("product_price_point_id") if dictionary.get("product_price_point_id") else APIHelper.SKIP
        component_id = dictionary.get("component_id") if "component_id" in dictionary.keys() else APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if "price_point_id" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(uid,
                   title,
                   description,
                   quantity,
                   unit_price,
                   subtotal_amount,
                   discount_amount,
                   tax_amount,
                   total_amount,
                   tiered_unit_price,
                   period_range_start,
                   period_range_end,
                   product_id,
                   product_version,
                   product_price_point_id,
                   component_id,
                   price_point_id)