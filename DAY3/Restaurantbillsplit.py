
'''Assignment 1: Restaurant Bill Split

A group of friends went to a restaurant. The restaurant adds GST and service charge to the bill, and then the total is divided equally.

Input:
Total bill amount = 2500
GST = 5%
Service charge = 10%
Number of friends = 4

Expected Output:
Final Bill = 2875.0
Each Person Pays = 718.75'''





total = int(input("enter the value:"))
gst = float(input ("enter the value:"))
servicecharge = int(input ("enter the value:"))
friends = int(input ("enter the value :"))
charge = gst + servicecharge
amount = (total*charge/100)+ total
pay = amount / friends
print ("Final bill:",amount)
print("Each Person pays :",pay)
