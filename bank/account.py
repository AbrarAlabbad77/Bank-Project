import csv
from bank.customer import Customer
from bank.csv_bank import csvFile
from bank.error import customerNotFoundError
from bank.error import NagitveBalancError, balanceNotEnoghError




class Withdraw():
    def __init__(self, customer):
        self.customer = customer
        # self.withdraw_operation()
        
        
    def withdraw_operation(self):
        
        if self.customer.state == 'inactive':
            raise NagitveBalancError('Your account is deactivated due to overdrafts.')
            return
        
        print("Do You want to withdraw from Saving or checking account ?")
        print("Enter 1 for checking")
        print("      2 for saving")
        userChoose = int(input(''))
        
        match userChoose:
            case 1 :
                print(f'Your current checking Balance :,{self.customer.balancCheckingAccount} ...') 
                amount = int(input('Enter the amount you want to withdraw'))
                if(int(self.customer.balancCheckingAccount) <= 0):
                    if(amount>100):
                        raise NagitveBalancError("sorry [Nagitive Mode]! you can not withdraw more than $100")
                        return
                # self.customer.balancCheckingAccount = int(self.customer.balancCheckingAccount) - amount
                temp_balance = int(self.customer.balancCheckingAccount) - amount
                
                # handle overdraft 
                if temp_balance <= -100:
                    raise raise NagitveBalancError("withdraw denied")
                    return
                
                if temp_balance < 0 :
                    print("overdraft happen ! it cost 35$ ")
                    temp_balance = temp_balance - 35
                    self.customer.overdraftCounter = self.overdraftCounter + 1
                    
                    if self.customer.overdraftCounter == 2 :
                        self.customer.state ="inactive"
                
                self.customer.balancCheckingAccount = temp_balance
                print(f" Withdraw successfuly. New Checking Balance: {self.customer.balancCheckingAccount}")
                update_balance(self.customer)     
            case 2 :
                print(f'Your current saving Balance :,{self.customer.balancSavingAccount} ...') 
                amount = int(input('Enter the amount you want to withdraw'))
                if(int(self.customer.balancSavingAccount) <= 0):
                    if(amount>100):
                        raise NagitveBalancError("sorry [Nagitive Mode]! you can not withdraw more than $100")
                        return
                # self.customer.balancSavingAccount = int(self.customer.balancSavingAccount) - amount
                temp_balance = int(self.customer.balancSavingAccount) - amount
                
                # handle overdraft 
                if temp_balance < -100:
                    raise  NagitveBalancError("withdraw denied")
                    return
                
                if temp_balance < 0 :
                    print("overdraft happen ! it cost 35$ ")
                    temp_balance = temp_balance - 35
                    self.customer.overdraftCounter = self.customer.overdraftCounter + 1
                    
                    if self.customer.overdraftCounter == 2 :
                        self.customer.state ="inactive"
                
                self.customer.balancSavingAccount = temp_balance
                print(f" Withdraw successfuly. New Saving Balance: {self.customer.balancSavingAccount}")
                update_balance(self.customer)  
                   
            
# #  # update the csv file after witdrawing from cheking account 
# def update_checking_balance(updated_customer):
#     all_rows = []
#     with open('bank.csv', 'r', newline='') as file:
#         reader = list(csv.DictReader(file))
#         for row in reader:
#             if str(updated_customer.id) == row['id'] and str(updated_customer.password)== row["password"]:
#                 row['checkingBalacne'] = str(updated_customer.balancCheckingAccount)
#             all_rows.append(row)    
            
#     with open('bank.csv', 'w', newline='') as file: 
#         fieldnames = ['id','FirstName','lastName','password','SavingBalance','checkingBalacne','state']
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(all_rows)      
                    
# # update the csv file after witdrawing/deposit 
# def update_saving_balance(updated_customer):
#     all_rows = []
#     with open('bank.csv', 'r', newline='') as file:
#         reader = list(csv.DictReader(file))
#         for row in reader:
#             if str(updated_customer.id) == row['id'] and str(updated_customer.password)== row["password"]:
#                 row['SavingBalance'] = str(updated_customer.balancSavingAccount)
#             all_rows.append(row)    
            
#     with open('bank.csv', 'w', newline='') as file: 
#         fieldnames = ['id','FirstName','lastName','password','SavingBalance','checkingBalacne','state']
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(all_rows)                 
  
