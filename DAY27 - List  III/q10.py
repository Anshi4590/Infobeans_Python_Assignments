'''====================================================================
10. Find Duplicate Numbers
==========================

Scenario

A company stores employee IDs in a list. Some IDs may appear more than once due to data entry errors.

Requirements

* Read N and list elements from user
* Find all duplicate numbers
* Store duplicates in another list
* Count total duplicate numbers
* Display duplicates in sorted order

Test Case 1

Input:
[1, 2, 3, 2, 4, 5, 1]

Output:
Duplicate Numbers = [1, 2]
Count = 2

Test Case 2

Input:
[10, 20, 30]

Output:
No Duplicate Numbers Found

---'''

n = int(input("Enter Size:"))
num =[]
for i in range(n):
    num.append(int(input("Enter number : ")))
print(num)
duplicate = []
dcount = 0 

for i in num:
  if i not in duplicate:
    m = num.count(i)
    if m>1:
        duplicate.append(i)
        dcount+=1
            
if duplicate == []:
    print("No duplicate element found")
else:
    print(sorted(duplicate))
    print(dcount)