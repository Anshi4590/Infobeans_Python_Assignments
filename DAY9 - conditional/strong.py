'''4. Strong Number Checker

A digital lock opens only for strong numbers.

A strong number is a number whose sum of factorial of digits equals the number.

Example:
145 = 1! + 4! + 5!

Write a program using loops to check strong number.

Input:
145

Output:
Strong Number'''

#solution

n = int(input("Enter the number:"))
fact = 1
sum = 0

for i in str(n):
    i=int(i) # string to int
    for j in range(1,i+1):
        fact*=j
    sum+=fact
    fact=1
print(sum)   
if sum==n:
    print("Strong no.")
else:
    print("not a Strong")
  




