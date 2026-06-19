
'''Assignment 2: Lifetime Calculator
========================================

You are developing a feature for a health and wellness mobile app that helps users understand how long they've been alive in a more tangible way.

Write a Python program that:
- Accepts the user’s age in years as input.
- Calculates the approximate number of:
  Days lived (1 year = 365 days)
  Hours lived
  Minutes lived
- Displays the output in the format:

You've lived approximately:
Days: xxx
Hours: yyy
Minutes: zzz

Sample Input:
Enter your age in years: 18

Sample Output:
You've lived approximately:
Days: 6570
Hours: 157680
Minutes: 9460800'''


age = int (input("enter the age in years"))
days = age*365
hours = days*24
minutes = hours*60
print( "You have lived: \nDays :{} \nHours: {} \nMinutes:{}".format( days,hours,minutes))