'''=====================================================================
QUESTION 1: EMPLOYEE SALARY ANALYSIS
====================================

A company wants to store employee details and generate salary reports using NamedTuple.

Fields:
emp_id, emp_name, department, salary

Requirements:

1. Read N employee details from the user and store them in a list of NamedTuples.

---

2. Display all employee details.

---

3. Find and display the employee with the highest salary.

---

4. Find and display the employee with the lowest salary.

---

5. Calculate and display the average salary of all employees.

---

6. Accept a department name from the user and display all employees belonging to that department.

---

Test Case:

Input:
Enter number of employees: 4

101 Rahul IT 50000
102 Priya HR 45000
103 Amit IT 70000
104 Neha Finance 60000

Enter department: IT

Expected Output:
Highest Salary Employee:
103 Amit IT 70000

Lowest Salary Employee:
102 Priya HR 45000

Average Salary:
56250.0

Employees in IT Department:
101 Rahul IT 50000
103 Amit IT 70000'''


from collections import namedtuple

Employee = namedtuple("Employee",["emp_id","emp_name","department","salary"])

n = int(input("Enter number of Employees : "))
employeelist = []

for i in range(n):

    print(f"Enter Employee {i+1} Details ")
    id = int(input("Enter Id      :"))
    name = input("Enter Name     :")
    dept = input("Enter Department      : ")
    salary = int(input("Enter Salary      :"))
    print()
    emp = Employee(id , name, dept , salary)
    employeelist.append(emp)

print(employeelist)

for i in employeelist:

    #print(i.emp_id,i.emp_name,i.department,i.salary)

    print(f"    Employee Details     ")
    print(f"ID           :{i.emp_id}")
    print(f"Name         :{i.emp_id}")
    print(f"Department   :{i.department}")
    print(f"Salary       :{i.salary}")



max = 0
min = employeelist[0]
sum = 0

for i in employeelist:
    sum+=i.salary

    if i.salary>max:
        max = i.salary

    if i.salary<min:
        min = i.salary

avg = sum//n

# For printing maximum salary

print("Highest Salary Employee : ")
print(f"ID           :{max.emp_id}")
print(f"Name         :{max.emp_id}")
print(f"Department   :{max.department}")
print(f"Salary       :{max.salary}")

# For printing minimum salary

print("Highest Salary Employee : ")
print(f"ID           :{min.emp_id}")
print(f"Name         :{min.emp_id}")
print(f"Department   :{min.department}")
print(f"Salary       :{min.salary}")


print(f"Average Salary     :{avg}")


avg = sum//n

# department check

dept = input("Enter Department : ")
print(f"Employees in {dept} Department : ")

for i in employeelist:
    if i.dept == dept:
       print(i)

    

    