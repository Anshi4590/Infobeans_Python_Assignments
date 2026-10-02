def mainmenu():

    
        from models.bank import BankAccount,InsufficientBalanceException,InvalidAmountException,InvalidWithdrawalException,NegativeDepositException
        account_number = int(input("Enter Account Number : "))
        account_holder = input("Enter Name : ")

        balance = int(input("Enter Balance : "))
    
        cust = BankAccount(account_number,account_holder,balance)
    
    
        while True :
    
            print("""==================
        BANK ACCOUNT SYSTEM
        ===================
    
        1. Deposit
        2. Withdraw
        3. Check Balance
        4. Display Account Details
        5. Exit
        """)
    
    
            choice = int(input("Enter Your choice : "))
    
            match choice :
    
                case 1:
                    print("\n ----- Deposit Amount ------ \n")
                    amount = int(input("Enter Amount : "))

                    try:
                        cust.deposit(amount)
    
                    except InvalidAmountException as e:
                        print("InvalidAmountException",e)
    
    
                    except NegativeDepositException as e:
                        print("NegativeDepositException",e) 
    
                    else:
                        print("Deposit Successfully.......\n")

                        print("\nUpdated Balance : \n")
                        print(balance+amount)
    
    
                case 2:
                    print("\n ----- Withdraw Amount ------ \n")
                    amount = int(input("Enter Amount : "))
    
                    try:
                        cust.withdraw(amount)
    
                    except InvalidWithdrawalException as e:
                        print("InvalidWithdrawalException",e)
    
                    except InvalidAmountException as e:
    
                        print("InvalidAmountException",e)
    
                    except InsufficientBalanceException as e:
                        print("InsufficientBalanceException",e)
    
                    else:
                        print("\nwithdrawn Successfully.......\n")
                        print("\nUpdated Balance : \n")
                        print(balance - amount)
    
    
                case 3:
                    print("\nCurrent Balance :\n")
                    cust.check_balance()
    
                case 4:
                    
                    cust.display_account_details()
    
                case 5:
                    print("Thank you for using Bank Account System")
                    break
                case _:
                    print("Invalid Choice")
                
    