'''
Assignment 2: Employee Salary Calculator

A company wants to calculate an employee's gross salary.

Create a class Employee with the following attributes:

Employee ID

Employee name

Basic salary

HRA percentage

DA percentage

Create the following methods:

calculate_hra() – Calculate HRA.

calculate_da() – Calculate DA.

calculate_gross_salary() – Calculate gross salary.

display_salary() – Display employee salary details.

Formula:

HRA = Basic Salary × HRA Percentage / 100
DA = Basic Salary × DA Percentage / 100
Gross Salary = Basic Salary + HRA + DA

'''

class Employee:

    def __init__(self,eId,ename,salary,HRAp,DAp):
        self.eId = eId
        self.ename = ename
        self.salary = salary
        self.HRAp = HRAp
        self.DAp= DAp


    def calculate_hra(self):

        hra = (self.salary*self.HRAp)/100

        return hra

    def calculate_da(self):
    
        da = (self.salary*self.DAp)/100

        return da

    def calculate_gross_salary(self):

        gsalary = self.salary + self.calculate_da() + self.calculate_hra()

        return gsalary

    def display(self):
        
        print(f"Employee ID     :{self.eId}")
        print(f"Employee name   :{self.ename}")
        print(f"Basic salary    :{self.salary}")
        print(f"HRA percentage  :{self.HRAp}")
        print(f"DA percentage   :{self.DAp}") 
        print(f"HRA             :{self.calculate_hra()}")
        print(f"DA              :{self.calculate_da()}")
        print(f"Gross Salary    :{self.calculate_gross_salary()}")  


emp1 = Employee(101,"Anamika",40000,20,20) 
emp1.display()

