'''9. Library Access System
   A library checks:

* If membership is active → Entry allowed
* If books issued < 3 → Can issue more books

Input:
Membership active (yes/no): yes
Books issued: 2

Output:
Entry allowed
Can issue more books'''

#solution
a =input("Membership active (yes/no):")
b =int(input("book issued:"))
if a.lower()== 'yes':
    print("Entry allowed")
    
    if b<3:
        print("can issue more book:")
else:
    print("not allowed")
