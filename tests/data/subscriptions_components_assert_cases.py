class SubscriptionsComponentsAssertCases:
    @staticmethod
    def get_on_off_component_data(on_off_component_id: int, expected_quantity: int | str) -> dict:
        return {
            "component_id": on_off_component_id,
            "quantity": expected_quantity,
        }

    @staticmethod
    def get_quantity_based_component_data(quantity_based_component_id: int, expected_quantity: int | str) -> dict:
        return {
            "component_id": quantity_based_component_id,
            "quantity": expected_quantity,
        }
