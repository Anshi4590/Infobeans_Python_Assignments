'''
Problem 5: Plus One

You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.

The digits are ordered from most significant to least significant
in left-to-right order.

Increment the large integer by one and return the resulting array
of digits.

Example 1:
Input:
digits = [1, 2, 3]

Output:
[1, 2, 4]

Explanation:
The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.

Example 2:
Input:
digits = [4, 3, 2, 1]

Output:
[4, 3, 2, 2]

Example 3:
Input:
digits = [9]

Output:
[1, 0]

Explanation:
The array represents the integer 9.
Incrementing by one gives 10.

'''
nums = list(map(int,input("Enter number :").split(" ")))
m = len(nums)-1
if nums[m]!=9:
    new = nums[m]+1
    nums[m] = new
    print(nums)
    
else:
    for i in range(-1,-(len(nums)+1),-1):
        if nums[i]==9 :
            nums[i] = 0
            
    else:
        nums=[1]+nums
            

            
    print(nums)