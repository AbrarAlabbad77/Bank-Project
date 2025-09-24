import unittest
import csv 
from bank.customer import Customer
from bank.account import Withdraw
# python3 -m unittest test.test_account

class test_withdraw(unittest.TestCase):
    def setUp(self):
        self.customer = Customer ("99", "Abrar", "Ahmed", "999", "100", "600", "active")
        
    def test_withdraw_checking(self):
        self.customer.balancCheckingAccount = "600"
        withdrawObject = Withdraw(self.customer)
        new_balance = int(self.customer.balancCheckingAccount) - 50
        withdrawObject.customer.balancCheckingAccount = new_balance
        self.assertEqual(int(withdrawObject.customer.balancCheckingAccount), 550)
        
    def test_withdraw_saving(self):
        self.customer.balancSavingAccount = "100"
        withdrawObject = Withdraw(self.customer)
        new_balance = int(self.customer.balancSavingAccount)  - 50 
        withdrawObject.customer.balancSavingAccount = new_balance
        self.assertEqual(int(withdrawObject.customer.balancSavingAccount), 50)

