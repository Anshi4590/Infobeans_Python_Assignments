'''6. Sum of Factors
A puzzle-based game rewards users based on the sum of all factors of a chosen number. The system calculates the total score using all factors of the entered number.
Write a program to find sum of factors using loops.

Input:
6

Output:
Sum = 12'''
 
#solution

n = int(input("enter number"))
count=0

for i in range(1,n+1,+1):
   if n%i==0:
      count = count +i
print("Factors Count =",count)


print ("while loop:")
j=1
sum =0
while j<=n:
  if n%j==0:
     sum = sum+j
  j=j+1
print("Factors Count:",sum)