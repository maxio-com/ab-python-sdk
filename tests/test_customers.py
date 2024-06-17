import pytest

from advancedbilling.exceptions.customer_error_response_exception import CustomerErrorResponseException
from advancedbilling.controllers.customers_controller import CustomersController
from advancedbilling.models.create_customer_request import CreateCustomerRequest
from tests.data import InitCases


class TestCustomers:
    def test_invalid_customer_creation_throws_422_error(self, customers_controller: CustomersController):
        customer_request = CreateCustomerRequest(InitCases.get_customer_request())
        customers_controller.create_customer(
            customer_request
        )

        with pytest.raises(CustomerErrorResponseException) as e:
            customers_controller.create_customer(
                customer_request
            )

        assert e.value.response_code == 422
        assert e.value.errors == ['Reference: must be unique - that value has been taken.']