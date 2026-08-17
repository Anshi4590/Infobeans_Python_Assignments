'''1. Count Pairs with Difference K

A company records the ages of employees. Find how many pairs of employees have an age difference exactly equal to K.

Problem Statement:

Given an array of employee ages and an integer K, count the number of pairs whose absolute difference is K.

Example:

Input:

N = 5
K = 2
ages[] = {1, 5, 3, 4, 2}

Output:

3

Explanation:

(1,3), (3,5), (2,4)'''

n = int(input("Enter  total no.of elements : "))
k = int(input("Enter absolute Difference : "))

arr = list(map(int,input("Enter number : ").split(" ")))
print (arr)
sub  = []
count=0
for i in arr:
    for j in arr:
        diff=abs(i-j)
        if diff== k:
            if i and j not in sub:
                sub.append(i)
            else:
                count+=1
                print(j,i)
           


       

            

print(count)