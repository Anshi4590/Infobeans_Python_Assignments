'''4. Numbers Divisible by 3 Between Two Numbers
A school is organizing a quiz competition. Only students whose roll numbers are divisible by 3 are selected for the first round. The teacher enters a roll number range and wants the system to display eligible roll numbers.
Write a program to display numbers divisible by 3 between two given numbers using loops.

Input:
10 25

Output:
12 15 18 21 24'''


#solution

#using for loop

a,b = map(int,input("enter the number:").split())
for i in range(a,b,+1):
    if i%3==0:
      print(i,end=" ")


#using while loop

while a<=b:
    if a%3==0:
      print("\nroll number",a,end=" ")
    a = a+1

      