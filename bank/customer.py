
class Customer():
    def __init__(self,idd,firstName ,secondName, password ,balancSavingAccount,balancCheckingAccount):  
        self.id= idd
        self.firstName = firstName
        self.secondName =secondName
        self.password = password 
        self.balancSavingAccount = balancSavingAccount
        self.balancCheckingAccount = balancCheckingAccount
        
        
        
    def __str__(self):
        return f"{self.firstName} {self.secondName}"
        

    

