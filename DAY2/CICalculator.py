
'''Assignment 13: Compound Interest Calculator

Write a Python program that:

Accepts principal, rate, and time.
Calculates compound interest.

Input:
Principal = 1000
Rate = 10
Time = 2

Output:
Amount = 1210.0
Compound Interest = 210.0'''


p,r,t=map(int,input("enter the principle,rate,time:").split(","))
si=(p*r*t)/100
amount=int(p*((1+(r/100))**t))
CI=amount-p
print(f"Amount:{amount}\n Compound Interest ={CI}")