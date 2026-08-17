'''2. First Repeating Number
=========================

Scenario

A security system logs employee IDs.

Find the first ID that repeats in the list.

Requirements

* Read N and list elements from user
* Find the first repeating number
* If no repeating number exists, display an appropriate message

Test Case 1

Input:
[10, 5, 3, 4, 3, 5]

Output:
First Repeating Number = 3

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Repeating Number Found'''

arr = list(map(int,input("Enter number: ").split(" ")))

print(arr)

for i in arr:
    count = 0
    for j in arr:
        if i == j:
           count+=1
    if count>1:
       print(f"First Repeating Number = {i}")
       break
else:
    print("No Repeating Number Found")