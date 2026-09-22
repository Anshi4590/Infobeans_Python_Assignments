'''
QNO 1: Bank Account Management System

ABC Bank wants to develop a software application to manage customer accounts.

Each customer has:

Account Number
Customer Name
Account Balance

A customer should be able to:

Deposit money
Withdraw money
Check account balance
Transfer money to another customer

The bank also wants to maintain information that is common for all customers:

Bank Name
Interest Rate

The bank management may change the interest rate in the future, and the change should apply to all customers.

Additionally, the application should provide some utility operations:

Validate whether an account number is valid.
Calculate interest on a given amount.
Generate a transaction ID.
Requirements

Class Variables

bank_name
interest_rate

Instance Variables

account_no
customer_name
balance

Instance Methods

deposit(amount)
withdraw(amount)
transfer_money(receiver, amount)
display_balance()

Class Methods

change_interest_rate(new_rate)
change_bank_name(new_name)
display_bank_info()

Static Methods

validate_account_number(account_no)
calculate_interest(amount, rate)
generate_transaction_id()

Sample Input

Customer 1
Account No : 1001
Name       : deepika
Balance    : 50000

Customer 2
Account No : 1002
Name       : Priya
Balance    : 30000

Deposit Amount : 10000
Transfer Amount : 15000
New Interest Rate : 7.5

Sample Output
Customer : deepika
Balance  : 45000

Customer : Priya
Balance  : 45000

Bank Name      : ABC Bank
Interest Rate  : 7.5%
Transaction ID : TXN1025

Task: Design a Python class named Bank and implement all the above methods using instance methods, class methods, and static methods appropriately.'''


class Bank:
    
    bank_name = "ABC Bank"
    interest_rate = 7.5
    transaction_id = 1000

    def __init__(self,account_no,name,balance):

        self.account_no = account_no
        self.name = name 
        self.balance = balance


    def deposit(self,amount):

        self.balance = amount + self.balance
        
        print(f"Balance   : {self.balance}")
        print("Amount Deposited Successfully")
        print()

    def withdraw(self,amount):

        self.balance = self.balance - amount
        
        print(f"Balance   : {self.balance}")
        print("Amount withdrawn Successfully")

    def transfer_money(self,receiver, amount):

        receiver.balance = amount + receiver.balance
        self.balance = self.balance - amount
        print(f"Balance   : {self.balance}")
        print(f"{receiver.name} Balance : {receiver.balance}")
        print()

        
    def display_balance(self):
        print(f"customer       : {self.name}")
        print(f"Balance        : {self.balance}")

    def account_info(self):
        
        print(f"------- customer details --------")
        print(f"Account Number    : {self.account_no}")
        print(f"Name              : {self.name}")
        print(f"Balance           : {self.balance}")
         
    @classmethod
    def change_interest_rate(cls,new_rate):

        cls.interest_rate = new_rate
        print(f"New Interest Rate :{cls.interest_rate}")

    @classmethod 
    def change_bank_name(cls,new_name):

        cls.bank_name = new_name 
        print(f"New Bank Name : {cls.bank_name}")

    @classmethod
    def display_bank_info(cls):
        print(f"Bank Name      : {cls.bank_name}")
        print(f"Interest Rate  : {cls.interest_rate}%")
        print(f"Transaction Id : {cls.generate_transaction_id()}")
        print()



    @staticmethod
    def validate_account_number(account_no):

        if 1000<=account_no<=9999:
            print("validate Account Number")

        else:
            print("Invalid Account Number ")

    @staticmethod
    def calculate_interest(amount, rate):

        interest = (amount*rate)/100
        print(f"Interest : {interest}")

    @staticmethod        
    def generate_transaction_id():

        Bank.transaction_id+=25
        transaction_id = "TXN"+str(Bank.transaction_id)
        return transaction_id




cust1 = Bank(1001,"Deepika",50000)
cust1.account_info()
print()

cust2 = Bank(1002,"Priya",30000)
cust2.account_info()
print()


Bank.change_interest_rate(7.5)

cust1.change_interest_rate(8)
print()
cust1.validate_account_number(1001)
print()

cust1.deposit(10000)
cust1.transfer_money(cust2,15000)
cust1.display_balance()
print()

cust2.deposit(10000)
cust2.transfer_money(cust1,15000)
cust2.display_balance()
print()

Bank.display_bank_info()
