
class Customer():
    def __init__(self,idd,FirstName ,secondName, password ,balancSavingAccount,balancCheckingAccount, state):  
        self.id= idd
        self.FirstName = FirstName
        self.secondName =secondName
        self.password = password 
        self.balancSavingAccount = balancSavingAccount
        self.balancCheckingAccount = balancCheckingAccount
        self.state = state
        
        
        
    def __str__(self):
        return f"{self.FirstName} {self.secondName}"
        

    

