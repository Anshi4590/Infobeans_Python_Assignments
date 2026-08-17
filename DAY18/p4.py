'''
4.
Employee ID Validator

A company wants to validate employee IDs before storing them in the database.

Conditions:
- ID must start with "EMP"
- Total length should be 8
- Remaining characters should be digits only

Input:
Enter Employee ID: EMP10234

Output:
Valid Employee ID

'''
n = input("Enter Employee ID :")
result = ""
count = 0
for i in range(0,3):
    result+=n[i] 
print(result)
for i in range(3,len(n)):
    if n[i]>="0" and n[i]<="9":
        count=1
print(count)
if len(n)==8 and count==1 and result == "EMP":
    print("Valid Employee ID")
else:
    print("INValid Employee ID")

