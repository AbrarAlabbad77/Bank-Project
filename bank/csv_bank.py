import csv
from customer import Customer

# data = [
#     ['First Name', 'Second Name ', 'Password' , "Balanc Saving Account", "Balanc checking Account"],
#     # ['Abrar', 25, 'Dammam']
# ]
def header(filename='bank.csv'):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['First Name', 'Second Name', 'ID','Password', 'Balance Saving Account', 'Balance Checking Account'])

idd = 1000
def addNewCustomer(Customer):
    # Use w to overwrite a file, use a to append to a file (w is probably fine)
    with open('bank.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(Customer)
        idd = idd+1
        writer.writerow([Customer.firstName, Customer.secondName, idd,Customer.password,
                         Customer.balancSavingAccount, Customer.balancCheckingAccount])


# Reading from a CSV file
with open('bank.csv', 'r', newline='') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row[0])