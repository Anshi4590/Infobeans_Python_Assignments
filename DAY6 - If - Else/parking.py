'''15. Smart Parking System

A smart parking system charges based on vehicle type and parking duration:

* Bike → ₹10/hour
* Car → ₹20/hour
* Bus → ₹50/hour
  If parking duration exceeds 5 hours, an additional ₹100 penalty is applied.

Write a Python program to calculate total parking fee.

Input:
Enter vehicle type: Car
Enter hours parked: 6

Output:
Total Parking Fee: ₹220'''


#solution



type = input("Enter vehicle type:")
hours = int(input("Enter hours parked:"))

if type.lower() == "car" and hours<=5:
   fee = 20*hours
   print("Total Parking fee",fee)

elif type.lower() == "car" and hours>5:
   fee = (20*hours) + 100
   print("Total Parking fee",fee)

elif type.lower() == "bike" and hours<=5:
   fee = (10*hours) 
   print("Total Parkingfee",fee)

elif type.lower() == "bike" and hours>5:
   fee = (10*hours) + 100
   print("Total Parking fee",fee)

elif type.lower() == "bus" and hours<=5:
   fee = (50*hours) 
   print("Total Parking fee",fee)

elif type.lower() == "bus" and hours>5:
   fee = (50*hours) + 100
   print("Total Parkingfee",fee)

else :
   print("Invalid choice")


























