'''7. Power of a Number
A scientific calculator app is used by engineering students for repeated multiplication operations. It should calculate the value of a number raised to a given power.
Write a program to calculate n raised to power p using loops.

Input:
2 5

Output:
32'''


#solution

value,power = map(int,input("enter the number:").split())
product =1
for i in range(1,power+1,+1):
   product = product*value
   print (product)
print("power of the given number is:",product)


#while loop

pro = 1
while power>0:
   pro = pro*value
   power-=1
print("power of the given number is=",pro) 