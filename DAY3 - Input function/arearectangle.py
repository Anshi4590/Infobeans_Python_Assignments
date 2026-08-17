
'''Assignment 4: Area of Rectangle

Write a Python program that:

Accepts length and breadth.
Calculates area.

Input:
Length = 10
Breadth = 5

Output:
Area = 50'''


length ,breadth = map(int,input("enter the value of length and breadth:").split())
area = length*breadth
print("Area of the Rectangle is:", area)