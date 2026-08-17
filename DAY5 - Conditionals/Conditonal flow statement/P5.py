'''5. Banking Security System
   A bank validates login attempt:

* If username is "admin" → Valid user
* If password length ≥ 8 → Strong password

Input:
Enter username: admin
Enter password: secure123

Output:
Valid user
Strong password'''


#solution
username = input("Enter username:")
password = input("Enter password:")
 
if username =="admin":
    print("Valid User")

    if len(password) >= 8:
        print("Strong password")

else:
    print("invalid user")
