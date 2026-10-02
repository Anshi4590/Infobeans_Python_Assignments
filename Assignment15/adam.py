'''7.
Adam Number Verification System – Question

A high-security digital system is designed to validate special mirrored numbers known as Adam Numbers before granting access to sensitive data.

When a user enters a numeric code, the system performs a dual verification process:

* It calculates the square of the entered number.
* It reverses the number and calculates the square of the reversed value.
* Finally, it checks whether both results are mirror images (reverses) of each other.

A number is called an Adam Number if:
The square of the number and the square of its reverse are reverses of each other.

Task:
Write a Python program to check whether a given number is an Adam Number or not.

Examples:

Input:
12
Output:
Adam Number

Input:
13
Output:
Not an Adam Number

Input:
11
Output:
Adam Number

Example:
12 → 12² = 144, reverse(12) = 21 → 21² = 441 → reverse of 144
'''


a = int(input("Enter number"))
square = a**2
rev = 0
rev1 = 0

for i in range(len(str(a))):
    d = a%10
    rev =rev*10 +d
    a = a//10

revsquare = rev**2
print(square)
print(rev)
print(revsquare)

for i in range(len(str(revsquare))):
    d = revsquare%10
    rev1 =rev1*10 +d
    revsquare = revsquare//10

print(rev1)
if square == rev1:
   print("Adam Number")
else:
   print("Not Adam Number")


  


































