'''2.
Smart City Traffic Peak Load Analyzer

Problem Statement

A smart city monitors traffic density at different time intervals in a day.

An element is called a peak traffic point if it is greater than or equal to its adjacent elements.

You are given an array traffic[] of size N.

Tasks:

Find all peak elements
Calculate the sum of all peak traffic values
Find the product of all peak traffic values
Return the maximum peak value

Note:
If only one element exists, it is the only peak.

Test Case 1

Input:
traffic = [10, 50, 30, 70, 60, 90, 80]

Output:
Peaks = [50, 70, 90]
Sum = 210
Product = 315000
Max Peak = 90

Test Case 2

Input:
traffic = [100, 200, 150, 180, 170]

Output:
Peaks = [200, 180]
Sum = 380
Product = 36000
Max Peak = 200

Test Case 3

Input:
traffic = [5]

Output:
Peaks = [5]
Sum = 5
Product = 5
Max Peak = 5
'''


n = int(input("Enter size:"))
num = []
for i in range(n):
    a = int(input("Enter element:"))
    num.append(a)
print(num)

peakelement = []
for i in range(n):
    if i == 0 :
       if n == 1 or num[i]>=num[i+1] :
          peakelement.append(num[i])
          
    elif i == n-1 :
        if num[i]>=num[i-1]:
          peakelement.append(num[i])
          
    else:
        if num[i]>=num[i+1] and num[i]>=num[i-1]:
          peakelement.append(num[i])
        

print("peak:",peakelement)
sum = 0
product =1
largest = peakelement[0]
for i in peakelement:
    sum+=i
    product = product*i
    if i>largest:
       largest = peakelement[i]

print("sum:",sum)
print("Product: ",product)
print("Largest: ",largest)