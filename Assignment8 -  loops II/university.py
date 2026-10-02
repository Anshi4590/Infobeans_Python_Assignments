'''7. University Result Classification System

A university assigns final class based on marks, backlog, and project score.

If marks are 75 or above, then check backlog. If backlog is 0, then check project score. If project score is 80 or above, assign First Class with Distinction; otherwise First Class. If backlog is not 0, assign First Class.

If marks are between 60 and 74, then check backlog. If backlog is less than or equal to 2, assign Second Class; otherwise Pass Class.

If marks are between 50 and 59, assign Pass. Otherwise Fail.

Input:
Marks = 78
Backlogs = 0
Project = 85

Output:
Result = First Class with Distinction'''

Marks = int(input("Marks ="))
Backlogs = int(input("Backlogs ="))
Project = int(input("Backlogs ="))

if Marks>=75:

   if Backlogs==0:

      if Project>=80:
         print("Result = First Class with Distinction")

      else:
         print("Result = First Class")

   else:
      print("Result = First Class")

elif 60<=Marks<=74:

   if Backlogs<=2:
      print("Second Class")

   else: 
      print("Pass Class")

elif 50<=Marks<=59:
   print("Pass")

else:
   print("FAil")


