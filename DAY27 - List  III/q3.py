'''3. Missing Number Detector
==========================

Scenario

Numbers from 1 to N should exist in a sequence, but one number is missing.

Requirements

* Read N and list elements from user
* Find the missing number
* Assume numbers belong to the range 1 to N+1

Test Case 1

Input:
[1, 2, 3, 5]

Output:
Missing Number = 4

Test Case 2

Input:
[2, 3, 4, 5]

Output:
Missing Number = 1

Test Case 3

Input:
[1, 2, 4, 5]

Output:
Missing Number = 3

---
'''
n = int(input("Enter Size:"))
num =[]
for i in range(n):
    num.append(int(input("Enter number : ")))
print(num)
miss = ""

for i in num:
    for j in range(1,n+1):
        if i!=j:
           miss+=j+" "
if miss == " ":
   print("No missing element found")
else:
   print(f"Missing Number : {miss}")


