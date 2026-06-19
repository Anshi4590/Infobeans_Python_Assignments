

'''Assignment 14: Simple Profit or Loss Calculator

Write a Python program that:

Accepts cost price and selling price.
Calculates profit/loss and percentage.

Input:
Cost Price = 1000
Selling Price = 1200

Output:
Profit = 200
Profit % = 20.0'''



cp, sp = map(int, input("Enter Cost Price and Selling Price: ").split(","))
profitloss = sp - cp
profitlossper = (profitloss/ cp) * 100
print("Note: +ve = Profit, -ve = Loss")
print("Profit/Loss =", profitloss)
print("Profit/Loss % =", profitlossper)