'''8.
Trimorphic Number Analyzer

A coding system checks cube-based patterns.

A Trimorphic Number:
Cube of number ends with the same number.

Example:
4³ = 64

Write a program to check Trimorphic Number.

Input:
4

Output:
Trimorphic Number'''

a = int(input("Enter Number"))
cube = a**3
l = len(str(a))
print(cube)
d = cube%10**l
print(d)

if d == a:
   print("is a Trimorphic Number")
else:
   print("not a Trimorphic Number")

    
 
