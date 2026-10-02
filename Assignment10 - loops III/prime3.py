'''8. Largest Smallest Sum Prime Checker

A number analyzer finds largest and smallest digit.

Write a program to:

- Find largest digit
- Find smallest digit
- Find sum of both
- Check whether sum is Prime or Not

Input:
57294

Output:
Largest = 9
Smallest = 2
Sum = 11
Prime'''

n = int(input("enter the number"))
max = 0
min = 9
sum = 0
for i in range(len(str(n))):
    d = n%10
    n = n//10
    if d>max:
       max=d
    if d<min:
       min=d
sum = min + max
print("Largest = ",max)
print("Smallest = ",min)
print("Sum = ",sum)
if sum<=1:
   print("not prime")
else:
   for i in range(2,sum//2+1):
       if sum%i == 0:
         print("not prime")
         break
   else:
      print("prime number")
       
   
