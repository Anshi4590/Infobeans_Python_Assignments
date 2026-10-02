
'''Assignment 5: Shopping Tax Calculator
========================================

Your shopping cart total doesn’t include tax. A 12% GST is applied.

Write a Python program that:
- Accepts the cart total amount.
- Calculates 12% tax.
- Displays the tax and final total amount.

Example:
Cart = ₹2000
Tax = ₹240
Total = ₹2240'''

amount= int(input("Enter the total amount:"))
Tax = amount*12/100
Total = amount + Tax
print("Cart :Rs{}\nTax :Rs{}\nTotal :Rs{}".format(amount,Tax,Total))
