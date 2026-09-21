
'''
Given an integer array nums and an integer target, find three integers
in nums such that their sum is closest to target.

Return the sum of the three integers.

You may assume that each input has exactly one solution.

Example 1:

Input:
nums = [-1, 2, 1, -4]
target = 1

Output:
2

Explanation:
The sum 2 is closest to the target 1.
(-1 + 2 + 1 = 2)


Example 2:

Input:
nums = [0, 0, 0]
target = 1

Output:
0

Explanation:
The only possible sum is 0.


Example 3:

Input:
nums = [1, 1, 1, 0]
target = -100

Output:
2

Explanation:
The closest possible sum is 1 + 1 + 0 = 2.


Constraints:

- 3 <= len(nums) <= 500
- -1000 <= nums[i] <= 1000
- -10^4 <= target <= 10^4

Note:
The three selected elements must come from three different indices.
The goal is to minimize the absolute difference:

abs(sum - target)
'''


list =  [-1, 2, 1, -4]
closet  = float('-inf' )
target = -4
list.sort()
print(list)

for i in range(len(list)):
    #fixed
    n1 = list[i]
   

    if i>0  and list[i] == list[i-1]:
        continue
    
    left = i+1
    right = len(list)-1
  

    while left<right:

        sum = n1+ list[left] + list[right]

        if sum == target:

            closet = sum
            break

        if abs(sum-target)<abs(closet-target):
            closet=sum

        elif sum<target:
            left+=1

        else:
            right-=1

   
    
print(closet)

               


