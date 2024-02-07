from advancedbilling.models.credit_card_payment_profile import CreditCardPaymentProfile
from advancedbilling.models.customer import Customer
from advancedbilling.models.product import Product


class SubscriptionsAssertCases:
    @staticmethod
    def get_subscription_data(product: Product, customer: Customer, payment_profile: CreditCardPaymentProfile) -> dict:
        return {
            "product": {
                "id": product.id,
            },
            "customer": {
                "id": customer.id,
            },
            "payment_type": payment_profile.payment_type,
            "state": "active",
            "total_revenue_in_cents": 410,
            "product_price_in_cents": 10,
            "product_version_number": 1,
            "cancellation_message": None,
            "cancellation_method": None,
            "cancel_at_end_of_period": None,
            "canceled_at": None,
            "previous_state": "active",
            "signup_revenue": "4.10",
            "coupon_code": None,
            "snap_day": None,
            "payment_collection_method": "automatic",
            "credit_card": {
                "card_type": "visa",
                "current_vault": "bogus",
                "customer_id": customer.id,
            },
            "group": None,
            "referral_code": None,
            "next_product_id": None,
            "next_product_handle": None,
            "coupon_use_count": None,
            "coupon_uses_allowed": None,
            "reason_code": None,
            "automatically_resume_at": None,
            "offer_id": None,
            "payer_id": None,
            "product_price_point_type": "default",
            "next_product_price_point_id": None,
            "net_terms": None,
            "stored_credential_transaction_id": None,
            "reference": None,
            "on_hold_at": None,
            "dunning_communication_delay_enabled": False,
            "dunning_communication_delay_time_zone": None,
            "receives_invoice_emails": None,
            "locale": None,
            "currency": "USD",
            "scheduled_cancellation_at": None,
        }
