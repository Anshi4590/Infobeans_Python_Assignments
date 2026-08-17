'''7.
Vehicle Number Plate Checker

The traffic department wants to validate vehicle registration numbers.

Conditions:
- First 2 characters should be alphabets
- Next 2 should be digits
- Total length should be 10

Input:
Enter vehicle number: MP04AB1234

Output:
Valid Vehicle Number'''

n = input("Enter vehicle number:")
y = n[2:4]
print(y)
if n.startswith("MP") and len(n)==10 and y.isnumeric():
   print("Valid Vehicle Number")
else:
   print("InValid Vehicle Number")

