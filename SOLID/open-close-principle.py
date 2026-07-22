from abc import ABC, abstractmethod
# Base class for payment processing
class PaymentProcessor(ABC):
    @abstractmethod
    def processPayment(self, amount):
        pass
# Concrete implementation for credit card payment processing
class CreditCardPaymentProcessor(PaymentProcessor):
    def processPayment(self, amount):
        print(f"Processing credit card payment of ${amount:.2f}")

# Now we want to extend the functionality to support PayPal payments. We can create a new class that inherits from PaymentProcessor and implements the processPayment method for PayPal.
class PayPalPaymentProcessor(PaymentProcessor):
    def processPayment(self, amount):
        print(f"Processing PayPal payment of ${amount:.2f}")

# Example usage- use either CreditCardPaymentProcessor or PayPalPaymentProcessor without modifying the existing code.
def main():
    # Create an instance of CreditCardPaymentProcessor
    credit_card_processor = CreditCardPaymentProcessor()
    credit_card_processor.processPayment(100.00)

    # Create an instance of PayPalPaymentProcessor
    paypal_processor = PayPalPaymentProcessor()
    paypal_processor.processPayment(150.00)

if __name__ == "__main__":
    main()