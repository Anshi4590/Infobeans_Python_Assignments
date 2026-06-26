'''5. Count Factors of Number
A mathematics learning app gives practice questions where students must know how many factors a number has. The app should automatically count the total factors of the entered number.
Write a program to count total factors of a number using loops.

Input:
12

Output:
Factors Count = 6'''

n = int(input("enter number"))
count=0

for i in range(1,n+1,+1):
   if n%i==0:
      count+=1
print("Factors Count =",count)


print ("while loop:")
j=1
sum =0
while j<=n:
  if n%j==0:
     sum+=1
  j=j+1
print("Factors Count:",sum)