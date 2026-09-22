'''
Question 1: Employee Salary Management System
Scenario

A company wants to automate employee salary calculations. The HR department needs a system that calculates the gross salary of an employee by including allowances.

Requirements

Create a class named Employee with the following attributes:

employee_id
employee_name
basic_salary

Initialize the values using a constructor.

Calculations
HRA = 20% of Basic Salary
DA = 15% of Basic Salary
Gross Salary = Basic Salary + HRA + DA

Sample Input

Enter Employee ID : E101
Enter Employee Name : Rahul Sharma
Enter Basic Salary : 50000

Sample Output

------ Employee Salary Details ------
Employee ID      : E101
Employee Name    : Rahul Sharma
Basic Salary     : 50000.0
HRA              : 10000.0
DA               : 7500.0
Gross Salary     : 67500.0

'''
class Employee:

    def __init__(self,employee_id ,employee_name,basic_salary):

        self.employee_id = employee_id
        self.employee_name = employee_name
        self.basic_salary = basic_salary

    def calculate_hra(self):

        hra  = self.basic_salary*20/100
        return hra
    
    def calculate_da(self):

        da =  self.basic_salary*15/100
        return da
    
    def calculate_gross_salary(self):

        Gross_Salary = self.basic_salary + self.calculate_hra() + self.calculate_da()
        return Gross_Salary

    def display(self):


        print("\n------ Employee Salary Details ------")
        print(f"Employee ID      : {self.employee_id}")
        print(f"Employee Name    : {self.employee_name}")
        print(f"Basic Salary     : {self.basic_salary}")
        print(f"HRA              : {self.calculate_hra()}")
        print(f"DA               : {self.calculate_da()}")
        print(f"Gross Salary     : {self.calculate_gross_salary()}")

        
employee_id   = input("Enter Employee Id : ")
employee_name = input("Enter Employee Name : ")
basic_salary  = int(input("Enter Employee Salary : "))


emp1 = Employee(employee_id ,employee_name,basic_salary)

emp1.display()