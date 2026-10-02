'''1.
Mountain Hiking Elevation Analysis

Problem Statement

A trekking company records the elevation (in meters) reached by a hiker at different checkpoints during a mountain climb.

A checkpoint is considered a peak checkpoint if its elevation is not smaller than its adjacent checkpoints.

Given an array elevation[] of size N, find the index of any one peak checkpoint.

Test Case 1

Input:
elevation = [1200, 1450, 1700, 1600, 1500]

Output:
2

Explanation:
1700 is greater than both adjacent values 1450 and 1600.

Test Case 2

Input:
elevation = [800, 900, 950, 1000]

Output:
3

Explanation:
Last element can also be a peak because it has no right neighbor.

Test Case 3

Input:
elevation = [3000]

Output:
0

Explanation:
Single element is always a peak.'''


n = int(input("Enter size:"))
num = []
for i in range(n):
    a = int(input("Enter element:"))
    num.append(a)
print(num)

peakelement = -1
for i in range(n):
    if i == 0 :
       if n == 1 or num[i]>=num[i+1] :
          peakelement = i
          break
    elif i == -1 :
        if num[i]>=n[i-1]:
          peakelement = i
          break
    elif num[i]>=num[i+1] and num[i]>=num[i-1]:
          peakelement = i
          break 

if peakelement == -1:
    print("peak not found")
else:
    print("peakelement:",num[peakelement])