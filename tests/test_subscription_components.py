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
from advancedbilling.models.preview_allocations_request import PreviewAllocationsRequest
from advancedbilling.models.product import Product
from advancedbilling.models.product_family import ProductFamily
from advancedbilling.models.subscription import Subscription

from .data import InitCases, SubscriptionsComponentsAssertCases
from .utils import assert_properties


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
            CreateProductFamilyRequest(InitCases.get_product_family_request())
        ).product_family

        product: Product = products_controller.create_product(
            product_family.id,
            CreateOrUpdateProductRequest(InitCases.get_product_request()),
        ).product

        customer: Customer = customers_controller.create_customer(
            CreateCustomerRequest(InitCases.get_customer_request())
        ).customer

        payment_profile: CreditCardPaymentProfile = payment_profiles_controller.create_payment_profile(
            CreatePaymentProfileRequest(InitCases.get_payment_profile_request(customer.id))
        ).payment_profile

        on_off_component: Component = components_controller.create_on_off_component(
            product_family.id,
            CreateOnOffComponent(InitCases.get_on_off_component_data()),
        ).component

        quantity_based_component: Component = components_controller.create_quantity_based_component(
            product_family.id,
            CreateQuantityBasedComponent(InitCases.get_quantity_based_component_data()),
        ).component

        quantity_based_component_two: Component = components_controller.create_quantity_based_component(
            product_family.id,
            CreateQuantityBasedComponent(InitCases.get_quantity_based_component_data()),
        ).component

        subscription: Subscription = subscriptions_controller.create_subscription(
            CreateSubscriptionRequest(InitCases.get_subscription_request(product.id, customer.id, payment_profile.id))
        ).subscription

        # THEN
        allocation: AllocationPreview = subscription_components_controller.preview_allocations(
            subscription.id,
            PreviewAllocationsRequest(
                InitCases.get_allocation_request(
                    on_off_component.id, quantity_based_component.id, quantity_based_component_two.id
                )
            ),
        ).allocation_preview

        assert allocation.direction == "upgrade"
        assert len(allocation.allocations) == 3

        (
            on_off_component_allocation,
            quantity_based_component_allocation,
            quantity_based_component_two_allocation,
        ) = allocation.allocations

        assert_properties(
            on_off_component_allocation,
            SubscriptionsComponentsAssertCases.get_on_off_component_data(on_off_component.id, expected_quantity=1),
        )
        assert_properties(
            quantity_based_component_allocation,
            SubscriptionsComponentsAssertCases.get_quantity_based_component_data(
                quantity_based_component.id, expected_quantity="10.5"
            ),
        )
        assert_properties(
            quantity_based_component_two_allocation,
            SubscriptionsComponentsAssertCases.get_quantity_based_component_data(
                quantity_based_component_two.id, expected_quantity="1.0"
            ),
        )

        # AND
        allocated_components = subscription_components_controller.allocate_components(
            subscription.id,
            AllocateComponents(
                proration_upgrade_scheme="prorate-attempt-capture",
                proration_downgrade_scheme="no-prorate",
                allocations=InitCases.get_allocation_request(
                    on_off_component.id, quantity_based_component.id, quantity_based_component_two.id
                ),
            ),
        )

        assert len(allocated_components) == 3

        allocated_on_off_component, allocated_quantity_based_component, allocated_quantity_based_component_two = [
            component.allocation for component in allocated_components
        ]

        assert_properties(
            allocated_on_off_component,
            SubscriptionsComponentsAssertCases.get_on_off_component_data(
                on_off_component.id, expected_quantity=on_off_component_allocation.quantity
            ),
        )

        assert_properties(
            allocated_quantity_based_component,
            SubscriptionsComponentsAssertCases.get_quantity_based_component_data(
                quantity_based_component.id, expected_quantity=quantity_based_component_allocation.quantity
            ),
        )

        assert_properties(
            allocated_quantity_based_component_two,
            SubscriptionsComponentsAssertCases.get_quantity_based_component_data(
                quantity_based_component_two.id, expected_quantity=quantity_based_component_two_allocation.quantity
            ),
        )

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
            CreateProductFamilyRequest(InitCases.get_product_family_request())
        ).product_family

        product: Product = products_controller.create_product(
            product_family.id,
            CreateOrUpdateProductRequest(InitCases.get_product_request()),
        ).product

        customer: Customer = customers_controller.create_customer(
            CreateCustomerRequest(InitCases.get_customer_request())
        ).customer

        payment_profile: CreditCardPaymentProfile = payment_profiles_controller.create_payment_profile(
            CreatePaymentProfileRequest(InitCases.get_payment_profile_request(customer.id))
        ).payment_profile

        on_off_component: Component = components_controller.create_on_off_component(
            product_family.id,
            CreateOnOffComponent(InitCases.get_on_off_component_data()),
        ).component

        subscription: Subscription = subscriptions_controller.create_subscription(
            CreateSubscriptionRequest(InitCases.get_subscription_request(product.id, customer.id, payment_profile.id))
        ).subscription
        # THEN

        with pytest.raises(ComponentAllocationErrorException) as exc_info:
            subscription_components_controller.preview_allocations(
                subscription.id,
                AllocateComponents(
                    proration_upgrade_scheme="prorate-attempt-capture",
                    proration_downgrade_scheme="no-prorate",
                    allocations=[
                        {
                            "component_id": on_off_component.id,
                            "memo": "TestSubscriptionComponents_On_Off_Component_memo_1",
                            "quantity": "20",
                        },
                    ],
                ),
            )

        assert exc_info.value.response_code == 422
        error: ComponentAllocationErrorItem = exc_info.value.errors[0]

        assert error.component_id == on_off_component.id
        assert error.kind == "allocation"
        assert error.message == "Quantity: must be either 1 (on) or 0 (off)."
        assert error.on == "quantity"

        subscriptions_controller.purge_subscription(subscription.id, customer.id)
        customers_controller.delete_customer(customer.id)
