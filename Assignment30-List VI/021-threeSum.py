'''
Given an integer array nums, find all unique triplets
[a, b, c] such that:

    a + b + c = 0

Return all the triplets in the array.

Each triplet must contain three different indices,
and the solution must not contain duplicate triplets.

Example:

Input:
nums = [-1, 0, 1, 2, -1, -4]

Output:
[[-1, -1, 2],
 [-1, 0, 1]]

Explanation:
- (-1) + (-1) + 2 = 0
- (-1) + 0 + 1 = 0

The order of the triplets does not matter.
'''

list =  [-1, 0, 1, 2, -1, -4]
ans =[]
list.sort()
print(list)

for i in range(len(list)):

    n1 = list[i]
    target = -(n1)

    if list[i] == list[i-1]:
        continue
    
    left = i+1
    right = len(list)-1
    anssub = []

    while left<right:

        sum = list[left] + list[right]

        if sum == target:

            anssub = [n1,list[left],list[right]]
            ans.append(anssub)
            left+=1
            right-=1

            while left<right and list[left] == list[left-1]:
                left+=1

            while left<right and list[right] == list[right-1]:
                right-=1

        elif sum<target:
            left+=1

        elif sum>target:
            right-=1

    # ans.append(anssub)
    # anssub = []
    
print(ans)

               


