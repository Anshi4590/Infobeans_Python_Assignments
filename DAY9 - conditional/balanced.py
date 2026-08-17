'''9.
Step Difference Number Analyzer

A mathematics research center studies hidden patterns inside numbers.
For every entered number, the system compares adjacent digits step by step.

Write a program to:

Find the absolute difference between every pair of adjacent digits
Display all step differences
Find the sum of all step differences
Find the largest step difference
If the sum of step differences is divisible by the number of digits, print Balanced Number
Otherwise print Unbalanced Number
 
Use loops wherever required.

Input:
57294
Output:
Step Differences: 2 5 7 5
Sum = 19
Largest = 7
Unbalanced Number'''

n = int(input("Enter the number:"))
l =len(str(n))-1
temp =n
first = n%10
n = n//10
sum =0

while n>0:

   second = n%10
   diff = abs(second-first)
   sum = sum*10 + diff
   n = n//10
   first = second

print(sum)
new=0
total =0
max =0
while sum>0:
  d = sum%10
  new = new*10 + d
  total = total + d
  
  if d>max:
    max = d
  
  sum = sum//10
print(max)
print(total)


if total%l==0:
   print("balanced")
else:
   print("unbalanced")
  
   
  


 
 
