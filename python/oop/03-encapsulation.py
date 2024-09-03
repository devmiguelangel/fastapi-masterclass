"""
Encapsulation

Encapsulation refers to the bundling of data (attributes) and methods (functions) that operate on the data into a single unit, or class.
It restricts direct access to some of an object's components, which means the internal representation of an object is hidden from the outside. Only specific methods are exposed, making it easier to prevent unauthorized access and changes.
This concept helps in safeguarding the state of an object by allowing only controlled access and modifications. It typically involves using private or protected access specifiers.

Step-by-step Example:
1. Define a Class with Private Attributes: We'll create a class BankAccount with a private attribute _balance.
2. Provide Public Methods: We'll use public methods to interact with the balance, like deposit() and withdraw(), ensuring that any changes to the balance are validated.

"""

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f'Deposited ${amount}. New balance: ${self.__balance}')
        else:
            print('Deposit amount must be greater than 0')

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f'Withdrew ${amount}. New balance: ${self.__balance}')
        else:
            print('Insufficient balance or invalid withdrawal amount')

    def get_balance(self):
        return self.__balance

account1 = BankAccount(account_number='12345', balance=1000)
print(f'Account Number: {account1.account_number}')
account1.deposit(500)
account1.withdraw(200)

print(f'Current Balance: ${account1.get_balance()}')

# Try to access the private attribute directly
# print(account1.__balance)  # This will raise an error
