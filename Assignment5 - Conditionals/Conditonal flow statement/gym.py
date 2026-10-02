'''4. Gym Membership Eligibility Checker
   A gym checks multiple conditions:

* If age ≥ 18 → Allowed for gym
* If BMI > 25 → Suggest weight loss program

Input:
Enter age: 25
Enter BMI: 27

Output:
Gym access granted
Enroll in weight loss program'''


#solution


age = int(input("Enter Your Age:"))
bmi = int(input("Enter BMI:"))
if age>=18:
   print("Allowed for gym")

   if bmi>25:
      print("Enroll in Weight loss program")
else:
   print("Do Home workout") 