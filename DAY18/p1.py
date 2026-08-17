'''
1.
Email Username Validator

A company wants to check whether an employee email username is valid before creating an official account.

Conditions:
- Username should start with a letter
- Username can contain letters, digits, underscore (_)
- No spaces allowed
- Length should be between 5 and 12 characters

Input:
Enter username: ajay_123

Output:
Valid Username

'''

n = input("Enter username:")
letter = 0
digits = 0
space = 0
underscore = 0
for i  in range(len(n)):
    ch = n[i]
    if  ch>='a' and ch<='z':
        letter=1
    elif ch>='0' and ch<='9':
        digits=1
    elif ch == " ":
        space =1
    elif ch == "_":
        underscore =1
    else:
        print("InValid Username") 
if len(n)>=5 and len(n)<=12 and letter == 1 and digits == 1 and space== 0 and underscore == 1:
      print("Valid Username")
else:
      print("InValid Username")

