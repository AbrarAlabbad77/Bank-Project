import csv
from bank.customer import Customer
class NagitveBalancError(Exception):
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
                print(f'Your curent checking Balance :,{self.customer.balancCheckingAccount} ...') 
                amount = int(input('Enter the amount you want to withdraw'))
                if(int(self.customer.balancCheckingAccount) <= 0):
                    if(amount>65):
                        raise NagitveBalancError("sorry [Nagitive Mode]! you can not withdraw more than $65")
                        return
                self.customer.balancCheckingAccount = int(self.customer.balancCheckingAccount) - amount
                print(f" Withdraw successfuly. New Checking Balance: {self.customer.balancCheckingAccount}")
                update_checking_balance(self.customer)   
            case 2 :
                print(f'Your curent saving Balance :,{self.customer.balancSavingAccount} ...') 
                amount = int(input('Enter the amount you want to withdraw'))
                if(int(self.customer.balancSavingAccount) <= 0):
                    if(amount>65):
                        raise NagitveBalancError("sorry [Nagitive Mode]! you can not withdraw more than $65")
                        return
                self.customer.balancSavingAccount = int(self.customer.balancSavingAccount) - amount
                print(f" Withdraw successfuly. New Saving Balance: {self.customer.balancSavingAccount}")
                update_saving_balance(self.customer)   
                   
            
 # update the csv file after witdrawing from cheking account 
def update_checking_balance(updated_customer):
    all_rows = []
    with open('bank.csv', 'r', newline='') as file:
        reader = list(csv.DictReader(file))
        for row in reader:
            if str(updated_customer.id) == row['id'] and str(updated_customer.password)== row["password"]:
                row['checkingBalacne'] = str(updated_customer.balancCheckingAccount)
            all_rows.append(row)    
            
    with open('bank.csv', 'w', newline='') as file: 
        fieldnames = ['id','FirstName','lastName','password','SavingBalance','checkingBalacne','state']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)      
                    
# update the csv file after witdrawing from cheking account 
def update_saving_balance(updated_customer):
    all_rows = []
    with open('bank.csv', 'r', newline='') as file:
        reader = list(csv.DictReader(file))
        for row in reader:
            if str(updated_customer.id) == row['id'] and str(updated_customer.password)== row["password"]:
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
                print(f'Your curent checking Balance :,{self.customer.balancCheckingAccount} ...') 
                amount = int(input('Enter the amount you want to deposit : '))
                
                self.customer.balancCheckingAccount = int(self.customer.balancCheckingAccount) + amount
                print(f" Diposit successfuly. New Checking Balance: {self.customer.balancCheckingAccount}")
                update_checking_balance(self.customer)   
            case 2 :
                print(f'Your curent saving Balance :,{self.customer.balancSavingAccount} ...') 
                amount = int(input('Enter the amount you want to deposit : '))
                
                self.customer.balancSavingAccount = int(self.customer.balancSavingAccount) + amount
                print(f" Diposit successfuly. New Saving Balance: {self.customer.balancSavingAccount}")
                update_saving_balance(self.customer)   
                   
        
    
    