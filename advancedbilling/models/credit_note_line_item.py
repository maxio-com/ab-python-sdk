# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from advancedbilling.api_helper import APIHelper


class CreditNoteLineItem(object):

    """Implementation of the 'Credit Note Line Item' model.

    TODO: type model description here.

    Attributes:
        uid (str): Unique identifier for the line item.  Useful when
            cross-referencing the line against individual discounts in the
            `discounts` or `taxes` lists.
        title (str): A short descriptor for the credit given by this line.
        description (str): Detailed description for the credit given by this
            line.  May include proration details in plain text.  Note: this
            string may contain line breaks that are hints for the best display
            format on the credit note.
        quantity (str): The quantity or count of units credited by the line
            item.  This is a decimal number represented as a string. (See
            "About Decimal Numbers".)
        unit_price (str): The price per unit for the line item.  When tiered
            pricing was used (i.e. not every unit was actually priced at the
            same price) this will be the blended average cost per unit and the
            `tiered_unit_price` field will be set to `true`.
        subtotal_amount (str): The line subtotal, generally calculated as
            `quantity * unit_price`. This is the canonical amount of record
            for the line - when rounding differences are in play,
            `subtotal_amount` takes precedence over the value derived from
            `quantity * unit_price` (which may not have the proper precision
            to exactly equal this amount).
        discount_amount (str): The approximate discount of just this line. 
            The value is approximated in cases where rounding errors make it
            difficult to apportion exactly a total discount among many lines.
            Several lines may have been summed prior to applying the discount
            to arrive at `discount_amount` for the invoice - backing that out
            to the discount on a single line may introduce rounding or
            precision errors.
        tax_amount (str): The approximate tax of just this line.  The value is
            approximated in cases where rounding errors make it difficult to
            apportion exactly a total tax among many lines. Several lines may
            have been summed prior to applying the tax rate to arrive at
            `tax_amount` for the invoice - backing that out to the tax on a
            single line may introduce rounding or precision errors.
        total_amount (str): The non-canonical total amount for the line. 
            `subtotal_amount` is the canonical amount for a line. The invoice
            `total_amount` is derived from the sum of the line
            `subtotal_amount`s and discounts or taxes applied thereafter. 
            Therefore, due to rounding or precision errors, the sum of line
            `total_amount`s may not equal the invoice `total_amount`.
        tiered_unit_price (bool): When `true`, indicates that the actual
            pricing scheme for the line was tiered, so the `unit_price` shown
            is the blended average for all units.
        period_range_start (date): Start date for the period credited by this
            line. The format is `"YYYY-MM-DD"`.
        period_range_end (date): End date for the period credited by this
            line. The format is `"YYYY-MM-DD"`.
        product_id (int): The ID of the product being credited.  This may be
            set even for component credits, so true product-only
            (non-component) credits will also have a nil `component_id`.
        product_version (int): The version of the product being credited.
        component_id (int): The ID of the component being credited. Will be
            `nil` for non-component credits.
        price_point_id (int): The price point ID of the component being
            credited. Will be `nil` for non-component credits.
        billing_schedule_item_id (int): TODO: type description here.
        custom_item (bool): TODO: type description here.
        additional_properties (Dict[str, object]): The additional properties
            for the model.

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
        "component_id": 'component_id',
        "price_point_id": 'price_point_id',
        "billing_schedule_item_id": 'billing_schedule_item_id',
        "custom_item": 'custom_item'
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
        'component_id',
        'price_point_id',
        'billing_schedule_item_id',
        'custom_item',
    ]

    _nullables = [
        'component_id',
        'price_point_id',
        'billing_schedule_item_id',
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
                 component_id=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 billing_schedule_item_id=APIHelper.SKIP,
                 custom_item=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the CreditNoteLineItem class"""

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
        if component_id is not APIHelper.SKIP:
            self.component_id = component_id 
        if price_point_id is not APIHelper.SKIP:
            self.price_point_id = price_point_id 
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
        unit_price = dictionary.get("unit_price") if dictionary.get("unit_price") else APIHelper.SKIP
        subtotal_amount = dictionary.get("subtotal_amount") if dictionary.get("subtotal_amount") else APIHelper.SKIP
        discount_amount = dictionary.get("discount_amount") if dictionary.get("discount_amount") else APIHelper.SKIP
        tax_amount = dictionary.get("tax_amount") if dictionary.get("tax_amount") else APIHelper.SKIP
        total_amount = dictionary.get("total_amount") if dictionary.get("total_amount") else APIHelper.SKIP
        tiered_unit_price = dictionary.get("tiered_unit_price") if "tiered_unit_price" in dictionary.keys() else APIHelper.SKIP
        period_range_start = dateutil.parser.parse(dictionary.get('period_range_start')).date() if dictionary.get('period_range_start') else APIHelper.SKIP
        period_range_end = dateutil.parser.parse(dictionary.get('period_range_end')).date() if dictionary.get('period_range_end') else APIHelper.SKIP
        product_id = dictionary.get("product_id") if dictionary.get("product_id") else APIHelper.SKIP
        product_version = dictionary.get("product_version") if dictionary.get("product_version") else APIHelper.SKIP
        component_id = dictionary.get("component_id") if "component_id" in dictionary.keys() else APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if "price_point_id" in dictionary.keys() else APIHelper.SKIP
        billing_schedule_item_id = dictionary.get("billing_schedule_item_id") if "billing_schedule_item_id" in dictionary.keys() else APIHelper.SKIP
        custom_item = dictionary.get("custom_item") if "custom_item" in dictionary.keys() else APIHelper.SKIP
        # Clean out expected properties from dictionary
        additional_properties = {k: v for k, v in dictionary.items() if k not in cls._names.values()}
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
                   component_id,
                   price_point_id,
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
