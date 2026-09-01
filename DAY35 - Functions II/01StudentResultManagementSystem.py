'''

1. STUDENT RESULT MANAGEMENT SYSTEM

Scenario:

A college examination department wants to automate the process of generating student results. The staff should be able to
enter student details, calculate marks, determine grades, and display a complete report card using a menu-driven application.

Develop a Python program using multiple user-defined functions and a menu-driven approach to perform the following operations.

MENU

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Complete Result
6. Find Highest Subject Mark
7. Find Lowest Subject Mark
8. Exit

Functional Requirements

1. Add Student Details

   * Student Name
   * Roll Number
   * Marks of 5 Subjects

2. Calculate Total Marks

3. Calculate Percentage

4. Find Grade

5. Display Complete Result

6. Find Highest Subject Mark

7. Find Lowest Subject Mark

8. Exit

Grade Criteria

Percentage        Grade

90 - 100          A+
80 - 89           A
70 - 79           B
60 - 69           C
50 - 59           D
Below 50          Fail

Constraints

* Marks should be between 0 and 100.
* Display an appropriate message for invalid marks.
* The program should continue until the user chooses Exit.

Sample Input / Output

******** STUDENT RESULT MANAGEMENT ********

1. Add Student Details
2. Calculate Total Marks
3. Calculate Percentage
4. Find Grade
5. Display Result
6. Find Highest Mark
7. Find Lowest Mark
8. Exit

Enter Choice : 1

Enter Student Name : Ajay
Enter Roll Number : 101

Enter Mark 1 : 78
Enter Mark 2 : 85
Enter Mark 3 : 92
Enter Mark 4 : 88
Enter Mark 5 : 77

Student details added successfully.

Enter Choice : 2

Total Marks = 420

Enter Choice : 3

Percentage = 84.0

Enter Choice : 4

Grade = A

Enter Choice : 6

Highest Mark = 92

Enter Choice : 7

Lowest Mark = 77

Enter Choice : 5

----------- RESULT CARD -----------

Name        : Ajay
Roll Number : 101

Marks
Subject 1 : 78
Subject 2 : 85
Subject 3 : 92
Subject 4 : 88
Subject 5 : 77

Total Marks : 420
Percentage  : 84.0
Grade       : A
Highest Mark: 92
Lowest Mark : 77

Enter Choice : 8

Thank You. Program Terminated.

Important Instructions

1. The solution must be developed using multiple user-defined functions.
2. Use appropriate parameters wherever data needs to be passed between functions.
3. Use return statements wherever a function needs to send a result back to the caller.
4. Avoid using unnecessary global variables.
5. Implement the application using a menu-driven approach.
6. Perform proper input validation.
7. Write meaningful function names and maintain proper code readability.
'''

l = []

def add():

    print("Add Student Details :")

    name = input("Enter student Name : ")
    rollno = int(input("Enter Rollnumber : "))
    marks = []
    
    for i in range(5):
        marks.append(int(input("Enter number : ")))
   
    l.append(name)
    l.append(rollno)
    l.append(marks)

    print("Added Student Data Successfully")


def total(l):

    sum = 0
    for i in l[2]:
        sum+=i
    return sum

def percent():

    p = total(l)/500*100

    return p 

def grade():

    ans = percent()

    if 90<=ans<=100:
        return "A+"
    elif 80<=ans<90:
        return "A"
    elif 70<=ans<80:
        return "B"
    elif 60<=ans<70:
        return "C"
    elif 50<=ans<60:
        return "D"
    else:
        return"Fail"

def result():

    print("----------- RESULT CARD -----------")  
    print()
    print(f"Name   : {l[0]}")
    print(f"Rollno : {l[1]}")
    print()
    print("Marks")

    for i in range(len(l[2])):
        print(f"Subject {i+1} : {l[2][i]}")
    print()
    print(f"Total Marks : {total(l)}")
    print(f"Percentage  : {percent()}")
    print(f"Grade  : {grade()}")
    print(f"Highest Marks : {high(l)}")
    print(f"Lowest Marks  : {low(l)}")
    print() 

def high(l):

    max = 0

    for i in l[2]:

        if max<i:
            max = i

    return max

def low(l):

    min = float("inf")

    for i in l[2]:

        if min>i:
            min = i

    return min

while True:

    print("1. Add Student Details")
    print("2. Calculate Total Marks")
    print("3. Calculate Percentage")
    print("4. Find Grade")
    print("5. Display Complete Result")
    print("6. Find Highest Subject Mark")
    print("7. Find Lowest Subject Mark")
    print("8. Exit")

    choice = int(input("Enter Choice : "))
    match choice:

        case 1:
            add()

        case 2:
            print(f"Total Marks : {total(l)}")

        case 3:
          
            print(f"Percentage : {percent()}")

        case 4:
            print(f"Grade : {grade()}")

        case 5:
            result()

        case 6:
            print(f"Highest Subject Mark : {high(l)}")

        case 7:
            print(f"Lowest Subject Mark  : {low(l)}")

        case 8:
            print("Exiting....")
            break

        case _:
            print("Invalid Choice..")
