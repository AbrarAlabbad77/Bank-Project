import csv
from customer import Customer

# def header(filename='bank.csv'):
#     with open(filename, 'a', newline='') as file:
#         writer = csv.writer(file)
#         writer.writerow(['First Name', 'Second Name','Password', 'Balance Saving Account', 'Balance Checking Account'])

def addNewCustomer(Customer):
    idd = 1000 
    # Use w to overwrite a file, use a to append to a file (w is probably fine)
    with open('bank.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([Customer.firstName, Customer.secondName,Customer.password,
                         Customer.balancSavingAccount, Customer.balancCheckingAccount])


# Reading from a CSV file
with open('bank.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0])