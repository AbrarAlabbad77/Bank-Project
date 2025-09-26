import csv
from bank.customer import Customer

#  Errors classes
class NagitveBalancError(Exception):
    pass

class balanceNotEnoghError(Exception):
    pass



class Withdraw():
    def __init__(self, customer):
        self.customer = customer
        # self.withdraw_operation()
        
        
    def withdraw_operation(self):
        print("Do You want to withdraw from Saving or checking account ?")
        print("Enter 1 for checking")
        print("      2 for saving")
        userChoose = int(input(''))
        
        match userChoose:
            case 1 :
                print(f'Your current checking Balance :,{self.customer.balancCheckingAccount} ...') 
                amount = int(input('Enter the amount you want to withdraw'))
                if(int(self.customer.balancCheckingAccount) <= 0):
                    if(amount>65):
                        raise NagitveBalancError("sorry [Nagitive Mode]! you can not withdraw more than $65")
                        return
                self.customer.balancCheckingAccount = int(self.customer.balancCheckingAccount) - amount
                print(f" Withdraw successfuly. New Checking Balance: {self.customer.balancCheckingAccount}")
                # update_checking_balance(self.customer)
                update_balance(self.customer)     
            case 2 :
                print(f'Your current saving Balance :,{self.customer.balancSavingAccount} ...') 
                amount = int(input('Enter the amount you want to withdraw'))
                if(int(self.customer.balancSavingAccount) <= 0):
                    if(amount>65):
                        raise NagitveBalancError("sorry [Nagitive Mode]! you can not withdraw more than $65")
                        return
                self.customer.balancSavingAccount = int(self.customer.balancSavingAccount) - amount
                print(f" Withdraw successfuly. New Saving Balance: {self.customer.balancSavingAccount}")
                # update_saving_balance(self.customer)  
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
            all_rows.append(row)    
            
    with open('bank.csv', 'w', newline='') as file: 
        fieldnames = ['id','FirstName','lastName','password','SavingBalance','checkingBalacne','state']
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
                
                self.customer.balancCheckingAccount = int(self.customer.balancCheckingAccount) + amount
                print(f" Diposit successfuly. New Checking Balance: {self.customer.balancCheckingAccount}")
                # update_checking_balance(self.customer) 
                update_balance(self.customer)   
            case 2 :
                print(f'Your current saving Balance :,{self.customer.balancSavingAccount} ...') 
                amount = int(input('Enter the amount you want to deposit : '))
                
                self.customer.balancSavingAccount = int(self.customer.balancSavingAccount) + amount
                print(f" Diposit successfuly. New Saving Balance: {self.customer.balancSavingAccount}")
                # update_saving_balance(self.customer)  
                update_balance(self.customer)   
                   
  
class Transfer():
    
    def __init__(self,customer):
        self.customer = customer
    
    def transfer_operation(self):
        print('Do you want to transfer locally or to another account ? ')
        print("Enter 1 for locally")
        print("      2 for another account")
        userChoose = int(input(''))
        
        match userChoose:
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
                pss 
                
    
    