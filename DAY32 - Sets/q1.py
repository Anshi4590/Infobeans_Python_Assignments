'''1.
=========================================
STUDENT CLUB MEMBERSHIP SYSTEM
=========================================

A college has two clubs:
1. Coding Club
2. Robotics Club

Store student IDs of both clubs using sets.

Menu:
1. Add Student to Coding Club
2. Add Student to Robotics Club
3. Display Students in Coding Club
4. Display Students in Robotics Club
5. Find Students in Both Clubs
6. Find Students Only in Coding Club
7. Find Students Only in Robotics Club
8. Display All Unique Club Members
9. Display Total Unique Club Members
10. Exit

Requirements:
- Use two sets.
- Apply intersection, difference, and union operations.'''


set1 = set()  
set2 = set()

while True:

    print("---------- Menu ----------")
    print("1. Add Student to Coding Club")
    print("2. Add Student to Robotics Club")
    print("3. Display Students in Coding Club")
    print("4. Display Students in Robotics Club")
    print("5. Find Students in Both Clubs")
    print("6. Find Students Only in Coding Club")
    print("7. Find Students Only in Robotics Club") 
    print("8. Display All Unique Club Members") 
    print("9. Display Total Unique Club Members") 
    print("10. Exit")

    choice = int(input("Enter choice:"))
    
    match choice :

        case 1:

            num = int(input("Enter no. of student you want to add in Coding Club"))
            for i in range(num):
                m = input("Enter Name :")
                set1.add(m)
            

        case 2:

            num = int(input("Enter no. of student you want to add in Robotics Club"))
            for i in range(num):
                n = input("Enter Name : ")
                set2.add(m)
            

        case 3:
            if set1 == set() and set2 ==set():
                print("Operations can't be performed on empty set")
                print("Add element in the set first")

            else:

                print(f"coding Club members:{set1}")

        case 4:
            if set1 == set() and set2 ==set():
                print("Operations can't be performed on empty set")
                print("Add element in the set first")

            else:
            
                print(f"Robotics Club members:{set2}")

        case 5:

            if set1 == set() and set2 ==set():
                print("Operations can't be performed on empty set")
                print("Add element in the set first")

            elif set1.intersection(set2) == set():
                print("No Common Student")

            else:
                common = set1&set2
                print(f"Students in Both Clubs : {common}")

        case 6:

            if set1 == set() and set2 ==set():
                print("Operations can't be performed on empty set")
                print("Add element in the set first")

            else:
                
                print("Students Only in Coding Club : ")
                diff = set1-set2
                print(diff)

        case 7:

            print("Students Only in Robotics Club : ")
            diff = set2-set1
            print(diff)

        case 8:

            print(" All Unique Club Members :") 
            print(set1|set2)

        case 9:

            print("Total All Unique Club Members :") 
            print(len(set1|set2))

        case 10:
            print("Exit")
            break

        case __:
            print("Invalid choice")
            print("Choose Again")
        

            


