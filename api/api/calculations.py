def add(a: int, b: int):
    return a + b

def subtract(a: int, b: int):
    return a - b

def multiply(a: int, b: int):
    return a * b

def divide(a: int, b: int):
    return a / b


class BankAccount:
    def __init__(self, balance: int = 0):
        self.balance = balance

    def deposit(self, amount: int):
        self.balance += amount

    def withdraw(self, amount: int):
        self.balance -= amount

    def collect_interest(self, rate: float = 1.1):
        self.balance = round(self.balance * rate, 2)
