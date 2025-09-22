from customer import Customer
import csv_bank

print("What action do you want to preform")
print(" 1/ Add New Customer ")
print(" 2/ Log in ")
print(" 2/ Exit ")

# createing a new customer and pass it info
new_customer = Customer('Abrar','Mahdi','123','10','20')
file = csv_bank 
file.addNewCustomer(new_customer)
    

