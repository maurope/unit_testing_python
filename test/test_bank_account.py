import unittest
from src.bank_account import BankAccount

class BankAccountTest(unittest.TestCase):

    def setUp(self) -> None:                        #The method setUp empty and is always called so we can use it
        self.account = BankAccount(balance = 1000) 

    def test_deposit(self):
        new_balance = self.account.deposit(500)
        assert new_balance == 1500

    def test_withdraw(self):
        new_balance = self.account.withdraw(200)
        assert new_balance == 800

    def test_get_balance(self):
        assert self.account.get_balance() == 1000
