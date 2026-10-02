'''
7.

=========================================
ONLINE EXAM RESULT SYSTEM
=========================

Store student marks in a dictionary.

results = {
"Ajay":88,
"Ravi":45,
"Neha":76,
"Aman":39
}

Write a program to:

* Display names of students who passed.
  (Passing Marks = 50)

Sample Output:
Ajay
Neha
Ravi

---

'''

m = int(input("Enter total of no. students : "))

results = {}
ans = {}

for i in range(m):

    key = input("Enter key : ")
    value = input("Enter value : ")
    results[key] = value

for k ,v in results.items():
    
    if v>=50:
       ans[i]=v

for i in ans:
    print(i)