'''.

ASSIGNMENT: ONLINE COURSE ENROLLMENT & STUDENT MANAGEMENT SYSTEM

A training institute offers multiple courses such as Python, Java, Full Stack Development, Data Science, and React.

Currently, student enrollment details are maintained manually in Excel sheets. As the number of students is increasing, the institute wants to develop a Student Management System using Python.

The system should store student records in a nested dictionary where:

Key → Student ID
Value → Dictionary containing student information

Each student record should contain:

Student Name
Course Name
Mobile Number
Fees
City
Sample Data Structure
{
101:{
    "name":"Ajay",
    "course":"Python",
    "mobile":"9876543210",
    "fees":25000,
    "city":"Indore"
},
102:{
    "name":"Ravi",
    "course":"Java",
    "mobile":"9876500000",
    "fees":22000,
    "city":"Bhopal"
}
}
Menu Driven Program

Display the following menu repeatedly until the user chooses Exit.

=========================================
 STUDENT MANAGEMENT SYSTEM
=========================================

1. Add New Student
2. Search Student
3. Update Course
4. Delete Student
5. Display All Students
6. Count Total Students
7. Display Students By Course
8. Display Students By City
9. Find Student Paying Highest Fees
10. Find Student Paying Lowest Fees
11. Exit
Functional Requirements
1. Add New Student

Accept the following details:

Student ID
Student Name
Course Name
Mobile Number
Fees
City

Store the information in the nested dictionary.

Validation

If Student ID already exists:

Student ID Already Exists
2. Search Student

Accept Student ID from the user.

If found, display complete student information.

Sample Output
Student ID : 101
Name       : Ajay
Course     : Python
Mobile     : 9876543210
Fees       : 25000
City       : Indore

If not found:

Student Not Found
3. Update Course

Accept Student ID.

If found:

Ask for new course name.
Update the course.
Sample Output
Course Updated Successfully
4. Delete Student

Accept Student ID.

If found:

Delete the record.
Sample Output
Student Deleted Successfully

Otherwise:

Student Not Found
5. Display All Students

Display all student records in a proper format.

Sample Output
-----------------------------------
Student ID : 101
Name       : Ajay
Course     : Python
Fees       : 25000
-----------------------------------

Student ID : 102
Name       : Ravi
Course     : Java
Fees       : 22000
-----------------------------------
6. Count Total Students

Display total number of students enrolled.

Sample Output
Total Students : 45
7. Display Students By Course

Accept a course name from the user.

Display all students enrolled in that course.

Sample Output
Enter Course : Python

101  Ajay
105  Neha
112  Aman

If no students are found:

No Students Found
8. Display Students By City

Accept city name from the user.

Display all students belonging to that city.

Sample Output
Enter City : Indore

101  Ajay
108  Ravi
115  Pooja
9. Find Student Paying Highest Fees

Display complete details of the student who has paid the highest fees.

Sample Output
Highest Fee Paying Student

Student ID : 121
Name       : Neha
Course     : Data Science
Fees       : 50000
10. Find Student Paying Lowest Fees

Display complete details of the student who has paid the lowest fees.

Sample Output
Lowest Fee Paying Student

Student ID : 131
Name       : Aman
Course     : React
Fees       : 15000
11. Exit

Terminate the application.

Sample Output
Thank You For Using Student Management System'''



def display():

    print("""
=========================================
       STUDENT MANAGEMENT SYSTEM
=========================================

1. Add New Student
2. Search Student
3. Update Course
4. Delete Student
5. Display All Students
6. Count Total Students
7. Display Students By Course
8. Display Students By City
9. Find Student Paying Highest Fees
10. Find Student Paying Lowest Fees
11. Exit

""")


def add(id):

    if id not in d:
        name = input("Enter The Student Name : ")
        mobile = int(input("Enter The Student Mobile : "))
        fees = int(input("Enter The Student Fees : "))
        course = input("Enter The Course : ")
        city = input("Enter The City : ")

        d[id] = {
            "name": name,
            "mobile": mobile,
            "fees": fees,
            "course": course,
            "city": city
        }

        print(f"Student Added Successfully At ID : {id}")

    else:
        print("Student ID Already Exists")
        print(d[id])


def search(id):

    if id in d:
        print()
        print("Student ID :", id)
        print("Name       :", d[id]["name"])
        print("Mobile     :", d[id]["mobile"])
        print("Fees       :", d[id]["fees"])
        print("Course     :", d[id]["course"])
        print("City       :", d[id]["city"])

    else:
        print("Student Not Found")


def update(id):

    if id in d:
        newCourse = input("Enter The New Course : ")

        d[id]["course"] = newCourse

        print("Course Updated Successfully")

    else:
        print("Student Not Found")


def delete(id):

    if id in d:
        d.pop(id)

        print("Student Deleted Successfully")

    else:
        print("Student Not Found")


def displaystudent():

    for i in d:
        print()
        print("-" * 30)
        print("Student ID :", i)
        print("Name       :", d[i]["name"])
        print("Course     :", d[i]["course"])
        print("Mobile     :", d[i]["mobile"])
        print("Fees       :", d[i]["fees"])
        print("City       :", d[i]["city"])
        print("-" * 30)


def findCourseInStudent(course):

    found = False

    for i in d:
        if d[i]["course"] == course:
            print(f"{i}  {d[i]['name']}")
            found = True

    if not found:
        print(f"No Student Is Found With {course}")


def findCityInStudent(city):

    found = False

    for i in d:
        if d[i]["city"] == city:
            print(f"{i}  {d[i]['name']}")
            found = True

    if not found:
        print(f"No Student Is Found From {city}")


def highestFees():

    high = 0
    id = 0

    for i in d:
        fees = d[i]["fees"]

        if fees > high:
            high = fees
            id = i

    print("Highest Fee Paying Student")
    print(f"Student ID : {id}")
    print(f"Student Name : {d[id]['name']}")
    print(f"Course : {d[id]['course']}")
    print(f"Fees : {d[id]['fees']}")


def lowestFees():

    low = d[0]["fees"]
    id = 0

    for i in d:
        fees = d[i]["fees"]

        if fees < low:
            low = fees
            id = i

    print("Lowest Fee Paying Student")
    print(f"Student ID : {id}")
    print(f"Student Name : {d[id]['name']}")
    print(f"Course : {d[id]['course']}")
    print(f"Fees : {d[id]['fees']}")


d = {}
id = 100


while True:

    display()

    choice = int(input("Enter The Option : "))

    match choice:

        case 1:
            print("ADD NEW STUDENT")

            id += 1
            add(id)

        case 2:
            print("Search Student")

            userId = int(input("Enter The ID : "))
            search(userId)

        case 3:
            print("Update Student Course")

            userId = int(input("Enter The ID : "))
            update(userId)

        case 4:
            print("Delete Student Record")

            userId = int(input("Enter The ID : "))
            delete(userId)

        case 5:
            print("Display All Students")

            displaystudent()

        case 6:
            print("Count Total Students")

            print(f"Total Students : {len(d)}")

        case 7:
            print("Display Students By Course")

            userCourse = input("Enter The Course : ")
            findCourseInStudent(userCourse)

        case 8:
            print("Display Students By City")

            userCity = input("Enter The City : ")
            findCityInStudent(userCity)

        case 9:
            print("Find Student Paying Highest Fees")

            highestFees()

        case 10:
            print("Find Student Paying Lowest Fees")

            lowestFees()

        case 11:
            print("Thank You For Using Student Management System")
            break

        case _:
            print("Invalid Choice")