# update the csv file after witdrawing/deposit or tansferm 
def update_balance(updated_customer):
    all_rows = []
    with open('bank.csv', 'r', newline='') as file:
        reader = list(csv.DictReader(file))
        for row in reader:
            if str(updated_customer.id) == row['id'] and str(updated_customer.password)== row["password"]:
                row['checkingBalacne'] = str(updated_customer.balancCheckingAccount)
                row['SavingBalance'] = str(updated_customer.balancSavingAccount)
                row['state'] = updated_customer.state
                row['overdraftCounter'] = updated_customer.overdraftCounter
            all_rows.append(row)    
            
    with open('bank.csv', 'w', newline='') as file: 
        fieldnames = ['id','FirstName','lastName','password','SavingBalance','checkingBalacne','state','overdraftCounter']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)     
  
#   handle deposit  
class Deposit():
    def __init__(self, customer):
        self.customer = customer
        
    def deposit_operation(self):
        print("Do You want to deposit into Saving or checking account ?")
        print("Enter 1 for checking")
        print("      2 for saving")
        userChoose = int(input(''))
        
        match userChoose:
            case 1 :
                print(f'Your current checking Balance :,{self.customer.balancCheckingAccount} ...') 
                amount = int(input('Enter the amount you want to deposit : '))
                
                if self.customer.balancCheckingAccount <= 0 and amount > 0 :
                    self.customer.state= "active"
                    self.customer.overdraftCounter = 0 
                    print('Account reactivated')
                    
                    
                self.customer.balancCheckingAccount = int(self.customer.balancCheckingAccount) + amount
                print(f" Diposit successfuly. New Checking Balance: {self.customer.balancCheckingAccount}")
                update_balance(self.customer)   
            case 2 :
                print(f'Your current saving Balance :,{self.customer.balancSavingAccount} ...') 
                amount = int(input('Enter the amount you want to deposit : '))
                
                
                self.customer.balancSavingAccount = int(self.customer.balancSavingAccount) + amount
                print(f" Diposit successfuly. New Saving Balance: {self.customer.balancSavingAccount}") 
                update_balance(self.customer)   
                   
  
class Transfer():
    
    def __init__(self,customer):
        self.customer = customer
    
    def transfer_operation(self):
        print('Do you want to transfer locally or to another account ? ')
        print("Transfer 1 into locally")
        print("         2 into another account")
        userChoose = int(input(''))
        
        match userChoose:
            # transfer locally
            case 1 :
                print('Do you wnt to trasfer ')
                print("Enter 1 from saving into checking")
                print("      2 from checking into saving")
                choose = int(input(''))
                
                match choose:
                    # from saving into checking
                    case 1:
                        amount = int(input('how much do you want to transfer into checking'))
                        if(amount > int(self.customer.balancSavingAccount)):
                            raise balanceNotEnoghError('Sorry!  insufficient balance to make a transfer ')
                            return 
                        self.customer.balancSavingAccount = int(self.customer.balancSavingAccount) - amount
                        self.customer.balancCheckingAccount = int(self.customer.balancCheckingAccount) + amount
                        update_balance(self.customer)  
                
                    # from checking into saving
                    case 2:
                        amount = int(input('how much do you want to transfer into saving'))
                        if(amount > int(self.customer.balancCheckingAccount)):
                            raise balanceNotEnoghError('Sorry!  insufficient balance to make a transfer ')
                            return 
                        self.customer.balancCheckingAccount = int(self.customer.balancCheckingAccount) - amount
                        self.customer.balancSavingAccount = int(self.customer.balancSavingAccount) + amount
                        update_balance(self.customer)  
            
            #  transfer to another account 
            case 2 : 
                reciverID =input('Enter the account number you want to transferm into ')
                reciverName =input('Enter FIRST name of account onwer')
                receiver = csvFile.search_between_account(reciverID,reciverName)
                if(receiver == False): 
                    raise customerNotFoundError("name or  customer Id not correct, Please try again !")
                    return
                transfer_between_account(self.customer,receiver)
                
              
def transfer_between_account(customer,receiver):
    amount = int(input('Enter the amount you want to transfer'))   
    if(amount > int(customer.balancCheckingAccount)):
        raise balanceNotEnoghError('Sorry!  insufficient balance to make a transfer ')
    customer.balancCheckingAccount = int(customer.balancCheckingAccount) - amount
    receiver.balancCheckingAccount = int(receiver.balancCheckingAccount) + amount 
    print('Transfered Successfully ')  
    print(f'Your new balance is {customer.balancCheckingAccount} ..')      
    update_balance(customer)
    update_balance(receiver)
      
    
    