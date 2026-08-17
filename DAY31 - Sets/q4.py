'''4.
=========================================
FROZEN SET SUBJECT MANAGEMENT
=========================================

An institute offers fixed subjects:

Python
Java
MySQL
React
Spring Boot

These subjects cannot be modified after creation.

Menu:
1. Display Subjects
2. Search Subject
3. Count Subjects
4. Attempt to Add Subject
5. Exit

Requirements:
- Use Frozen Set.
- Show that modification is not allowed.'''

visitors = set()

while True:

    print("===== WEBSITE VISITOR TRACKING SYSTEM =====")
    print()
    print("1. Add Visitor")
    print("2. Remove Visitor")
    print("3. Check Visitor")
    print("4. Display All Visitors")
    print("5. Count Unique Visitors")
    print("6. Clear Visitor Data")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            m = input("Enter Name of Visitor :")
            visitors.add(m)

        case 2:
            m = input("Enter Name of Visitor :")
            visitors.remove(m)

        case 3:

            name = input("Enter Name:")
            if name in visitors:
               print("Visitor is Present")
            else:
               print("Visitor is not Present")
               
        case 4:

            print("ALL the Visitors are : ")
            print(visitors)

        case 5:
            print(f"Total no. of visitors are : {len(visitors)} ")

        case 6:
            visitors.clear()
            print(f"visitors data cleared{visitors}")


        case 7:
            print("Exiting...")
            break

        case _:
            print("Invalid choice!")
