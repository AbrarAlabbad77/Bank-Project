from bank.customer import Customer
# import bank.csv_bank 
from bank.csv_bank import csvFile
# python3 main.py

# Error Exception classes 
class customerNotFoundError(Exception):
    pass




def customerInfo():
    print("Hello , welcome to our bank !! ")
    idd = input("Enter Id : ")
    fname = input("Enter First Name : ")
    lname = input("Enter last Name : ")
    password = input("Enter Password : ")
    saving = input("Enter Saving account inital Balance : ")
    checking = input("Enter Checking account inital Balance : ")
    
    return Customer(idd, fname, lname, password, saving, checking)


def userLogin():
    print("Enter Your id and password to login ")
    idd = input("Enter Id : ")
    password = input("Enter Password : ")
    
    #  sraech for the user info
   result = csvFile.search(idd,password)
   if(result == False):
        raise customerNotFoundError("Paaword or Id not correct, Please try again !")
   else:
       Print(f'Weclome {result} !! ')
       whilte(True):
            print("What action do you want to preform")
            print(" 1/ Withdraw ")
            print(" 2/ Deposit ")
            print(" 3/ Transfer ")
            print(" 4/ log out ")
            choose = int(input('Enter Your choose number'))
    
            match choose :
                case 1 :
                    pass
                case 2 :
                    pass 
                case 3 :
                    pass 
                case 4 : 
                    pass
                    
                 
            
                
       
       
   
   

try:
    userLogin()
except customerNotFoundError as e:
        print("Formula Error:", e) 
except Exception as e:
        print("Unexpected Error:", e)            
    




#  main flow 
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

    


    
    