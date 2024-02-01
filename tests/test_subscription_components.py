import pytest

from advancedbilling.advanced_billing_client import (
    ComponentsController,
    CustomersController,
    PaymentProfilesController,
    ProductFamiliesController,
    ProductsController,
    SubscriptionComponentsController,
    SubscriptionsController,
)
from advancedbilling.exceptions.component_allocation_error_exception import (
    ComponentAllocationErrorException,
)
from advancedbilling.models.allocate_components import AllocateComponents
from advancedbilling.models.allocation_preview import AllocationPreview
from advancedbilling.models.component import Component
from advancedbilling.models.component_allocation_error_item import (
    ComponentAllocationErrorItem,
)
from advancedbilling.models.create_customer_request import CreateCustomerRequest
from advancedbilling.models.create_on_off_component import CreateOnOffComponent
from advancedbilling.models.create_or_update_product_request import (
    CreateOrUpdateProductRequest,
)
from advancedbilling.models.create_payment_profile_request import (
    CreatePaymentProfileRequest,
)
from advancedbilling.models.create_product_family_request import (
    CreateProductFamilyRequest,
)
from advancedbilling.models.create_quantity_based_component import (
    CreateQuantityBasedComponent,
)
from advancedbilling.models.create_subscription_request import CreateSubscriptionRequest
from advancedbilling.models.credit_card_payment_profile import CreditCardPaymentProfile
from advancedbilling.models.customer import Customer
from advancedbilling.models.interval_unit import IntervalUnit
from advancedbilling.models.payment_type import PaymentType
from advancedbilling.models.preview_allocations_request import PreviewAllocationsRequest
from advancedbilling.models.pricing_scheme import PricingScheme
from advancedbilling.models.product import Product
from advancedbilling.models.product_family import ProductFamily
from advancedbilling.models.subscription import Subscription


