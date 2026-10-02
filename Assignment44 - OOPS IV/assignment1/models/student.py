'''
==========================================
ASSIGNMENT 1 : STUDENT MANAGEMENT SYSTEM
==========================================

Create a `Student` class inside:

models/student.py

ATTRIBUTES:

* roll_no
* name
* marks

TASKS:

1. Take details of 5 students from the user.
2. Create a Student object for each student.
3. Store all Student objects inside a list.
4. Display all students.
5. Display students whose marks are greater than 60. 
6. Find the student having the highest marks.
7. Calculate the average marks of all students.

SAMPLE INPUT:

Enter Roll No: 101
Enter Name: Amit
Enter Marks: 78

Enter Roll No: 102
Enter Name: Rahul
Enter Marks: 55

Enter Roll No: 103
Enter Name: Priya
Enter Marks: 91

Enter Roll No: 104
Enter Name: Neha
Enter Marks: 67

Enter Roll No: 105
Enter Name: Rohit
Enter Marks: 45

EXPECTED OUTPUT:

All Students:
101 Amit 78
102 Rahul 55
103 Priya 91
104 Neha 67
105 Rohit 45

Students having marks greater than 60:
101 Amit 78
103 Priya 91
104 Neha 67

Highest Marks:
103 Priya 91

Average Marks:
67.2

'''

class Student :

    def __init__(self,rollno,name,marks):
        self.rollno = rollno
        self.name = name 
        self.marks = marks

    # def display_details(self,studentlist):

    #     print("All Student")
    #     for s in studentlist:
    #         print(s.rollno, s.name, s.marks)

    def display_details(self):
        print(f"{self.rollno} {self.name} {self.marks}")



    def search_marks(self):
        return self.marks>=60

    def  highest_marks(self,other):
        return self.marks>other.marks

    @staticmethod
    def average(student):

        total =0
        for i in student:
            total+=i.marks

        average = total/len(student)
        return average