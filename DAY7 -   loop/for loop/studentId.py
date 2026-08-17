'''10. Student ID Validity Checker (Count Odd Digits)
A school management system assigns numeric IDs to students. The administration wants to verify IDs by checking how many odd digits are present in each ID number. IDs with more odd digits are sent for manual review.

Write a program to count the number of odd digits in a given student ID using loops.

Input:
572943

Output:
Odd Digits Count = 3'''


#solution

n =int(input("enter number"))

rem = 0
count = 0
'''
for i in range(len(str(n))):
    rem = n%10
    if rem%2!=0:
       count+=1
    n = n//10
print("Even digits count =",count)
'''
sum = 0
while n>0:
    rem = n%10
    if rem%2!=0:
      sum+=1
    n = n//10
print("Even digits count =",sum)

    