
'''Assignment 12: Change Return System

Write a Python program that:

Accepts amount.
Calculates ₹100, ₹50, ₹10 notes.

Input:
Amount = 380

Output:
₹100 x 3
₹50 x 1
₹10 x 3'''


amount = int( input("enter the value:"))
x = (amount //100)
reminder  = amount%100 
y = reminder //50
rem = reminder%50
z = rem //10
print("Rs 100 X{}\nRS 50X{}\nRs 10X {}".format(x,y,z))