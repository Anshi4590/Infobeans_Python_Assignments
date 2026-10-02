'''10. Military Recruitment Fitness System

Selection is based on age, BMI, running time, and medical condition.

If age is between 18 and 25, then check BMI. If BMI is between 18 and 25, then check running time. If running time is less than or equal to 15 minutes, then check medical. If medical is fit, select; otherwise medical reject. If running time is more than 15, physical fail. If BMI is not in range, BMI fail.

If age is between 26 and 30, then check running time and medical. If running time is less than or equal to 14 and medical is fit, conditional selection; otherwise reject.

If age is above 30 or below 18, not eligible.

Input:
Age = 23
BMI = 22
Running Time = 14
Medical = fit

Output:
Selection Status = Selected'''

#solution

Age = int(input("Age = "))
BMI = int(input("BMI ="))
Time = int(input(" Running Time ="))
Medical = input("Medical =")

if 18<=Age<=25:

   if 18<=BMI<=25:

      if Time<=15:

         if Medical.lower() == "fit":
            print("Select")

         else:
            print(" medical reject")

      else:
         print("physical fail")

   else:
      print("BMI Fail")

elif 26<=Age<=30:

   if Time<=14 and Medical.lower() == "fit":
      print("conditional selection")

   else:
      print("reject")

else:
   print("Not Eligible")