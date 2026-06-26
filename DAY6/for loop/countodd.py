'''*8. Count Odd Digits*
A banking system flags IDs with too many odd digits for further verification.
Write a program to *count the number of odd digits in a given number using loops*.

Input: 123456
Output: Odd digits count = 3'''

#solution

n =int(input("enter number"))
rem = 0
count = 0
for i in range(len(str(n))):
    rem = n%10
    if rem%2!=0:
       count+=1
    n = n//10
print("Even digits count =",count)

