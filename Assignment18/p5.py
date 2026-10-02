'''
5.

Palindrome Product Code Checker

A factory wants to identify whether a product code reads the same forward and backward.

Input:
Enter product code: MADAM

Output:
Palindrome Code

Input:
Enter product code: PRODUCT

Output:
Not a Palindrome Code

'''
n =input("Enter product code:")
result = ""

for i in range(-1,-(len(n)+1),-1):
    result+= n[i]

print(result)

if n == result:
   print("Palindrome Code")
   
else:
   print("Not a Palindrome Code")


