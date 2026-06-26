'''6. Armstrong Number (3-digit)
In coding competitions, certain numbers are considered unique. A 3-digit Armstrong number is one where the sum of the cubes of its digits equals the number itself.
Write a program to *check whether a number is an Armstrong number using loops*.

Input: 153
Output: Armstrong'''


#solution

n = int(input("enter the number"))
temp =n
rem = 0
sum = 0
'''l =len(str(n))
for i in range(l):
   rem = n%10
   sum = sum + rem**l
   n = n//10
print(sum)   
if sum == temp:
   print("is Armstrong")
else:
   print("not a Armstrong")'''
   

#while loop


while n>0:
   rem = n%10
   sum = sum + rem**l
   n = n//10
print(sum)   
if sum == temp:
   print("is Armstrong")
else:
   print("not a Armstrong")
   
