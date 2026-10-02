'''5.
 Student Grade Classification System (Python List Assignment)


A school stores student marks in a list. The system must analyze the marks and generate a **clear performance report**
by grouping students into grade categories.



Write a Python program to:

* Iterate through the list of marks
* Assign grades based on marks:

  * **>= 90 → A**
  * **>= 75 and < 90 → B**
  * **>= 50 and < 75 → C**
  * **< 50 → Fail**
* Store each category in separate lists
* Count students in each category
* Display a **final structured report (important)**

---

## 📌 Output Format (Mandatory)

Your output must be displayed exactly in this format:

```
===== STUDENT GRADE REPORT =====

A Grade Students   : [list]
B Grade Students   : [list]
C Grade Students   : [list]
Fail Students      : [list]

--------------------------------
A Count   : X
B Count   : X
C Count   : X
Fail Count: X
--------------------------------

Total Students: X
```

---

 Input

[95, 82, 67, 45, 30]

Output

```
===== STUDENT GRADE REPORT =====

A Grade Students   : [95]
B Grade Students   : [82]
C Grade Students   : [67]
Fail Students      : [45, 30]

--------------------------------
A Count   : 1
B Count   : 1
C Count   : 1
Fail Count: 2
--------------------------------

Total Students: 5



'''
mark = list(map(int,input("Enter marks:").split(" ")))
print(mark)
lista =[]
listb =[]
listc =[]
flist = []
for i in mark:
    if i>= 90:
       lista.append(i)
    elif i>= 75 and i< 90:
       listb.append(i)
    elif i>= 50 and i< 75:
       listc.append(i)
    else:
       flist.append(i)
print("===== STUDENT GRADE REPORT =====")
print()
print(f"A Grade Students     : {lista}")
print(f"B Grade Students     : {listb}")
print(f"C Grade Students     : {listc}")
print(f"Fail Students        : {flist}")
print()
print("--------------------------------")
print(f"A Count            : {len(lista)}")
print(f"B Count            : {len(listb)}")
print(f"C Count            : {len(listc)}")
print(f"Fail Count         : {len(flist)}")
print("--------------------------------")
print()
print(f"Total Students     : {len(mark)}")
