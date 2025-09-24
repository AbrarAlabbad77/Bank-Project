import unittest
import csv
from bank.customer import Customer
from bank.csv_bank import csvFile
from main import customerNotFoundError
#  python3 -m unittest test.test_csv_bank

class test_AddCustmer(unittest.TestCase):
    
    def setUp(self):
        self.fileObject = 'bank.csv'
      
    def test_add_customer(self):
        customer = Customer('1','Reema', 'Ahmed', '555', '10', '20','active')
        csvFile.addNewCustomer(customer)

        with open(self.fileObject, 'r', newline='') as file:
            reader = list(csv.reader(file))           
            self.assertIn(['1','Reema', 'Ahmed', '555', '10', '20','active'],reader)

    
class test_search(unittest.TestCase):
    def test_search_found(self):
        result = csvFile.search("77", "777")   
        self.assertIsInstance(result, Customer)

    def test_search_not_found(self):
        result = csvFile.search("9999", "66")
        with self.assertRaises(customerNotFoundError):
            raise customerNotFoundError("Paaword or Id not correct, Please try again !")
    