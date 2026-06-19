
'''Assignment 11: Time Duration Adder

Write a Python program that:

Accepts hours, minutes, seconds.
Converts into total seconds.

Input:
Hours = 1
Minutes = 2
Seconds = 30

Output:
Total Seconds = 3750'''


hour, min ,sec = map(int,input("enter the hours minutes and second:").split())
a = hour*3600
b = min*60
c = sec+a+b
print("Total seconds:",c)
