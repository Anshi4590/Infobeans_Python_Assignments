'''Assignment 1: Student Result Calculator

A school wants to calculate the total marks and percentage of a student.

Create a class Student with the following attributes:

Student name

Roll number

Marks in English

Marks in Mathematics

Marks in Science

Create the following methods:

calculate_total() – Calculate the total marks.

calculate_percentage() – Calculate the percentage.

display_result() – Display student details, total, and percentage.

Expected output:

Student Name: Ajay
Roll Number: 101
Total Marks: 240
Percentage: 80.0%
'''

class Student :



    def __init__(self,name,rollno,Emarks,Mmarks,Smarks):
        self.name = name 
        self.rollno = rollno
        self.Emarks = Emarks
        self.Mmarks = Mmarks
        self.Smarks = Smarks

    def calculate_total(self):

        total_marks = self.Emarks + self.Mmarks + self.Smarks 
        return total_marks

    def percentage(self):

        percent = (self.calculate_total()/300)*100

        return percent
    
    def display(self):

        print(f"student Name :{self.name}")
        print(f"Roll Number  :{self.rollno}")
        print(f"Total Marks  :{self.calculate_total()}")
        print(f"Percentage   :{self.percentage()}")

s1 = Student("Anshika",12,34,34,46)
s1.display()




    