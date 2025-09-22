import csv
from bank.customer import Customer

# def header(filename='bank.csv'):
#     with open(filename, 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['First Name', 'Second Name','Password', 'Balance Saving Account', 'Balance Checking Account'])

def addNewCustomer(Customer):
    idd = 1000 
    with open('bank.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([Customer.firstName, Customer.secondName,Customer.password,
                         Customer.balancSavingAccount, Customer.balancCheckingAccount])


# Reading from a CSV file
def reading():
    with open('bank.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(row[0])