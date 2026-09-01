'''
Problem 2: Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove
the duplicates in-place such that each unique element appears only
once.

The relative order of the elements should be kept the same.

Return the number of unique elements in nums.

Example 1:
Input:
nums = [1, 1, 2]

Output:
2

Explanation:
The first two elements of nums should be [1, 2].

Example 2:
Input:
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

Output:
5

Explanation:
The first five elements of nums should be [0, 1, 2, 3, 4].

'''

arr = list(map(int,input("Enter number :").split(" ")))
print(arr)

unique =[]
checked = []
flag = 1

for i in range(len(arr)):

    if i not in checked:

        for j in range(i+1,len(arr)):
            checked.append(arr[i])
            if arr[i] == arr[j]:
               flag =0
               break

        if flag == 1:
        
           unique.append(arr[i])

        flag = 1
        
print(unique)


# optimal solution

i = 0

for j in range(1,len(arr)):

    if arr[i]!= arr[j]:
        i+=1
        arr[i]=arr[j]

    print(i+1)
       