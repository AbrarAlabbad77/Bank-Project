import csv
from bank.customer import Customer
# from .customer import Customer

class csvFile:
    # cearte the reader to read  from a CSV file
    with open('bank.csv', 'r', newline='') as file:
        # reader = csv.reader(file)
        reader = list(csv.reader(file))
        

    def search(idd , password):
        with open('bank.csv', 'r', newline='') as file:
            reader = list(csv.DictReader(file))
            for row in reader:
                if idd.strip() == row['id'].strip() and password.strip()== row["Password"].strip():
                    return row["FirstaName"].strip()+' '+row["SecondName"].strip()
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


