'''Assignment 1 – Employee Bonus System

Create a parent class Employee with the following attributes:

employee_id
employee_name
salary

Create two child classes:

Developer
Manager


Requirements

Take employee details from the user.
Use super() to initialize the common attributes.
Create a method calculate_bonus() in the parent class.
Override calculate_bonus() in both child classes.
Developer gets 10% of salary as bonus.
Manager gets 20% of salary as bonus.
Display employee details, bonus and total salary.
Sample Input
Enter Employee ID: 101
Enter Employee Name: Rahul
Enter Salary: 50000
Enter Employee Type: Developer

Expected Output
----- Employee Details -----
Employee ID   : 101
Employee Name : Rahul
Salary        : 50000
Employee Type : Developer
Bonus         : 5000
Total Amount  : 55000

'''

class Employee:
    
    def __init__(self,employee_id,employee_name,salary):

        self.salary = salary
        self.employee_id =employee_id
        self.employee_name = employee_name
        
    def calculate_bonus(self):
        self.salary = self.salary +1000
        return 0
        
    def display(self):
        
        print("====== Employee Details =======")
        print(f"Employee Name :{self.employee_name}")
        print(f"Employee Id   :{self.employee_id}")
        print(f"salary        :{self.salary}")

        
class Developer(Employee):
    
    def __init__(self,employee_id,employee_name,salary):
        
        super().__init__(employee_id,employee_name,salary,bonus)
        
        self.bonus = bonus
        
    def calculate_bonus(self):
        
       return self.salary*0.10
       
    def display(self):
        
        super().display()
        print("Employee Type : Developer ")
        print(f"Bonus        : {self.bonus}")
        print(f"Total Amount : {self.calculate_bonus()}")
       
class Manager(Employee):

    def __init__(self,employee_id,employee_name,salary):
    
    super().__init__(employee_id,employee_name,salary,bonus)
    
    self.bonus = bonus
        
    def calculate_bonus(self):
        
       return self.salary*20
   
    def display(self):
    
    super().display()
    print("Employee Type : Developer ")
    print(f"Bonus        : {self.bonus}")
   





     