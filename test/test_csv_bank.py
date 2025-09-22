import unittest
import csv
from bank.customer import Customer
from bank.csv_bank import addNewCustomer

# python3 -m unittest test.test_csv_bank

class test_AddCustmer(unittest.TestCase):
    
    def setUp(self):
        self.fileObject = 'bank.csv'
      
    def test_add_customer(self):
        customer = Customer('Reema', 'Ahmed', '555', '10', '20')
        addNewCustomer(customer)

        with open(self.fileObject, 'r', newline='') as file:
            reader = list(csv.reader(file))           
            self.assertIn(['Reema', 'Ahmed', '555', '10', '20'],reader)
            # self.assertEqual(len(reader), 5)
            # row = reader[1]
            # self.assertEqual(row[0], 'Reema')
            # self.assertEqual(row[1], 'Ahmed')
            # self.assertEqual(row[2], '123')
            # self.assertEqual(row[3], '10')
            # self.assertEqual(row[4], '20')
    
        