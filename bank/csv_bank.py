import csv
from bank.customer import Customer
# from .customer import Customer

class csvFile:
    # cearte the reader to read  from a CSV file
    with open('bank.csv', 'r', newline='') as file:
        # reader = csv.reader(file)
        reader = list(csv.reader(file))
        

    def search(idd , password):
        for row in reader:
            #if current rows 2nd value is equal to input, print that row
            if id == row[1] and password == row[4]:
                return row[2]+row[3]
            else:
                return False


    def reading():
        with open('bank.csv', 'r', newline='') as file:
            # reader = csv.reader(file)
            reader = list(csv.reader(file))
            for row in reader:
                print(row[0])



    #  writing into the csv file 
    def addNewCustomer(Customer):
            # reader = list(csv.reader(file))
        with open('bank.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([Customer.id,Customer.firstName, Customer.secondName,Customer.password,
                            Customer.balancSavingAccount, Customer.balancCheckingAccount])


