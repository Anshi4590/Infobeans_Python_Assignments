
'''Assignment 3: Student Marks Analysis

A student wants to calculate total marks, average, and percentage from 5 subjects.

Input:
Marks = 78, 85, 90, 88, 80

Expected Output:
Total = 421
Average = 84.2
Percentage = 84.2'''



a,b,c,d,e = map(int,input("Enter the marks of the 5 subjects:").split())
outof = int(input("enter the max marks:"))
total = a+b+c+d+e
Average = total/5
percent = (total/(outof*5))*100
print("Total:",total)
print("Average:",Average)
print("Percentage:",percent)