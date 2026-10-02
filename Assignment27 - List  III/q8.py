'''====================================================================
8. Majority Element Detector
============================

Scenario

Find an element occurring more than N/2 times.

Requirements

* Read N and list elements from user
* Find majority element
* If not present, display appropriate message

Test Case 1

Input:
[2, 2, 1, 2, 3, 2, 2]

Output:
Majority Element = 2

Test Case 2

Input:
[1, 2, 3, 4]

Output:
No Majority Element Found '''

n = int(input("Enter size : "))
num =[]
for i in range(n):
    num.append(int(input("Enter number : ")))
print(num)
major = 0
element = 0
for i in num:
    count = 0
    for j in num:
        if i == j:
            count+=1
    
    if count>major:
        major = count
        element = i
if major == 0:

   print(major)
   print(element)
 
