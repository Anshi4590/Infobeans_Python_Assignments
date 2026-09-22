'''
============================================================
ASSIGNMENT 1 � EMPLOYEE MANAGEMENT SYSTEM
=========================================

SCENARIO:

A company wants to maintain information about different types of employees.

Create the following class hierarchy:

Employee
|
+-------- Developer
|
+-------- Manager

REQUIREMENTS:

1. Create a parent class Employee.

Employee should contain:

* employee_id
* employee_name
* salary

2. Create Developer and Manager classes that inherit from Employee.

3. Employee should have a method:

display_details()

4. Developer should have:

programming_language

and a method:

write_code()

5. Manager should have:

team_size

and a method:

manage_team()

6. The child-class constructors must initialize parent-class data using super().

7. Override display_details() in both child classes.

8. From the overridden method, call the parent display_details() using super().

9. salary must be encapsulated.

Implement:

@property
@salary.setter
@salary.deleter

10. Salary setter must reject salary <= 0.

11. Read ALL employee information from the user.

INPUT REQUIREMENT:

Ask the user:

Enter Employee ID:
Enter Employee Name:
Enter Salary:
Enter Employee Type:

1. Developer
2. Manager

If Developer:

Enter Programming Language:

If Manager:

Enter Team Size:

SAMPLE INPUT:

Enter Employee ID: 101
Enter Employee Name: Rahul
Enter Salary: 45000
Enter Employee Type: 1
Enter Programming Language: Python

EXPECTED OUTPUT:

## Employee Details

Employee ID: 101
Employee Name: Rahul
Salary: 45000
Role: Developer
Programming Language: Python

Rahul is developing applications using Python.

============================================================

'''

class Employee:

    def __init__(self,employee_id,employee_name,salary):

        self.employee_id = employee_id
        self.employee_name = employee_name
        self.salary = salary

    @property
    def salary(self):
        return self.__salary 


    @salary.setter
    def salary(self,value):

        if value>0:
            self.__salary = value
            

        else:
            print("Reject")

    @salary.deleter
    def salary (self):
        print("Deleting the salary")
        del self.__salary

    def display_details(self): 
        print(f"Employee Id   : {self.employee_id}") 
        print(f"Employee Name : {self.employee_name}") 
        print(f"Salary        : {self.__salary} ")



        
class Developer(Employee):

    def __init__(self,employee_id,employee_name ,salary ,programming_language):

        super().__init__(employee_id,employee_name,salary)
        self.programming_language = programming_language

    def write_code(self):
        
        print(f"{self.employee_name} is developing applications using {self.programming_language}.")

    def display_details(self):

        super().display_details()
        print(f"Role     : Developer")
        print(f"Programmming Langauge   : {self.programming_language}")

class Manager(Employee):

    def __init__(self,employee_id,employee_name ,salary,team_size):

        super().__init__(employee_id,employee_name,salary)
        self.team_size = team_size

    def manage_team(self):

        print(f"{self.employee_name} is managing a team of {self.team_size} members.")

    def display_details(self):
    
        super().display_details()
        print(f"Role     : Manager")
        print(f"Team size  : {self.team_size}")