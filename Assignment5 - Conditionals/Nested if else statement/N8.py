'''8. A warehouse management system needs to identify the highest stock level among six different storage units to prioritize dispatch.
 The system should take the quantity of items stored in six units as input. It should compare all six values using nested conditions
 and determine which unit has the maximum stock. Display the highest stock value among all six units.

Input:
Unit1 = 120
Unit2 = 450
Unit3 = 300
Unit4 = 275
Unit5 = 500
Unit6 = 390

Output:
Highest Stock = 500'''

#solution


Unit1 = int(input("Enter the unit1:"))
unit2 = int(input("unit2:"))
unit3 = int(input("unit3:"))
unit4 = int(input("unit4:"))
unit5 = int(input("unit5:"))
Unit6 = int(input("unit6:"))

if Unit1>unit2:
    if Unit1>Unit3:
        if Unit1>unit4:
            if Unit1>unit5:
                if Unit1>Unit6:
                    print("Unit1 is greater")
                else:
                    print("Unit6 is greater")
            else:
                if unit5>Unit6:
                    print("unit5 is greater")
                else:
                    print("Unit6 is greater")
        else:
            if unit4>unit5:
                if unit4>Unit6:
                    print("unit4 is greater")    
                else:
                    print("Unit6 is greater")

            else:
                if unit5>Unit6:
                    print("unit5 is greater")
                else:
                    print("Unit6 is greater")
              
    else:
        if Unit3>unit4:
            if Unit3>unit5:
                if Unit3>Unit6:
                    print("Unit3 is greater")
                else:
                    print("Unit6 is greater")
            else:
                if unit5>Unit6:
                    print("unit5 is greater")
                else:
                    print("Unit6 is greater")
        else:
            if unit4>unit5:
                if unit4>Unit6:
                    print("unit4 is greater")    
                else:
                    print("Unit6 is greater")

            else:
                if unit5>Unit6:
                    print("unit5  is greater")
                else:
                    print("Unit6 is greater")
else:
    if unit2>unit3:
        if unit2>unit4:
            if unit2>unit5:
                if unit2>Unit6:
                    print("unit2 is greater")
                else:
                    print("Unit6 is greater")           
           
            else:
                if unit5>Unit6:
                    print("unit5 is greater")
                else:
                    print("Unit6 is greater")
        else:
            if unit4>unit5:
                if unit4>Unit6:
                    print("unit4 is greater")    
                else:
                    print("Unit6 is greater")

            else:
                if unit5>Unit6:
                    print("unit5 is greater")
                else:
                    print("Unit6 is greater")
    else:
        if unit3>unit4:
            if unit3>unit5:
                if unit3>Unit6:
                    print("unit3 is greater")
                else:
                    print("Unit6 is greater")
            else:
                if unit5>Unit6:
                    print("unit5 is greater")
                else:
                    print("Unit6 is greater")
        else:
            if unit4>unit5:
                if unit4>Unit6:
                    print("unit4 is greater")    
                else:
                    print("Unit6 is greater")

            else:
                if unit5>Unit6:
                    print("unit5 is greater")
                else:
                    print("Unit6 is greater")
                

