'''2.Employee Salary Processing
Store employee salaries in a List and calculate details.

Requirements:

Store salaries
Find average salary
Display salaries greater than average
Remove salaries below 15000

Test Cases:

Input: [10000, 20000, 30000] → Average = 20000, Above Average = 30000
Input: [15000, 15000, 15000] → Average = 15000
Input: [5000, 7000] → Remaining List = []'''
n = int(input("Enter size means how many elemnets you want: "))
nums =[]

for i in range((n)):
    a = int(input("Enter elements:"))
    nums.append(a)
print(nums)
average =0
sum =0
for i in nums:
    sum+=i
average = sum/n
print(average)
for i in nums:
    if average<i:
        print("Average",i)
    else:
        print(nums.remove(i))
print(nums)