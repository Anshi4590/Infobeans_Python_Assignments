'''4.Spy Number Detector

A cybersecurity system flags special numeric codes.

A number is called a Spy Number if:
Sum of digits = Product of digits

Write a program to check whether the entered number is Spy Number or Not.

Input:
1124

Output:
Spy Number'''



m = int(input("Enter number"))
sum = 0
product =1

for i in range(len(str(m))):
     d = m%10
     sum = sum + d
     product = product*d
     m = m//10

print(sum)
print(product)

if sum == product:
   print("Spy Number")
else:
   print("Not a Spy Number")


