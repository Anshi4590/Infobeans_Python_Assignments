'''
====================================================================
6. Product Except Self
======================

Scenario

For every element, calculate the product of all other elements except itself.

Requirements

* Read N and list elements from user
* Create a new list containing products
* Display the result

Test Case 1

Input:
[1, 2, 3, 4]

Output:
[24, 12, 8, 6]

Test Case 2

Input:
[2, 3, 5]

Output:
[15, 10, 6]

---'''
arr = list(map(int,input("Enter number: ").split(" ")))

print(arr)
new = []
product = 1
for i in arr:
    arr.remove(i)
    for j in arr:
        product*=j
    new.append(j)
    arr.append(i)
print(new)



arr=list(map(int,input("Enter The Elements : ").split(' ')))
print(arr)
n=len(arr)

result=[]


for i in range(n):
    p=1
    for j in range(n):
        if i==j:
            continue
        else:
            p*=arr[j]
    
    result.append(p)

print(result)