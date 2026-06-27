'''2. Hospital Emergency Priority System

A hospital assigns treatment priority based on age, severity, and insurance.

If severity is critical, then check age. If age is 60 or above, assign Immediate ICU; otherwise assign Emergency Ward.

If severity is moderate, then check insurance. If insured, assign Priority Treatment; otherwise assign General Queue.

If severity is low, then check age. If age is less than 10, assign Pediatric Priority; otherwise assign Wait.

Input:
Age = 65
Severity = critical
Insurance = yes

Output:
Treatment = Immediate ICU'''


Age = int(input("Age ="))
Severity = input("Severity =")
Insurance = input("Insurance =")

if Severity.lower() == "critical":
   if Age>=60:
      print("Treatment = Immediate ICU")

   else:
      print("Treatment = Emergency Ward")

elif Severity.lower() == "Moderate":

   if Insurance.lower() == "yes":
      print(" Treatment = Priority Treatment")

   else:
      print("Treatment = General Queue")

else:

   if Age < 10:
      print("Treatment = Pediatric Priority")

   else:
      print("Treatment = wait")
