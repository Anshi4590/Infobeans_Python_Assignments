'''Assignment 5: Salary Breakdown

An employee wants to calculate salary per day and per hour.

Input:
Monthly salary = 36000
Working days = 24
Working hours per day = 8

Expected Output:
Salary per day = 1500.0
Salary per hour = 187.5'''


salary = int(input("Enter the Monthly Salary:"))
days = int(input("Enter the total working days:"))
hours = int(input("Enter the total working hours:"))
salaryd = salary/days
salaryh = salaryd/hours
print("Salary per day =",salaryd)
print("Salary per hour =",salaryh)