# -*- coding: utf-8 -*-

"""
advanced_billing

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
import dateutil.parser

from advancedbilling.api_helper import APIHelper
from advancedbilling.models.invoice_line_item_component_cost_data import InvoiceLineItemComponentCostData


class InvoiceLineItem(object):

    """Implementation of the 'Invoice Line Item' model.

    Attributes:
        uid (str): Unique identifier for the line item.  Useful when
            cross-referencing the line against individual discounts in the
            `discounts` or `taxes` lists.
        title (str): A short descriptor for the charge or item represented by
            this line.
        description (str): Detailed description for the charge or item
            represented by this line.  May include proration details in plain
            text.  Note: this string may contain line breaks that are hints
            for the best display format on the invoice.
        quantity (str): The quantity or count of units billed by the line
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
        discount_amount (str): The approximate discount applied to just this
            line.  The value is approximated in cases where rounding errors
            make it difficult to apportion exactly a total discount among many
            lines. Several lines may have been summed prior to applying the
            discount to arrive at `discount_amount` for the invoice - backing
            that out to the discount on a single line may introduce rounding
            or precision errors.
        tax_amount (str): The approximate tax applied to just this line.  The
            value is approximated in cases where rounding errors make it
            difficult to apportion exactly a total tax among many lines.
            Several lines may have been summed prior to applying the tax rate
            to arrive at `tax_amount` for the invoice - backing that out to
            the tax on a single line may introduce rounding or precision
            errors.
        total_amount (str): The non-canonical total amount for the line. 
            `subtotal_amount` is the canonical amount for a line. The invoice
            `total_amount` is derived from the sum of the line
            `subtotal_amount`s and discounts or taxes applied thereafter. 
            Therefore, due to rounding or precision errors, the sum of line
            `total_amount`s may not equal the invoice `total_amount`.
        tiered_unit_price (bool): When `true`, indicates that the actual
            pricing scheme for the line was tiered, so the `unit_price` shown
            is the blended average for all units.
        period_range_start (date): Start date for the period covered by this
            line. The format is `"YYYY-MM-DD"`.  * For periodic charges paid
            in advance, this date will match the billing date, and the end
            date will be in the future. * For periodic charges paid in arrears
            (e.g. metered charges), this date will be the date of the previous
            billing, and the end date will be the current billing date. * For
            non-periodic charges, this date and the end date will match.
        period_range_end (date): End date for the period covered by this line.
            The format is `"YYYY-MM-DD"`.  * For periodic charges paid in
            advance, this date will match the next (future) billing date. *
            For periodic charges paid in arrears (e.g. metered charges), this
            date will be the date of the current billing date. * For
            non-periodic charges, this date and the start date will match.
        transaction_id (int): The model property of type int.
        product_id (int): The ID of the product subscribed when the charge was
            made.  This may be set even for component charges, so true
            product-only (non-component) charges will also have a nil
            `component_id`.
        product_version (int): The version of the product subscribed when the
            charge was made.
        component_id (int): The ID of the component being billed. Will be
            `nil` for non-component charges.
        price_point_id (int): The price point ID of the component being
            billed. Will be `nil` for non-component charges.
        billing_schedule_item_id (int): The model property of type int.
        hide (bool): The model property of type bool.
        component_cost_data (InvoiceLineItemComponentCostData): The model
            property of type InvoiceLineItemComponentCostData.
        product_price_point_id (int): The price point ID of the line item's
            product
        custom_item (bool): The model property of type bool.
        kind (str): The model property of type str.
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
        "transaction_id": 'transaction_id',
        "product_id": 'product_id',
        "product_version": 'product_version',
        "component_id": 'component_id',
        "price_point_id": 'price_point_id',
        "billing_schedule_item_id": 'billing_schedule_item_id',
        "hide": 'hide',
        "component_cost_data": 'component_cost_data',
        "product_price_point_id": 'product_price_point_id',
        "custom_item": 'custom_item',
        "kind": 'kind'
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
        'transaction_id',
        'product_id',
        'product_version',
        'component_id',
        'price_point_id',
        'billing_schedule_item_id',
        'hide',
        'component_cost_data',
        'product_price_point_id',
        'custom_item',
        'kind',
    ]

    _nullables = [
        'product_id',
        'product_version',
        'component_id',
        'price_point_id',
        'billing_schedule_item_id',
        'component_cost_data',
        'product_price_point_id',
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
                 transaction_id=APIHelper.SKIP,
                 product_id=APIHelper.SKIP,
                 product_version=APIHelper.SKIP,
                 component_id=APIHelper.SKIP,
                 price_point_id=APIHelper.SKIP,
                 billing_schedule_item_id=APIHelper.SKIP,
                 hide=APIHelper.SKIP,
                 component_cost_data=APIHelper.SKIP,
                 product_price_point_id=APIHelper.SKIP,
                 custom_item=APIHelper.SKIP,
                 kind=APIHelper.SKIP,
                 additional_properties=None):
        """Constructor for the InvoiceLineItem class"""

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
        if transaction_id is not APIHelper.SKIP:
            self.transaction_id = transaction_id 
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
        if hide is not APIHelper.SKIP:
            self.hide = hide 
        if component_cost_data is not APIHelper.SKIP:
            self.component_cost_data = component_cost_data 
        if product_price_point_id is not APIHelper.SKIP:
            self.product_price_point_id = product_price_point_id 
        if custom_item is not APIHelper.SKIP:
            self.custom_item = custom_item 
        if kind is not APIHelper.SKIP:
            self.kind = kind 

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
        transaction_id = dictionary.get("transaction_id") if dictionary.get("transaction_id") else APIHelper.SKIP
        product_id = dictionary.get("product_id") if "product_id" in dictionary.keys() else APIHelper.SKIP
        product_version = dictionary.get("product_version") if "product_version" in dictionary.keys() else APIHelper.SKIP
        component_id = dictionary.get("component_id") if "component_id" in dictionary.keys() else APIHelper.SKIP
        price_point_id = dictionary.get("price_point_id") if "price_point_id" in dictionary.keys() else APIHelper.SKIP
        billing_schedule_item_id = dictionary.get("billing_schedule_item_id") if "billing_schedule_item_id" in dictionary.keys() else APIHelper.SKIP
        hide = dictionary.get("hide") if "hide" in dictionary.keys() else APIHelper.SKIP
        if 'component_cost_data' in dictionary.keys():
            component_cost_data = InvoiceLineItemComponentCostData.from_dictionary(dictionary.get('component_cost_data')) if dictionary.get('component_cost_data') else None
        else:
            component_cost_data = APIHelper.SKIP
        product_price_point_id = dictionary.get("product_price_point_id") if "product_price_point_id" in dictionary.keys() else APIHelper.SKIP
        custom_item = dictionary.get("custom_item") if "custom_item" in dictionary.keys() else APIHelper.SKIP
        kind = dictionary.get("kind") if dictionary.get("kind") else APIHelper.SKIP
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
                   transaction_id,
                   product_id,
                   product_version,
                   component_id,
                   price_point_id,
                   billing_schedule_item_id,
                   hide,
                   component_cost_data,
                   product_price_point_id,
                   custom_item,
                   kind,
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
                f'quantity={(self.quantity if hasattr(self, "quantity") else None)!r}, '
                f'unit_price={(self.unit_price if hasattr(self, "unit_price") else None)!r}, '
                f'subtotal_amount={(self.subtotal_amount if hasattr(self, "subtotal_amount") else None)!r}, '
                f'discount_amount={(self.discount_amount if hasattr(self, "discount_amount") else None)!r}, '
                f'tax_amount={(self.tax_amount if hasattr(self, "tax_amount") else None)!r}, '
                f'total_amount={(self.total_amount if hasattr(self, "total_amount") else None)!r}, '
                f'tiered_unit_price={(self.tiered_unit_price if hasattr(self, "tiered_unit_price") else None)!r}, '
                f'period_range_start={(self.period_range_start if hasattr(self, "period_range_start") else None)!r}, '
                f'period_range_end={(self.period_range_end if hasattr(self, "period_range_end") else None)!r}, '
                f'transaction_id={(self.transaction_id if hasattr(self, "transaction_id") else None)!r}, '
                f'product_id={(self.product_id if hasattr(self, "product_id") else None)!r}, '
                f'product_version={(self.product_version if hasattr(self, "product_version") else None)!r}, '
                f'component_id={(self.component_id if hasattr(self, "component_id") else None)!r}, '
                f'price_point_id={(self.price_point_id if hasattr(self, "price_point_id") else None)!r}, '
                f'billing_schedule_item_id={(self.billing_schedule_item_id if hasattr(self, "billing_schedule_item_id") else None)!r}, '
                f'hide={(self.hide if hasattr(self, "hide") else None)!r}, '
                f'component_cost_data={(self.component_cost_data if hasattr(self, "component_cost_data") else None)!r}, '
                f'product_price_point_id={(self.product_price_point_id if hasattr(self, "product_price_point_id") else None)!r}, '
                f'custom_item={(self.custom_item if hasattr(self, "custom_item") else None)!r}, '
                f'kind={(self.kind if hasattr(self, "kind") else None)!r}, '
                f'additional_properties={self.additional_properties!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'uid={(self.uid if hasattr(self, "uid") else None)!s}, '
                f'title={(self.title if hasattr(self, "title") else None)!s}, '
                f'description={(self.description if hasattr(self, "description") else None)!s}, '
                f'quantity={(self.quantity if hasattr(self, "quantity") else None)!s}, '
                f'unit_price={(self.unit_price if hasattr(self, "unit_price") else None)!s}, '
                f'subtotal_amount={(self.subtotal_amount if hasattr(self, "subtotal_amount") else None)!s}, '
                f'discount_amount={(self.discount_amount if hasattr(self, "discount_amount") else None)!s}, '
                f'tax_amount={(self.tax_amount if hasattr(self, "tax_amount") else None)!s}, '
                f'total_amount={(self.total_amount if hasattr(self, "total_amount") else None)!s}, '
                f'tiered_unit_price={(self.tiered_unit_price if hasattr(self, "tiered_unit_price") else None)!s}, '
                f'period_range_start={(self.period_range_start if hasattr(self, "period_range_start") else None)!s}, '
                f'period_range_end={(self.period_range_end if hasattr(self, "period_range_end") else None)!s}, '
                f'transaction_id={(self.transaction_id if hasattr(self, "transaction_id") else None)!s}, '
                f'product_id={(self.product_id if hasattr(self, "product_id") else None)!s}, '
                f'product_version={(self.product_version if hasattr(self, "product_version") else None)!s}, '
                f'component_id={(self.component_id if hasattr(self, "component_id") else None)!s}, '
                f'price_point_id={(self.price_point_id if hasattr(self, "price_point_id") else None)!s}, '
                f'billing_schedule_item_id={(self.billing_schedule_item_id if hasattr(self, "billing_schedule_item_id") else None)!s}, '
                f'hide={(self.hide if hasattr(self, "hide") else None)!s}, '
                f'component_cost_data={(self.component_cost_data if hasattr(self, "component_cost_data") else None)!s}, '
                f'product_price_point_id={(self.product_price_point_id if hasattr(self, "product_price_point_id") else None)!s}, '
                f'custom_item={(self.custom_item if hasattr(self, "custom_item") else None)!s}, '
                f'kind={(self.kind if hasattr(self, "kind") else None)!s}, '
                f'additional_properties={self.additional_properties!s})')
