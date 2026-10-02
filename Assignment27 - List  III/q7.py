'''7. Array Rotation Analyzer
==========================

Scenario

Rotate the array K times towards the right.

Requirements

* Read N and list elements from user
* Read K
* Rotate the array
* Display rotated array

Test Case 1

Input:
Array = [1, 2, 3, 4, 5]
K = 2

Output:
[4, 5, 1, 2, 3]

Test Case 2

Input:
Array = [10, 20, 30, 40]
K = 1

Output:
[40, 10, 20, 30]

--- '''
arr=list(map(int,input("Enter The Elements : ").split(' ')))
k=int(input("Enter The Number Of Rotation : "))
print(arr)


n=len(arr)
k=k%n
arr1=[]

for i in range(n-k,n):
    arr1.append(arr[i])

print(arr1)
for i in range(0,n-k):
    arr1.append(arr[i])

print(arr1)