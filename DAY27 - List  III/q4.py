'''====================================================================
4. Longest Consecutive Sequence
===============================

Scenario

Find the longest sequence of consecutive numbers present in the list.

Requirements

* Read N and list elements from user
* Find the length of the longest consecutive sequence
* Display the sequence length

Test Case 1

Input:
[100, 4, 200, 1, 3, 2]

Output:
Longest Consecutive Length = 4

Explanation:
Sequence = 1, 2, 3, 4

Test Case 2

Input:
[10, 11, 12, 20]

Output:
Longest Consecutive Length = 3
'''
n = int(input("Enter Size:"))
num =[]
for i in range(n):
    num.append(int(input("Enter number : ")))
print(num)

count2 = 0
for i in num:
    count = 1
    if i+1 in num:
        count+=1
    if count>count2:
       count2=count
print(count2)


arr=list(map(int,input("Enter The Elements : ").split(' ')))
print(arr)

n=len(arr)
arr.sort()
long=1
curr=1
start=0
end=0

for i in range(1,n):
    if arr[i]-arr[i-1]==1:
        curr+=1
    else:
        curr=1
        start=i
    
    if curr>long:
        long=curr
        end=i

print(f"Longest  cons.. length {long}")

for i in range(end - long + 1, end + 1):
    print(arr[i], end=" ")

       