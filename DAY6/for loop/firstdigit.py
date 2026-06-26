'''3. First Digit of Number
A university receives thousands of application IDs. The first digit of each ID represents the department code, so the admission software must read the first digit quickly.
Write a program to find the first digit of a number using loops.

Input:
53892

Output:
First Digit = 5'''

#solution

n = int(input("enter number:"))

for i in range(len(str(n))):
   rem = n %10
   n = n//10
print(rem)

#while loop

while n>0:
   rem = n%10
   n = n//10
print("First Digit:",rem)