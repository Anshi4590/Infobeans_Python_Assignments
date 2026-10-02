
'''
Question 14: Find the Difference of Two Arrays

Easy

Given two integer arrays nums1 and nums2, find the distinct integers that are present in nums1 but not in nums2, and the distinct integers that are present in nums2 but not in nums1.

Return the result as a list containing two lists:
- The first list contains elements that are in nums1 but not in nums2.
- The second list contains elements that are in nums2 but not in nums1.

Example 1:
Input:
nums1 = [1, 2, 3]
nums2 = [2, 4, 6]

Output:
[[1, 3], [4, 6]]

Example 2:
Input:
nums1 = [1, 2, 3, 3]
nums2 = [1, 1, 2, 2]

Output:
[[3], []]

Example 3:
Input:
nums1 = [4, 5, 6]
nums2 = [4, 5, 6]

Output:
[[], []]

Constraints:
- 1 <= len(nums1), len(nums2) <= 1000
- Elements are integers.
- Duplicate elements should appear only once in the result.

'''

num1 = list(map(int,input("Enter Number : ").split(" ")))
num2 = list(map(int,input("Enter Number : ").split(" ")))

set1= set(num1)
set2 = set(num2)

a = set1-set2
b = set2-set1

print([list(a),list(b)])


