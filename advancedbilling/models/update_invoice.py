"""advanced_billing.

This file was automatically generated for Maxio by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""

# ruff: noqa: E501
import dateutil.parser

from advancedbilling.api_helper import APIHelper
from advancedbilling.models.create_invoice_address import (
    CreateInvoiceAddress,
)
from advancedbilling.models.create_invoice_coupon import (
    CreateInvoiceCoupon,
)
from advancedbilling.models.update_invoice_item import (
    UpdateInvoiceItem,
)


class UpdateInvoice(object):
    """Implementation of the 'Update Invoice' model.

    Attributes of a draft ad hoc invoice which can be updated. Only the submitted
    attributes are changed.

    Attributes:
        line_items (List[UpdateInvoiceItem]): Line item changes to apply. Line items
            without a `uid` are added, line items with a `uid` are updated, and line
            items with a `uid` and `_destroy` set to `true` are removed. Existing
            line items not referenced in the array remain unchanged.
        issue_date (date): New issue date for the invoice (format YYYY-MM-DD). This
            date is interpreted and validated in your site's time zone. It must be
            today or a date in the past — future dates are not accepted. The due date
            is recalculated from the issue date and net terms.
        net_terms (int): Number of days after the issue date on which the invoice is
            due. The due date is recalculated when net terms or the issue date change.
        payment_instructions (str): Custom payment instructions displayed on the
            invoice.
        memo (str): A custom memo displayed on the invoice.
        seller_address (CreateInvoiceAddress): Replaces the seller address on the
            invoice
        billing_address (CreateInvoiceAddress): Replaces the billing address on the
            invoice
        shipping_address (CreateInvoiceAddress): Replaces the shipping address on the
            invoice
        coupons (List[CreateInvoiceCoupon]): When present, replaces all discounts
            currently applied to the invoice. Send an empty array to remove all
            discounts.
        additional_properties (Dict[str, object]): The additional properties for the
            model.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "line_items": "line_items",
        "issue_date": "issue_date",
        "net_terms": "net_terms",
        "payment_instructions": "payment_instructions",
        "memo": "memo",
        "seller_address": "seller_address",
        "billing_address": "billing_address",
        "shipping_address": "shipping_address",
        "coupons": "coupons",
    }

    _optionals = [
        "line_items",
        "issue_date",
        "net_terms",
        "payment_instructions",
        "memo",
        "seller_address",
        "billing_address",
        "shipping_address",
        "coupons",
    ]

    def __init__(
        self,
        line_items=APIHelper.SKIP,
        issue_date=APIHelper.SKIP,
        net_terms=APIHelper.SKIP,
        payment_instructions=APIHelper.SKIP,
        memo=APIHelper.SKIP,
        seller_address=APIHelper.SKIP,
        billing_address=APIHelper.SKIP,
        shipping_address=APIHelper.SKIP,
        coupons=APIHelper.SKIP,
        additional_properties=None):
        """Initialize a UpdateInvoice instance."""
        # Initialize members of the class
        if line_items is not APIHelper.SKIP:
            self.line_items = line_items
        if issue_date is not APIHelper.SKIP:
            self.issue_date = issue_date
        if net_terms is not APIHelper.SKIP:
            self.net_terms = net_terms
        if payment_instructions is not APIHelper.SKIP:
            self.payment_instructions = payment_instructions
        if memo is not APIHelper.SKIP:
            self.memo = memo
        if seller_address is not APIHelper.SKIP:
            self.seller_address = seller_address
        if billing_address is not APIHelper.SKIP:
            self.billing_address = billing_address
        if shipping_address is not APIHelper.SKIP:
            self.shipping_address = shipping_address
        if coupons is not APIHelper.SKIP:
            self.coupons = coupons

        # Add additional model properties to the instance
        if additional_properties is None:
            additional_properties = {}
        self.additional_properties = additional_properties

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Create an instance of this model from a dictionary

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
        line_items = None
        if dictionary.get("line_items") is not None:
            line_items = [
                UpdateInvoiceItem.from_dictionary(x)
                    for x in dictionary.get("line_items")
            ]
        else:
            line_items = APIHelper.SKIP
        issue_date = dateutil.parser.parse(
            dictionary.get("issue_date")).date()\
            if dictionary.get("issue_date") else APIHelper.SKIP
        net_terms =\
            dictionary.get("net_terms")\
            if dictionary.get("net_terms")\
                else APIHelper.SKIP
        payment_instructions =\
            dictionary.get("payment_instructions")\
            if dictionary.get("payment_instructions")\
                else APIHelper.SKIP
        memo =\
            dictionary.get("memo")\
            if dictionary.get("memo")\
                else APIHelper.SKIP
        seller_address =\
            CreateInvoiceAddress.from_dictionary(
                dictionary.get("seller_address"))\
                if "seller_address" in dictionary.keys()\
                else APIHelper.SKIP
        billing_address =\
            CreateInvoiceAddress.from_dictionary(
                dictionary.get("billing_address"))\
                if "billing_address" in dictionary.keys()\
                else APIHelper.SKIP
        shipping_address =\
            CreateInvoiceAddress.from_dictionary(
                dictionary.get("shipping_address"))\
                if "shipping_address" in dictionary.keys()\
                else APIHelper.SKIP
        coupons = None
        if dictionary.get("coupons") is not None:
            coupons = [
                CreateInvoiceCoupon.from_dictionary(x)
                    for x in dictionary.get("coupons")
            ]
        else:
            coupons = APIHelper.SKIP

        # Clean out expected properties from dictionary
        additional_properties =\
            {k: v for k, v in dictionary.items() if k not in cls._names.values()}

        # Return an object of this model
        return cls(line_items,
                   issue_date,
                   net_terms,
                   payment_instructions,
                   memo,
                   seller_address,
                   billing_address,
                   shipping_address,
                   coupons,
                   additional_properties)

    def __repr__(self):
        """Return a unambiguous string representation."""
        _line_items=(
            self.line_items
            if hasattr(self, "line_items")
            else None
        )
        _issue_date=(
            self.issue_date
            if hasattr(self, "issue_date")
            else None
        )
        _net_terms=(
            self.net_terms
            if hasattr(self, "net_terms")
            else None
        )
        _payment_instructions=(
            self.payment_instructions
            if hasattr(self, "payment_instructions")
            else None
        )
        _memo=(
            self.memo
            if hasattr(self, "memo")
            else None
        )
        _seller_address=(
            self.seller_address
            if hasattr(self, "seller_address")
            else None
        )
        _billing_address=(
            self.billing_address
            if hasattr(self, "billing_address")
            else None
        )
        _shipping_address=(
            self.shipping_address
            if hasattr(self, "shipping_address")
            else None
        )
        _coupons=(
            self.coupons
            if hasattr(self, "coupons")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"line_items={_line_items!r}, "
            f"issue_date={_issue_date!r}, "
            f"net_terms={_net_terms!r}, "
            f"payment_instructions={_payment_instructions!r}, "
            f"memo={_memo!r}, "
            f"seller_address={_seller_address!r}, "
            f"billing_address={_billing_address!r}, "
            f"shipping_address={_shipping_address!r}, "
            f"coupons={_coupons!r}, "
            f"additional_properties={_additional_properties!r}, "
            f")"
        )

    def __str__(self):
        """Return a human-readable string representation."""
        _line_items=(
            self.line_items
            if hasattr(self, "line_items")
            else None
        )
        _issue_date=(
            self.issue_date
            if hasattr(self, "issue_date")
            else None
        )
        _net_terms=(
            self.net_terms
            if hasattr(self, "net_terms")
            else None
        )
        _payment_instructions=(
            self.payment_instructions
            if hasattr(self, "payment_instructions")
            else None
        )
        _memo=(
            self.memo
            if hasattr(self, "memo")
            else None
        )
        _seller_address=(
            self.seller_address
            if hasattr(self, "seller_address")
            else None
        )
        _billing_address=(
            self.billing_address
            if hasattr(self, "billing_address")
            else None
        )
        _shipping_address=(
            self.shipping_address
            if hasattr(self, "shipping_address")
            else None
        )
        _coupons=(
            self.coupons
            if hasattr(self, "coupons")
            else None
        )
        _additional_properties=self.additional_properties
        return (
            f"{self.__class__.__name__}("
            f"line_items={_line_items!s}, "
            f"issue_date={_issue_date!s}, "
            f"net_terms={_net_terms!s}, "
            f"payment_instructions={_payment_instructions!s}, "
            f"memo={_memo!s}, "
            f"seller_address={_seller_address!s}, "
            f"billing_address={_billing_address!s}, "
            f"shipping_address={_shipping_address!s}, "
            f"coupons={_coupons!s}, "
            f"additional_properties={_additional_properties!s}, "
            f")"
        )
