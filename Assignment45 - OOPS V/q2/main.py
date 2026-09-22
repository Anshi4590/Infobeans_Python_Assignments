from models.bank import Account,SavingsAccount,PremiumSavingsAccount

account_number = int(input("Enter Account Number :"))
customer_name = input("Enter Customer Name :")
balance = int(input("Enter Balance :"))


while True:

    print("Account Type:")
    print("1.Savings Account")
    print("2.Premium Savings Account")

    choice = int(input("Enter Account Type :"))
 
    match choice:

        case 1:
        
            
            interest_rate = (int(input("Enter Interest Rate : ")))
            amount = int(input("Enter amount to deposit : "))
            amount1 = int(input("Enter amount to withdraw : "))
            print()
            cust1 = SavingsAccount(account_number,customer_name,balance ,interest_rate)
            cust1.display_account()

            print()
            print("After Deposit")
            cust1.deposit(amount)
            cust1.display_account()

            print()
            print("After Withdraw")
            cust1.withdraw(amount1)
            cust1.display_account()
            break

        case 2:
            
            interest_rate = int(input("Enter Interest Rate : "))
            cashback_percent = int(input("Enter Cashback Percentage: "))
            amount = int(input("Enter amount to deposit : "))
            amount1 = int(input("Enter amount to withdraw : "))
            print()
            cust1 = PremiumSavingsAccount(account_number,customer_name,balance ,interest_rate,cashback_percent)
            cust1.display_account()

            print()
            print("After Deposit")
            cust1.deposit(amount)
            cust1.display_account()

            print()
            print("After Withdraw")
            cust1.withdraw(amount1)
            cust1.display_account()
            break

     
        

        case _:

            print("Invalid choice")


