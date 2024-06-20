import pytest

from api.calculations import BankAccount, add, divide, multiply, subtract


@pytest.mark.parametrize('a, b, expected', [
    (1, 1, 2),
    (2, 3, 5),
    (4, 5, 9),
    (10, 2, 12),
])
def test_add(a, b, expected):
    assert add(a, b) == expected


def test_subtract():
    assert subtract(1, 1) == 0


def test_multiply():
    assert multiply(3, 4) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_bank_account_initial_balance():
    bank_account = BankAccount(30)
    assert bank_account.balance == 30


def test_bank_account_default_balance():
    bank_account = BankAccount()
    assert bank_account.balance == 0


def test_bank_account_deposit():
    bank_account = BankAccount(30)
    bank_account.deposit(20)
    assert bank_account.balance == 50


def test_bank_account_withdraw():
    bank_account = BankAccount(30)
    bank_account.withdraw(20)
    assert bank_account.balance == 10


def test_bank_account_collect_interest():
    bank_account = BankAccount(100)
    bank_account.collect_interest(1.1)
    assert bank_account.balance == 110
