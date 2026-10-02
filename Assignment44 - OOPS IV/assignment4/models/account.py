
class Account:

    def __init__(self,account_no,customer_name,balance):
        self.account_no =account_no
        self.customer_name = customer_name
        self.balance = balance 


    def deposit(self,amount):

        self.balance = self.balance + amount
        return self.balance

        
    def withdraw(self,amount):
        self.balance =  self.balance - amount
        return self.balance
        
    def display(self):
        print(f"{self.account_no} {self.customer_name} {self.balance}")

    def greater_than (self):

        return self.balance>50000

    def highest_balance(self,high):

        return self.balance>high.balance

    

