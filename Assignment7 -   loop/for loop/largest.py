
'''1. Largest Digit in Number
A cybersecurity company checks numeric passwords used in smart lockers. To identify password strength, the system finds the highest digit present in the entered password. Higher digits indicate stronger variation in the password pattern.
Write a program to find the largest digit in a number using loops.

Input:
57294

Output:
Largest Digit = 9'''





n = int(input("enter number:"))
max = 0
rem = 0

for i in range(len(str(n))):
   rem = n%10
   if max<=rem:
      max = rem
   n = n//10
   
print("Largest Digit =", max)     
 

#while loop

while n>0:
   rem = n%10
   if max<=rem:
      max = rem
   n = n//10
print("Largest Digit:", max)