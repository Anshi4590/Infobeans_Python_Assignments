'''
Assignment 2: Binary Converter for Embedded System

Task:
Write a recursive function to convert a decimal number
into its binary representation.

Input:
Enter a decimal number:
25

Output:
Binary Number = 11001
'''

def binary(n,ans):
    if n//2 < 1:

       return "1"+ ans

    r = n%2
    return binary(n//2,str(r)+ans)

n = int(input("Enter Number : "))
ans =""
print(binary(n,ans))