import csv
from bank.customer import Customer
# from .customer import Customer


def heading():
    with open('bank.csv', 'r', newline='') as file:
        reader = list(csv.reader(file))
        if len(reader) == 3:   # empty file
            next_id = 3
        else:
            next_id = len(reader) 
        
    with open('bank.csv', 'a', newline='') as file:
        writer = csv.writer(file)   
        if len(reader) == 3:
            writer.writerow(["ID", "FirstName", "LastName", "Password", "BalanceSaving", "BalanceChecking"])
    

# Reading from a CSV file
def reading():
    with open('bank.csv', 'r', newline='') as file:
        # reader = csv.reader(file)
        reader = list(csv.reader(file))
        for row in reader:
            print(row[0])


def addNewCustomer(Customer):
    idd = 1000 
        
        # reader = list(csv.reader(file))
    with open('bank.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([Customer.firstName, Customer.secondName,Customer.password,
                         Customer.balancSavingAccount, Customer.balancCheckingAccount])


