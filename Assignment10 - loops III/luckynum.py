'''Prime Sum Lucky Number

A lottery app checks if sum of digits is prime.

Write a program to:

- Find sum of digits
- If prime print Lucky Number
- Else Normal Number

Input:
4528

Output:
Sum = 19
Lucky Number'''

m = int(input("enter the number"))
sum =0
for i in range(len(str(m))):
    d = m%10
    sum = sum +d
    m = m//10
print(sum)
if sum <=1:
   print("not prime")
else:
   i = 2
   while i<=sum//2:
      if sum%i==0:
         print("not prime")
         break
      i = i+1
   else:
     print("prime number\nLucky number")
   
      