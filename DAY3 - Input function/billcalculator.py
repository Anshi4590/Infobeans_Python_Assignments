
'''Assignment 3: Electricity Bill Calculator

Write a Python program that:

Accepts number of units.
Calculates bill (₹6 per unit).

Input:
Units = 100

Output:
Bill = 600'''


units = int(input("enter the number of units:"))
bill = units*6
print("BILL :Rs",bill)