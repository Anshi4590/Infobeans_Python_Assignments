'''
2.  Corporate Employee Short ID Generator

A multinational company wants to automatically generate short IDs for employees while creating official email accounts. The system should take the employee’s full name and create an ID using the first character of each word.

Conditions: - Take first character of every word - Convert all characters to uppercase

Input: Enter employee name: ajay singh thakur

Output: Employee Short ID: AST

'''

n = input("Enter Employee Name: ")
result =""
m = (n.title()) 
for i in range(0,len(m)):
    if  m[i-1] == " " or i==0:
        result+=m[i]
print("Employee Short ID:",result)