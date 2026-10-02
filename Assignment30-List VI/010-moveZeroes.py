'''
Problem 10: Move Zeroes

Given an integer array nums, move all 0's to the end of it while
maintaining the relative order of the non-zero elements.

Note:
You must do this in-place without making a copy of the array.

Example 1:
Input:
nums = [0, 1, 0, 3, 12]

Output:
[1, 3, 12, 0, 0]

Example 2:
Input:
nums = [0]

Output:
[0]

Example 3:
Input:
nums = [1, 2, 3]

Output:
[1, 2, 3]


'''

nums = list(map(int,input("Enter numbers : ").split(" ")))

i = 0
for j in range(0,len(nums)):
    if nums[j]!= 0:
       temp = nums[j]
       nums[j] = nums[i]
       nums[i] = temp
       i+=1
       
print(nums)