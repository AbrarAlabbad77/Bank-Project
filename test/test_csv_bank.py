import unittest
# from csv_bank import addNewCustomer
import bank.csv_bank
from bank.customer import Customer

# python3 -m unittest test.test_csv_bank

class test_AddCustmer(unittest.TestCase):
    
    def setUp(self):
        self.fileObject = 'bank.csv'
      
    def test_add_customer(self):
        self.customer = Customer('Abrar', 'Mahdi', '123', '10', '20')
        self.file = csv_bank 
        self.file.addNewCustomer(customer)
    

        with open(self.test_file, 'r', newline='') as file:
            reader = list(csv.reader(file))
            # 2 rows: header + 1 customer
            self.assertEqual(len(reader), 2)
            row = reader[1]
            self.assertEqual(row[0], 'Abrar')
            self.assertEqual(row[1], 'Mahdi')
            self.assertEqual(row[2], '123')
            self.assertEqual(row[3], '10')
            self.assertEqual(row[4], '20')
    
        