class TestSubscriptionComponents:
    def test_preview_allocations_subscription_and_on_off_component_and_quantity_based_component_then_preview_allocations_and_allocate_components(  # noqa: E501
        self,
        components_controller: ComponentsController,
        customers_controller: CustomersController,
        payment_profiles_controller: PaymentProfilesController,
        product_families_controller: ProductFamiliesController,
        products_controller: ProductsController,
        subscription_components_controller: SubscriptionComponentsController,
        subscriptions_controller: SubscriptionsController,
    ):
        product_family: ProductFamily = product_families_controller.create_product_family(
            CreateProductFamilyRequest.from_dictionary(
                {
                    "product_family": {
                        "name": "TestSubscriptionComponents_Product_Family_Name_1",
                        "description": "TestSubscriptionComponents_Product_Family_Description_1",
                    }
                }
            )
        ).product_family

        product: Product = products_controller.create_product(
            product_family.id,
            CreateOrUpdateProductRequest.from_dictionary(
                {
                    "product": {
                        "name": "TestSubscriptionComponents_Product_Name_1",
                        "handle": "testsubscriptioncomponents_product_handle_1",
                        "description": "TestSubscriptionComponents_Product_Description_1",
                        "interval": 1,
                        "price_in_cents": 10,
                        "interval_unit": IntervalUnit.DAY,
                    }
                }
            ),
        ).product

        customer: Customer = customers_controller.create_customer(
            CreateCustomerRequest.from_dictionary(
                {
                    "customer": {
                        "first_name": "TestSubscriptionComponents_Customer_FirstName_1",
                        "last_name": "TestSubscriptionComponents_Customer_LastName_1",
                        "email": "tscce1@email.com",
                        "cc_emails": ["email@email.com"],
                        "organization": "TestSubscriptionComponents_CustomerOrganization_1",
                        "reference": "TestSubscriptionComponents_CustomerReference_1",
                        "address": "test address",
                        "address_2": "test address two",
                        "city": "Ohio",
                        "state": "TX",
                        "zip": "test zip",
                        "country": "US",
                        "phone": "+00 123 456 789",
                        "tax_exempt": False,
                        "vat_number": "test vat number",
                        "parent_id": None,
                        "locale": None,
                    }
                }
            )
        ).customer

        payment_profile: CreditCardPaymentProfile = payment_profiles_controller.create_payment_profile(
            CreatePaymentProfileRequest.from_dictionary(
                {
                    "payment_profile": {
                        "customer_id": customer.id,
                        "payment_type": PaymentType.CREDIT_CARD,
                        "expiration_month": 12,
                        "expiration_year": 2027,
                        "full_number": "4111111111111111",
                    }
                }
            )
        ).payment_profile

        on_off_component: Component = components_controller.create_on_off_component(
            product_family.id,
            CreateOnOffComponent.from_dictionary(
                {
                    "on_off_component": {
                        "name": "TestSubscriptionComponents_On_Off_Component_Name_1",
                        "unit_price": "1.0",
                        "prices": [{"unit_price": "0.10", "starting_quantity": "0"}],
                    }
                }
            ),
        ).component

        quantity_based_component: Component = components_controller.create_quantity_based_component(
            product_family.id,
            CreateQuantityBasedComponent.from_dictionary(
                {
                    "quantity_based_component": {
                        "name": "TestSubscriptionComponents_QuantityBased_Component_Name_1",
                        "unit_name": "Component",
                        "unit_price": "1.0",
                        "allow_fractional_quantities": True,
                        "pricing_scheme": PricingScheme.PER_UNIT,
                    }
                }
            ),
        ).component

        quantity_based_component_two: Component = components_controller.create_quantity_based_component(
            product_family.id,
            CreateQuantityBasedComponent.from_dictionary(
                {
                    "quantity_based_component": {
                        "name": "TestSubscriptionComponents_QuantityBased_Component_Name_2",
                        "unit_name": "Component",
                        "unit_price": "1.0",
                        "allow_fractional_quantities": True,
                        "pricing_scheme": PricingScheme.PER_UNIT,
                    }
                }
            ),
        ).component

        subscription: Subscription = subscriptions_controller.create_subscription(
            CreateSubscriptionRequest.from_dictionary(
                {
                    "subscription": {
                        "product_id": product.id,
                        "customer_id": customer.id,
                        "dunning_communication_delay_enabled": False,
                        "payment_collection_method": "automatic",
                        "skip_billing_manifest_taxes": False,
                        "payment_profile_id": payment_profile.id,
                    }
                }
            )
        ).subscription

        # THEN
        allocation: AllocationPreview = subscription_components_controller.preview_allocations(
            subscription.id,
            PreviewAllocationsRequest.from_dictionary(
                {
                    "allocations": [
                        {
                            "component_id": on_off_component.id,
                            "memo": "TestSubscriptionComponents_On_Off_Component_memo_1",
                            "quantity": "1",
                        },
                        {
                            "component_id": quantity_based_component.id,
                            "memo": "TestSubscriptionComponents_QuantityBased_Component_memo_1",
                            "quantity": "10.5",
                        },
                        {
                            "component_id": quantity_based_component_two.id,
                            "memo": "TestSubscriptionComponents_QuantityBased_Component_memo_2",
                            "quantity": 1,
                        },
                    ]
                }
            ),
        ).allocation_preview

        assert allocation.direction == "upgrade"
        assert len(allocation.allocations) == 3

        (
            on_off_component_allocation,
            quantity_based_component_allocation,
            quantity_based_component_two_allocation,
        ) = allocation.allocations

        assert on_off_component.id == on_off_component_allocation.component_id
        assert on_off_component_allocation.quantity == 1

        assert quantity_based_component.id == quantity_based_component_allocation.component_id
        assert quantity_based_component_allocation.quantity == "10.5"

        assert quantity_based_component_two.id == quantity_based_component_two_allocation.component_id
        assert quantity_based_component_two_allocation.quantity == "1.0"

        # AND
        allocated_components = subscription_components_controller.allocate_components(
            subscription.id,
            AllocateComponents.from_dictionary(
                {
                    "proration_upgrade_scheme": "prorate-attempt-capture",
                    "proration_downgrade_scheme": "no-prorate",
                    "allocations": [
                        {
                            "component_id": on_off_component.id,
                            "memo": "TestSubscriptionComponents_On_Off_Component_memo_1",
                            "quantity": "1",
                        },
                        {
                            "component_id": quantity_based_component.id,
                            "memo": "TestSubscriptionComponents_QuantityBased_Component_memo_1",
                            "quantity": "10.5",
                        },
                        {
                            "component_id": quantity_based_component_two.id,
                            "memo": "TestSubscriptionComponents_QuantityBased_Component_memo_2",
                            "quantity": 1,
                        },
                    ],
                }
            ),
        )

        assert len(allocated_components) == 3

        allocated_on_off_component, allocated_quantity_based_component, allocated_quantity_based_component_two = [
            component.allocation for component in allocated_components
        ]

        assert on_off_component.id == allocated_on_off_component.component_id
        assert on_off_component_allocation.quantity == allocated_on_off_component.quantity

        assert quantity_based_component.id == allocated_quantity_based_component.component_id
        assert quantity_based_component_allocation.quantity == allocated_quantity_based_component.quantity

        assert quantity_based_component_two.id == allocated_quantity_based_component_two.component_id
        assert allocated_quantity_based_component_two.quantity == allocated_quantity_based_component_two.quantity

        subscriptions_controller.purge_subscription(subscription.id, customer.id)
        customers_controller.delete_customer(customer.id)

    def test_allocate_components_given_on_off_component_with_invalid_quantity_then_raises_exception_with_422_status_code(
        self,
        components_controller: ComponentsController,
        customers_controller: CustomersController,
        payment_profiles_controller: PaymentProfilesController,
        product_families_controller: ProductFamiliesController,
        products_controller: ProductsController,
        subscription_components_controller: SubscriptionComponentsController,
        subscriptions_controller: SubscriptionsController,
    ):
        # GIVEN
        product_family: ProductFamily = product_families_controller.create_product_family(
            CreateProductFamilyRequest.from_dictionary(
                {
                    "product_family": {
                        "name": "TestSubscriptionComponents_Product_Family_Name_2",
                        "description": "TestSubscriptionComponents_Product_Family_Description_2",
                    }
                }
            )
        ).product_family

        product: Product = products_controller.create_product(
            product_family.id,
            CreateOrUpdateProductRequest.from_dictionary(
                {
                    "product": {
                        "name": "TestSubscriptionComponents_Product_Name_2",
                        "handle": "testsubscriptioncomponents_product_handle_2",
                        "description": "TestSubscriptionComponents_Product_Description_2",
                        "interval": 1,
                        "price_in_cents": 10,
                        "interval_unit": IntervalUnit.DAY,
                    }
                }
            ),
        ).product

        customer: Customer = customers_controller.create_customer(
            CreateCustomerRequest.from_dictionary(
                {
                    "customer": {
                        "first_name": "TestSubscriptionComponents_Customer_FirstName_2",
                        "last_name": "TestSubscriptionComponents_Customer_LastName_2",
                        "email": "tscce1@email.com",
                        "cc_emails": ["email@email.com"],
                        "organization": "TestSubscriptionComponents_CustomerOrganization_2",
                        "reference": "TestSubscriptionComponents_CustomerReference_2",
                        "address": "test address",
                        "address_2": "test address two",
                        "city": "Ohio",
                        "state": "TX",
                        "zip": "test zip",
                        "country": "US",
                        "phone": "+00 123 456 789",
                        "tax_exempt": False,
                        "vat_number": "test vat number",
                        "parent_id": None,
                        "locale": None,
                    }
                }
            )
        ).customer

        payment_profile: CreditCardPaymentProfile = payment_profiles_controller.create_payment_profile(
            CreatePaymentProfileRequest.from_dictionary(
                {
                    "payment_profile": {
                        "customer_id": customer.id,
                        "payment_type": PaymentType.CREDIT_CARD,
                        "expiration_month": 12,
                        "expiration_year": 2027,
                        "full_number": "4111111111111111",
                    }
                }
            )
        ).payment_profile

        on_off_component: Component = components_controller.create_on_off_component(
            product_family.id,
            CreateOnOffComponent.from_dictionary(
                {
                    "on_off_component": {
                        "name": "TestSubscriptionComponents_On_Off_Component_Name_2",
                        "unit_price": "1.0",
                        "prices": [{"unit_price": "0.10", "starting_quantity": "0"}],
                    }
                }
            ),
        ).component

        subscription: Subscription = subscriptions_controller.create_subscription(
            CreateSubscriptionRequest.from_dictionary(
                {
                    "subscription": {
                        "product_id": product.id,
                        "customer_id": customer.id,
                        "dunning_communication_delay_enabled": False,
                        "payment_collection_method": "automatic",
                        "skip_billing_manifest_taxes": False,
                        "payment_profile_id": payment_profile.id,
                    }
                }
            )
        ).subscription
        # THEN

        with pytest.raises(ComponentAllocationErrorException) as exc_info:
            subscription_components_controller.preview_allocations(
                subscription.id,
                AllocateComponents.from_dictionary(
                    {
                        "proration_upgrade_scheme": "prorate-attempt-capture",
                        "proration_downgrade_scheme": "no-prorate",
                        "allocations": [
                            {
                                "component_id": on_off_component.id,
                                "memo": "TestSubscriptionComponents_On_Off_Component_memo_1",
                                "quantity": "20",
                            },
                        ],
                    }
                ),
            )

        error: ComponentAllocationErrorItem = exc_info.value.errors[0]

        assert exc_info.value.response_code == 422
        assert error.component_id == on_off_component.id
        assert error.kind == "allocation"
        assert error.message == "Quantity: must be either 1 (on) or 0 (off)."
        assert error.on == "quantity"

        subscriptions_controller.purge_subscription(subscription.id, customer.id)
        customers_controller.delete_customer(customer.id)
