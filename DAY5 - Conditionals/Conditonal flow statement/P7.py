'''7. Salary Benefits System
   A company provides benefits:

* If salary ≥ 30000 → Eligible for PF
* If salary ≥ 50000 → Eligible for bonus

Input:
Enter salary: 55000

Output:
PF applicable
Bonus applicable'''

#solution


salary = int(input("enter the salary"))
if salary>=30000:
     print("Eligible for pf")
    
     if salary>=50000:
          print("Eligible for bonus")
else:
      print("nothing")


