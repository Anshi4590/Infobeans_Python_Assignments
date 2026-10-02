'''
8.
Online Exam Result Processing System

An online examination system stores marks of multiple classes.
Each class contains multiple students, and each student has marks for multiple subjects.

The program should use:
- First loop for classes
- Second loop for students
- Third loop for subjects

The system calculates total marks of every student.

Input:
Enter number of classes: 2
Enter students per class: 2
Enter subjects per student: 3

Class 1

Student 1
Enter mark: 70
Enter mark: 80
Enter mark: 90

Student 2
Enter mark: 60
Enter mark: 75
Enter mark: 85

Class 2

Student 1
Enter mark: 88
Enter mark: 77
Enter mark: 66

Student 2
Enter mark: 90
Enter mark: 92
Enter mark: 95

Output:
Class 1
Student 1 Total = 240
Student 2 Total = 220

Class 2
Student 1 Total = 231
Student 2 Total = 277'''


class1 = int(input("Enter the number of the classes:"))
student = int(input("Enter the number of the students:"))
sub =  int(input("Enter the number of the subjects:"))


a = 1
while a<=class1:
   
   print("class",a)
   b = 1
   while b<=student:
      print("student",b)
      c =1;total =0
      while c<=sub:
         m = int(input("Enter marks:"))
         total+=m
         c = c+1
      print("students marks :",total)
      total=0
      b = b+1
   print()
   a = a+1







