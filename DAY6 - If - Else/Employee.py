'''13. Employee Performance Appraisal System


A company evaluates employees based on performance rating (1–5):

* 5 → 25% salary hike
* 4 → 20% salary hike
* 3 → 10% salary hike
* 2 → 5% salary hike
* 1 → No hike
  If salary is below ₹20000 and rating is 4 or above, an additional ₹2000 bonus is given.

Write a Python program to calculate revised salary.

Input:
Enter salary: 18000
Enter rating: 4

Output:
Revised Salary: ₹23600'''

#solution

salary = int(input("Enter salary:"))
rating = int(input("Enter salary:"))

if rating == 5:
   salary = salary +salary*25/100
   print("Revised Salary:",salary)

elif rating ==4:
   salary = salary +salary*20/100
   print("Revised Salary:",salary)

elif rating ==3:
   salary = salary +salary*10/100
   print("Revised Salary:",salary)

elif rating ==2:
   salary = salary +salary*5/100
   print("Revised Salary:",salary)

elif rating == 1:
   print("no hike:",salary)  


