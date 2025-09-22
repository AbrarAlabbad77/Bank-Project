from bank.customer import Customer
import bank.csv_bank


# python3 main.py


def customerInfo():
    print("Hello , welcome to our bank !! ")
    idd = input("Enter Id : ")
    fname = input("Enter First Name : ")
    lname = input("Enter last Name : ")
    password = input("Enter Password : ")
    saving = input("Enter Saving account inital Balance : ")
    checking = input("Enter Checking account inital Balance : ")
    
    return Customer(idd, fname, lname, password, saving, checking)
    

while(True):
    print("What action do you want to preform")
    print(" 1/ Add New Customer ")
    print(" 2/ Log in ")
    print(" 3/ Exit ")
    userChoose = int(input('Enter Your choose number'))
    
    match userChoose:
        case 1 :
            # createing a new customer and pass it info
            # new_customer = Customer('1','Rema','Ahmed','123','10','20')
            new_customer = customerInfo()
            file = bank.csv_bank 
            file.addNewCustomer(new_customer)
            print(f'Welcome , {new_customer.fname}  /n Added Sueccssflly')
        case 2:  
            print('in case 2')
        case 3 :
            print("Exiting...")
            break 

    


    
    