'''
1. Remove All Special Characters from a String

Online Banking Customer Data Cleaning System

A private bank has launched a new online account opening portal. While entering customer details, many users accidentally type unnecessary symbols, emojis, hashtags, dollar signs, and special characters in their names and addresses.

Before storing the data into the database, the bank wants a Python program that removes all unwanted special characters and keeps only:

* Alphabets
* Numbers
* Spaces

The cleaned value should be stored back into the original string variable.

Input:

Deepika@@ Padukone!! 123
Output:
Deepika Padukone 123
Input:
Output:
AjaySingh
'''
n = input("Enter input")
result = ""
for i in n:
    if i>='a' and i<='z':
       result+=i
    elif i>='A' and i<='Z':
       result+=i
    elif i>='0' and i<='9':
       result+=i
    elif i==" ":
       result+=i
    else:
       continue
print(result)

       