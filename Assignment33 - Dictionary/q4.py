'''4.

=========================================
STUDENT GRADE ANALYSIS
======================

Store student marks in a dictionary.

students = {
"Ajay":78,
"Ravi":92,
"Neha":85,
"Aman":65
}

Write a program to:

* Find the student with highest marks.
* Find the student with lowest marks.

Sample Output:
Highest Marks : Ravi 92
Lowest Marks : Aman 65

---
'''

m = int(input("Enter number of values :"))

d ={}

for i in range (m):
    key = input("Enter key:")
    value = int(input("Enter value:"))
    d[key] = value

print(d)

max = 0
max_name = ""
min = list(d.values())[0]
min_name =""

for k ,v in d.items():
    
    if v > max:
       max = v
       max_name = k

    if v <min:
       min = v
       min_name = k

print(f"Highest Marks :{max} {max_name}")
print(f"lowest Marks :{min} {min_name}")