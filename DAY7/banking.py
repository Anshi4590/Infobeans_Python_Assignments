'''6. Banking Fraud Detection System

A bank checks fraud risk based on transaction amount, location, device, and transaction count.

If amount is greater than or equal to 50000, then check location. If location is international, then check device. If device is new, then check transaction count. If transactions are more than 3, mark High Risk (Block); otherwise Medium Risk. If device is not new, mark Medium Risk.

If location is domestic, then check transaction count. If more than 5, mark Medium Risk; otherwise Low Risk.

If amount is less than 50000, then check unusual activity. If yes, then check device. If device is new, mark Medium Risk; otherwise Low Risk. If no unusual activity, mark Safe.

Input:
Amount = 70000
Location = international
Device = new
Transactions = 4

Output:
Risk Level = High Risk (Blocked)'''

#solution

amount = int(input(" Amount ="))
location = input("location =")
device = input("Device =")
count = int(input("Transactions ="))

if amount>=50000:

   if location.lower() =="international":

      if device.lower() =="new":
         if count>3:
            print("Risk Level = High Risk (Blocked)")
         else:
            print("Risk Level = Medium Risk")
      else:
          print("Risk Level = Medium Risk")

   elif location.lower() =="domestic":

       if count>5:
            print("Risk Level = Medium Risk")
          else:
            print("Risk Level = low Risk")
      
else:
   activity = input(" Unusual Activity =")
   if activity.lower() == "yes":
      print("Flag")
   else:
      print("Allow")

