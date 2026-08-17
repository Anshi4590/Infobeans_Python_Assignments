'''=====================================================================
QUESTION 2: STUDENT RESULT PROCESSING
=====================================

A training institute wants to manage student records using NamedTuple.

Fields:
roll_no, name, course, marks

Requirements:

1. Read N student records from the user and store them in a list of NamedTuples.

---

2. Display all student details.

---

3. Find and display the topper of the class.

---

4. Count and display the number of students scoring above 80 marks.

---

5. Calculate and display the average marks.

---

6. Accept a course name from the user and display all students enrolled in that course.

---

Test Case:

Input:
Enter number of students: 4

1 Ravi Python 85
2 Anjali Java 78
3 Karan Python 92
4 Pooja Testing 88

Enter course: Python

Expected Output:
Topper:
3 Karan Python 92

Students Above 80:
3

Average Marks:
85.75

Students in Python Course:
1 Ravi Python 85
3 Karan Python 92'''

from collections import namedtuple

student = namedtuple("student",["rollno", "name", "course", "marks"])

n = int(input("Enter Total number of Students : "))

list =[]

for i in range(n):
    print(f"Enter Student {i+1} Details : ")
    rollno = int(input("Enter  Rollno         : "))
    name = input("Enter  Name           : ")
    course = input("Enter  Course         : ")
    marks = int(input("Enter  Marks          : "))
    print()

    list.append(student(rollno,name,course,marks))

print(list)
count = 1
 
for i in list:
  
    print(f"Student {count} Details : ")
    print(f"Rollno         : {rollno}")
    print(f"Name           : {name}")
    print(f"Course         : {course}")
    print(f"Marks          : {marks}")
    count+=1

max = list[0]
sum = 0

for i in list:
    sum+=i.marks
    if i.marks>max.marks:
        max = i

avg = sum//n

print(" ----- Topper Student -----")
print(f"Rollno          :{max.rollno}")
print(f"Name            :{max.name}")
print(f"Course          :{max.course}")
print(f"Marks           :{max.marks}")

scount = 0 # student count

for i in list :
    if i.marks>80:
       scount+=1

print(f"The  Total number of students scoring above 80 marks : {scount}")

print(f"The Average Marks   : {avg}")

course = input("Enter Course : ")

for i in list:
    if i.course == course:
       print(i)
