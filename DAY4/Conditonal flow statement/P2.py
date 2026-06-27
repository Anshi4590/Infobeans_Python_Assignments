'''2. Student Performance Analyzer
   A school wants to evaluate students based on marks.

* If marks ≥ 40 → Pass
* If marks ≥ 75 → Distinction

Input:
Enter marks: 80

Output:
Pass
Distinction'''


#solution

marks = int(input("Enter the marks:"))
if marks>=40:
   if marks>=75: 
        print("Distinction")
   print("pass")
else:
    print("fail")

