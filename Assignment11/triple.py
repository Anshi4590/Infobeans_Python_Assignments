'''1. Triple Operation Prime Verification System


A cybersecurity company generates a security score from entered access code.


Write a program to:


- Find sum of digits of the number

- Reverse the number

- Find absolute difference between original number and reverse

- Add digit sum and difference

- Check whether final result is Prime or Not Prime


Input:

4215


Output:

Sum of Digits = 12

Reverse = 5124

Difference = 909

Final Result = 921

Not Prime'''



m = int(input("Enter the number = "))
original = m
sum =0
rev=0

i=1

while m>0:
    d = m%10
    sum = sum+d
    rev = rev*10+d
    m = m//10

print("Sum Of the Digits = ",sum)

print("Reverse of the number = ",rev)

diff = abs(original - rev)

total = sum + diff

print("Difference =",diff)

print("Final Result =",total)

if total<=1:

   print("Not Prime")

else:

   for i in range(2,total//2+1):

       if total%i ==0:

          print("Not Prime")

          break

   else:

      print("Prime number")

         



