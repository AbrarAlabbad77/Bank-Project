from bank.customer import Customer
from bank.csv_bank import csvFile
from bank.account import Withdraw, Deposit, Transfer
from bank.error import customerNotFoundError

# python3 main.py

def customerInfo():
    print("Hello , welcome to our bank !! ")
    idd = input("Enter Id : ")
    fname = input("Enter First Name : ")
    lname = input("Enter last Name : ")
    password = input("Enter Password : ")
    saving = input("Enter Saving account inital Balance : ")
    checking = input("Enter Checking account inital Balance : ")
    state = "active"
    
    return Customer(idd, fname, lname, password, saving, checking, state , 0)


def userLogin():
    print("Enter Your id and password to login ")
    idd = input("Enter Id : ")
    password = input("Enter Password : ")
    
    #  sraech for the user info
    customer_result = csvFile.search(idd, password)
    if customer_result == False :
        raise customerNotFoundError("Paaword or Id not correct, Please try again !")
        return False
    else:
       print(f'Weclome {customer_result} !! ')
       while(True):
            print("What action do you want to preform")
            print(" 1/ Withdraw ")
            print(" 2/ Deposit ")
            print(" 3/ Transfer ")
            print(" 4/ log out ")
            choose = int(input('Enter Your choose number'))
    
            match choose :
                case 1 :
                    Withdraw_object = Withdraw(customer_result)
                    Withdraw_object.withdraw_operation()
                case 2 :
                    deposit_object = Deposit(customer_result)
                    deposit_object.deposit_operation()
                case 3 :
                    try:
                        transfer_object = Transfer(customer_result)
                        transfer_object.transfer_operation()
                    except Exception as e:
                        print("Unexpected Error:", e)
                    
                case 4 : 
                    print("Logining out...")
                    break
           
                    


#  main flow 
if __name__ == "__main__":
    while(True):
        print("What action do you want to preform")
        print(" 1/ Add New Customer ")
        print(" 2/ Log in ")
        print(" 3/ Exit ")
        userChoose = int(input('Enter Your choose number'))
        
        match userChoose:
            case 1 :
                new_customer = customerInfo()
                # file = bank.csv_bank 
                file = csvFile
                file.addNewCustomer(new_customer)
                print(f'Welcome , {new_customer.FirstName }   Added Sueccssflly')
            case 2:
                try:
                    userLogin()
                except Exception as e:
                    print("Unexpected Error:", e)
            case 3 :
                print("Exiting...")
                break 

    

 
    