
'''Assignment 2: Mobile EMI Calculation

You purchased a mobile phone using EMI. After paying a down payment, the remaining amount includes interest and is divided into monthly installments.

Input:
Mobile price = 30000
Down payment = 5000
Interest rate = 10%
Months = 10

Expected Output:
Remaining Amount = 25000
Total with Interest = 27500
Monthly EMI = 2750.0'''


mobileprice = int(input("enter the mobileprice:"))
downpayment = int(input("Enter the Down payment:"))
Interestrate = int(input("Enter the Interest rate:"))
Months = int(input("enter the total Months:"))
Ramount = mobileprice - downpayment
interest = (Ramount*Interestrate/100) + Ramount
emi = interest/Months
print("Remaining Amount:",Ramount)
print("Total with Interest:",interest)
print("Monthly EMI:",emi)