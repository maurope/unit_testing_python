import pytest
from src.bank_account import BankAccount

def test_sum():
    a = 4
    b = 4
    assert a + b == 8



@pytest.mark.parametrize('amount, expected', [
    (100, 1100),
    (3000, 4000),
    (4500, 5500),
    ])
def test_deposit_multiple_ammounts(amount, expected):
    account = BankAccount(balance=1000, log_file='transactions.txt')
    new_balance = account.deposit(amount)
    assert new_balance == expected




# TODO: Create a test that doesn´t allow the deposit to be negative
def test_deposit_negative_amount():
    account = BankAccount(balance=1000, log_file='transactions.txt')
    with pytest.raises(ValueError):
        account.deposit(-100)

