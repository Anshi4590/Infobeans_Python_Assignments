'''10.Zero Count Prime Scanner

A banking system checks account numbers.

Write a program to:

- Count zero digits
- Find sum of digits
- Add zero count and sum
- Multiply by smallest digit
- Check whether final result is Prime or Not

Input:
908406

Output:
Zero Count = 2
Sum = 27
Smallest Digit = 0
Final Result = 0
Not Prime'''

n = int(input("Enter the number"))
min = 9
sum=0
count =0

for i in range(len(str(n))):
   d = n%10
   n = n//10
   sum = sum+d
   if d == 0:
      count+=1
   if d<min:
      min = d
total = (sum +count)*min


print(count)
print(sum)
print(min)
print(total)

if total<=1:
   print("not prime")
else:
   for i in range(2,total//2+1):
      if total%i==0:
        print("not prime")
        break
   else:
      print("prime number")
 

   
