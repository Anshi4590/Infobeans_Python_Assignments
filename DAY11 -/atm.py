'''8.

 ATM Note Counter


A bank ATM dispenses ₹100 notes.


Write a program to:


- Read withdrawal amount

- Count how many ₹100 notes needed using loop


Input:

700


Output:

Notes = 7'''

n = int(input("Enter number"))
if n>100:
   d = n//100
   print("Notes =",d)

   