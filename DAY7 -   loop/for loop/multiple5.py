'''8. Count Multiples of 5 Between Two Numbers
A supermarket gives coupons to customers whose token numbers are multiples of 5. The manager enters a token range and wants to know how many eligible token numbers exist.
Write a program to count numbers divisible by 5 between two given numbers using loops.

Input:
1 20

Output:
Count = 4'''


#solution


x,y = map(int,input("enter number:").split())
count = 0
for i in range(x,y+1,+1):
   if i%5==0:
      count+=1
print(count)
     

#while loop

sum = 0

while x<=y:
   if x%5==0:
      sum+=1
   x+=1
print(sum)

