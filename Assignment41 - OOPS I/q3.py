'''Assignment 3: Bank Account Operations
 A bank wants to perform basic operations on a customer's account.

Create a class BankAccount with the following attributes:

Account number

Account holder name

Balance

Create the following methods:

deposit() – Add an amount to the balance.

withdraw() – Subtract an amount from the balance.

display_account() – Display account details and final balance.

Sample data:

Account Number: 1001
Account Holder: Rahul
Opening Balance: 25000
Deposit: 5000
Withdrawal: 3000

Expected result:

Final Balance: 27000'''
   
class BankAccount:

    def __init__(self,accno,name,balance,damount,wamount):
        self.accno = accno
        self.name = name
        self.balance = balance
        self.damount = damount
        self.wamount = wamount

    def deposit(self):
       
        self.balance = self.balance + damount

        return self.balance

    def withdraw(self):
       
        self.balance = self.balance - wamount

        return self.balance

    def total_balance(self):

        total = self.balance + self.damount - self.wamount
        return total

    def display(self):

        
        print(f"Account Number    :{self.accno}")
        print(f"Account Holder    :{self.name}")
        print(f"Opening Balance   :{self.balance}")
        print(f"Deposit           :{self.damount}")
        print(f"Withdrawal        :{self.wamount}")
        print()
        print(f"Final Balance     :{self.total_balance()}")


damount = int(input("Enter Amount : "))
wamount = int(input("Enter Amount : "))
cust1 = BankAccount(101,"Nimesh",20000,damount,wamount)
cust1.display()

    