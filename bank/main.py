from .customer import Customer
import bank.csv_bank


# python3 bank/main.py

while(True):
    print("What action do you want to preform")
    print(" 1/ Add New Customer ")
    print(" 2/ Log in ")
    print(" 2/ Exit ")
    userChoose = int(input('Enter Your choose number'))

    match userChoose:
        case 1 :
            # createing a new customer and pass it info
            new_customer = Customer('Ahmad','Mahdi','123','10','20')
            
            #  create file object and pass the customer to it 
            file = csv_bank 
            file.addNewCustomer(new_customer)
        case 2:  
            print('in case 2')
        case 3 :
            print("Exiting...")
            break 

    