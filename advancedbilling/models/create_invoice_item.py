# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper


class CreateInvoiceItem(object):

    """Implementation of the 'Create Invoice Item' model.

    TODO: type model description here.

    Attributes:
        title (str): TODO: type description here.
        quantity (float | str | None): The quantity can contain up to 8
            decimal places. i.e. 1.00 or 0.0012 or 0.00000065. If you submit a
            value with more than 8 decimal places, we will round it down to
            the 8th decimal place.
        unit_price (float | str | None): The unit_price can contain up to 8
            decimal places. i.e. 1.00 or 0.0012 or 0.00000065. If you submit a
            value with more than 8 decimal places, we will round it down to
            the 8th decimal place.
        taxable (bool): Set to true to automatically calculate taxes. Site
            must be configured to use and calculate taxes.  If using Avalara,
            a tax_code parameter must also be sent.
        tax_code (str): TODO: type description here.
        period_range_start (str): YYYY-MM-DD
        period_range_end (str): YYYY-MM-DD
        product_id (str | int | None): Product handle or product id.
        component_id (str | int | None): Component handle or component id.
        price_point_id (str | int | None): Price point handle or id. For
            component.
        product_price_point_id (str | int | None): TODO: type description here.
        description (str): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "title": 'title',
        "quantity": 'quantity',
        "unit_price": 'unit_price',
        "taxable": 'taxable',
        "tax_code": 'tax_code',
        "period_range_start": 'period_range_start',
        "period_range_end": 'period_range_end',
        "product_id": 'product_id',
        "component_id": 'component_id',
        "price_point_id": 'price_point_id',
        "product_price_point_id": 'product_price_point_id',
        "description": 'description'
    }

    _optionals = [
        'title',
        'quantity',
        'unit_price',
        'taxable',
        'tax_code',
        'period_range_start',
        'period_range_end',
        'product_id',
        'component_id',
        'price_point_id',
        'product_price_point_id',
        'description',
    ]

    def __init__(self,
                 title=APIHelper.SKIP,
                 quantity=APIHelper.SKIP,
                 unit_price=APIHelper.SKIP,
                 taxable=APIHelper.SKIP,
                 tax_code=APIHelper.SKIP,
                 period_range_start=APIHelper.SKIP,
                 period_range_end=APIHelper.SKIP,
                 product_id=APIHelper.SKIP,
                 component_id=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 product_price_point_id=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CreateInvoiceItem class"""

        # Initialize members of the class
        if title is not APIHelper.SKIP:
            self.title = title 
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if unit_price is not APIHelper.SKIP:
            self.unit_price = unit_price 
        if taxable is not APIHelper.SKIP:
            self.taxable = taxable 
        if tax_code is not APIHelper.SKIP:
            self.tax_code = tax_code 
        if period_range_start is not APIHelper.SKIP:
            self.period_range_start = period_range_start 
        if period_range_end is not APIHelper.SKIP:
            self.period_range_end = period_range_end 
        if product_id is not APIHelper.SKIP:
            self.product_id = product_id 
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 
        if product_price_point_id is not APIHelper.SKIP:
            self.product_price_point_id = product_price_point_id 
        if description is not APIHelper.SKIP:
            self.description = description 

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
        title = dictionary.get("title") if dictionary.get("title") else APIHelper.SKIP
        quantity = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateInvoiceItemQuantity'), dictionary.get('quantity'), False) if dictionary.get('quantity') is not None else APIHelper.SKIP
        unit_price = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateInvoiceItemUnitPrice'), dictionary.get('unit_price'), False) if dictionary.get('unit_price') is not None else APIHelper.SKIP
        taxable = dictionary.get("taxable") if "taxable" in dictionary.keys() else APIHelper.SKIP
        tax_code = dictionary.get("tax_code") if dictionary.get("tax_code") else APIHelper.SKIP
        period_range_start = dictionary.get("period_range_start") if dictionary.get("period_range_start") else APIHelper.SKIP
        period_range_end = dictionary.get("period_range_end") if dictionary.get("period_range_end") else APIHelper.SKIP
        product_id = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateInvoiceItemProductId'), dictionary.get('product_id'), False) if dictionary.get('product_id') is not None else APIHelper.SKIP
        component_id = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateInvoiceItemComponentId'), dictionary.get('component_id'), False) if dictionary.get('component_id') is not None else APIHelper.SKIP
        price_point_id = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateInvoiceItemPricePointId'), dictionary.get('price_point_id'), False) if dictionary.get('price_point_id') is not None else APIHelper.SKIP
        product_price_point_id = APIHelper.deserialize_union_type(UnionTypeLookUp.get('CreateInvoiceItemProductPricePointId'), dictionary.get('product_price_point_id'), False) if dictionary.get('product_price_point_id') is not None else APIHelper.SKIP
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(title,
                   quantity,
                   unit_price,
                   taxable,
                   tax_code,
                   period_range_start,
                   period_range_end,
                   product_id,
                   component_id,
                   price_point_id,
                   product_price_point_id,
                   description,
                   additional_properties)
