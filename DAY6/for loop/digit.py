'''*9. Check All Digits Are Even*
A machine only accepts numbers where every digit is even. If any digit is odd, the number is rejected.
Write a program to *check whether all digits of a number are even using loops*.

Input: 2468
Output: All Even

Input: 2456
Output: Not All Even'''


#solution


n = int(input("Enter the number"))
rem = 0
x = len(str(n))
count = 0
for i in range(x):
    rem = n%10
    if rem%2==0:
        count+=1
    n = n//10
if count==x:
     print("All are even")
else: 
     print("All are not even")
