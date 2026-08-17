'''2. Multi Stage Prime Lock System


A smart locker opens only if final derived number is prime.


Write a program to:


- Find sum of digits

- Find product of digits

- Find difference between product and sum

- Count digits in difference

- Add digit count to difference

- Check whether final result is Prime or Not


Input:

234


Output:

Sum = 9

Product = 24

Difference = 15

Digits = 2

Final Result = 17

Prime'''




a = int(input("enter the number ="))
sum = 0
product = 1
count = 0
i=1

while a>0:
    d = a%10
    sum = sum+d
    product = product*d
    a = a//10

print("Sum Of the Digits = ",sum)

print("Product of the digits =",product)

diff = (abs(product - sum))
temp = diff

print("Difference =",diff)

for i in range(len(str(diff))):

    e = diff%10
    count+=1
    diff = diff//10

print("Total count of the Digits in Difference = ",count)


result = count + temp

print("Final Result=",result)

if result<=1:

   print("Not Prime")

else:

   for i in range(2,result//2+1):

       if result%i ==0:

          print("Not Prime")

          break

   else:

      print("Prime number")