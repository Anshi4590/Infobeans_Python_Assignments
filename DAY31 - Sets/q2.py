'''2.
=========================================
ONLINE COURSE ENROLLMENT SYSTEM
=========================================

An institute offers:
1. Python Course
2. Java Course

Store enrolled student email IDs using sets.

Menu:
1. Enroll Student in Python
2. Enroll Student in Java
3. Display Python Students
4. Display Java Students
5. Find Students Enrolled in Both Courses
6. Find Students Enrolled in Both pyhton
7. Find Students Enrolled Only in Java
8. Check Enrollment in Python Course
9. Display Total Unique Students
10. Exit

Requirements:
- Use two sets.
- Use membership operator (in).
- Use union, intersection and difference operations.'''


python = set()  
java = set()

while True:
    print("======== ONLINE COURSE ENROLLMENT SYSTEM ========")
    print()
    print("---------- Menu ----------")
    print()
    print("1. Enroll Student in Python")
    print("2. Enroll Student in Java")
    print("3. Display Python Students")
    print("4. Display Java Students")
    print("5. Find Students Enrolled in Both Courses")
    print("6. Find Students Enrolled in Both Courses")
    print("7. Find Students Enrolled Only in Java") 
    print("8. Check Enrollment in Python Course") 
    print("9. Display Total Unique Students") 
    print("10. Exit")

    choice = int(input("Enter choice:"))
    
    match choice :

        case 1:

            num = int(input("Enter no. of student want to Enroll in Python "))
            for i in range(num):
                m = input("Enter Name :")
                python .add(m)
            

        case 2:

            num = int(input("Enter no. of student want to Enroll in Java"))
            for i in range(num):
                n = input("Enter Name : ")
                java.add(n)
            

        case 3:
            if python  == set() and java ==set():
                print("Operations can't be performed on empty set")
                print("Add element in the set first")

            else:

                print(f"Python Students:{python}")

        case 4:
            if python  == set() and  java ==set():
                print("Operations can't be performed on empty set")
                print("Add element in the set first")

            else:
            
                print(f"Java Students:{java}")

        case 5:

            if python == set() and java ==set():
                print("Operations can't be performed on empty set")
                print("Add element in the set first")

            elif python.intersection(java) == set():
                print("No Common Student")

            else:
                common = python& java
                print(f"Students Enrolled in Both Courses : {common}")

        case 6:
            
            if python  == set() and  java ==set():
                print("Operations can't be performed on empty set")
                print("Add element in the set first")

            else:
                
                print("Students Enrolled only in pyhton : ")
                diff = python - java
                print(diff)

        case 7:

            print("Students Enrolled only in Java: ")
            diff = java-python 
            print(diff)

        case 8:
            name = input("Enter Name :")

            if name in python:
               print(f"Student{name}is Enrolled in python")

            else:
               print(f"Student{name}is not Enrolled in python")
            

        case 9:

            print("Total All Unique Club Members :") 
            print(len(python|java))

        case 10:
            print("Exit")
            break

        case __:
            print("Invalid choice")
            print("Choose Again")


