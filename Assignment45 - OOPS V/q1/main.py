from model.employee import Employee,Developer,Manager

employee_id = input("Enter Employee Id : ")
employee_name = input("Enter Employee Name : ")
salary = int(input("Enter Salary : "))
print()
while True:

    print("Employee Type")
    print("1.Developer")
    print("2.Manager")
    print()

    choice = int(input("Enter choice : "))
    print()
    match choice:

        case 1:

            employee_type = "Developer"
            programming_language = input("Enter Programming Language : ")
            emp1 = Developer(employee_id, employee_name, salary, programming_language)
            
            emp1.display_details()
            print()
            emp1.write_code()
            break

        case 2:

            employee_type = "Manager"
            team_size = int(input("Enter Team Size :"))
            emp1 = Manager(employee_id, employee_name, salary, team_size)
            emp1.display_details()
            print()
            emp1.manage_team()
            break

        case _:

            print("Invalid choice")

