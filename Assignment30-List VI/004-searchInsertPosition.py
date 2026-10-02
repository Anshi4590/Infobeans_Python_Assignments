'''
Problem 4: Search Insert Position

Given a sorted array of distinct integers and a target value,
return the index if the target is found.

If the target is not found, return the index where it would be
inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input:
nums = [1, 3, 5, 6]
target = 5

Output:
2

Example 2:
Input:
nums = [1, 3, 5, 6]
target = 2

Output:
1

Example 3:
Input:
nums = [1, 3, 5, 6]
target = 7

Output:
4

Example 4:
Input:
nums = [1, 3, 5, 6]
target = 0

Output:
0
'''

target = int(input("Enter Target :"))
nums = list(map(int,input("Enter number :").split(" ")))

for j in range(len(nums)):
    if nums[j]>=target:
        print(j)
        break

else:
    print(len(nums))