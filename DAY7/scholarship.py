'''3. Smart Scholarship Allocation System

A scholarship is provided based on marks, family income, and category.

If marks are 85 or above, then check income. If income is less than or equal to 300000, then check category. If category is not general, give Full Scholarship; otherwise give 75% Scholarship. If income is above 300000, give 50% Scholarship.

If marks are between 70 and 84, then check income. If income is less than or equal to 200000, give 50% Scholarship; otherwise give 25% Scholarship.

If marks are below 70, no scholarship is given.

Input:
Marks = 88
Income = 250000
Category = OBC

Output:
Scholarship = Full Scholarship'''

#solution

Marks = int(input("Marks ="))
Income = int(input("Income ="))
Category = input("Category =")

if Marks>=85:

   if Income<=300000:

      if Category.lower()!= "general":
         print("Scholarship = Full Scholarship")

      else:
         print("Scholarship = 75% Scholarship")

   else:
      print("Scholarship = 50% Scholarship")

elif 70<Marks<84:

   if Income<=200000:
      print("Scholarship = 50% Scholarship")

   else: 
      print("Scholarship = 25% Scholarship")

else:
   print("Scholarship = No Scholarship")
