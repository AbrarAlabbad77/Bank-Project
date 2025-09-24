import csv
from bank.customer import Customer
# from .customer import Customer

class csvFile:
    
    def search(idd , password):
        with open('bank.csv', 'r', newline='') as file:
            reader = list(csv.DictReader(file))
            for row in reader:
                if idd.strip() == row['id'].strip() and password.strip()== row["password"].strip():
                    # return row["FirstaName"].strip()+' '+row["SecondName"].strip()
                    return Customer(
                    row["id"].strip(),
                    row["FirstName"].strip(),
                    row["lastName"].strip(),
                    row["password"].strip(),
                    row["SavingBalance"].strip(),
                    row["checkingBalacne"].strip(),
                    row["state"].strip())
            return False


    def reading():
        with open('bank.csv', 'r', newline='') as file:
            reader = list(csv.reader(file))
            for row in reader:
                print(row[0])



    #  writing into the csv file 
    def addNewCustomer(Customer):
            # reader = list(csv.reader(file))
        with open('bank.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([Customer.id,Customer.FirstName, Customer.secondName,Customer.password,
                            Customer.balancSavingAccount, Customer.balancCheckingAccount, Customer.state])


