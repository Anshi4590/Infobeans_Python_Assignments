'''9. Smart Loan Eligibility System

A bank approves loans based on salary, age, credit score, and EMI.

If salary is 40000 or above, then check age. If age is between 21 and 60, then check credit score. If credit score is 750 or above, then check EMI. If EMI is less than or equal to 40% of salary, approve at 8%; otherwise approve at 10%. If credit score is below 750, then check if it is at least 650. If yes, approve at 12%; otherwise reject.

If salary is below 40000, then check if salary is at least 25000 and credit score is at least 700. If yes, approve at 13%; otherwise reject.

Input:
Salary = 50000
Age = 30
Credit Score = 760
EMI = 18000

Output:
Loan Status = Approved at 8%'''5

Salary = int(input("Salary ="))
Age = int(input("Age ="))
Score = int(input("Credit Score ="))
EMI = int(input("EMI ="))

if Salary>=40000:
   if 21<=Age<=60:
      if Score>=750:
         if EMI <=(40/100*Salary):
            print("Approved at 8%")
         else:
            print("Approved at 10%")
      else:
         if Score>=650:
            print("approve at 12%")
         else:
            print("Reject")
else:
    if Salary>=25000 and Score>=700:
       print("Approved at 13%")
    else:  
       print("Reject")