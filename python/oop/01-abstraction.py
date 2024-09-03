"""
Abstraction

Abstraction allows us to focus on the what of an object rather than the how. It's about defining the necessary attributes and behaviors of an object and hiding the complex implementation details.

Real-World Example of Abstraction
Let's consider a real-world scenario where we need to create a system for managing different types of payment methods.
We could use abstraction to define a generic payment process, and then create specific implementations for each payment type, such as credit card, PayPal, or cryptocurrency.

Step-by-step Example:
1. Define an Abstract Class: We'll start by creating an abstract class called Payment that defines the structure of a payment method.
2. Abstract Methods: This class will have abstract methods like authorize() and pay() that any subclass must implement.
3. Subclasses: We'll create specific subclasses like CreditCardPayment and PayPalPayment that implement these methods.
"""

from abc import ABC, abstractmethod

# Define an abstract class
class Payment(ABC):
    @abstractmethod
    def authorize(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass

# Create a subclass for credit card payments
class CreditCarPayment(Payment):
    def authorize(self):
        print('Authorizing credit card payment')

    def pay(self, amount):
        print(f'Paying ${amount} using credit card')

# Create a subclass for PayPal payments
class PayPalPayment(Payment):
    def authorize(self):
        print('Authorizing PayPal payment')

    def pay(self, amount):
        print(f'Paying ${amount} using PayPal')

# Create instances of the subclasses
credit_card = CreditCarPayment()
paypal = PayPalPayment()

# Call the methods
credit_card.authorize()
credit_card.pay(100)

paypal.authorize()
paypal.pay(50)

