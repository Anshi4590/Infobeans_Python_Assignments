
'''Assignment 7: Temperature Converter
========================================

A weather application needs to convert temperature from Celsius to Fahrenheit.

Write a Python program that:
- Accepts temperature in Celsius as input.
- Converts it to Fahrenheit using the formula:
  F = (C × 9/5) + 32
- Displays the result.

Example:
Celsius = 25
Fahrenheit = 77.0'''

temp = float(input("enter the temperature in Celsius:"))
F = (temp*9/5)+32
result= F
print("Fahrenheit:",result)