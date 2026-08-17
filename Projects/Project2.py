import random
from datetime import datetime

# Initialize variables 
account_number = 0
pin = 0
balance = 0.0
opening_balance = 0.0
customer_id = 0
name = ""
father_name = ""
dob = ""
phone = ""
address = ""
gender = ""
account_type = ""
deposit_amount = 0
withdraw_amount = 0
transfer_amount = 0
formatted1 = "No deposits yet."
formatted2 = "No withdrawals yet."
formatted3 = "No transfers yet."
loan_id = 0
loan_type = ""
loan_amount = 0
loan_duration = 0
interest = 0
EMI = 0

while True:
   
   print("\n===================================")
   print("         HDFC BANK         ")
   print("====================================")
   print("1. Create Account")
   print("2. Login")
   print("3. Exit")

   choice = input("Enter Your Choice : ")

   match choice:
         
         case "1":
            print("\n------- Create Account --------")
            print()
            name = input("Enter Your Name  : ")
            father_name = input("Enter Father Name : ")
            dob = input("Enter Date of Birth (DD/MM/YYYY) : ")
            age = int(input("Enter Your Age  : "))
            phone = input("Enter Phone Number : ")
            
            gender =input("Enter your Gender : ")
            address = input("Enter Address : ")
            city = input("Enter City :")
            pincode = input("Enter Pincode :")

            aadhar = input("Enter Aadhar Number : ")
            pan = input("Enter PAN Number : ")
            print("\nchoose Account Type : ")
            print("1. Savings Account")
            print("2. Current Account")
            print()
            account_choice = int(input("Enter Your Choice : "))
            if account_choice == 1:
                  account_type = "Savings"
            else:
                  account_type = "Current"

            balance =float(input("Enter Initial Deposit Amount :"))
          

            while balance < 1000:
               print("Minimum Deposit Amount is Rs1000")
               balance = float(input("Please Enter Amount Again : "))
               print()
            
            customer_id = random.randint(100000,999999)
            account_number = random.randint(1000000000,9999999999)

            pin = int(input("Set your 4-Digit Pin : "))
            confirm_pin = int(input("RE-Enter your Pin : "))
            while pin != confirm_pin:
               print("PINs do not match. Try again.")
               pin = int(input("Set your 4-Digit Pin : "))
               confirm_pin = int(input("RE-Enter your Pin : ")) 
               
            print()
            print("Account Created Successfully")
            print("Your Customer ID : ",customer_id)
            print("Your Account Number : ",account_number)

         case "2" :
              
            a = int(input("Enter Your Account Number :"))
            if a == account_number:
               b = int(input("Enter PIN : "))
               if b == pin:
                  print("Login Successfully...")
               else:
                  print("Incorrect PIN ")
                  continue
            else:
               print("Account Not Found")
               continue

            while True:

               print("\n============ DASHBOARD ============")
               print("1. Check Balance")
               print("2. Deposit Money")
               print("3. Withdraw Money")
               print("4. Transfer Money")
               print("5. Mini Statement")
               print("6. Account Details")
               print("7. Apply for Loan")
               print("8. Loan Details")
               print("9. Change PIN")
               print("10. Logout")
               print("\n===================================")
         
               choice =int(input("Enter choice : "))
         
               match choice :
                  
                     case 1:
                        print("Current Balance : ", balance)
                        opening_balance = balance
                     case 2:
                        deposit_amount = int(input("Enter Deposit Amount : "))
                        if  deposit_amount>0:
                           balance = balance + deposit_amount
                           print("Amount Deposited successfully")
                        else:
                           print("Re-Enter the Amount")
                           deposit_amount = int(input("Enter Deposit Amount : "))
                           if deposit_amount>0:
                              balance = balance + deposit_amount
                              print("Amount Deposited successfully")
                           else:
                              print("Invalid Amount")
                        
                        current1 = datetime.now()
                        
                        formatted1 = current1.strftime("%d-%m-%Y %I:%M:%S %p")

                        print(formatted1) 
                        
                        print("Deposit Amount : ",deposit_amount)

                     case 3:
                        withdraw_amount = int(input("Enter Withdraw Amount : "))
                        if  withdraw_amount>0:
                           balance = balance - withdraw_amount
                           print("Amount Withdrawn successfully")
                        else:
                           print("Re-Enter the Amount")
                           withdraw_amount = int(input("Enter Withdraw Amount : "))
                           if withdraw_amount>0:
                              balance = balance - withdraw_amount
                              print("Amount Withdrawn successfully")
                           else:
                              print("Invalid amount.")
                        
                        current2 = datetime.now()
                        
                        formatted2 = current2.strftime("%d-%m-%Y %I:%M:%S %p")

                        print(formatted2)
                        print("Withdrawn Amount : ",withdraw_amount)

                     case 4:
                        receivers_account = int(input("Enter Receiver Account Number"))
                        transfer_amount = int(input("Enter Amount to be transferred :"))
                        receiver_balance = 0
                        if receivers_account>0:
                           balance = balance - transfer_amount
                           receiver_balance = receiver_balance + transfer_amount
                           print("Transfered Amount Successfully")

                           current3 = datetime.now()
                        
                           formatted3 = current3.strftime("%d-%m-%Y %I:%M:%S %p")

                           print(formatted3)
                           print("Transfered Amount : ",transfer_amount)
                       
                     case 5:
                           print("----------- Mini Statement ------------")
                           print()
                           print(formatted1)
                           print("Deposit Amount : ",deposit_amount)
                           print()
                           print(formatted2)
                           print("Withdrawn Amount : ",withdraw_amount)
                           print()
                           print(formatted3)
                           print("Transfered Amount : ",transfer_amount)

                     case 6:
                           print("Customer ID : ",customer_id)
                           print("Account Number : ",account_number)
                           print("Name : ",name)
                           print("Father's Name : ",father_name)
                           print("DOB : ",dob)
                           print("Phone: ", phone)
                           print("Address : ",address)
                           print("Gender : ",gender)
                           print("Account Type : ",account_type)
                           print("Opening Balance: ",opening_balance)
                           print("Current Balance: ",balance)

                     case 7:
                        loan = input("Loan Already Active?(Yes/No) :")
                        if loan.lower() == "yes":

                           print("Can't Give Loan ")
                           continue
                        else:
                           print("-------- Available Loan ---------")
                           print("1. Personal Loan")
                           print("2. Education Loan")
                           print("3. Home Loan")
                           

                           loan_type = input("Enter loan type :")
                        
                           loan_amount = int(input("Enter Loan Amount :"))
                           loan_duration = int(input("Enter Loan Duration in years :")) 

                              #Eligibility checks
                           if account_number!=0 and balance>=5000 and loan.lower() == "no" :                             
                                 loan_id = random.randint(10000,99999)
                                    
                                 print("Loan Id : ",loan_id )
                                    
                                 if  loan_type.lower() == "1" or loan_type.lower() == "personal" or loan_type.lower() == "personal loan" or loan_type.lower() == "personal_loan":
                                    print("Interest : 10%")
                                    interest = loan_amount*loan_duration*10/100 
                                    total_amount = loan_amount + interest
                                       
                                       #EMI calculation
                                    EMI = total_amount/(loan_duration*12)
                                    print()
                                    print("Loan Approved Successfully")
                                    print("Loan ID : ",loan_id)
                                    print("Loan Type : ",loan_type)
                                    print("Loan Amount : ",loan_amount)
                                    print("Amount Credited to Your Account")
                                    balance = balance + loan_amount

                                    

                                 elif  loan_type.lower() == "2" or loan_type.lower() == "education" or loan_type.lower() == "education loan" or loan_type.lower() == "education_loan":
                                    print("Interest : 7%")
                                    interest = loan_amount*loan_duration*7/100 
                                    total_amount = loan_amount + interest
                                       
                                       #EMI calculation
                                    EMI = total_amount/(loan_duration*12)
                                    print()
                                    print("Loan Approved Successfully")
                                    print("Loan ID : ",loan_id)
                                    print("Loan Type : ",loan_type)
                                    print("Loan Amount : ",loan_amount)
                                    print("Amount Credited to Your Account")
                                    balance = balance + loan_amount

                                 elif  loan_type.lower() == "3" or loan_type.lower() == "home" or loan_type.lower() == "home loan" or loan_type.lower() == "home_loan":
                                    print("Interest : 8%")
                                    interest = loan_amount*loan_duration*8/100 
                                    total_amount = loan_amount + interest
                                    
                                    #EMI calculation
                                    EMI = total_amount/(loan_duration*12)
                                    print()
                                    print("Loan Approved Successfully")
                                    print("Loan ID : ",loan_id)
                                    print("Loan Type : ",loan_type)
                                    print("Loan Amount : ",loan_amount)
                                    print("Amount Credited to Your Account")
                                    balance = balance + loan_amount

                                 else:
                                    print("Invalid loan Type")

                     
                     case 8:
                        loan_exits  = input("Already loan Exits(yes/no):")
                        if loan_exits.lower() == "yes":
                           print("----------- Loan Status ------------")
                           print("Loan ID : ",loan_id)
                           print("Loan Type : ",loan_type)
                           print("Loan Amount : ",loan_amount)
                           print("Loan Durtion : ",loan_duration)
                           print("Interest Rate : ", interest)
                           print("EMI : ",EMI)
                           print("------------------------------------")

                        else:
                            print("Firstly Take a Loan")
                            break
                               
                     case 9:
                        print("------------- Change Pin ----------")
                        old_pin =int(input("Enter old PIN : "))
                        if pin == old_pin:
                           new_pin = int(input("Enter New PIN : "))
                           confirm = int(input("Re-Enter New PIN : "))
                           if new_pin == confirm :
                              pin = new_pin
                              print("PIN Updated")


                           else:
                              print("Try Again") 
                              new_pin = int(input("Enter New PIN : "))
                              confirm = int(input("Re-Enter New PIN : "))
                              if new_pin == confirm :
                                 pin = new_pin
                                 print("PIN Updated")
                              else:
                                 print("PINs do not match.")

                     case 10:
                          print("Logout Successfully from the Account")
                          break
                   
         case "3":
               print("\n====================================")
               print("  Thank you for using HDFC Bank!    ")
               print("           Have a great day.        ")
               print("====================================\n")
               break   

         case __ : 
           print("Enter valid choice")
            






















              


