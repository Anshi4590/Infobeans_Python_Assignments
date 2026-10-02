'''12. Restaurant Bill with GST System

A restaurant applies GST based on the total bill amount:

* Up to ₹1000 → 5% GST
* ₹1001 to ₹5000 → 12% GST
* Above ₹5000 → 18% GST
  Additionally, if the bill exceeds ₹3000, a service charge of ₹200 is added.

Write a Python program to calculate the final bill.

Input:
Enter bill amount: 4000

Output:
Final Bill Amount: ₹4680'''

#solution

bill = int(input("enter the  total amount:"))

if bill<=1000:
   gst = bill + bill*5/100
   print("Final Bill Amount:",gst)

elif bill>=1001 and bill<=3000:
   gst = bill + bill*12/100
   print("Final Bill Amount:",gst)

elif bill>3000 and bill<=5000: 
   gst = bill + (bill*12/100)+200
   print("Final Bill Amount:",gst)

else:
   gst = bill + (bill*18/100)+200
   print("Final Bill Amount:",gst)