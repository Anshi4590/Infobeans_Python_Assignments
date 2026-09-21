"""
Third Maximum Number

Given an integer array nums, return the third distinct maximum number
in the array.

If the third maximum number does not exist, return the maximum number.

Note:
The third maximum number must be distinct.

Examples:

Example 1:
Input:
nums = [3, 2, 1]

Output:
1

Explanation:
The maximum number is 3.
The second maximum number is 2.
The third maximum number is 1.

Example 2:
Input:
nums = [1, 2]

Output:
2

Explanation:
There is no third distinct maximum number,
so return the maximum number 2.

Example 3:
Input:
nums = [2, 2, 3, 1]

Output:
1

Explanation:
The distinct numbers are [1, 2, 3].
The third maximum number is 1.

Example 4:
Input:
nums = [5, 5, 4, 3, 2, 1]

Output:
3

Explanation:
The distinct maximum numbers are:
5 → first maximum
4 → second maximum
3 → third maximum

"""

l = list(map(int,input("Enter Number : ").split(" ")))
firstmax =  0
secondmax = 0
thirdmax =  0


# firstmax =  float("-inf")
# secondmax = float("-inf")
# thirdmax = float("-inf")

for i in list(set(l)):

   if i > firstmax:
         thirdmax = secondmax
         secondmax = firstmax
         firstmax = i

   elif i > secondmax:
         thirdmax = secondmax
         secondmax = i

   elif i > thirdmax:
         thirdmax = i
         
if  thirdmax== float("-inf"):       
   print(firstmax)

else:
   print(thirdmax)

