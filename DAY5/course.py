'''14. Online Course Fee System

An online platform offers courses with fixed fees:

* Programming → ₹5000
* Design → ₹4000
* Marketing → ₹3000
  Discount is applied based on user type:
* Student → 20% discount
* Working Professional → 10% discount
* Others → No discount

Write a Python program to calculate final course fee.

Input:
Enter course category: Programming
Enter user type: Student

Output:
Final Course Fee: ₹4000'''

category =input("enter course category:")
type = input("Enter user Type:")

if category.lower() == "programming" and type.lower() == "student":
   fee = 5000 - 5000*20/100
   print("Final Course Fee:",fee)

elif category.lower() == "programming" and type.lower() == "Working Professional":
   fee = 5000 - 5000*10/100
   print("Final Course Fee:",fee)

elif category.lower() == "programming" and type.lower() == "others":
   print("Final Course Fee:Rs 5000")

elif category.lower() == "Design" and type.lower() == "student":
   fee = 4000 - 4000*20/100
   print("Final Course Fee:",fee)

elif category.lower() == "Design" and type.lower() == "Working Professional":
   fee = 4000 - 4000*10/100
   print("Final Course Fee:",fee)

elif category.lower() == "Design" and type.lower() == "others":
   print("Final Course Fee:Rs 4000")

elif category.lower() == "Marketing" and type.lower() == "student":
   fee = 3000 - 3000*20/100
   print("Final Course Fee:",fee)

elif category.lower() == "Marketing" and type.lower() == "Working Professional":
   fee = 3000 - 3000*10/100
   print("Final Course Fee:",fee)

elif category.lower() == "Marketing" and type.lower() == "others":
   print("Final Course Fee:Rs 3000")

else:
   print("invalid choice")





