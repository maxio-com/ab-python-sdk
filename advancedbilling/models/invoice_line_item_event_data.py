# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_line_item_pricing_detail import InvoiceLineItemPricingDetail


class InvoiceLineItemEventData(object):

    """Implementation of the 'Invoice Line Item Event Data' model.

    Attributes:
        uid (str): The model property of type str.
        title (str): The model property of type str.
        description (str): The model property of type str.
        quantity (int): The model property of type int.
        quantity_delta (int): The model property of type int.
        unit_price (str): The model property of type str.
        period_range_start (str): The model property of type str.
        period_range_end (str): The model property of type str.
        amount (str): The model property of type str.
        line_references (str): The model property of type str.
        pricing_details_index (int): The model property of type int.
        pricing_details (List[InvoiceLineItemPricingDetail]): The model
            property of type List[InvoiceLineItemPricingDetail].
        tax_code (str): The model property of type str.
        tax_amount (str): The model property of type str.
        product_id (int): The model property of type int.
        product_price_point_id (int): The model property of type int.
        price_point_id (int): The model property of type int.
        component_id (int): The model property of type int.
        billing_schedule_item_id (int): The model property of type int.
        custom_item (bool): The model property of type bool.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "uid": 'uid',
        "title": 'title',
        "description": 'description',
        "quantity": 'quantity',
        "quantity_delta": 'quantity_delta',
        "unit_price": 'unit_price',
        "period_range_start": 'period_range_start',
        "period_range_end": 'period_range_end',
        "amount": 'amount',
        "line_references": 'line_references',
        "pricing_details_index": 'pricing_details_index',
        "pricing_details": 'pricing_details',
        "tax_code": 'tax_code',
        "tax_amount": 'tax_amount',
        "product_id": 'product_id',
        "product_price_point_id": 'product_price_point_id',
        "price_point_id": 'price_point_id',
        "component_id": 'component_id',
        "billing_schedule_item_id": 'billing_schedule_item_id',
        "custom_item": 'custom_item'
    }

    _optionals = [
        'uid',
        'title',
        'description',
        'quantity',
        'quantity_delta',
        'unit_price',
        'period_range_start',
        'period_range_end',
        'amount',
        'line_references',
        'pricing_details_index',
        'pricing_details',
        'tax_code',
        'tax_amount',
        'product_id',
        'product_price_point_id',
        'price_point_id',
        'component_id',
        'billing_schedule_item_id',
        'custom_item',
    ]

    _nullables = [
        'quantity_delta',
        'pricing_details_index',
        'tax_code',
        'product_price_point_id',
        'price_point_id',
        'component_id',
        'billing_schedule_item_id',
        'custom_item',
    ]

    def __init__(self,
                 uid=APIHelper.SKIP,
                 title=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 quantity=APIHelper.SKIP,
                 quantity_delta=APIHelper.SKIP,
                 unit_price=APIHelper.SKIP,
                 period_range_start=APIHelper.SKIP,
                 period_range_end=APIHelper.SKIP,
                 amount=APIHelper.SKIP,
                 line_references=APIHelper.SKIP,
                 pricing_details_index=APIHelper.SKIP,
                 pricing_details=APIHelper.SKIP,
                 tax_code=APIHelper.SKIP,
                 tax_amount=APIHelper.SKIP,
                 product_id=APIHelper.SKIP,
                 product_price_point_id=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 component_id=APIHelper.SKIP,
                 billing_schedule_item_id=APIHelper.SKIP,
                 custom_item=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the InvoiceLineItemEventData class"""

        # Initialize members of the class
        if uid is not APIHelper.SKIP:
            self.uid = uid 
        if title is not APIHelper.SKIP:
            self.title = title 
        if description is not APIHelper.SKIP:
            self.description = description 
        if quantity is not APIHelper.SKIP:
            self.quantity = quantity 
        if quantity_delta is not APIHelper.SKIP:
            self.quantity_delta = quantity_delta 
        if unit_price is not APIHelper.SKIP:
            self.unit_price = unit_price 
        if period_range_start is not APIHelper.SKIP:
            self.period_range_start = period_range_start 
        if period_range_end is not APIHelper.SKIP:
            self.period_range_end = period_range_end 
        if amount is not APIHelper.SKIP:
            self.amount = amount 
        if line_references is not APIHelper.SKIP:
            self.line_references = line_references 
        if pricing_details_index is not APIHelper.SKIP:
            self.pricing_details_index = pricing_details_index 
        if pricing_details is not APIHelper.SKIP:
            self.pricing_details = pricing_details 
        if tax_code is not APIHelper.SKIP:
            self.tax_code = tax_code 
        if tax_amount is not APIHelper.SKIP:
            self.tax_amount = tax_amount 
        if product_id is not APIHelper.SKIP:
            self.product_id = product_id 
        if product_price_point_id is not APIHelper.SKIP:
            self.product_price_point_id = product_price_point_id 
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if billing_schedule_item_id is not APIHelper.SKIP:
            self.billing_schedule_item_id = billing_schedule_item_id 
        if custom_item is not APIHelper.SKIP:
            self.custom_item = custom_item 

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
        description = dictionary.get("description") if dictionary.get("description") else APIHelper.SKIP
        quantity = dictionary.get("quantity") if dictionary.get("quantity") else APIHelper.SKIP
        quantity_delta = dictionary.get("quantity_delta") if "quantity_delta" in dictionary.keys() else APIHelper.SKIP
        unit_price = dictionary.get("unit_price") if dictionary.get("unit_price") else APIHelper.SKIP
        period_range_start = dictionary.get("period_range_start") if dictionary.get("period_range_start") else APIHelper.SKIP
        period_range_end = dictionary.get("period_range_end") if dictionary.get("period_range_end") else APIHelper.SKIP
        amount = dictionary.get("amount") if dictionary.get("amount") else APIHelper.SKIP
        line_references = dictionary.get("line_references") if dictionary.get("line_references") else APIHelper.SKIP
        pricing_details_index = dictionary.get("pricing_details_index") if "pricing_details_index" in dictionary.keys() else APIHelper.SKIP
        pricing_details = None
        if dictionary.get('pricing_details') is not None:
            pricing_details = [InvoiceLineItemPricingDetail.from_dictionary(x) for x in dictionary.get('pricing_details')]
        else:
            pricing_details = APIHelper.SKIP
        tax_code = dictionary.get("tax_code") if "tax_code" in dictionary.keys() else APIHelper.SKIP
        tax_amount = dictionary.get("tax_amount") if dictionary.get("tax_amount") else APIHelper.SKIP
        product_id = dictionary.get("product_id") if dictionary.get("product_id") else APIHelper.SKIP
        product_price_point_id = dictionary.get("product_price_point_id") if "product_price_point_id" in dictionary.keys() else APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if "price_point_id" in dictionary.keys() else APIHelper.SKIP
        component_id = dictionary.get("component_id") if "component_id" in dictionary.keys() else APIHelper.SKIP
        billing_schedule_item_id = dictionary.get("billing_schedule_item_id") if "billing_schedule_item_id" in dictionary.keys() else APIHelper.SKIP
        custom_item = dictionary.get("custom_item") if "custom_item" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
        # Return an object of this model
        return cls(uid,
                   title,
                   description,
                   quantity,
                   quantity_delta,
                   unit_price,
                   period_range_start,
                   period_range_end,
                   amount,
                   line_references,
                   pricing_details_index,
                   pricing_details,
                   tax_code,
                   tax_amount,
                   product_id,
                   product_price_point_id,
                   price_point_id,
                   component_id,
                   billing_schedule_item_id,
                   custom_item,
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
                f'uid={self.uid!r}, '
                f'title={self.title!r}, '
                f'description={self.description!r}, '
                f'quantity={self.quantity!r}, '
                f'quantity_delta={self.quantity_delta!r}, '
                f'unit_price={self.unit_price!r}, '
                f'period_range_start={self.period_range_start!r}, '
                f'period_range_end={self.period_range_end!r}, '
                f'amount={self.amount!r}, '
                f'line_references={self.line_references!r}, '
                f'pricing_details_index={self.pricing_details_index!r}, '
                f'pricing_details={self.pricing_details!r}, '
                f'tax_code={self.tax_code!r}, '
                f'tax_amount={self.tax_amount!r}, '
                f'product_id={self.product_id!r}, '
                f'product_price_point_id={self.product_price_point_id!r}, '
                f'price_point_id={self.price_point_id!r}, '
                f'component_id={self.component_id!r}, '
                f'billing_schedule_item_id={self.billing_schedule_item_id!r}, '
                f'custom_item={self.custom_item!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'uid={self.uid!s}, '
                f'title={self.title!s}, '
                f'description={self.description!s}, '
                f'quantity={self.quantity!s}, '
                f'quantity_delta={self.quantity_delta!s}, '
                f'unit_price={self.unit_price!s}, '
                f'period_range_start={self.period_range_start!s}, '
                f'period_range_end={self.period_range_end!s}, '
                f'amount={self.amount!s}, '
                f'line_references={self.line_references!s}, '
                f'pricing_details_index={self.pricing_details_index!s}, '
                f'pricing_details={self.pricing_details!s}, '
                f'tax_code={self.tax_code!s}, '
                f'tax_amount={self.tax_amount!s}, '
                f'product_id={self.product_id!s}, '
                f'product_price_point_id={self.product_price_point_id!s}, '
                f'price_point_id={self.price_point_id!s}, '
                f'component_id={self.component_id!s}, '
                f'billing_schedule_item_id={self.billing_schedule_item_id!s}, '
                f'custom_item={self.custom_item!s}, '
                f'additional_properties={self.additional_properties!s})')
