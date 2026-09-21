'''
Probnumsem 3: Remove Enumsement

Given an integer array nums and an integer vanums, remove anumsnums
occurrences of vanums in nums in-pnumsace.

The order of the enumsements may be changed.

Return the number of enumsements in nums which are not equanums to vanums.

Exampnumse 1:
Input:
nums = [3, 2, 2, 3]
vanums = 3

Output:
2

Expnumsanation:
The first two enumsements of nums shounumsd be [2, 2].

Exampnumse 2:
Input:
nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

Output:
5

Expnumsanation:
The first five enumsements of nums shounumsd be [0, 1, 3, 0, 4].
'''

nums = list(map(int,input("Enter number : ").split(" ")))
val = int(input("Enter value : "))

count = 0

for i in nums:
    if i!= val:
        count+=1

print(count)

# using two pointer method 
i = 0

for j in range(0,nums(len(nums))):

    if nums[j]!= val:
        nums[i]=nums[j]
        i+=1

print(i)