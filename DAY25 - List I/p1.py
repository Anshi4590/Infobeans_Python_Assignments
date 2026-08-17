'''.Student Marks Management
Create a program to store student marks in a List and perform operations.

Requirements:

Add student marks into a List
Display all marks
Find highest and lowest marks
Count students who scored above 75

Test Cases:

Input: [45, 67, 89, 90, 76] → Highest = 90, Lowest = 45, Count Above 75 = 3
Input: [10, 20, 30] → Highest = 30, Lowest = 10, Count Above 75 = 0
Input: [100, 99, 98] → Highest = 100, Lowest = 98, Count Above 75 = 3'''

n = int(input("Enter size means how many elemnets you want: "))
nums =[]
for i in range((n)):
    a = int(input("Enter elements:"))
    nums.append(a)
print(nums)
largest = nums[0]
smallest = nums[0]
count =0
for i in nums:
    if i >largest:
       largest = i
    if i <smallest:
       smllest = i
    if i>75:
       count+=1
print(f"largest of the elements:{largest}")
print(f"Smallest of the elements:{smallest}")
print(f"count:{count}")