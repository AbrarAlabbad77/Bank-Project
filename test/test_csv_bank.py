import unittest
import csv
from bank.customer import Customer
# from bank.csv_bank import addNewCustomer
from bank.csv_bank import search

# python3 -m unittest test.test_csv_bank

class test_AddCustmer(unittest.TestCase):
    
    def setUp(self):
        self.fileObject = 'bank.csv'
      
    def test_add_customer(self):
        customer = Customer('1','Reema', 'Ahmed', '555', '10', '20')
        addNewCustomer(customer)

        with open(self.fileObject, 'r', newline='') as file:
            reader = list(csv.reader(file))           
            self.assertIn(['1','Reema', 'Ahmed', '555', '10', '20'],reader)

    
class test_search(unittest.TestCase):
    def test_search_found(self):
        result = search("77", "777")   
        self.assertIsInstance(result, Customer)

    def test_search_not_found(self):
        result = search("999", "wrong")
        self.assertFalse(result)
    
    