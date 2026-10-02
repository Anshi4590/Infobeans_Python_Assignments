'''4. Electricity Bill Management System

You are developing an Electricity Bill Management System for a power distribution company. The system helps calculate electricity bills for customers based on their unit consumption.

Sometimes, the operator may try to calculate the bill or apply surcharge before entering the number of units consumed. Your system must handle such situations properly.

👉 Important Condition:
If units are not entered, the system should display:
"Please enter units consumed first"
and should not perform further calculations.

The system should be menu-driven and must continue running until the user selects Exit. All operations should be handled using match-case.

Menu Options:
1 → Enter Units Consumed
2 → Calculate Bill Amount

* First 100 units → ₹5 per unit
* Next 100 units → ₹7 per unit
* Above 200 units → ₹10 * per unit
  3 → Apply Surcharge
* If bill > 2000 → 10% surcharge
* Otherwise → 5% surcharge
  4 → Display Final Bill
  5 → Exit
---

Sample Run 1:
Input:
Enter your choice: 2

Output:
Please enter units consumed first

---

Sample Run 2:
Input:
Enter your choice: 1
Enter units consumed: 250

Output:
Units recorded successfully

---

Sample Run 3:
Input:
Enter your choice: 2

Output:
Bill Amount: 1700

(Explanation: 100×5 = 500, 100×7 = 700, 50×10 = 500 → Total = 1700)

---

Sample Run 4:
Input:
Enter your choice: 3

Output:
Surcharge: 85

---

Sample Run 5:
Input:
Enter your choice: 4

Output:
----- Final Bill -----
Units: 250
Bill Amount: 1700
Surcharge: 85
Total Payable: 1785

---

Sample Run 6 (Invalid Choice):
Input:
Enter your choice: 9

Output:
Invalid choice. Please try again.

---

Sample Run 7 (Exit):
Input:
Enter your choice: 5

Output:
Exiting system... Thank you!'''

unit =0
while True:
   print("1 →Enter Units Consume ")
   print("2 → Calculate Bill Amount ")
   print("3 → Apply Surcharge ")
   print("4 → Display Final Bill ")
   print("5 → Exit ")

   choice = int(input("Enter the number : "))

   match choice:  
     
      case 1: 
         unit = int(input("Enter the units : "))
         print("units recorded successfully")
      
      case 2:
         if unit == 0:
            print("Please enter units consumed first")

         else:
            if unit<=100:

               bill = unit*5
               print("Bill Amount : ",bill)

            elif unit>100 and unit<=200:

               bill =(unit-100)*7+500
               print("Bill Amount : ",bill)

            elif unit>200:

               bill = (unit-200)*10+500+700
               print("Bill Amount :",bill)

            else:
               print("bill")
        

      case 3:
            if unit == 0:
               print("Please enter units consumed first")

            else:
              if bill>2000:
               charge = bill*10/100
               print("Surcharge : ",charge)
              else:
               charge = bill*5/100
               print("Surcharge : ",charge)
          
      case 4:
            if unit == 0:
                 print("Please enter units consumed first")
            else:
                final = bill + charge
                print("  ----- Final Bill -----")
                print("Units:",unit)
                print("Bill Amount:",bill)
                print("Surcharge:",charge)
                print("Total Payable:",final)
                print("------------------------")
      
      case 5:
           print("Exiting system... Thank you!")
           break
      case __:
           print("invalid choice")
print("Thank youuu")




              





