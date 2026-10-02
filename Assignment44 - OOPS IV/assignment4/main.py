'''============================================================
ASSIGNMENT 4 – BANK ACCOUNT SYSTEM
==================================

Create an `Account` class inside:

models/account.py

ATTRIBUTES:

* account_no
* customer_name
* balance

METHODS:

* deposit()
* withdraw()
* display()

TASKS:

1. Create 5 Account objects.
2. Store all Account objects in a list.
3. Display all accounts.
4. Search an account using Account Number.
5. Deposit money into a selected account.
6. Withdraw money from a selected account.
7. Display accounts having balance greater than 50,000.
8. Find the account having the highest balance.

SAMPLE DATA:

101 Amit 45000
102 Rahul 75000
103 Priya 35000
104 Neha 90000
105 Rohit 55000

SAMPLE OPERATIONS:

Enter Account No: 101

Enter amount to deposit: 10000

After Deposit:
101 Amit 55000

Enter Account No: 103

Enter amount to withdraw: 5000

After Withdrawal:
103 Priya 30000

EXPECTED OUTPUT:

Accounts having balance greater than 50000:

102 Rahul 75000
104 Neha 90000
105 Rohit 55000

Highest Balance Account:

104 Neha 90000
'''

from models.account import Account

bank_db = []

for i in range(2):

    account_no = int(input("Enter Account Number : "))
    customer_name = input("Enter Customer Name : ")
    balance = int(input("Enter Balance : "))
    print()

    cust = Account(account_no,customer_name,balance)

    bank_db.append(cust)

print("\nSAMPLE DATA : ")

for i in bank_db:

    i.display()


print("\nBank Operations : ")

account = int(input("Enter Account number : "))

for i in bank_db:

    if account == i.account_no:
        amount = int(input("Enter amount to deposit : "))
      

        print("After Deposit : ")
        print()
        i.deposit(amount)
        i.display()
        print()

account = int(input("Enter Account number : "))

for i in bank_db:

    if account == i.account_no:
        amount = int(input("Enter amount to withdraw  : "))
      

        print("After Withdrawn : ")
        print()
        i.withdraw(amount)
        i.display()

print("\nAccounts having balance greater than 50000 : ")

for i in bank_db:
    if i.greater_than:

        i.display()

print("\nHighest Balance Account : ")
high = bank_db[0]

for i in bank_db:

    if i.highest_balance(high):

        high = i


high.display()








    


