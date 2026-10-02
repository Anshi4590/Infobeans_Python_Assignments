'''2. Smallest Digit in Number
A manufacturing company prints serial numbers on products. During quality testing, the scanner needs to detect the smallest digit in the serial number to verify coding standards.
Write a program to find the smallest digit in a number using loops.

Input:
57294

Output:
Smallest Digit = 2'''

#solution
# for loop

n = int(input("enter number:"))
min = 9
rem = 0
for i in range(len(str(n))):
   rem = n%10
   if min>=rem:
      min = rem
   n = n//10
 
print("Smallest number =",min)     

#while loop


while n>0:
   rem = n%10
   if min>=rem:
      min = rem
   n = n//10
print("Smallest number:",min)